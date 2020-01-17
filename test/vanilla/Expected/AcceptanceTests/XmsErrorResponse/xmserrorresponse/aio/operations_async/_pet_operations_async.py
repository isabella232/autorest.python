# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import warnings

from azure.core.exceptions import HttpResponseError, map_error
from azure.core.tracing.decorator_async import distributed_trace_async

from ... import models


class PetOperations:
    """PetOperations async operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~xmserrorresponse.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace_async
    async def get_pet_by_id(self, pet_id, cls=None, **kwargs):
        """Gets pets by id..

        FIXME: add operation.summary

        :param pet_id: pet id
        :type pet_id: str
        :param callable cls: A custom type or function that will be passed the direct response
        :return: Pet or  or the result of cls(response)
        :rtype: ~xmserrorresponse.models.Pet or None
        :raises: ~azure.core.HttpResponseError
        """
        error_map = {
            400: HttpResponseError,
            404: lambda response: models.NotFoundErrorBaseException.from_response(response, self._deserialize),
            501: HttpResponseError,
        }
        error_map.update(kwargs.pop('error_map', {}))

        # Construct URL
        url = self.get_pet_by_id.metadata['url']
        path_format_arguments = {
            'petId': self._serialize.url("pet_id", pet_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'


        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Pet', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    get_pet_by_id.metadata = {'url': '/errorStatusCodes/Pets/{petId}/GetPet'}

    @distributed_trace_async
    async def do_something(self, what_action, cls=None, **kwargs):
        """Asks pet to do something.

        FIXME: add operation.summary

        :param what_action: what action the pet should do
        :type what_action: str
        :param callable cls: A custom type or function that will be passed the direct response
        :return: PetAction or the result of cls(response)
        :rtype: ~xmserrorresponse.models.PetAction
        :raises: ~xmserrorresponse.models.PetActionErrorException:
        """
        error_map = {
            500: lambda response: models.PetActionErrorException.from_response(response, self._deserialize),
        }
        error_map.update(kwargs.pop('error_map', {}))

        # Construct URL
        url = self.do_something.metadata['url']
        path_format_arguments = {
            'whatAction': self._serialize.url("what_action", what_action, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'


        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.PetActionErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('PetAction', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    do_something.metadata = {'url': '/errorStatusCodes/Pets/doSomething/{whatAction}'}