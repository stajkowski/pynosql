from abc import ABCMeta, abstractmethod


class BaseProvider():
    """ Base NOSQL Provider """

    __metaclass__ = ABCMeta

    @abstractmethod
    def get_record(self, model, table, **kwargs):
        """ Get a single record from DB

        :param model: obj BaseModel
        :param table: str table
        :return: dict record
        :raises: ClientException
        """

    @abstractmethod
    def get_records(self, model, table, **kwargs):
        """ Get multiple records from DB

        :param model: obj BaseModel
        :param table: str table
        :param options: obj options
        :return: list records
        :raises: ClientException
        """

    @abstractmethod
    def scan_records(self, model, table, **kwargs):
        """ Get multiple records from DB through scan without index

        :param model: obj BaseModel
        :param table: str table
        :param options: obj options
        :return: list records
        :raises: ClientException
        """

    @abstractmethod
    def put_record(self, model, table, record, **kwargs):
        """ Put record into DB

        :param model: obj BaseModel
        :param table: str table
        :param record: dict record
        :return: bool status
        :raises: ClientException
        """

    @abstractmethod
    def delete_record(self, model, table, **kwargs):
        """ Delete record from DB

        :param model: obj BaseModel
        :param table: str table
        :return: bool status
        :raises: ClientException
        """
