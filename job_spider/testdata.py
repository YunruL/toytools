from pymongo import MongoClient

client = MongoClient()
db = client.test
cursor = db['upwork_jobs'].find()
for document in cursor:
    print document['skills']

result = db['upwork_jobs'].delete_many({})
print result.deleted_count
