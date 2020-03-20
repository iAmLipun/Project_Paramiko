from pymongo import MongoClient
import socket
import platform
try:
    conn = MongoClient()
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")

# database
db = conn.hpe_db

# Created or Switched to collection names: my_gfg_collection
collection = db.hpe_ci_collection
hostname= socket.gethostname()
host_ip= socket.gethostbyname(hostname)
system = platform.system()
machine = platform.machine()
platform = platform.platform()

emp_rec1 = {
    'hostname': hostname,
    'IP': host_ip,
    'platform': platform,
    'system' : system ,
    'machine' : machine

}

# Insert Data

rec_id1 = collection.insert(emp_rec1)


print("Data inserted with record ids", rec_id1, " ")

# Printing the data inserted
cursor = collection.find()
for record in cursor:
    print(record)