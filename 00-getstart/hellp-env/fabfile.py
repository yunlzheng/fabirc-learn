from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm


def test():
    with settings(warn_only=True):
        result = local('./manage.py test my_app', capture=True)
    if result.failed and not confirm("Tests failed. Continue anyway?"):
        abort("Aborting at user request.")


def installs():
    with cd("/home"):
        run("sudo apt-get install git")
        run("sudo apt-get install redis-server")
        run("sudo apt-get install python-pip")
        run("sudo apt-get install build-essential")


def commit():
    local("git add -p && git commit")


def push():
    local("git push")


def prepare_deploy():
    test()
    commit()
    push()


def deploy():
    code_dir = '/home/vagrant/git/chat'
    with settings(warn_only=True):
        if run("test -d %s" % code_dir).failed:
            run("git clone https://github.com/yunlzheng/chat.git %s" % code_dir)
    with cd(code_dir):
        run("git pull")
        run("sudo pip install -r requirements.txt")
        run("sudo killall -9 python")
        run("python server.py")