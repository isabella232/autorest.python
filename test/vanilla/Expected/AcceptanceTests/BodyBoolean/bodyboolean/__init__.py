# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from ._configuration import AutoRestBoolTestServiceConfiguration
from ._auto_rest_bool_test_service import AutoRestBoolTestService
__all__ = ['AutoRestBoolTestService', 'AutoRestBoolTestServiceConfiguration']

try:
    from ._auto_rest_bool_test_service_async import AutoRestBoolTestServiceAsync
    __all__ += ['AutoRestBoolTestServiceAsync']
except (SyntaxError, ImportError):  # Python 2
    pass

from .version import VERSION

__version__ = VERSION

