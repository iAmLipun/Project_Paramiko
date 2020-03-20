import paramiko
from pymongo import MongoClient

hostname = input("Enter Hostname : ")
username = input("Enter username : ")
password = input("Enter Password : ")
try:
    conn = MongoClient()
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")

# database
db = conn.hpe_db
# Created or Switched to collection names: my_gfg_collection
collection = db.ci_collection

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=hostname, username=username, password=password)

stdin, stdout, stderr = client.exec_command('hostname ; hostname -i ;  uname ; uname -r ;')

list = []
for line in stdout:
    list.append( line.strip('\n'))

rec = ({ "hostname" : list[0], "host_ip" : list[1], "os" : list[2], "os_version" : list[3]})
print(rec)

#print(list)
client.close()

rec_id = collection.insert(rec)
print("data inserted with ", rec_id,  " ")
cursor = collection.find()
for record in cursor:
    print(record)


#print(hostname)
#print(host_ip)
#print(os_name)
#print(os_version)



