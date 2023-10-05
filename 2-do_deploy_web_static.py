#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
"""
from fabric.api import run, env, put, task
import os

env.hosts = ["54.173.75.28", "54.197.74.184"]
env.user = "ubuntu"


@task
def do_deploy(archive_path):
    """
    Fabric script that distributes an archive to your web servers
    """
    try:
        if not os.path.exists(archive_path):
            return False
        put(archive_path, "/tmp/")

        archive_file = archive_path.split("/")[-1]
        release_path = "/data/web_static/releases/{}".format(archive_file[:-4])
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
