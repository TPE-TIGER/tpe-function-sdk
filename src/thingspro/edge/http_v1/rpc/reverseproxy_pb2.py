# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: reverseproxy.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='reverseproxy.proto',
  package='trigger',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12reverseproxy.proto\x12\x07trigger\"+\n\x07Profile\x12\x0e\n\x06method\x18\x01 \x01(\t\x12\x10\n\x08\x65ndpoint\x18\x02 \x01(\t\"=\n\x07Request\x12\x0f\n\x07headers\x18\x01 \x01(\t\x12\x0f\n\x07payload\x18\x02 \x01(\t\x12\x10\n\x08resource\x18\x03 \x01(\t\"Z\n\x05Reply\x12!\n\x07profile\x18\x01 \x01(\x0b\x32\x10.trigger.Profile\x12\x0f\n\x07headers\x18\x02 \x01(\t\x12\x0f\n\x07payload\x18\x03 \x01(\t\x12\x0c\n\x04\x63ode\x18\x04 \x01(\x04\x32k\n\x07Trigger\x12\x30\n\x08Register\x12\x10.trigger.Profile\x1a\x10.trigger.Profile\"\x00\x12.\n\x04\x46ire\x12\x0e.trigger.Reply\x1a\x10.trigger.Request\"\x00(\x01\x30\x01\x62\x06proto3'
)




_PROFILE = _descriptor.Descriptor(
  name='Profile',
  full_name='trigger.Profile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='method', full_name='trigger.Profile.method', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='endpoint', full_name='trigger.Profile.endpoint', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=31,
  serialized_end=74,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='trigger.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='headers', full_name='trigger.Request.headers', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='payload', full_name='trigger.Request.payload', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resource', full_name='trigger.Request.resource', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=76,
  serialized_end=137,
)


_REPLY = _descriptor.Descriptor(
  name='Reply',
  full_name='trigger.Reply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='profile', full_name='trigger.Reply.profile', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='headers', full_name='trigger.Reply.headers', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='payload', full_name='trigger.Reply.payload', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='code', full_name='trigger.Reply.code', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=139,
  serialized_end=229,
)

_REPLY.fields_by_name['profile'].message_type = _PROFILE
DESCRIPTOR.message_types_by_name['Profile'] = _PROFILE
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Reply'] = _REPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Profile = _reflection.GeneratedProtocolMessageType('Profile', (_message.Message,), {
  'DESCRIPTOR' : _PROFILE,
  '__module__' : 'reverseproxy_pb2'
  # @@protoc_insertion_point(class_scope:trigger.Profile)
  })
_sym_db.RegisterMessage(Profile)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'reverseproxy_pb2'
  # @@protoc_insertion_point(class_scope:trigger.Request)
  })
_sym_db.RegisterMessage(Request)

Reply = _reflection.GeneratedProtocolMessageType('Reply', (_message.Message,), {
  'DESCRIPTOR' : _REPLY,
  '__module__' : 'reverseproxy_pb2'
  # @@protoc_insertion_point(class_scope:trigger.Reply)
  })
_sym_db.RegisterMessage(Reply)



_TRIGGER = _descriptor.ServiceDescriptor(
  name='Trigger',
  full_name='trigger.Trigger',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=231,
  serialized_end=338,
  methods=[
  _descriptor.MethodDescriptor(
    name='Register',
    full_name='trigger.Trigger.Register',
    index=0,
    containing_service=None,
    input_type=_PROFILE,
    output_type=_PROFILE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Fire',
    full_name='trigger.Trigger.Fire',
    index=1,
    containing_service=None,
    input_type=_REPLY,
    output_type=_REQUEST,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TRIGGER)

DESCRIPTOR.services_by_name['Trigger'] = _TRIGGER

# @@protoc_insertion_point(module_scope)
