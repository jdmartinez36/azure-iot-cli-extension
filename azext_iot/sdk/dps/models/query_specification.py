# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class QuerySpecification(Model):
    """A Json query request.

    :param query: The query.
    :type query: str
    """

    _validation = {
        'query': {'required': True},
    }

    _attribute_map = {
        'query': {'key': 'query', 'type': 'str'},
    }

    def __init__(self, query):
        super(QuerySpecification, self).__init__()
        self.query = query