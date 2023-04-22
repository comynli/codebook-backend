from collections import OrderedDict

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class StandardResultSetPagination(PageNumberPagination):
    page_size_query_param = "size"

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('current', self.page.number),
            ('size', self.page.paginator.per_page),
            ('results', data)
        ]))

    def get_paginated_response_schema(self, schema):
        return {
            'type': 'object',
            'properties': {
                'count': {
                    'type': 'integer',
                    'example': 123,
                },
                'current': {
                    'type': 'integer',
                    'example': 1
                },
                'size': {
                    'type': 'integer',
                    'example': 20
                },
                'results': schema,
            },
        }
