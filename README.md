# git2ftp
A python script to publish to a webserver using git via FTP

This work was based on an original script by [Kristijan Burnik](https://invision-web.net/web/deploying-to-production-via-ftp-with-git-hooks/).

This script was developed to overcome a recent problem I had with being unable to have SSH access to a web host on a shared server and therefore not being able to use git to update the production server.

The basic principle of this project is that you have a remote repository on your local machine and a working repository on your local machine. When changes in your working repository are pushed to your remote repository, the post-update hook is executed which in turn executes the deploy.py script that is responsible for making the FTP connection and deploying files from your working repository.

In the original script by [Kristijan Burnik](https://invision-web.net/web/deploying-to-production-via-ftp-with-git-hooks/), it wasn't possible to exclude directories or files from the FTP upload, this functionality was added.

#Usage
###The remote (local) repository
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


