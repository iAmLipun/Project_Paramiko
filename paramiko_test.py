import base64
import paramiko
key = paramiko.RSAKey(data=base64.b64decode(ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC2hZf/DqbiqWMiAtyKS+osYps6O5bXa1fDuxv+zPZe2vcXbbiOgqWbj7yyvAncTNfoZFLW4S1/IdKvNjHV4Uqa5VVklWZG0MlWy7wXVORmBVNEZ44MymQckidcfjettgx3TCWFQBN/9ZXsKsylz5JQ4lCcgFjNE14tpAVLhyxy3pNiz0if2rFgqxXmJOXdtaLTD5gpBAA2H3s7gYYZ+nSkHm2iLtJzDEvWi3y3Gc78nsGj0lgwqTKZ2krIJXC9N9ZDEb6pOcYDsnvqF4OetMvDOfA3gH9EaTSHOs+Ep6CZQjdszqgo5RAqa95+HgIU8QG0jD2KwzCiheVs89NQ6NIz masterhost@masterhost))
client = paramiko.SSHClient()
client.get_host_keys().add('ssh.example.com', 'ssh-rsa', key)
client.connect('masterhost@23.101.130.248', username='masterhost', password='masterhost@007')
stdin, stdout, stderr = client.exec_command('hostname')
for line in stdout:
    print('... ' + line.strip('\n'))
client.close()