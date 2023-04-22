from collections import OrderedDict


class NonRequiredMixin:
    def get_fields(self):
        fields = OrderedDict()
        for name, field in super().get_fields().items():
            field.required = False
            fields[name] = field
        return fields