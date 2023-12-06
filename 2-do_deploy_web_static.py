#!/usr/bin/python3
"""that distributes an archive to your web servers"""
import os
from fabric.api import *
from datetime import datetime
from os.path import exists


env.hosts = ['3.84.222.176', '34.207.63.171']


def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    if exists(archive_path) is False:
        return False
    file_name = archive_path.split('/')[-1]
    nfil = '/data/web_static/releases/' + "{}".format(file_name.split('.')[0])
    tmp = "/tmp/" + file_name

    try:
        """upload the archive to the tmp & uncompress the
        the archive to the folder /data/web_static/releases/"""
        put(archive_path, "/tmp/")
        run("mkdir -p {}/".format(nfil))
        run("tar -xzf {}  -C {}/".format(tmp, nfil))
        run("rm {}".format(tmp))
        run("mv {}/web_static/* {}/".format(nfil, nfil))
        """Delete the archive from the web server"""
        run("rm -rf {}/web_static".format(nfil))
        """Delete the symbolic link from the web server"""
        run("rm -rf /data/web_static/current")
        """create a new symbloic link"""
        run("ln -s {}/ /data/web_static/current".format(nfil))
        return True
    except Exception as e:
        print("Exception:", e)
        return False
