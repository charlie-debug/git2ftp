#!/usr/bin/python
import os
import time
from ftplib import FTP_TLS


def senddir(path,dest,ftp,exclude_dirs, exclude_files):

  for root, dirs, files in os.walk(path):
    for d in dirs:
      if d in exclude_dirs:
        dirs.remove(d)
        

    for file in files:
      if file not in exclude_files:
		  source_filename = os.path.join(root, file)
		  print "Source file: " + file
		  dest_filename = dest + source_filename.replace(path,'')
		  dest_dir = os.path.dirname( dest_filename )
	  
		  list = dest_dir.split('/')
	  
		  ftp.cwd( "/" )
		  partial_dir = ""
		  for part in list:
			partial_dir += "/" + part
			partial_dir = partial_dir.replace('//','/')        
			if part != "" and not (part in ftp.nlst() ):      
			  ftp.mkd( partial_dir )
			  print "Created " + partial_dir + " on remote server"        
			ftp.cwd( partial_dir )
	  
		  ftp.cwd( "/" )
	  
		  ftp.storlines("STOR " + dest_filename, open(source_filename,"r"))
		  print "Stored " + dest_filename  + " on remote server"
      

timestamp = str(int( time.time()))

#List of directory names to exclude
exclude_dirs = [".git"]

#List of file names to exclude
exclude_files = [".DS_Store"]

# local directory
local_dir = "../../work-repo"

# FTP server connection strings      
ftp_host = "ftp.example.com"
ftp_username = "my-username"
ftp_password = "my-password"

# remote server paths
dest_dir = "/production/deploy-" + timestamp
backup_dir = "/production/archive/www-" + timestamp
production_dir = "/production/www"


if __name__ == '__main__':  

  os.chdir(os.path.dirname(__file__))
  
  print "Connecting to FTP host " + ftp_host
  ftp = FTP_TLS( ftp_host , ftp_username , ftp_password )
  
  wmsg = FTP_TLS.getwelcome(ftp)
  print wmsg

  #Upload the local dir excluding any directories or files as listed
  print "Starting directory transfer of " + local_dir
  senddir( local_dir , dest_dir, ftp, exclude_dirs, exclude_files)

  #Archive the current production directory
  print "Renaming " + production_dir + " to " + backup_dir
  ftp.rename( production_dir , backup_dir )
  
  #Rename the uploaded directory to production dirrectory
  print "Renaming " + dest_dir + " to " + production_dir
  ftp.rename( dest_dir , production_dir )
  
  print "Transfer complete"