# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: otel_python_grpc_nested_spans/sleeper.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+otel_python_grpc_nested_spans/sleeper.proto\x12-github.com.erichulburd.otel_grpc_nested_spans\"\x1e\n\x0cSleepRequest\x12\x0e\n\x06\x61mount\x18\x01 \x01(\x02\"\x1f\n\rSleepResponse\x12\x0e\n\x06\x61mount\x18\x01 \x01(\x02\x32\x90\x01\n\x07Sleeper\x12\x84\x01\n\x05Sleep\x12;.github.com.erichulburd.otel_grpc_nested_spans.SleepRequest\x1a<.github.com.erichulburd.otel_grpc_nested_spans.SleepResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'otel_python_grpc_nested_spans.sleeper_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SLEEPREQUEST._serialized_start=94
  _SLEEPREQUEST._serialized_end=124
  _SLEEPRESPONSE._serialized_start=126
  _SLEEPRESPONSE._serialized_end=157
  _SLEEPER._serialized_start=160
  _SLEEPER._serialized_end=304
# @@protoc_insertion_point(module_scope)