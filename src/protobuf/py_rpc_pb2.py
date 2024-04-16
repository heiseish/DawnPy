# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: py_rpc.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='py_rpc.proto',
  package='PyRPC',
  syntax='proto3',
  serialized_options=b'\242\002\003RTG',
  serialized_pb=b'\n\x0cpy_rpc.proto\x12\x05PyRPC\"&\n\x08TTSInput\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x0c\n\x04lang\x18\x02 \x01(\t\"\x19\n\tTTSOutput\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"\x18\n\x08STTInput\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"\'\n\tSTTOutput\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x0c\n\x04lang\x18\x02 \x01(\t\"3\n\x11\x43onversationInput\x12\x10\n\x08trans_id\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\"\x9a\x01\n\x14\x43onversationResponse\x12\x10\n\x08trans_id\x18\x01 \x01(\t\x12\x30\n\x05state\x18\x02 \x01(\x0e\x32!.PyRPC.ConversationResponse.State\x12\x0c\n\x04text\x18\x03 \x01(\t\"0\n\x05State\x12\x0b\n\x07SUCCESS\x10\x00\x12\r\n\tMODEL_ERR\x10\x01\x12\x0b\n\x07UNKNOWN\x10\x02\x32\xbc\x01\n\x0cPyRPCService\x12\x31\n\x0cTextToSpeech\x12\x0f.PyRPC.TTSInput\x1a\x10.PyRPC.TTSOutput\x12\x31\n\x0cSpeechToText\x12\x0f.PyRPC.STTInput\x1a\x10.PyRPC.STTOutput\x12\x46\n\rRespondToText\x12\x18.PyRPC.ConversationInput\x1a\x1b.PyRPC.ConversationResponseB\x06\xa2\x02\x03RTGb\x06proto3'
)



_CONVERSATIONRESPONSE_STATE = _descriptor.EnumDescriptor(
  name='State',
  full_name='PyRPC.ConversationResponse.State',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MODEL_ERR', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=317,
  serialized_end=365,
)
_sym_db.RegisterEnumDescriptor(_CONVERSATIONRESPONSE_STATE)


_TTSINPUT = _descriptor.Descriptor(
  name='TTSInput',
  full_name='PyRPC.TTSInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='PyRPC.TTSInput.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lang', full_name='PyRPC.TTSInput.lang', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=23,
  serialized_end=61,
)


_TTSOUTPUT = _descriptor.Descriptor(
  name='TTSOutput',
  full_name='PyRPC.TTSOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='PyRPC.TTSOutput.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=63,
  serialized_end=88,
)


_STTINPUT = _descriptor.Descriptor(
  name='STTInput',
  full_name='PyRPC.STTInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='PyRPC.STTInput.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=90,
  serialized_end=114,
)


_STTOUTPUT = _descriptor.Descriptor(
  name='STTOutput',
  full_name='PyRPC.STTOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='PyRPC.STTOutput.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lang', full_name='PyRPC.STTOutput.lang', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=116,
  serialized_end=155,
)


_CONVERSATIONINPUT = _descriptor.Descriptor(
  name='ConversationInput',
  full_name='PyRPC.ConversationInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trans_id', full_name='PyRPC.ConversationInput.trans_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text', full_name='PyRPC.ConversationInput.text', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=157,
  serialized_end=208,
)


_CONVERSATIONRESPONSE = _descriptor.Descriptor(
  name='ConversationResponse',
  full_name='PyRPC.ConversationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trans_id', full_name='PyRPC.ConversationResponse.trans_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='PyRPC.ConversationResponse.state', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text', full_name='PyRPC.ConversationResponse.text', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CONVERSATIONRESPONSE_STATE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=211,
  serialized_end=365,
)

_CONVERSATIONRESPONSE.fields_by_name['state'].enum_type = _CONVERSATIONRESPONSE_STATE
_CONVERSATIONRESPONSE_STATE.containing_type = _CONVERSATIONRESPONSE
DESCRIPTOR.message_types_by_name['TTSInput'] = _TTSINPUT
DESCRIPTOR.message_types_by_name['TTSOutput'] = _TTSOUTPUT
DESCRIPTOR.message_types_by_name['STTInput'] = _STTINPUT
DESCRIPTOR.message_types_by_name['STTOutput'] = _STTOUTPUT
DESCRIPTOR.message_types_by_name['ConversationInput'] = _CONVERSATIONINPUT
DESCRIPTOR.message_types_by_name['ConversationResponse'] = _CONVERSATIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TTSInput = _reflection.GeneratedProtocolMessageType('TTSInput', (_message.Message,), {
  'DESCRIPTOR' : _TTSINPUT,
  '__module__' : 'py_rpc_pb2'
  # @@protoc_insertion_point(class_scope:PyRPC.TTSInput)
  })
_sym_db.RegisterMessage(TTSInput)

TTSOutput = _reflection.GeneratedProtocolMessageType('TTSOutput', (_message.Message,), {
  'DESCRIPTOR' : _TTSOUTPUT,
  '__module__' : 'py_rpc_pb2'
  # @@protoc_insertion_point(class_scope:PyRPC.TTSOutput)
  })
_sym_db.RegisterMessage(TTSOutput)

STTInput = _reflection.GeneratedProtocolMessageType('STTInput', (_message.Message,), {
  'DESCRIPTOR' : _STTINPUT,
  '__module__' : 'py_rpc_pb2'
  # @@protoc_insertion_point(class_scope:PyRPC.STTInput)
  })
_sym_db.RegisterMessage(STTInput)

STTOutput = _reflection.GeneratedProtocolMessageType('STTOutput', (_message.Message,), {
  'DESCRIPTOR' : _STTOUTPUT,
  '__module__' : 'py_rpc_pb2'
  # @@protoc_insertion_point(class_scope:PyRPC.STTOutput)
  })
_sym_db.RegisterMessage(STTOutput)

ConversationInput = _reflection.GeneratedProtocolMessageType('ConversationInput', (_message.Message,), {
  'DESCRIPTOR' : _CONVERSATIONINPUT,
  '__module__' : 'py_rpc_pb2'
  # @@protoc_insertion_point(class_scope:PyRPC.ConversationInput)
  })
_sym_db.RegisterMessage(ConversationInput)

ConversationResponse = _reflection.GeneratedProtocolMessageType('ConversationResponse', (_message.Message,), {
  'DESCRIPTOR' : _CONVERSATIONRESPONSE,
  '__module__' : 'py_rpc_pb2'
  # @@protoc_insertion_point(class_scope:PyRPC.ConversationResponse)
  })
_sym_db.RegisterMessage(ConversationResponse)


DESCRIPTOR._options = None

_PYRPCSERVICE = _descriptor.ServiceDescriptor(
  name='PyRPCService',
  full_name='PyRPC.PyRPCService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=368,
  serialized_end=556,
  methods=[
  _descriptor.MethodDescriptor(
    name='TextToSpeech',
    full_name='PyRPC.PyRPCService.TextToSpeech',
    index=0,
    containing_service=None,
    input_type=_TTSINPUT,
    output_type=_TTSOUTPUT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SpeechToText',
    full_name='PyRPC.PyRPCService.SpeechToText',
    index=1,
    containing_service=None,
    input_type=_STTINPUT,
    output_type=_STTOUTPUT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RespondToText',
    full_name='PyRPC.PyRPCService.RespondToText',
    index=2,
    containing_service=None,
    input_type=_CONVERSATIONINPUT,
    output_type=_CONVERSATIONRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PYRPCSERVICE)

DESCRIPTOR.services_by_name['PyRPCService'] = _PYRPCSERVICE

# @@protoc_insertion_point(module_scope)
