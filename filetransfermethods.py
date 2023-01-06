import os
# transfer all files from that path
def transferfile(spath,dpath,sftp,inbound_files):
    source_folder=spath
    destination=dpath
    for file in inbound_files :
        filepath = destination+"/"+file
        localpath = source_folder+"\\"+file
        try :
            sftp.put(localpath,filepath)
            os.remove(localpath)
        except:
            print ("Not able to transfer thrwoing error....")