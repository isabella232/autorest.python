# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional

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


class Product(msrest.serialization.Model):
    """Product.

    :param integer:
    :type integer: int
    :param string:
    :type string: str
    """

    _attribute_map = {
        'integer': {'key': 'integer', 'type': 'int'},
        'string': {'key': 'string', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        integer: Optional[int] = None,
        string: Optional[str] = None,
        **kwargs: Any
    ):
        super(Product, self).__init__(**kwargs)
        self.integer = integer
        self.string = string
