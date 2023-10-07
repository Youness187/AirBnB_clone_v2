#!/usr/bin/python3
"""
# Fabric script that distributes an archive to your web servers
"""
from fabric.api import run, env, put, task
from datetime import datetime
import os

env.hosts = ["54.173.75.28", "54.197.74.184"]
env.user = "ubuntu"


@task
def do_pack():
    """
    Fabric script that generates a .tgz
    """
    if not os.path.exists("versions"):
        os.makedirs("versions")
    date_format = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "web_static_{}.tgz".format(date_format)

    if local("tar -cvzf versions/{} web_static".format(file_name)).succeeded:
        return "versions/{}".format(file_name)
    return None


@task
def do_deploy(archive_path):
    """
    Fabric script that distributes an archive to your web servers
    """
    try:
        if not os.path.exists(archive_path):
            return False

        archive_file = os.path.basename(archive_path)
        release_path = "/data/web_static/releases/{}".format(
            os.path.splitext(archive_file)[0]
        )
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(release_path))

        run("tar -xzf /tmp/{} -C {}".format(archive_file, release_path))

        run("rm /tmp/{}".format(archive_file))

        run("mv {}/web_static/* {}/".format(release_path, release_path))

        run("rm -rf {}/web_static".format(release_path))

        run("rm -rf /data/web_static/current")

        run("ln -s {} /data/web_static/current".format(release_path))

        return True
    except Exception:
        return False
