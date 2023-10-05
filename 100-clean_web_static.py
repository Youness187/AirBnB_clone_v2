#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to your web servers
"""
from fabric.api import run, local, task, env, lcd, cd
import os

env.hosts = ["54.173.75.28", "54.197.74.184"]


@task
def do_clean(number=0):
    """
    Fabric script that deletes out-of-date archives
    """
    try:
        number = int(number)
        if number < 0:
            number = 0
        archives = sorted(os.listdir("versions"))
        for i in range(number):
            archives.pop()
        with lcd("versions"):
            for a in archives:
                local("rm ./{}".format(a))

        with cd("/data/web_static/releases"):
            archives = run("ls -tr").split()
            archives = [a for a in archives if "web_static_" in a]
            for i in range(number):
                archives.pop()
            for a in archives:
                run("rm -rf ./{}".format(a))
        return True
    except Exception:
        return False
