import paramiko
#connection method
def sftpconnection(pemfilepath,host,user):
    key = paramiko.RSAKey.from_private_key_file(pemfilepath)
    transport = paramiko.Transport((host, 22))
    transport.connect(username=user, pkey=key)
    sftp = paramiko.SFTPClient.from_transport(transport)
    return sftp
    
#close sftp connection
def sftpclose(sftp):
    sftp.close