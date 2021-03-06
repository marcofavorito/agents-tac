#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ------------------------------------------------------------------------------
#
#   Copyright 2018-2019 Fetch.AI Limited
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------

"""Start a Visdom server, an OEF node instance, and run the simulation script."""
import importlib
import inspect
import os
import platform
import re
import subprocess
import sys
import time

import docker

import tac
from tac.platform.oef_health_check import OEFHealthCheck
from tac.platform.shared_sim_status import register_shared_dir, get_shared_dir
from tac.platform.simulation import parse_arguments, build_simulation_parameters

CUR_PATH = inspect.getfile(inspect.currentframe())  # type: ignore
ROOT_DIR = os.path.join(os.path.dirname(CUR_PATH), "..")
stack_tracer = importlib.import_module("stack_tracer", package=CUR_PATH)


class VisdomServer:
    """Class to manage the visdom server."""

    def __enter__(self):
        """Define what the context manager should do at the beginning of the block."""
        if platform.system() == 'Darwin':
            # This is required due to a bug in mac os Mojave
            print("Setting environment var...")
            os.environ["OBJC_DISABLE_INITIALIZE_FORK_SAFETY"] = "YES"
        print("Starting Visdom server...")
        self.proc = subprocess.Popen(["python3", "-m", "visdom.server"], env=os.environ, cwd=ROOT_DIR)

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Define what the context manager should do after the block has been executed."""
        print("Terminating Visdom server...")
        self.proc.terminate()


class OEFNode:
    """Class to manage the OEF node."""

    def _stop_oef_search_images(self):
        """Stop any running OEF nodes."""
        client = docker.from_env()
        for container in client.containers.list():
            if any(re.match("fetchai/oef-search", tag) for tag in container.image.tags):
                print("Stopping existing OEF Node...")
                container.stop()

    def _wait_for_oef(self):
        """Wait for the OEF to come live."""
        print("Waiting for the OEF to be operative...")
        for loop in range(0, 30):
            oef_healthcheck = OEFHealthCheck("127.0.0.1", 10000)
            is_success = oef_healthcheck.run()
            if is_success: break
            time.sleep(1)

    def __enter__(self):
        """Define what the context manager should do at the beginning of the block."""
        self._stop_oef_search_images()
        script_path = os.path.join("scripts", "oef", "launch.py")
        configuration_file_path = os.path.join("scripts", "oef", "launch_config.json")

        register_shared_dir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../data/shared'))
        os.environ['SHARED_DIR'] = get_shared_dir()

        print("Launching new OEF Node...")
        self.oef_process = subprocess.Popen(["python3", script_path, "-c", configuration_file_path, "--background"],
                                            stdout=subprocess.PIPE, env=os.environ, cwd=ROOT_DIR)
        self._wait_for_oef()
        self.id = self._get_image_id()
        print("ID: ", self.id)

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Define what the context manager should do after the block has been executed."""
        print("Stopping OEF Node...")
        p = subprocess.Popen(["docker", "stop", self.id], env=os.environ)
        p.wait()

    def _get_image_id(self):
        output = self.oef_process.communicate()[0]
        id = output.splitlines()[-1].decode("utf-8")
        return id


if __name__ == '__main__':
    sys.argv += ['--dashboard', '--version-id', 'tac_v1']
    args = parse_arguments()
    simulation_params = build_simulation_parameters(args)

    with VisdomServer(), OEFNode():
        stack_tracer.start_trace(os.path.join(ROOT_DIR, "data/trace.html"), interval=5, auto=True)  # type: ignore
        tac.platform.simulation.run(simulation_params)
        stack_tracer.stop_trace()  # type: ignore
