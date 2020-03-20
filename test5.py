import paramiko
import socket
import netifaces
import platform
from pymongo import MongoClient

host_list = [ "23.101.130.248" ]
uname = "masterhost"
pss = "masterhost@007"

docs = []

docs.append( { "hostname":socket.gethostname(), "ip":netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['addr'], "os":platform.system(), "os_version":platform.release() } )

for host in host_list :
  client = paramiko.SSHClient()
  client.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
  client.connect( host, username=uname, password=pss )
  stdin, stdout, stderr = client.exec_command( "hostname ; ifconfig | grep 'inet ' | head -n 1 | tr -s ' ' ' ' | cut -d ' ' -f 3 ; hostnamectl | grep 'Oper\|Ker' | cut-d ':' -f 2 | sed 's/^\s//g'" )
  tmp_lst = []
  for line in stdout :
    tmp_lst.append(  line.strip('\n') )
  docs.append( { "hostname":tmp_lst[0], "ip":tmp_lst[1], "os":tmp_lst[2], "os_version":tmp_lst[3] } )
  client.close()

db_client = MongoClient( "mongodb://127.0.0.1:27017" )
db = db_client['HOST_DETAILS']

db.detailSet.insert_many( docs )

print( "Database inserton successful !!\n"  )

print( "Now fetching object ids for inserted data !!\n" )

for doc in docs :
  results = db.detailSet.find( doc, { "_id":1 } )
  for res in results :
    print( res )

print('\n')

db_client.close()