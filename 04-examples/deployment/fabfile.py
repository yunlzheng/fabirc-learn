# coding:utf-8
from __future__ import with_statement
from fabric.api import *
from fabric.colors import *
from fabric.contrib.console import confirm


def commit():
    """
    commit本地代码
    """
    local("git add -p && git commit")


def push():
    """
    提交本地代码到服务器
    """
    local("git push")


def prepare_deploy():
    """
    commit并push本地代码
    """
    commit()
    push()


def installs():
    """
    安装服务器环境依赖 git,redis-server
    """
    with cd("/home"):
        run("sudo apt-get install git")
        run("sudo apt-get install redis-server")
        run("sudo apt-get install python-pip")
        run("sudo apt-get install build-essential")


def deploy():
    """
    拉取远程代码并在服务器运行
    """
    code_dir = '/home/vagrant/git/chat'
    with settings(warn_only=True):
        if run("test -d %s" % code_dir).failed:
            run("git clone https://github.com/yunlzheng/chat.git %s" % code_dir)
        with cd(code_dir):
            run("git pull")
            run("sudo pip install -r requirements.txt")
            run("sudo killall -9 python")
            run("python server.py", pty=False)

def start():
    """
    启动应用程序
    """
    code_dir = '/home/vagrant/git/chat'
    with settings(warn_only=True):
        if run("test -d %s" % code_dir).failed:
            deploy()
        else:
            with cd(code_dir):
                run("sudo killall -9 python")
                run("python server.py", pty=False)
                return

def stop():
    """
    停止应用程序
    """
    run("sudo killall -9 python", pty=False)
