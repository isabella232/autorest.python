# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, IO, List, Optional

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class Error(msrest.serialization.Model):
    """Error.

    :param status:
    :type status: int
    :param message:
    :type message: str
    """

    _attribute_map = {
        'status': {'key': 'status', 'type': 'int'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        status: Optional[int] = None,
        message: Optional[str] = None,
        **kwargs: Any
    ):
        super(Error, self).__init__(**kwargs)
        self.status = status
        self.message = message


class Paths1MqqetpFormdataStreamUploadfilePostRequestbodyContentMultipartFormDataSchema(msrest.serialization.Model):
    """Paths1MqqetpFormdataStreamUploadfilePostRequestbodyContentMultipartFormDataSchema.

    All required parameters must be populated in order to send to Azure.

    :param file_content: Required. File to upload.
    :type file_content: IO
    :param file_name: Required. File name to upload. Name has to be spelled exactly as written
     here.
    :type file_name: str
    """

    _validation = {
        'file_content': {'required': True},
        'file_name': {'required': True},
    }

    _attribute_map = {
        'file_content': {'key': 'fileContent', 'type': 'IO'},
        'file_name': {'key': 'fileName', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        file_content: IO,
        file_name: str,
        **kwargs: Any
    ):
        super(Paths1MqqetpFormdataStreamUploadfilePostRequestbodyContentMultipartFormDataSchema, self).__init__(**kwargs)
        self.file_content = file_content
        self.file_name = file_name


class Paths1P3Stk3FormdataStreamUploadfilesPostRequestbodyContentMultipartFormDataSchema(msrest.serialization.Model):
    """Paths1P3Stk3FormdataStreamUploadfilesPostRequestbodyContentMultipartFormDataSchema.

    All required parameters must be populated in order to send to Azure.

    :param file_content: Required. Files to upload.
    :type file_content: list[IO]
    """

    _validation = {
        'file_content': {'required': True},
    }

    _attribute_map = {
        'file_content': {'key': 'fileContent', 'type': '[IO]'},
    }

    def __init__(
        self,
        *,
        file_content: List[IO],
        **kwargs: Any
    ):
        super(Paths1P3Stk3FormdataStreamUploadfilesPostRequestbodyContentMultipartFormDataSchema, self).__init__(**kwargs)
        self.file_content = file_content
