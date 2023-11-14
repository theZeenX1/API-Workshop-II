from pymongo.mongo_client import MongoClient

uri = "<your mongodb uri>"

connection = MongoClient(uri)

try:
    connection.admin.command('ping')
    print('Your server has been deployed successfully!')
except Exception as e:
    print('Error: ', e)
