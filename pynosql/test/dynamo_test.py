import unittest
from boto3.dynamodb.conditions import Key
from pynosql.base.model import Model
from pynosql.clients.aws_mock import AWSMockResponses
from pynosql.providers.dynamo import DynamoDBProvider
from pynosql.credentials.aws import AWSCredentials
from pynosql.clients.aws import AWSClient


class TestModel(Model):

    BASE = {
        'test1': None,
        'test2': None,
        'test3': None,
        'test4': None
    }

    def __init__(self):
        super(TestModel, self).__init__(self.BASE)


class TestSetup(unittest.TestCase):
    """ Credentials Test """

    def setUp(self):
        """ Create Mock Client and Provider

        :return:
        """
        self.credentials = AWSCredentials(
            'AKIAIOSFODNN7EXAMPLE',
            'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY'
        )

    def test_basic_get_item(self):
        """ Test basic get_item from dynamodb table """
        expected = {
            'test1': 'value1',
            'test2': 'value2',
            'test3': 'value3',
            'test4': 'value4'
        }
        key = {
            'test1': 'value1',
            'test2': 'value2'
        }
        dynamo = DynamoDBProvider(
            AWSClient(self.credentials,
                      'us-west-2',
                      mock=AWSMockResponses.get_item_response)
        )
        response = dynamo.get_record(TestModel(), 'TestTable', Key=key)

        self.assertDictEqual(response, expected)

    def test_basic_query(self):
        """ Test basic query from dynamodb table """
        expected = [
            {
                'test1': 'value1',
                'test2': 'value2',
                'test3': 'value3',
                'test4': 'value4',
            },
            {
                'test1': 'value5',
                'test2': 'value6',
                'test3': 'value7',
                'test4': 'value8',
            },
            {
                'test1': 'value9',
                'test2': 'value10',
                'test3': 'value11',
                'test4': 'value12',
            },
            {
                'test1': 'value13',
                'test2': 'value14',
                'test3': 'value15',
                'test4': 'value16',
            },
        ]
        dynamo = DynamoDBProvider(
            AWSClient(self.credentials,
                      'us-west-2',
                      mock=AWSMockResponses.query_response)
        )
        response = dynamo.get_records(
            TestModel(), 'TestTable',
            KeyConditionExpression=Key('test1').eq('value1'),
            IndexName='TestIndex'
        )

        self.assertListEqual(response, expected)
