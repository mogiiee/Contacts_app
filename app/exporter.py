from dotenv import load_dotenv
import os
load_dotenv()

cluster = os.environ.get("CLUSTER")
db_name = os.environ.get("DB")
db_collection = os.environ.get("COLLECTION")