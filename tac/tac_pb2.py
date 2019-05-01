# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tac.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tac.proto',
  package='fetch.oef.pb',
  syntax='proto2',
  serialized_pb=_b('\n\ttac.proto\x12\x0c\x66\x65tch.oef.pb\"%\n\x07IntPair\x12\x0b\n\x03key\x18\x01 \x02(\x05\x12\r\n\x05value\x18\x02 \x02(\x05\"2\n\nDictionary\x12$\n\x05pairs\x18\x01 \x03(\x0b\x32\x15.fetch.oef.pb.IntPair\"\xb4\x06\n\rTACController\x1a\x0c\n\nRegistered\x1a\x0e\n\x0cUnregistered\x1a\x0b\n\tCancelled\x1aN\n\x08GameData\x12\r\n\x05money\x18\x01 \x02(\x05\x12\x11\n\tresources\x18\x02 \x03(\x05\x12\x13\n\x0bpreferences\x18\x03 \x03(\x05\x12\x0b\n\x03\x66\x65\x65\x18\x04 \x02(\x05\x1a\x31\n\x17TransactionConfirmation\x12\x16\n\x0etransaction_id\x18\x01 \x02(\t\x1a\xe6\x01\n\x05\x45rror\x12?\n\nerror_code\x18\x01 \x02(\x0e\x32+.fetch.oef.pb.TACController.Error.ErrorCode\x12\x11\n\terror_msg\x18\x02 \x02(\t\"\x88\x01\n\tErrorCode\x12\x11\n\rGENERIC_ERROR\x10\x00\x12\x15\n\x11REQUEST_NOT_VALID\x10\x01\x12\x1c\n\x18\x41GENT_ALREADY_REGISTERED\x10\x02\x12\x18\n\x14\x41GENT_NOT_REGISTERED\x10\x03\x12\x19\n\x15TRANSACTION_NOT_VALID\x10\x04\x1a\x8b\x03\n\x07Message\x12<\n\nregistered\x18\x01 \x01(\x0b\x32&.fetch.oef.pb.TACController.RegisteredH\x00\x12@\n\x0cunregistered\x18\x02 \x01(\x0b\x32(.fetch.oef.pb.TACController.UnregisteredH\x00\x12:\n\tcancelled\x18\x03 \x01(\x0b\x32%.fetch.oef.pb.TACController.CancelledH\x00\x12\x39\n\tgame_data\x18\x04 \x01(\x0b\x32$.fetch.oef.pb.TACController.GameDataH\x00\x12N\n\x0ftx_confirmation\x18\x05 \x01(\x0b\x32\x33.fetch.oef.pb.TACController.TransactionConfirmationH\x00\x12\x32\n\x05\x65rror\x18\x06 \x01(\x0b\x32!.fetch.oef.pb.TACController.ErrorH\x00\x42\x05\n\x03msg\"\xeb\x02\n\x08TACAgent\x1a\n\n\x08Register\x1a\x0c\n\nUnregister\x1a\x88\x01\n\x0bTransaction\x12\x16\n\x0etransaction_id\x18\x01 \x02(\t\x12\r\n\x05\x62uyer\x18\x02 \x02(\x08\x12\x14\n\x0c\x63ounterparty\x18\x03 \x02(\t\x12\x0e\n\x06\x61mount\x18\x04 \x02(\x05\x12,\n\nquantities\x18\x05 \x02(\x0b\x32\x18.fetch.oef.pb.Dictionary\x1a\xb9\x01\n\x07Message\x12\x33\n\x08register\x18\x01 \x01(\x0b\x32\x1f.fetch.oef.pb.TACAgent.RegisterH\x00\x12\x37\n\nunregister\x18\x02 \x01(\x0b\x32!.fetch.oef.pb.TACAgent.UnregisterH\x00\x12\x39\n\x0btransaction\x18\x03 \x01(\x0b\x32\".fetch.oef.pb.TACAgent.TransactionH\x00\x42\x05\n\x03msg')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_TACCONTROLLER_ERROR_ERRORCODE = _descriptor.EnumDescriptor(
  name='ErrorCode',
  full_name='fetch.oef.pb.TACController.Error.ErrorCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GENERIC_ERROR', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REQUEST_NOT_VALID', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AGENT_ALREADY_REGISTERED', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AGENT_NOT_REGISTERED', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRANSACTION_NOT_VALID', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=405,
  serialized_end=541,
)
_sym_db.RegisterEnumDescriptor(_TACCONTROLLER_ERROR_ERRORCODE)


_INTPAIR = _descriptor.Descriptor(
  name='IntPair',
  full_name='fetch.oef.pb.IntPair',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='fetch.oef.pb.IntPair.key', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='fetch.oef.pb.IntPair.value', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=27,
  serialized_end=64,
)


_DICTIONARY = _descriptor.Descriptor(
  name='Dictionary',
  full_name='fetch.oef.pb.Dictionary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pairs', full_name='fetch.oef.pb.Dictionary.pairs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=66,
  serialized_end=116,
)


_TACCONTROLLER_REGISTERED = _descriptor.Descriptor(
  name='Registered',
  full_name='fetch.oef.pb.TACController.Registered',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=136,
  serialized_end=148,
)

_TACCONTROLLER_UNREGISTERED = _descriptor.Descriptor(
  name='Unregistered',
  full_name='fetch.oef.pb.TACController.Unregistered',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=150,
  serialized_end=164,
)

_TACCONTROLLER_CANCELLED = _descriptor.Descriptor(
  name='Cancelled',
  full_name='fetch.oef.pb.TACController.Cancelled',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=166,
  serialized_end=177,
)

_TACCONTROLLER_GAMEDATA = _descriptor.Descriptor(
  name='GameData',
  full_name='fetch.oef.pb.TACController.GameData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='money', full_name='fetch.oef.pb.TACController.GameData.money', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resources', full_name='fetch.oef.pb.TACController.GameData.resources', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='preferences', full_name='fetch.oef.pb.TACController.GameData.preferences', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fee', full_name='fetch.oef.pb.TACController.GameData.fee', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=179,
  serialized_end=257,
)

_TACCONTROLLER_TRANSACTIONCONFIRMATION = _descriptor.Descriptor(
  name='TransactionConfirmation',
  full_name='fetch.oef.pb.TACController.TransactionConfirmation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transaction_id', full_name='fetch.oef.pb.TACController.TransactionConfirmation.transaction_id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=259,
  serialized_end=308,
)

_TACCONTROLLER_ERROR = _descriptor.Descriptor(
  name='Error',
  full_name='fetch.oef.pb.TACController.Error',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error_code', full_name='fetch.oef.pb.TACController.Error.error_code', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error_msg', full_name='fetch.oef.pb.TACController.Error.error_msg', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TACCONTROLLER_ERROR_ERRORCODE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=311,
  serialized_end=541,
)

_TACCONTROLLER_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='fetch.oef.pb.TACController.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='registered', full_name='fetch.oef.pb.TACController.Message.registered', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unregistered', full_name='fetch.oef.pb.TACController.Message.unregistered', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cancelled', full_name='fetch.oef.pb.TACController.Message.cancelled', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='game_data', full_name='fetch.oef.pb.TACController.Message.game_data', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tx_confirmation', full_name='fetch.oef.pb.TACController.Message.tx_confirmation', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error', full_name='fetch.oef.pb.TACController.Message.error', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='msg', full_name='fetch.oef.pb.TACController.Message.msg',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=544,
  serialized_end=939,
)

_TACCONTROLLER = _descriptor.Descriptor(
  name='TACController',
  full_name='fetch.oef.pb.TACController',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_TACCONTROLLER_REGISTERED, _TACCONTROLLER_UNREGISTERED, _TACCONTROLLER_CANCELLED, _TACCONTROLLER_GAMEDATA, _TACCONTROLLER_TRANSACTIONCONFIRMATION, _TACCONTROLLER_ERROR, _TACCONTROLLER_MESSAGE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=119,
  serialized_end=939,
)


_TACAGENT_REGISTER = _descriptor.Descriptor(
  name='Register',
  full_name='fetch.oef.pb.TACAgent.Register',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=954,
  serialized_end=964,
)

_TACAGENT_UNREGISTER = _descriptor.Descriptor(
  name='Unregister',
  full_name='fetch.oef.pb.TACAgent.Unregister',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=966,
  serialized_end=978,
)

_TACAGENT_TRANSACTION = _descriptor.Descriptor(
  name='Transaction',
  full_name='fetch.oef.pb.TACAgent.Transaction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transaction_id', full_name='fetch.oef.pb.TACAgent.Transaction.transaction_id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='buyer', full_name='fetch.oef.pb.TACAgent.Transaction.buyer', index=1,
      number=2, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='counterparty', full_name='fetch.oef.pb.TACAgent.Transaction.counterparty', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='amount', full_name='fetch.oef.pb.TACAgent.Transaction.amount', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quantities', full_name='fetch.oef.pb.TACAgent.Transaction.quantities', index=4,
      number=5, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=981,
  serialized_end=1117,
)

_TACAGENT_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='fetch.oef.pb.TACAgent.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='register', full_name='fetch.oef.pb.TACAgent.Message.register', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unregister', full_name='fetch.oef.pb.TACAgent.Message.unregister', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='transaction', full_name='fetch.oef.pb.TACAgent.Message.transaction', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='msg', full_name='fetch.oef.pb.TACAgent.Message.msg',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1120,
  serialized_end=1305,
)

_TACAGENT = _descriptor.Descriptor(
  name='TACAgent',
  full_name='fetch.oef.pb.TACAgent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_TACAGENT_REGISTER, _TACAGENT_UNREGISTER, _TACAGENT_TRANSACTION, _TACAGENT_MESSAGE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=942,
  serialized_end=1305,
)

_DICTIONARY.fields_by_name['pairs'].message_type = _INTPAIR
_TACCONTROLLER_REGISTERED.containing_type = _TACCONTROLLER
_TACCONTROLLER_UNREGISTERED.containing_type = _TACCONTROLLER
_TACCONTROLLER_CANCELLED.containing_type = _TACCONTROLLER
_TACCONTROLLER_GAMEDATA.containing_type = _TACCONTROLLER
_TACCONTROLLER_TRANSACTIONCONFIRMATION.containing_type = _TACCONTROLLER
_TACCONTROLLER_ERROR.fields_by_name['error_code'].enum_type = _TACCONTROLLER_ERROR_ERRORCODE
_TACCONTROLLER_ERROR.containing_type = _TACCONTROLLER
_TACCONTROLLER_ERROR_ERRORCODE.containing_type = _TACCONTROLLER_ERROR
_TACCONTROLLER_MESSAGE.fields_by_name['registered'].message_type = _TACCONTROLLER_REGISTERED
_TACCONTROLLER_MESSAGE.fields_by_name['unregistered'].message_type = _TACCONTROLLER_UNREGISTERED
_TACCONTROLLER_MESSAGE.fields_by_name['cancelled'].message_type = _TACCONTROLLER_CANCELLED
_TACCONTROLLER_MESSAGE.fields_by_name['game_data'].message_type = _TACCONTROLLER_GAMEDATA
_TACCONTROLLER_MESSAGE.fields_by_name['tx_confirmation'].message_type = _TACCONTROLLER_TRANSACTIONCONFIRMATION
_TACCONTROLLER_MESSAGE.fields_by_name['error'].message_type = _TACCONTROLLER_ERROR
_TACCONTROLLER_MESSAGE.containing_type = _TACCONTROLLER
_TACCONTROLLER_MESSAGE.oneofs_by_name['msg'].fields.append(
  _TACCONTROLLER_MESSAGE.fields_by_name['registered'])
_TACCONTROLLER_MESSAGE.fields_by_name['registered'].containing_oneof = _TACCONTROLLER_MESSAGE.oneofs_by_name['msg']
_TACCONTROLLER_MESSAGE.oneofs_by_name['msg'].fields.append(
  _TACCONTROLLER_MESSAGE.fields_by_name['unregistered'])
_TACCONTROLLER_MESSAGE.fields_by_name['unregistered'].containing_oneof = _TACCONTROLLER_MESSAGE.oneofs_by_name['msg']
_TACCONTROLLER_MESSAGE.oneofs_by_name['msg'].fields.append(
  _TACCONTROLLER_MESSAGE.fields_by_name['cancelled'])
_TACCONTROLLER_MESSAGE.fields_by_name['cancelled'].containing_oneof = _TACCONTROLLER_MESSAGE.oneofs_by_name['msg']
_TACCONTROLLER_MESSAGE.oneofs_by_name['msg'].fields.append(
  _TACCONTROLLER_MESSAGE.fields_by_name['game_data'])
_TACCONTROLLER_MESSAGE.fields_by_name['game_data'].containing_oneof = _TACCONTROLLER_MESSAGE.oneofs_by_name['msg']
_TACCONTROLLER_MESSAGE.oneofs_by_name['msg'].fields.append(
  _TACCONTROLLER_MESSAGE.fields_by_name['tx_confirmation'])
_TACCONTROLLER_MESSAGE.fields_by_name['tx_confirmation'].containing_oneof = _TACCONTROLLER_MESSAGE.oneofs_by_name['msg']
_TACCONTROLLER_MESSAGE.oneofs_by_name['msg'].fields.append(
  _TACCONTROLLER_MESSAGE.fields_by_name['error'])
_TACCONTROLLER_MESSAGE.fields_by_name['error'].containing_oneof = _TACCONTROLLER_MESSAGE.oneofs_by_name['msg']
_TACAGENT_REGISTER.containing_type = _TACAGENT
_TACAGENT_UNREGISTER.containing_type = _TACAGENT
_TACAGENT_TRANSACTION.fields_by_name['quantities'].message_type = _DICTIONARY
_TACAGENT_TRANSACTION.containing_type = _TACAGENT
_TACAGENT_MESSAGE.fields_by_name['register'].message_type = _TACAGENT_REGISTER
_TACAGENT_MESSAGE.fields_by_name['unregister'].message_type = _TACAGENT_UNREGISTER
_TACAGENT_MESSAGE.fields_by_name['transaction'].message_type = _TACAGENT_TRANSACTION
_TACAGENT_MESSAGE.containing_type = _TACAGENT
_TACAGENT_MESSAGE.oneofs_by_name['msg'].fields.append(
  _TACAGENT_MESSAGE.fields_by_name['register'])
_TACAGENT_MESSAGE.fields_by_name['register'].containing_oneof = _TACAGENT_MESSAGE.oneofs_by_name['msg']
_TACAGENT_MESSAGE.oneofs_by_name['msg'].fields.append(
  _TACAGENT_MESSAGE.fields_by_name['unregister'])
_TACAGENT_MESSAGE.fields_by_name['unregister'].containing_oneof = _TACAGENT_MESSAGE.oneofs_by_name['msg']
_TACAGENT_MESSAGE.oneofs_by_name['msg'].fields.append(
  _TACAGENT_MESSAGE.fields_by_name['transaction'])
_TACAGENT_MESSAGE.fields_by_name['transaction'].containing_oneof = _TACAGENT_MESSAGE.oneofs_by_name['msg']
DESCRIPTOR.message_types_by_name['IntPair'] = _INTPAIR
DESCRIPTOR.message_types_by_name['Dictionary'] = _DICTIONARY
DESCRIPTOR.message_types_by_name['TACController'] = _TACCONTROLLER
DESCRIPTOR.message_types_by_name['TACAgent'] = _TACAGENT

IntPair = _reflection.GeneratedProtocolMessageType('IntPair', (_message.Message,), dict(
  DESCRIPTOR = _INTPAIR,
  __module__ = 'tac_pb2'
  # @@protoc_insertion_point(class_scope:fetch.oef.pb.IntPair)
  ))
_sym_db.RegisterMessage(IntPair)

Dictionary = _reflection.GeneratedProtocolMessageType('Dictionary', (_message.Message,), dict(
  DESCRIPTOR = _DICTIONARY,
  __module__ = 'tac_pb2'
  # @@protoc_insertion_point(class_scope:fetch.oef.pb.Dictionary)
  ))
_sym_db.RegisterMessage(Dictionary)

TACController = _reflection.GeneratedProtocolMessageType('TACController', (_message.Message,), dict(

  Registered = _reflection.GeneratedProtocolMessageType('Registered', (_message.Message,), dict(
    DESCRIPTOR = _TACCONTROLLER_REGISTERED,
    __module__ = 'tac_pb2'
    # @@protoc_insertion_point(class_scope:fetch.oef.pb.TACController.Registered)
    ))
  ,

  Unregistered = _reflection.GeneratedProtocolMessageType('Unregistered', (_message.Message,), dict(
    DESCRIPTOR = _TACCONTROLLER_UNREGISTERED,
    __module__ = 'tac_pb2'
    # @@protoc_insertion_point(class_scope:fetch.oef.pb.TACController.Unregistered)
    ))
  ,

  Cancelled = _reflection.GeneratedProtocolMessageType('Cancelled', (_message.Message,), dict(
    DESCRIPTOR = _TACCONTROLLER_CANCELLED,
    __module__ = 'tac_pb2'
    # @@protoc_insertion_point(class_scope:fetch.oef.pb.TACController.Cancelled)
    ))
  ,

  GameData = _reflection.GeneratedProtocolMessageType('GameData', (_message.Message,), dict(
    DESCRIPTOR = _TACCONTROLLER_GAMEDATA,
    __module__ = 'tac_pb2'
    # @@protoc_insertion_point(class_scope:fetch.oef.pb.TACController.GameData)
    ))
  ,

  TransactionConfirmation = _reflection.GeneratedProtocolMessageType('TransactionConfirmation', (_message.Message,), dict(
    DESCRIPTOR = _TACCONTROLLER_TRANSACTIONCONFIRMATION,
    __module__ = 'tac_pb2'
    # @@protoc_insertion_point(class_scope:fetch.oef.pb.TACController.TransactionConfirmation)
    ))
  ,

  Error = _reflection.GeneratedProtocolMessageType('Error', (_message.Message,), dict(
    DESCRIPTOR = _TACCONTROLLER_ERROR,
    __module__ = 'tac_pb2'
    # @@protoc_insertion_point(class_scope:fetch.oef.pb.TACController.Error)
    ))
  ,

  Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), dict(
    DESCRIPTOR = _TACCONTROLLER_MESSAGE,
    __module__ = 'tac_pb2'
    # @@protoc_insertion_point(class_scope:fetch.oef.pb.TACController.Message)
    ))
  ,
  DESCRIPTOR = _TACCONTROLLER,
  __module__ = 'tac_pb2'
  # @@protoc_insertion_point(class_scope:fetch.oef.pb.TACController)
  ))
_sym_db.RegisterMessage(TACController)
_sym_db.RegisterMessage(TACController.Registered)
_sym_db.RegisterMessage(TACController.Unregistered)
_sym_db.RegisterMessage(TACController.Cancelled)
_sym_db.RegisterMessage(TACController.GameData)
_sym_db.RegisterMessage(TACController.TransactionConfirmation)
_sym_db.RegisterMessage(TACController.Error)
_sym_db.RegisterMessage(TACController.Message)

TACAgent = _reflection.GeneratedProtocolMessageType('TACAgent', (_message.Message,), dict(

  Register = _reflection.GeneratedProtocolMessageType('Register', (_message.Message,), dict(
    DESCRIPTOR = _TACAGENT_REGISTER,
    __module__ = 'tac_pb2'
    # @@protoc_insertion_point(class_scope:fetch.oef.pb.TACAgent.Register)
    ))
  ,

  Unregister = _reflection.GeneratedProtocolMessageType('Unregister', (_message.Message,), dict(
    DESCRIPTOR = _TACAGENT_UNREGISTER,
    __module__ = 'tac_pb2'
    # @@protoc_insertion_point(class_scope:fetch.oef.pb.TACAgent.Unregister)
    ))
  ,

  Transaction = _reflection.GeneratedProtocolMessageType('Transaction', (_message.Message,), dict(
    DESCRIPTOR = _TACAGENT_TRANSACTION,
    __module__ = 'tac_pb2'
    # @@protoc_insertion_point(class_scope:fetch.oef.pb.TACAgent.Transaction)
    ))
  ,

  Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), dict(
    DESCRIPTOR = _TACAGENT_MESSAGE,
    __module__ = 'tac_pb2'
    # @@protoc_insertion_point(class_scope:fetch.oef.pb.TACAgent.Message)
    ))
  ,
  DESCRIPTOR = _TACAGENT,
  __module__ = 'tac_pb2'
  # @@protoc_insertion_point(class_scope:fetch.oef.pb.TACAgent)
  ))
_sym_db.RegisterMessage(TACAgent)
_sym_db.RegisterMessage(TACAgent.Register)
_sym_db.RegisterMessage(TACAgent.Unregister)
_sym_db.RegisterMessage(TACAgent.Transaction)
_sym_db.RegisterMessage(TACAgent.Message)


# @@protoc_insertion_point(module_scope)