# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.core.tracing.decorator import distributed_trace

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsReturnType = TypeVar('ClsReturnType')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], ClsReturnType]]

class PetOperations(object):
    """PetOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~xmserrorresponse.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def get_pet_by_id(
        self,
        pet_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> Union[Optional["models.Pet"], ClsReturnType]
        """Gets pets by id.

        :param pet_id: pet id.
        :type pet_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Pet, or the result of cls(response)
        :rtype: ~xmserrorresponse.models.Pet or None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[Optional["models.Pet"], ClsReturnType]
        error_map = {
            409: ResourceExistsError,
            400: HttpResponseError,
            404: lambda response: ResourceNotFoundError(response=response, model=self._deserialize(models.NotFoundErrorBase, response)),
            501: HttpResponseError,
        }
        error_map.update(kwargs.pop('error_map', {}))

        # Construct URL
        url = self.get_pet_by_id.metadata['url']  # type: ignore
        path_format_arguments = {
            'petId': self._serialize.url("pet_id", pet_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Pet', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_pet_by_id.metadata = {'url': '/errorStatusCodes/Pets/{petId}/GetPet'}  # type: ignore

    @distributed_trace
    def do_something(
        self,
        what_action,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> Union["models.PetAction", ClsReturnType]
        """Asks pet to do something.

        :param what_action: what action the pet should do.
        :type what_action: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PetAction, or the result of cls(response)
        :rtype: ~xmserrorresponse.models.PetAction
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.PetAction", ClsReturnType]
        error_map = {
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            500: lambda response: HttpResponseError(response=response, model=self._deserialize(models.PetActionError, response)),
        }
        error_map.update(kwargs.pop('error_map', {}))

        # Construct URL
        url = self.do_something.metadata['url']  # type: ignore
        path_format_arguments = {
            'whatAction': self._serialize.url("what_action", what_action, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.PetActionError, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('PetAction', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    do_something.metadata = {'url': '/errorStatusCodes/Pets/doSomething/{whatAction}'}  # type: ignore
