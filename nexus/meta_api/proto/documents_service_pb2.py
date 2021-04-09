# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nexus/meta_api/proto/documents_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from nexus.models.proto import \
    typed_document_pb2 as nexus_dot_models_dot_proto_dot_typed__document__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
  name='nexus/meta_api/proto/documents_service.proto',
  package='nexus.meta_api.proto',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n,nexus/meta_api/proto/documents_service.proto\x12\x14nexus.meta_api.proto\x1a\'nexus/models/proto/typed_document.proto\"D\n\x0bRollRequest\x12\x10\n\x08language\x18\x01 \x01(\t\x12\x12\n\nsession_id\x18\x02 \x01(\t\x12\x0f\n\x07user_id\x18\x03 \x01(\x03\"#\n\x0cRollResponse\x12\x13\n\x0b\x64ocument_id\x18\x01 \x01(\x04\"r\n\x14TypedDocumentRequest\x12\x0e\n\x06schema\x18\x01 \x01(\t\x12\x13\n\x0b\x64ocument_id\x18\x02 \x01(\x04\x12\x10\n\x08position\x18\x03 \x01(\r\x12\x12\n\nsession_id\x18\x04 \x01(\t\x12\x0f\n\x07user_id\x18\x05 \x01(\x03\"\x1a\n\x18PutTypedDocumentResponse2\xb4\x01\n\tDocuments\x12V\n\x03get\x12*.nexus.meta_api.proto.TypedDocumentRequest\x1a!.nexus.models.proto.TypedDocument\"\x00\x12O\n\x04roll\x12!.nexus.meta_api.proto.RollRequest\x1a\".nexus.meta_api.proto.RollResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[nexus_dot_models_dot_proto_dot_typed__document__pb2.DESCRIPTOR,])




_ROLLREQUEST = _descriptor.Descriptor(
  name='RollRequest',
  full_name='nexus.meta_api.proto.RollRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='language', full_name='nexus.meta_api.proto.RollRequest.language', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='session_id', full_name='nexus.meta_api.proto.RollRequest.session_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='nexus.meta_api.proto.RollRequest.user_id', index=2,
      number=3, type=3, cpp_type=2, label=1,
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
  serialized_start=111,
  serialized_end=179,
)


_ROLLRESPONSE = _descriptor.Descriptor(
  name='RollResponse',
  full_name='nexus.meta_api.proto.RollResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='document_id', full_name='nexus.meta_api.proto.RollResponse.document_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
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
  serialized_start=181,
  serialized_end=216,
)


_TYPEDDOCUMENTREQUEST = _descriptor.Descriptor(
  name='TypedDocumentRequest',
  full_name='nexus.meta_api.proto.TypedDocumentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='schema', full_name='nexus.meta_api.proto.TypedDocumentRequest.schema', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='document_id', full_name='nexus.meta_api.proto.TypedDocumentRequest.document_id', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='position', full_name='nexus.meta_api.proto.TypedDocumentRequest.position', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='session_id', full_name='nexus.meta_api.proto.TypedDocumentRequest.session_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='nexus.meta_api.proto.TypedDocumentRequest.user_id', index=4,
      number=5, type=3, cpp_type=2, label=1,
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
  serialized_start=218,
  serialized_end=332,
)


_PUTTYPEDDOCUMENTRESPONSE = _descriptor.Descriptor(
  name='PutTypedDocumentResponse',
  full_name='nexus.meta_api.proto.PutTypedDocumentResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=334,
  serialized_end=360,
)

DESCRIPTOR.message_types_by_name['RollRequest'] = _ROLLREQUEST
DESCRIPTOR.message_types_by_name['RollResponse'] = _ROLLRESPONSE
DESCRIPTOR.message_types_by_name['TypedDocumentRequest'] = _TYPEDDOCUMENTREQUEST
DESCRIPTOR.message_types_by_name['PutTypedDocumentResponse'] = _PUTTYPEDDOCUMENTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RollRequest = _reflection.GeneratedProtocolMessageType('RollRequest', (_message.Message,), {
  'DESCRIPTOR' : _ROLLREQUEST,
  '__module__' : 'nexus.meta_api.proto.documents_service_pb2'
  # @@protoc_insertion_point(class_scope:nexus.meta_api.proto.RollRequest)
  })
_sym_db.RegisterMessage(RollRequest)

RollResponse = _reflection.GeneratedProtocolMessageType('RollResponse', (_message.Message,), {
  'DESCRIPTOR' : _ROLLRESPONSE,
  '__module__' : 'nexus.meta_api.proto.documents_service_pb2'
  # @@protoc_insertion_point(class_scope:nexus.meta_api.proto.RollResponse)
  })
_sym_db.RegisterMessage(RollResponse)

TypedDocumentRequest = _reflection.GeneratedProtocolMessageType('TypedDocumentRequest', (_message.Message,), {
  'DESCRIPTOR' : _TYPEDDOCUMENTREQUEST,
  '__module__' : 'nexus.meta_api.proto.documents_service_pb2'
  # @@protoc_insertion_point(class_scope:nexus.meta_api.proto.TypedDocumentRequest)
  })
_sym_db.RegisterMessage(TypedDocumentRequest)

PutTypedDocumentResponse = _reflection.GeneratedProtocolMessageType('PutTypedDocumentResponse', (_message.Message,), {
  'DESCRIPTOR' : _PUTTYPEDDOCUMENTRESPONSE,
  '__module__' : 'nexus.meta_api.proto.documents_service_pb2'
  # @@protoc_insertion_point(class_scope:nexus.meta_api.proto.PutTypedDocumentResponse)
  })
_sym_db.RegisterMessage(PutTypedDocumentResponse)



_DOCUMENTS = _descriptor.ServiceDescriptor(
  name='Documents',
  full_name='nexus.meta_api.proto.Documents',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=363,
  serialized_end=543,
  methods=[
  _descriptor.MethodDescriptor(
    name='get',
    full_name='nexus.meta_api.proto.Documents.get',
    index=0,
    containing_service=None,
    input_type=_TYPEDDOCUMENTREQUEST,
    output_type=nexus_dot_models_dot_proto_dot_typed__document__pb2._TYPEDDOCUMENT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='roll',
    full_name='nexus.meta_api.proto.Documents.roll',
    index=1,
    containing_service=None,
    input_type=_ROLLREQUEST,
    output_type=_ROLLRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DOCUMENTS)

DESCRIPTOR.services_by_name['Documents'] = _DOCUMENTS

# @@protoc_insertion_point(module_scope)
