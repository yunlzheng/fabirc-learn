from fabric.colors import *
from fabric.api import *


env.hosts = ['vagrant@127.0.0.1:2222']

env.key_filename = "~/.ssh/id_rsa"


@task
def ls():
    print(green("I'm local  /home/vagrant"))
    with cd('/home/vagrant'):
        run('ls -l')


@task
def put_dir():
    print(green("I'm put local's test file to 10 and 12"))
    put('/Users/ylzheng/test','/home/vagrant/')
    print(yellow("I'm 10 or 12 /home/vagrant/test"))
    with cd('/home/vagrant/test'):
        run('ls -l')


@task
def deploy():
    execute(ls)
    execute(put_dir)
