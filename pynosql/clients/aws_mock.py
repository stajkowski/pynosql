from botocore.stub import Stubber


class AWSMockResponses(object):
    """ Stubber for DynamoDB Mock Responses """

    @staticmethod
    def get_item_response(client):
        """ Mock GetItem Response

        :param client: obj AWS Client
        :return: None
        """
        get_item_response = {
            'Item': {
                'test1': {'S': 'value1'},
                'test2': {'S': 'value2'},
                'test3': {'S': 'value3'},
                'test4': {'S': 'value4'},
            },
            'ConsumedCapacity': {
                'TableName': 'TestTable',
                'CapacityUnits': 123.0,
                'Table': {
                    'CapacityUnits': 123.0
                },
                'LocalSecondaryIndexes': {
                    'string': {
                        'CapacityUnits': 123.0
                    }
                },
                'GlobalSecondaryIndexes': {
                    'string': {
                        'CapacityUnits': 123.0
                    }
                }
            }
        }
        stub = Stubber(client.meta.client)
        stub.add_response('get_item', get_item_response)
        stub.activate()

    @staticmethod
    def query_response(client):
        """ Mock Query Response

        :param client: obj AWS Client
        :return: None
        """
        query_response = {
            'Items': [
                {
                    'test1': {'S': 'value1'},
                    'test2': {'S': 'value2'},
                    'test3': {'S': 'value3'},
                    'test4': {'S': 'value4'},
                },
                {
                    'test1': {'S': 'value5'},
                    'test2': {'S': 'value6'},
                    'test3': {'S': 'value7'},
                    'test4': {'S': 'value8'},
                },
                {
                    'test1': {'S': 'value9'},
                    'test2': {'S': 'value10'},
                    'test3': {'S': 'value11'},
                    'test4': {'S': 'value12'},
                },
                {
                    'test1': {'S': 'value13'},
                    'test2': {'S': 'value14'},
                    'test3': {'S': 'value15'},
                    'test4': {'S': 'value16'},
                },
            ],
            'ConsumedCapacity': {
                'TableName': 'TestTable',
                'CapacityUnits': 123.0,
                'Table': {
                    'CapacityUnits': 123.0
                },
                'LocalSecondaryIndexes': {
                    'string': {
                        'CapacityUnits': 123.0
                    }
                },
                'GlobalSecondaryIndexes': {
                    'string': {
                        'CapacityUnits': 123.0
                    }
                }
            }
        }
        stub = Stubber(client.meta.client)
        stub.add_response('query', query_response)
        stub.activate()
