from fabric.api import *


env.hosts = ['vagrant@127.0.0.1:2222']

env.passwords = {
    'vagrant@127.0.0.1:2222': 'vagrant'
}


@task
def echo():
    run('echo "hello,world"')
