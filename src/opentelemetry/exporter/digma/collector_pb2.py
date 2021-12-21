# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: collector.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='collector.proto',
  package='collector',
  syntax='proto3',
  serialized_options=b'\252\002\017digma_collector',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0f\x63ollector.proto\x12\tcollector\"\xf3\x01\n\rExportRequest\x12\x0f\n\x07span_id\x18\x01 \x01(\t\x12\x10\n\x08trace_id\x18\x02 \x01(\t\x12\x14\n\x0cservice_name\x18\x03 \x01(\t\x12\x39\n\x06\x65rrors\x18\x04 \x03(\x0b\x32).collector.ExportRequest.ErrorInformation\x1an\n\x10\x45rrorInformation\x12\x16\n\x0e\x65xception_name\x18\x01 \x01(\t\x12\x16\n\x0e\x65xception_type\x18\x02 \x01(\t\x12\x17\n\x0f\x65xception_stack\x18\x03 \x01(\t\x12\x11\n\ttimestamp\x18\x04 \x01(\t\"!\n\x0e\x45xportResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2O\n\x0e\x44igmaCollector\x12=\n\x06\x45xport\x12\x18.collector.ExportRequest\x1a\x19.collector.ExportResponseB\x12\xaa\x02\x0f\x64igma_collectorb\x06proto3'
)




_EXPORTREQUEST_ERRORINFORMATION = _descriptor.Descriptor(
  name='ErrorInformation',
  full_name='collector.ExportRequest.ErrorInformation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='exception_name', full_name='collector.ExportRequest.ErrorInformation.exception_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='exception_type', full_name='collector.ExportRequest.ErrorInformation.exception_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='exception_stack', full_name='collector.ExportRequest.ErrorInformation.exception_stack', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='collector.ExportRequest.ErrorInformation.timestamp', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=164,
  serialized_end=274,
)

_EXPORTREQUEST = _descriptor.Descriptor(
  name='ExportRequest',
  full_name='collector.ExportRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='span_id', full_name='collector.ExportRequest.span_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='trace_id', full_name='collector.ExportRequest.trace_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='service_name', full_name='collector.ExportRequest.service_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='errors', full_name='collector.ExportRequest.errors', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_EXPORTREQUEST_ERRORINFORMATION, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=31,
  serialized_end=274,
)


_EXPORTRESPONSE = _descriptor.Descriptor(
  name='ExportResponse',
  full_name='collector.ExportResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='collector.ExportResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=276,
  serialized_end=309,
)

_EXPORTREQUEST_ERRORINFORMATION.containing_type = _EXPORTREQUEST
_EXPORTREQUEST.fields_by_name['errors'].message_type = _EXPORTREQUEST_ERRORINFORMATION
DESCRIPTOR.message_types_by_name['ExportRequest'] = _EXPORTREQUEST
DESCRIPTOR.message_types_by_name['ExportResponse'] = _EXPORTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ExportRequest = _reflection.GeneratedProtocolMessageType('ExportRequest', (_message.Message,), {

  'ErrorInformation' : _reflection.GeneratedProtocolMessageType('ErrorInformation', (_message.Message,), {
    'DESCRIPTOR' : _EXPORTREQUEST_ERRORINFORMATION,
    '__module__' : 'collector_pb2'
    # @@protoc_insertion_point(class_scope:collector.ExportRequest.ErrorInformation)
    })
  ,
  'DESCRIPTOR' : _EXPORTREQUEST,
  '__module__' : 'collector_pb2'
  # @@protoc_insertion_point(class_scope:collector.ExportRequest)
  })
_sym_db.RegisterMessage(ExportRequest)
_sym_db.RegisterMessage(ExportRequest.ErrorInformation)

ExportResponse = _reflection.GeneratedProtocolMessageType('ExportResponse', (_message.Message,), {
  'DESCRIPTOR' : _EXPORTRESPONSE,
  '__module__' : 'collector_pb2'
  # @@protoc_insertion_point(class_scope:collector.ExportResponse)
  })
_sym_db.RegisterMessage(ExportResponse)


DESCRIPTOR._options = None

_DIGMACOLLECTOR = _descriptor.ServiceDescriptor(
  name='DigmaCollector',
  full_name='collector.DigmaCollector',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=311,
  serialized_end=390,
  methods=[
  _descriptor.MethodDescriptor(
    name='Export',
    full_name='collector.DigmaCollector.Export',
    index=0,
    containing_service=None,
    input_type=_EXPORTREQUEST,
    output_type=_EXPORTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DIGMACOLLECTOR)

DESCRIPTOR.services_by_name['DigmaCollector'] = _DIGMACOLLECTOR

# @@protoc_insertion_point(module_scope)
