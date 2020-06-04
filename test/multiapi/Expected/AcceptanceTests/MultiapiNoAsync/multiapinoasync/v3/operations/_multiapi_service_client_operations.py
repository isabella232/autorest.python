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
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar, Union

    from azure.core import PipelineClient
    from msrest import Deserializer, Serializer

    from .._configuration import MultiapiServiceClientConfiguration


    T = TypeVar('T')
    ClsReturnType = TypeVar('ClsReturnType')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], ClsReturnType]]

    class AbstractServiceClient(object):
        """Abstract class of a service client to help with type hints for the following mixin class"""

        def __init__(self):
            # type: () -> None
            """
            Init for abstract service client class
            """

        @property
        def _client(self):
            # type: () -> PipelineClient
            """Pipeline client
            :rtype: PipelineClient
            """

        @_client.setter
        def _client(self, value):
            # type: (PipelineClient) -> None
            """Set the pipeline client"""

        @property
        def _config(self):
            # type: () -> MultiapiServiceClientConfiguration
            """Configuration of service client
            :rtype: MultiapiServiceClientConfiguration
            """

        @_config.setter
        def _config(self, value):
            # type: (MultiapiServiceClientConfiguration) -> None
            """Set the configuration"""

        @property
        def _serialize(self):
            # type: () -> Serializer
            """Serializer
            :rtype: Serializer
            """

        @_serialize.setter
        def _serialize(self, value):
            # type: (Serializer) -> None
            """Set the serializer"""

        @property
        def _deserialize(self):
            # type: () -> Deserializer
            """Deserializer
            :rtype: Deserializer
            """

        @_deserialize.setter
        def _deserialize(self, value):
            # type: (Deserializer) -> None
            """Set the deserializer"""

    # https://github.com/python/mypy/issues/5837
    _MIXIN_BASE = AbstractServiceClient
else:
    _MIXIN_BASE = object


class MultiapiServiceClientOperationsMixin(_MIXIN_BASE):

    def test_paging(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable[Union["models.PagingResult", ClsReturnType]]
        """Returns ModelThree with optionalProperty 'paged'.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either PagingResult or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~multiapinoasync.v3.models.PagingResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.PagingResult", ClsReturnType]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            if not next_link:
                # Construct URL
                url = self.test_paging.metadata['url']  # type: ignore
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('PagingResult', pipeline_response)
            list_of_elem = deserialized.values
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    test_paging.metadata = {'url': '/multiapi/paging'}  # type: ignore
