# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, List, Optional, Union

import msrest.serialization

from ._auto_rest_paging_test_service_enums import *


class CustomParameterGroup(msrest.serialization.Model):
    """Parameter group.

    All required parameters must be populated in order to send to Azure.

    :param api_version: Required. Sets the api version to use.
    :type api_version: str
    :param tenant: Required. Sets the tenant to use.
    :type tenant: str
    """

    _validation = {
        'api_version': {'required': True},
        'tenant': {'required': True},
    }

    _attribute_map = {
        'api_version': {'key': 'api_version', 'type': 'str'},
        'tenant': {'key': 'tenant', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        api_version: str,
        tenant: str,
        **kwargs: Any
    ):
        super(CustomParameterGroup, self).__init__(**kwargs)
        self.api_version = api_version
        self.tenant = tenant


class OdataProductResult(msrest.serialization.Model):
    """OdataProductResult.

    :param values:
    :type values: list[~custompollerpager.models.Product]
    :param odata_next_link:
    :type odata_next_link: str
    """

    _attribute_map = {
        'values': {'key': 'values', 'type': '[Product]'},
        'odata_next_link': {'key': 'odata\\.nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        values: Optional[List["Product"]] = None,
        odata_next_link: Optional[str] = None,
        **kwargs: Any
    ):
        super(OdataProductResult, self).__init__(**kwargs)
        self.values = values
        self.odata_next_link = odata_next_link


class OperationResult(msrest.serialization.Model):
    """OperationResult.

    :param status: The status of the request. Possible values include: "Succeeded", "Failed",
     "canceled", "Accepted", "Creating", "Created", "Updating", "Updated", "Deleting", "Deleted",
     "OK".
    :type status: str or ~custompollerpager.models.OperationResultStatus
    """

    _attribute_map = {
        'status': {'key': 'status', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        status: Optional[Union[str, "OperationResultStatus"]] = None,
        **kwargs: Any
    ):
        super(OperationResult, self).__init__(**kwargs)
        self.status = status


class PagingGetMultiplePagesLroOptions(msrest.serialization.Model):
    """Parameter group.

    :param maxresults: Sets the maximum number of items to return in the response.
    :type maxresults: int
    :param timeout: Sets the maximum time that the server can spend processing the request, in
     seconds. The default is 30 seconds.
    :type timeout: int
    """

    _attribute_map = {
        'maxresults': {'key': 'maxresults', 'type': 'int'},
        'timeout': {'key': 'timeout', 'type': 'int'},
    }

    def __init__(
        self,
        *,
        maxresults: Optional[int] = None,
        timeout: Optional[int] = 30,
        **kwargs: Any
    ):
        super(PagingGetMultiplePagesLroOptions, self).__init__(**kwargs)
        self.maxresults = maxresults
        self.timeout = timeout


class PagingGetMultiplePagesOptions(msrest.serialization.Model):
    """Parameter group.

    :param maxresults: Sets the maximum number of items to return in the response.
    :type maxresults: int
    :param timeout: Sets the maximum time that the server can spend processing the request, in
     seconds. The default is 30 seconds.
    :type timeout: int
    """

    _attribute_map = {
        'maxresults': {'key': 'maxresults', 'type': 'int'},
        'timeout': {'key': 'timeout', 'type': 'int'},
    }

    def __init__(
        self,
        *,
        maxresults: Optional[int] = None,
        timeout: Optional[int] = 30,
        **kwargs: Any
    ):
        super(PagingGetMultiplePagesOptions, self).__init__(**kwargs)
        self.maxresults = maxresults
        self.timeout = timeout


class PagingGetMultiplePagesWithOffsetOptions(msrest.serialization.Model):
    """Parameter group.

    All required parameters must be populated in order to send to Azure.

    :param maxresults: Sets the maximum number of items to return in the response.
    :type maxresults: int
    :param offset: Required. Offset of return value.
    :type offset: int
    :param timeout: Sets the maximum time that the server can spend processing the request, in
     seconds. The default is 30 seconds.
    :type timeout: int
    """

    _validation = {
        'offset': {'required': True},
    }

    _attribute_map = {
        'maxresults': {'key': 'maxresults', 'type': 'int'},
        'offset': {'key': 'offset', 'type': 'int'},
        'timeout': {'key': 'timeout', 'type': 'int'},
    }

    def __init__(
        self,
        *,
        offset: int,
        maxresults: Optional[int] = None,
        timeout: Optional[int] = 30,
        **kwargs: Any
    ):
        super(PagingGetMultiplePagesWithOffsetOptions, self).__init__(**kwargs)
        self.maxresults = maxresults
        self.offset = offset
        self.timeout = timeout


class PagingGetOdataMultiplePagesOptions(msrest.serialization.Model):
    """Parameter group.

    :param maxresults: Sets the maximum number of items to return in the response.
    :type maxresults: int
    :param timeout: Sets the maximum time that the server can spend processing the request, in
     seconds. The default is 30 seconds.
    :type timeout: int
    """

    _attribute_map = {
        'maxresults': {'key': 'maxresults', 'type': 'int'},
        'timeout': {'key': 'timeout', 'type': 'int'},
    }

    def __init__(
        self,
        *,
        maxresults: Optional[int] = None,
        timeout: Optional[int] = 30,
        **kwargs: Any
    ):
        super(PagingGetOdataMultiplePagesOptions, self).__init__(**kwargs)
        self.maxresults = maxresults
        self.timeout = timeout


class Product(msrest.serialization.Model):
    """Product.

    :param properties:
    :type properties: ~custompollerpager.models.ProductProperties
    """

    _attribute_map = {
        'properties': {'key': 'properties', 'type': 'ProductProperties'},
    }

    def __init__(
        self,
        *,
        properties: Optional["ProductProperties"] = None,
        **kwargs: Any
    ):
        super(Product, self).__init__(**kwargs)
        self.properties = properties


class ProductProperties(msrest.serialization.Model):
    """ProductProperties.

    :param id:
    :type id: int
    :param name:
    :type name: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        id: Optional[int] = None,
        name: Optional[str] = None,
        **kwargs: Any
    ):
        super(ProductProperties, self).__init__(**kwargs)
        self.id = id
        self.name = name


class ProductResult(msrest.serialization.Model):
    """ProductResult.

    :param values:
    :type values: list[~custompollerpager.models.Product]
    :param next_link:
    :type next_link: str
    """

    _attribute_map = {
        'values': {'key': 'values', 'type': '[Product]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        values: Optional[List["Product"]] = None,
        next_link: Optional[str] = None,
        **kwargs: Any
    ):
        super(ProductResult, self).__init__(**kwargs)
        self.values = values
        self.next_link = next_link


class ProductResultValue(msrest.serialization.Model):
    """ProductResultValue.

    :param value:
    :type value: list[~custompollerpager.models.Product]
    :param next_link:
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Product]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["Product"]] = None,
        next_link: Optional[str] = None,
        **kwargs: Any
    ):
        super(ProductResultValue, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class ProductResultValueWithXMSClientName(msrest.serialization.Model):
    """ProductResultValueWithXMSClientName.

    :param indexes:
    :type indexes: list[~custompollerpager.models.Product]
    :param next_link:
    :type next_link: str
    """

    _attribute_map = {
        'indexes': {'key': 'values', 'type': '[Product]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        indexes: Optional[List["Product"]] = None,
        next_link: Optional[str] = None,
        **kwargs: Any
    ):
        super(ProductResultValueWithXMSClientName, self).__init__(**kwargs)
        self.indexes = indexes
        self.next_link = next_link
