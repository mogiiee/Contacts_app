import pymongo
import exporter

cluster = pymongo.MongoClient(exporter.cluster)
db = cluster[exporter.db_name]
collection = db[exporter.db_collection]

