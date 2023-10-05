#!/usr/bin/python3
"""
Fabric script that generates a .tgz
"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    Fabric script that generates a .tgz
    """
    if not os.path.exists("versions"):
        os.makedirs("versions")
    date_format = datetime.now().strftime('%Y%m%d%H%M%S')
    file_name = "web_static_{}.tgz".format(date_format)

    if local("tar -cvzf versions/{} web_static".format(file_name)).succeeded:
        return "versions/{}".format(file_name)
    return None
