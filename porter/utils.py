import json

import yaml
from kubernetes.client import ApiClient



class _FakeResponse:
    def __init__(self, data):
        self.data = data


def serialize(obj):
    return yaml.dump(ApiClient().sanitize_for_serialization(obj))


def deserialize(text: str, klass):
    data = json.dumps(yaml.safe_load(text))
    return ApiClient().deserialize(_FakeResponse(data), klass)

