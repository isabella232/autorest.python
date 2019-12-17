from jinja2 import Template, PackageLoader, Environment

class ModelInitSerializer:
    def __init__(self, code_model, env):
        self.code_model = code_model
        self.env = env
        self._model_init_file = None

    def serialize(self):
        schemas = sorted(self.code_model.sorted_schemas, key=lambda x: x.name)
        enums = [e.enum_type for e in self.code_model.enums.values()] if self.code_model.enums else None

        if enums:
            enums.sort()

        template = self.env.get_template("model_init.py.jinja2")
        self._model_init_file = template.render(
            code_model=self.code_model,
            schemas=schemas,
            enums=enums
        )

    @property
    def model_init_file(self):
        return self._model_init_file
