from pynosql.providers.base_provider import BaseProvider


class DynamoDBProvider(BaseProvider):
    """ Dynamo DB Provider """

    def __init__(self, aws_client):
        """ Dynamo DB Provider

        :param aws_client: obj AWSClient
        """
        self._aws_client = aws_client

    def get_record(self, model, table, **kwargs):
        """ Get a single record from Dynamo

        :param model: obj BaseModel
        :param table: str table
        :return: dict record
        :raises: ClientException
        """
        table = self._aws_client.client.Table(table)
        response = self._aws_client.call(table.get_item, **kwargs)
