# from setuptools import setup, find_packages

# setup(
#     name="us_visa",
#     version="0.0.0",
#     author="Aayush",
#     author_email="sahuaayush6266@gmail.com",
#     packages=find_packages()
# )


from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://aayush:aayush3010@cluster0.gukq6ow.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)