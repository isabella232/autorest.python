# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------
import logging
from typing import Dict, List, Any

from .operation import Operation
from .imports import FileImport, ImportType


_LOGGER = logging.getLogger(__name__)

class OperationGroup:
    """Represent an operation group.

    """

    def __init__(
        self,
        code_model,
        yaml_data: Dict[str, Any],
        name: str,
        class_name: str,
        operations: List[Operation],
    ) -> None:
        self.code_model = code_model
        self.yaml_data = yaml_data
        self.name = name
        self.class_name = class_name
        self.operations = operations

    def imports(self):
        file_import = FileImport()
        for operation in self.operations:
            file_import.merge(operation.imports())
        if self.code_model.sorted_schemas:
            file_import.add_from_import("..", "models", ImportType.LOCAL)
        return file_import

    @classmethod
    def from_yaml(cls, code_model, yaml_data: Dict[str, Any], **kwargs) -> "OperationGroup":
        name = yaml_data['language']['python']['name']
        _LOGGER.info("Parsing %s operation group", name)

        operations = []
        for operation_yaml in yaml_data["operations"]:
            operations.append(Operation.from_yaml(operation_yaml, tracing=code_model.tracing))

        return cls(
            code_model=code_model,
            yaml_data=yaml_data,
            name=name,
            class_name=yaml_data['language']['python']['className'],
            operations=operations,
        )