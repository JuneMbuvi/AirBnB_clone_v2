#!/usr/bin/python3
"""script that generates a .tgz archive from the contents of the web_static"""
from fabric.api import *
from datetime import datetime


def do_pack():
    """function that creates a tgz file with timestamps and the
    other file systmes parameters"""
    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_{}.tgz".format(date)
    result = local(" sudo tar -czvf {} web_static".format(archive_name))
    if result.succeeded:
        return archive_name
    else:
        None
