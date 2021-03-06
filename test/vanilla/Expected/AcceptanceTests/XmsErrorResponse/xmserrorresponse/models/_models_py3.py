# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Optional

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class Animal(msrest.serialization.Model):
    """Animal.

    :param ani_type:
    :type ani_type: str
    """

    _attribute_map = {
        'ani_type': {'key': 'aniType', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        ani_type: Optional[str] = None,
        **kwargs
    ):
        super(Animal, self).__init__(**kwargs)
        self.ani_type = ani_type


class BaseError(msrest.serialization.Model):
    """BaseError.

    :param some_base_prop:
    :type some_base_prop: str
    """

    _attribute_map = {
        'some_base_prop': {'key': 'someBaseProp', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        some_base_prop: Optional[str] = None,
        **kwargs
    ):
        super(BaseError, self).__init__(**kwargs)
        self.some_base_prop = some_base_prop


class NotFoundErrorBase(BaseError):
    """NotFoundErrorBase.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: AnimalNotFound, LinkNotFound.

    All required parameters must be populated in order to send to Azure.

    :param some_base_prop:
    :type some_base_prop: str
    :param reason:
    :type reason: str
    :param what_not_found: Required. Constant filled by server.
    :type what_not_found: str
    """

    _validation = {
        'what_not_found': {'required': True},
    }

    _attribute_map = {
        'some_base_prop': {'key': 'someBaseProp', 'type': 'str'},
        'reason': {'key': 'reason', 'type': 'str'},
        'what_not_found': {'key': 'whatNotFound', 'type': 'str'},
    }

    _subtype_map = {
        'what_not_found': {'AnimalNotFound': 'AnimalNotFound', 'InvalidResourceLink': 'LinkNotFound'}
    }

    def __init__(
        self,
        *,
        some_base_prop: Optional[str] = None,
        reason: Optional[str] = None,
        **kwargs
    ):
        super(NotFoundErrorBase, self).__init__(some_base_prop=some_base_prop, **kwargs)
        self.reason = reason
        self.what_not_found = 'NotFoundErrorBase'  # type: str


class AnimalNotFound(NotFoundErrorBase):
    """AnimalNotFound.

    All required parameters must be populated in order to send to Azure.

    :param some_base_prop:
    :type some_base_prop: str
    :param reason:
    :type reason: str
    :param what_not_found: Required. Constant filled by server.
    :type what_not_found: str
    :param name:
    :type name: str
    """

    _validation = {
        'what_not_found': {'required': True},
    }

    _attribute_map = {
        'some_base_prop': {'key': 'someBaseProp', 'type': 'str'},
        'reason': {'key': 'reason', 'type': 'str'},
        'what_not_found': {'key': 'whatNotFound', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        some_base_prop: Optional[str] = None,
        reason: Optional[str] = None,
        name: Optional[str] = None,
        **kwargs
    ):
        super(AnimalNotFound, self).__init__(some_base_prop=some_base_prop, reason=reason, **kwargs)
        self.what_not_found = 'AnimalNotFound'  # type: str
        self.name = name


class LinkNotFound(NotFoundErrorBase):
    """LinkNotFound.

    All required parameters must be populated in order to send to Azure.

    :param some_base_prop:
    :type some_base_prop: str
    :param reason:
    :type reason: str
    :param what_not_found: Required. Constant filled by server.
    :type what_not_found: str
    :param what_sub_address:
    :type what_sub_address: str
    """

    _validation = {
        'what_not_found': {'required': True},
    }

    _attribute_map = {
        'some_base_prop': {'key': 'someBaseProp', 'type': 'str'},
        'reason': {'key': 'reason', 'type': 'str'},
        'what_not_found': {'key': 'whatNotFound', 'type': 'str'},
        'what_sub_address': {'key': 'whatSubAddress', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        some_base_prop: Optional[str] = None,
        reason: Optional[str] = None,
        what_sub_address: Optional[str] = None,
        **kwargs
    ):
        super(LinkNotFound, self).__init__(some_base_prop=some_base_prop, reason=reason, **kwargs)
        self.what_not_found = 'InvalidResourceLink'  # type: str
        self.what_sub_address = what_sub_address


class Pet(Animal):
    """Pet.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param ani_type:
    :type ani_type: str
    :ivar name: Gets the Pet by id.
    :vartype name: str
    """

    _validation = {
        'name': {'readonly': True},
    }

    _attribute_map = {
        'ani_type': {'key': 'aniType', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        ani_type: Optional[str] = None,
        **kwargs
    ):
        super(Pet, self).__init__(ani_type=ani_type, **kwargs)
        self.name = None


class PetAction(msrest.serialization.Model):
    """PetAction.

    :param action_response: action feedback.
    :type action_response: str
    """

    _attribute_map = {
        'action_response': {'key': 'actionResponse', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        action_response: Optional[str] = None,
        **kwargs
    ):
        super(PetAction, self).__init__(**kwargs)
        self.action_response = action_response


class PetActionError(PetAction):
    """PetActionError.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: PetSadError.

    All required parameters must be populated in order to send to Azure.

    :param action_response: action feedback.
    :type action_response: str
    :param error_type: Required. Constant filled by server.
    :type error_type: str
    :param error_message: the error message.
    :type error_message: str
    """

    _validation = {
        'error_type': {'required': True},
    }

    _attribute_map = {
        'action_response': {'key': 'actionResponse', 'type': 'str'},
        'error_type': {'key': 'errorType', 'type': 'str'},
        'error_message': {'key': 'errorMessage', 'type': 'str'},
    }

    _subtype_map = {
        'error_type': {'PetSadError': 'PetSadError'}
    }

    def __init__(
        self,
        *,
        action_response: Optional[str] = None,
        error_message: Optional[str] = None,
        **kwargs
    ):
        super(PetActionError, self).__init__(action_response=action_response, **kwargs)
        self.error_type = 'PetActionError'  # type: str
        self.error_message = error_message


class PetSadError(PetActionError):
    """PetSadError.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: PetHungryOrThirstyError.

    All required parameters must be populated in order to send to Azure.

    :param action_response: action feedback.
    :type action_response: str
    :param error_type: Required. Constant filled by server.
    :type error_type: str
    :param error_message: the error message.
    :type error_message: str
    :param reason: why is the pet sad.
    :type reason: str
    """

    _validation = {
        'error_type': {'required': True},
    }

    _attribute_map = {
        'action_response': {'key': 'actionResponse', 'type': 'str'},
        'error_type': {'key': 'errorType', 'type': 'str'},
        'error_message': {'key': 'errorMessage', 'type': 'str'},
        'reason': {'key': 'reason', 'type': 'str'},
    }

    _subtype_map = {
        'error_type': {'PetHungryOrThirstyError': 'PetHungryOrThirstyError'}
    }

    def __init__(
        self,
        *,
        action_response: Optional[str] = None,
        error_message: Optional[str] = None,
        reason: Optional[str] = None,
        **kwargs
    ):
        super(PetSadError, self).__init__(action_response=action_response, error_message=error_message, **kwargs)
        self.error_type = 'PetSadError'  # type: str
        self.reason = reason


class PetHungryOrThirstyError(PetSadError):
    """PetHungryOrThirstyError.

    All required parameters must be populated in order to send to Azure.

    :param action_response: action feedback.
    :type action_response: str
    :param error_type: Required. Constant filled by server.
    :type error_type: str
    :param error_message: the error message.
    :type error_message: str
    :param reason: why is the pet sad.
    :type reason: str
    :param hungry_or_thirsty: is the pet hungry or thirsty or both.
    :type hungry_or_thirsty: str
    """

    _validation = {
        'error_type': {'required': True},
    }

    _attribute_map = {
        'action_response': {'key': 'actionResponse', 'type': 'str'},
        'error_type': {'key': 'errorType', 'type': 'str'},
        'error_message': {'key': 'errorMessage', 'type': 'str'},
        'reason': {'key': 'reason', 'type': 'str'},
        'hungry_or_thirsty': {'key': 'hungryOrThirsty', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        action_response: Optional[str] = None,
        error_message: Optional[str] = None,
        reason: Optional[str] = None,
        hungry_or_thirsty: Optional[str] = None,
        **kwargs
    ):
        super(PetHungryOrThirstyError, self).__init__(action_response=action_response, error_message=error_message, reason=reason, **kwargs)
        self.error_type = 'PetHungryOrThirstyError'  # type: str
        self.hungry_or_thirsty = hungry_or_thirsty
