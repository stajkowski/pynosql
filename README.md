# PyNOSQL Library for Python
[![Build Status](https://travis-ci.org/stajkowski/pynosql.svg?branch=master)](https://travis-ci.org/stajkowski/pynosql)

# Summary
PyNOSQL is a simple library that wraps two popular NOSQL databases DynamoDB|MongoDB and provides the concept of a model
for maintaining, expanding, and reducing data structures stored in NOSQL tables.  Extend model.Model and pass to various
Dynamo operations to benefit from default values, adding/removing elements, and simplifying use of boto3 with DynamoDB.

# Versions
0.0.1 - Support for basic CRUD operations in DynamoDB

# Getting Started

1. Instantiate a client and pass to the desired provider:

```

from pynosql.credentials.aws import AWSCredentials
from pynosql.clients.aws import AWSClient
from pynosql.providers.dynamo import DynamoDBProvider

credentials = AWSCredentials(
    'AKIAIOSFODNN7EXAMPLE',
    'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY'
)

dynamo = DynamoDBProvider(
    AWSClient(self.credentials, 'us-west-2')
)

```

2. Extend base.model.Model to create the desired data structure to be stored in
your NOSQL DB:

```

from pynosql.base.model import Model

class TestModel(Model):

    BASE = {
        'test1': None,
        'test2': None,
        'test3': None,
        'test4': None
    }

    def __init__(self):
        super(TestModel, self).__init__(self.BASE)

```

3. Pass the model with the appropriate call to DynamoDB:

```

key = {
    'test1': 'value1',
    'test2': 'value2'
}

response = dynamo.get_record(TestModel(), 'TestTable', Key=key)

```

4. For paginating all results into the model, just keep passing the model
instance into your DynamoDB calls.  The new records will be appended to the
list within the model.
