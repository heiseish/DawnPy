# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: image_classification_service.proto

import sys
_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='image_classification_service.proto',
    package='ImageClassificationServiceRPC',
    syntax='proto3',
    serialized_options=_b('\242\002\003RTG'),
    serialized_pb=_b(
        '\n\"image_classification_service.proto\x12\x1dImageClassificationServiceRPC\"/\n\x0cImageRequest\x12\x10\n\x08trans_id\x18\x01 \x01(\t\x12\r\n\x05image\x18\x02 \x01(\t\"\xa4\x01\n\rImageResponse\x12\x10\n\x08trans_id\x18\x01 \x01(\t\x12\x41\n\x05state\x18\x02 \x01(\x0e\x32\x32.ImageClassificationServiceRPC.ImageResponse.State\x12\x0c\n\x04text\x18\x03 \x01(\t\"0\n\x05State\x12\x0b\n\x07SUCCESS\x10\x00\x12\r\n\tMODEL_ERR\x10\x01\x12\x0b\n\x07UNKNOWN\x10\x02\x32\x89\x01\n\x1aImageClassificationService\x12k\n\x0eRecognizeImage\x12+.ImageClassificationServiceRPC.ImageRequest\x1a,.ImageClassificationServiceRPC.ImageResponseB\x06\xa2\x02\x03RTGb\x06proto3'
    )
)

_IMAGERESPONSE_STATE = _descriptor.EnumDescriptor(
    name='State',
    full_name='ImageClassificationServiceRPC.ImageResponse.State',
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name='SUCCESS',
            index=0,
            number=0,
            serialized_options=None,
            type=None
        ),
        _descriptor.EnumValueDescriptor(
            name='MODEL_ERR',
            index=1,
            number=1,
            serialized_options=None,
            type=None
        ),
        _descriptor.EnumValueDescriptor(
            name='UNKNOWN',
            index=2,
            number=2,
            serialized_options=None,
            type=None
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=235,
    serialized_end=283,
)
_sym_db.RegisterEnumDescriptor(_IMAGERESPONSE_STATE)

_IMAGEREQUEST = _descriptor.Descriptor(
    name='ImageRequest',
    full_name='ImageClassificationServiceRPC.ImageRequest',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='trans_id',
            full_name='ImageClassificationServiceRPC.ImageRequest.trans_id',
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR
        ),
        _descriptor.FieldDescriptor(
            name='image',
            full_name='ImageClassificationServiceRPC.ImageRequest.image',
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=69,
    serialized_end=116,
)

_IMAGERESPONSE = _descriptor.Descriptor(
    name='ImageResponse',
    full_name='ImageClassificationServiceRPC.ImageResponse',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='trans_id',
            full_name='ImageClassificationServiceRPC.ImageResponse.trans_id',
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR
        ),
        _descriptor.FieldDescriptor(
            name='state',
            full_name='ImageClassificationServiceRPC.ImageResponse.state',
            index=1,
            number=2,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR
        ),
        _descriptor.FieldDescriptor(
            name='text',
            full_name='ImageClassificationServiceRPC.ImageResponse.text',
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[
        _IMAGERESPONSE_STATE,
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=119,
    serialized_end=283,
)

_IMAGERESPONSE.fields_by_name['state'].enum_type = _IMAGERESPONSE_STATE
_IMAGERESPONSE_STATE.containing_type = _IMAGERESPONSE
DESCRIPTOR.message_types_by_name['ImageRequest'] = _IMAGEREQUEST
DESCRIPTOR.message_types_by_name['ImageResponse'] = _IMAGERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ImageRequest = _reflection.GeneratedProtocolMessageType(
    'ImageRequest',
    (_message.Message, ),
    {
        'DESCRIPTOR': _IMAGEREQUEST,
        '__module__': 'image_classification_service_pb2'
        # @@protoc_insertion_point(class_scope:ImageClassificationServiceRPC.ImageRequest)
    }
)
_sym_db.RegisterMessage(ImageRequest)

ImageResponse = _reflection.GeneratedProtocolMessageType(
    'ImageResponse',
    (_message.Message, ),
    {
        'DESCRIPTOR': _IMAGERESPONSE,
        '__module__': 'image_classification_service_pb2'
        # @@protoc_insertion_point(class_scope:ImageClassificationServiceRPC.ImageResponse)
    }
)
_sym_db.RegisterMessage(ImageResponse)

DESCRIPTOR._options = None

_IMAGECLASSIFICATIONSERVICE = _descriptor.ServiceDescriptor(
    name='ImageClassificationService',
    full_name='ImageClassificationServiceRPC.ImageClassificationService',
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    serialized_start=286,
    serialized_end=423,
    methods=[
        _descriptor.MethodDescriptor(
            name='RecognizeImage',
            full_name=
            'ImageClassificationServiceRPC.ImageClassificationService.RecognizeImage',
            index=0,
            containing_service=None,
            input_type=_IMAGEREQUEST,
            output_type=_IMAGERESPONSE,
            serialized_options=None,
        ),
    ]
)
_sym_db.RegisterServiceDescriptor(_IMAGECLASSIFICATIONSERVICE)

DESCRIPTOR.services_by_name['ImageClassificationService'
                           ] = _IMAGECLASSIFICATIONSERVICE

# @@protoc_insertion_point(module_scope)
