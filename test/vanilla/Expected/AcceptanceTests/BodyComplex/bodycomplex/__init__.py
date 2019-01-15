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

from ._configuration import AutoRestComplexTestServiceConfiguration
from ._auto_rest_complex_test_service import AutoRestComplexTestService
__all__ = ['AutoRestComplexTestService', 'AutoRestComplexTestServiceConfiguration']

try:
    from ._auto_rest_complex_test_service_async import AutoRestComplexTestServiceAsync
    __all__ += ['AutoRestComplexTestServiceAsync']
except (SyntaxError, ImportError):  # Python 2
    pass

from .version import VERSION

__version__ = VERSION

