(function () {

    // the ID of the current sandbox running/finished/stopped. 'null' if no sandbox has been started yet.
    let currentSandboxID = null;
    let currentGameId = ""

    let configureSandboxForm = function () {

        let form = document.getElementById("form-sandbox");
        let startBtn = document.getElementById("btn-start-sandbox");
        let stopBtn = document.getElementById("btn-stop-sandbox");
        let process_statusBtn = document.getElementById("process-status-sandbox");
        let controller_statusBtn = document.getElementById("controller-status-sandbox");
        let game_id = document.getElementById("info-game-id");

        stopBtn.disabled = true;

        form.addEventListener("submit", function (ev) {
            ev.preventDefault();

            let clickedBtnId = ev.target.target;
            if (clickedBtnId === startBtn.id) {
                // start sandbox button clicked
                startSandbox();
            } else if (clickedBtnId === stopBtn.id) {
                // stop sandbox button clicked
                stopSandbox();
            }

        });

        let startSandbox = function () {
            let XHR = new XMLHttpRequest();

            // Bind the FormData object and the form element
            let FD = new FormData(form);

            // Define what happens on successful data submission
            XHR.addEventListener("load", function (event) {
                startBtn.disabled = true;
                stopBtn.disabled = false;
            });

            // Define what happens in case of error
            XHR.addEventListener("error", function (event) {
                startBtn.disabled = false;
                stopBtn.disabled = true;
            });

            XHR.open("POST", "/api/sandboxes", false);
            // Display the key/value pairs
            console.log("Form data");
            for (var pair of FD.entries()) {
                console.log(pair[0]+ ', ' + pair[1]);
            }
            XHR.send(FD);
            let jsonResponse = JSON.parse(XHR.response);
            console.log("ID=" + jsonResponse["id"]);
            currentSandboxID = jsonResponse["id"];
            return XHR.response;
        };

        let stopSandbox = function () {
            let XHR = new XMLHttpRequest();

            // Bind the FormData object and the form element
            let FD = new FormData(form);

            // Define what happens on successful data submission
            XHR.addEventListener("load", function (event) {
                startBtn.disabled = false;
                stopBtn.disabled = true;
            });

            // Define what happens in case of error
            XHR.addEventListener("error", function (event) {
                alert('ERROR: could not stop sandbox.');
                startBtn.disabled = true;
                stopBtn.disabled = false;
            });

            XHR.open("DELETE", "/api/sandboxes/" + currentSandboxID, true);
            XHR.send(FD);
            return XHR.responseText;
        };

        let getSandboxStatus = function () {
            console.log("getSandboxStatus called for ID=", currentSandboxID);
            if (currentSandboxID != null) {
                let XHR = new XMLHttpRequest();
                XHR.onreadystatechange = function () {
                    if (XHR.response != null && XHR.response != "null" && XHR.response != ""){
                        let jsonResponse = JSON.parse(XHR.response);
                        if (this.readyState == 4 && this.status == 200) {
                            process_statusBtn.innerHTML = "Process Status: " + jsonResponse["process_status"];
                            controller_statusBtn.innerHTML = "Controller Status: " + jsonResponse["controller_status"];
                            currentGameId = jsonResponse["game_id"]
                            game_id.innerHTML = "Game Id: " + currentGameId
                        }
                    }
                };
                console.log(" XHR Open: /api/sandboxes/" + currentSandboxID)
                XHR.open("GET", "/api/sandboxes/" + currentSandboxID, true);
                XHR.send();
            }
            setTimeout(getSandboxStatus, 500);
        };
        getSandboxStatus();
    };

    let configureAgentForm = function () {
        let form = document.getElementById("form-agent");
        let startBtn = document.getElementById("btn-start-agent");
        let stopBtn = document.getElementById("btn-stop-agent");
        let process_statusBtn = document.getElementById("process-status-agent");
        let agent_statusBtn = document.getElementById("agent-status-agent");

        stopBtn.disabled = true;

        form.addEventListener("submit", function (ev) {

            ev.preventDefault();

            let clickedBtnId = ev.target.target;
            if (clickedBtnId === startBtn.id) {
                // start agent button clicked
                startAgent();
            } else if (clickedBtnId === stopBtn.id) {
                // stop sandbox button clicked
                stopAgent();
            }

        });

        let startAgent = function () {
            console.log("******* startAgent")


            let XHR = new XMLHttpRequest();

            // Bind the FormData object and the form element
            let FD = new FormData(form);

            // Define what happens on successful data submission
            XHR.addEventListener("load", function (event) {
                startBtn.disabled = true;
                stopBtn.disabled = false;
            });

            // Define what happens in case of error
            XHR.addEventListener("error", function (event) {
                alert('ERROR: could not start agent.');
                startBtn.disabled = false;
                stopBtn.disabled = true;
            });
            // Add the game id
            FD.append("expected_version_id", currentGameId)
            // Display the key/value pairs
            console.log("Form data");
            for (var pair of FD.entries()) {
                console.log(pair[0]+ ', ' + pair[1]);
            }

            XHR.open("POST", "/api/agent", true);
            XHR.send(FD);
            return XHR.responseText;
        };


        let stopAgent = function () {
            let XHR = new XMLHttpRequest();

            // Bind the FormData object and the form element
            let FD = new FormData(form);

            // Define what happens on successful data submission
            XHR.addEventListener("load", function (event) {
                startBtn.disabled = false;
                stopBtn.disabled = true;
            });

            // Define what happens in case of error
            XHR.addEventListener("error", function (event) {
                alert('ERROR: could not stop agent.');
                startBtn.disabled = true;
                stopBtn.disabled = false;
            });

            XHR.open("DELETE", "/api/agent", true);
            XHR.send(FD);
            return XHR.responseText;
        };
        let getAgentStatus = function () {
            let XHR = new XMLHttpRequest();
            XHR.onreadystatechange = function () {
                if (XHR.response != null && XHR.response != "null" && XHR.response != ""){
                    let jsonResponse = JSON.parse(XHR.response);
                    if (this.readyState == 4 && this.status == 200) {
                        process_statusBtn.innerHTML = "Process Status: " + jsonResponse["process_status"];
                        agent_statusBtn.innerHTML = "Agent Status: " + jsonResponse["agent_status"];
                    }
                }
            };
            XHR.open("GET", "/api/agent", true);
            XHR.send();
            setTimeout(getAgentStatus, 2000);
        };
        getAgentStatus();

    };


    window.addEventListener("load", function () {
        configureSandboxForm();
        configureAgentForm();
    });


})();


