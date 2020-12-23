# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import msrest.serialization


class Product(msrest.serialization.Model):
    """Product.

    :param properties:
    :type properties: ~pagingspecial.models.ProductProperties
    """

    _attribute_map = {
        'properties': {'key': 'properties', 'type': 'ProductProperties'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Product, self).__init__(**kwargs)
        self.properties = kwargs.get('properties', None)


class ProductProperties(msrest.serialization.Model):
    """ProductProperties.

    :param name:
    :type name: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ProductProperties, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)


class ProductResultValue(msrest.serialization.Model):
    """ProductResultValue.

    :param value:
    :type value: list[~pagingspecial.models.Product]
    :param next_link:
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Product]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ProductResultValue, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = kwargs.get('next_link', None)


class ProductResultValueWithToken(msrest.serialization.Model):
    """ProductResultValueWithToken.

    :param value:
    :type value: list[~pagingspecial.models.Product]
    :param token:
    :type token: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Product]'},
        'token': {'key': 'token', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ProductResultValueWithToken, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.token = kwargs.get('token', None)