coverage run --source='./pynosql' --omit="*__init__*,*/test*" -m unittest discover -s pynosql/test -p '*_test.py'
coverage report -m
rm -rf ./htmlcov/*
coverage html
