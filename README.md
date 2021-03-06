# git2ftp
A python script to publish to a webserver using git via FTP

## THIS IS AN ALPHA SCRIPT AND SHOULD NOT BE USED IN PRODUCTION ENVIRONMENTS ##

This work was based on an original script by [Kristijan Burnik](https://invision-web.net/web/deploying-to-production-via-ftp-with-git-hooks/).

This script was developed to overcome a recent problem I had with being unable to have SSH access to a web host on a shared server and therefore not being able to use git to update the production server.

The basic principle of this project is that you have a remote repository on your local machine and a working repository on your local machine. When changes in your working repository are pushed to your remote repository, the post-update hook is executed which in turn executes the deploy.py script that is responsible for making the FTP connection and deploying files from your working repository.

In the original script by [Kristijan Burnik](https://invision-web.net/web/deploying-to-production-via-ftp-with-git-hooks/), it wasn't possible to exclude directories or files from the FTP upload, this functionality was added.

# Usage
### The remote (local) repository
Set up a bare git repository to which you will push commits:

```
mkdir $barerepo
cd $barerepo
git init --bare
```
Create a working repository:
```
mkdir $workrepo
cd $workrepo
git init
git remote add origin $barerepo
```
Copy the deploy.py script into the **hooks** directory within the $barepo repository.
Copy the post-update script into the **hooks** directory within the $barepo repository. Note you may already have a post-update script in here, back this up first.

### Configuration
#### post-update script
Open up the post-update script and change the paths to suit your local path, see comments in the file

#### deploy.py script
Open up the deploy.py script and configure the following:

exclude_dirs - This is a python array of directories not to be transferred to your remote server via FTP

exclude_files - This is a python array of files not to be transferred to your remote server via FTP

ftp_host

ftp_username

ftp_password

dest_dir - The FTP destination directory, that is the directory FTP will initially upload to

backup_dir - The archive directory. Your existing production directory will be backed up to an archive directory

production_dir - the live production directory which hosts your production website


You may also need to make your deploy.py script executable:
```
chmod +x deploy.py
```
### Testing
**WARNING - It is advisable not to test this set up on a live production server until you are satisfied you know how it works and you have configured it correctly. 
Initially configure your production_dir and backup_dir to a test location on your hosting server. You have been warned**

Drop a test text file in your **$workrepo** directory and execute deploy.py in a terminal window to ensure all files are copied to your server as expected.

Finally make changes in your working repository, commit changes and push to your remote. Upon the remote updating, the post-update hook will execute and in turn execute the deploy.py script which will upload your files to your FTP server.

### Future Work
In no particular order:
- [ ] Only upload changed/modified files to the FTP server not the full content of working repo
- [ ] Add missing directory checks and optionally create if not on server
