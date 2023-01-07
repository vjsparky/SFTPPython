import paramiko , os, time, sftpmethods, filetransfermethods

#file directory
spath="V:\SFTP"
dpath="/home/ec2-user"
pemfilelocation="C:\\Users\\vijay\\Downloads\\devibala.pem"
host="54.199.75.69"
user="ec2-user"



def directorymonitor(spath):
    inbound_files=os.listdir(spath)
    if not inbound_files:
        print ("No file in the location {}".format(spath))
        exit
    else:
        print ("File in the location {} is : {}" .format(spath,inbound_files))
        #methods calling 
        sftp = sftpmethods.sftpconnection(pemfilelocation,host,user)
        filetransfermethods.transferfile(spath,dpath,sftp,inbound_files)
        sftpmethods.sftpclose(sftp)




while True:
    directorymonitor(spath)
    val=10
    print("Directory monitor will check in another {} seconds . Terminate  to stop".format(val))
    time.sleep(val)
   

