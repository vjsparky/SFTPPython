import os, DBUpdate, datetime, shutil

# transfer all files from that path
def transferfile(spath,dpath,sftp,inbound_files):
    source_folder=spath
    destination=dpath
    
    for file in inbound_files :
        filepath = destination+"/"+file
        localpath = source_folder+"\\"+file
        failedpath="V:\\Failed"+file
        try :
            try :
                sftp.put(localpath,filepath)
                os.remove(localpath)
                Status,Timestamp="Success",datetime.datetime.now().strftime("%Y-%m-%d")
                print ("Successfully transferred file [{}] to remote server..".format(file))
            except:
                 Status,Timestamp="Failed",datetime.datetime.now().strftime("%Y-%m-%d")
                 shutil.move(localpath,failedpath)
                 print ("Not able to transfer the File --> {}. Moved to failed directory".format(file))
            DBUpdate.DBTableupdate(file,Status,Timestamp)
        except Exception as e:
            print ("There is some error {}".format(e))
