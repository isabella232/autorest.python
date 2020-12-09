# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Dict, Optional

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class PetAPTrue(msrest.serialization.Model):
    """PetAPTrue.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param id: Required.
    :type id: int
    :param name:
    :type name: str
    :ivar status:
    :vartype status: bool
    """

    _validation = {
        'id': {'required': True},
        'status': {'readonly': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'status': {'key': 'status', 'type': 'bool'},
    }

    def __init__(
        self,
        *,
        id: int,
        additional_properties: Optional[Dict[str, object]] = None,
        name: Optional[str] = None,
        **kwargs: Any
    ):
        super(PetAPTrue, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.id = id
        self.name = name
        self.status = None


class CatAPTrue(PetAPTrue):
    """CatAPTrue.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param id: Required.
    :type id: int
    :param name:
    :type name: str
    :ivar status:
    :vartype status: bool
    :param friendly:
    :type friendly: bool
    """

    _validation = {
        'id': {'required': True},
        'status': {'readonly': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'status': {'key': 'status', 'type': 'bool'},
        'friendly': {'key': 'friendly', 'type': 'bool'},
    }

    def __init__(
        self,
        *,
        id: int,
        additional_properties: Optional[Dict[str, object]] = None,
        name: Optional[str] = None,
        friendly: Optional[bool] = None,
        **kwargs: Any
    ):
        super(CatAPTrue, self).__init__(additional_properties=additional_properties, id=id, name=name, **kwargs)
        self.friendly = friendly


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


class PetAPInProperties(msrest.serialization.Model):
    """PetAPInProperties.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param id: Required.
    :type id: int
    :param name:
    :type name: str
    :ivar status:
    :vartype status: bool
    :param additional_properties: Dictionary of :code:`<number>`.
    :type additional_properties: dict[str, float]
    """

    _validation = {
        'id': {'required': True},
        'status': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'status': {'key': 'status', 'type': 'bool'},
        'additional_properties': {'key': 'additionalProperties', 'type': '{float}'},
    }

    def __init__(
        self,
        *,
        id: int,
        name: Optional[str] = None,
        additional_properties: Optional[Dict[str, float]] = None,
        **kwargs: Any
    ):
        super(PetAPInProperties, self).__init__(**kwargs)
        self.id = id
        self.name = name
        self.status = None
        self.additional_properties = additional_properties


class PetAPInPropertiesWithAPString(msrest.serialization.Model):
    """PetAPInPropertiesWithAPString.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, str]
    :param id: Required.
    :type id: int
    :param name:
    :type name: str
    :ivar status:
    :vartype status: bool
    :param odata_location: Required.
    :type odata_location: str
    :param additional_properties1: Dictionary of :code:`<number>`.
    :type additional_properties1: dict[str, float]
    """

    _validation = {
        'id': {'required': True},
        'status': {'readonly': True},
        'odata_location': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{str}'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'status': {'key': 'status', 'type': 'bool'},
        'odata_location': {'key': '@odata\\.location', 'type': 'str'},
        'additional_properties1': {'key': 'additionalProperties', 'type': '{float}'},
    }

    def __init__(
        self,
        *,
        id: int,
        odata_location: str,
        additional_properties: Optional[Dict[str, str]] = None,
        name: Optional[str] = None,
        additional_properties1: Optional[Dict[str, float]] = None,
        **kwargs: Any
    ):
        super(PetAPInPropertiesWithAPString, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.id = id
        self.name = name
        self.status = None
        self.odata_location = odata_location
        self.additional_properties1 = additional_properties1


class PetAPObject(msrest.serialization.Model):
    """PetAPObject.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param id: Required.
    :type id: int
    :param name:
    :type name: str
    :ivar status:
    :vartype status: bool
    """

    _validation = {
        'id': {'required': True},
        'status': {'readonly': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'status': {'key': 'status', 'type': 'bool'},
    }

    def __init__(
        self,
        *,
        id: int,
        additional_properties: Optional[Dict[str, object]] = None,
        name: Optional[str] = None,
        **kwargs: Any
    ):
        super(PetAPObject, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.id = id
        self.name = name
        self.status = None


class PetAPString(msrest.serialization.Model):
    """PetAPString.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, str]
    :param id: Required.
    :type id: int
    :param name:
    :type name: str
    :ivar status:
    :vartype status: bool
    """

    _validation = {
        'id': {'required': True},
        'status': {'readonly': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{str}'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'status': {'key': 'status', 'type': 'bool'},
    }

    def __init__(
        self,
        *,
        id: int,
        additional_properties: Optional[Dict[str, str]] = None,
        name: Optional[str] = None,
        **kwargs: Any
    ):
        super(PetAPString, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.id = id
        self.name = name
        self.status = None
