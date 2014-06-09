from fabric.api import *
from fabric.context_managers import *

env.hosts = ['ubuntu@127.0.0.1:3001', 'ubuntu@127.0.0.1:3002', 'ubuntu@127.0.0.1:3003']

env.passwords = {
    'ubuntu@127.0.0.1:3001': '123456',
    'ubuntu@127.0.0.1:3002': '123456',
    'ubuntu@127.0.0.1:3003': '123456'
}

env.roledefs = {'nginx': ['ubuntu@127.0.0.1:3001', 'ubuntu@127.0.0.1:3002'], 'mysql': 'ubuntu@127.0.0.1:3003'}

@roles('mysql')
@task
def mysql_start():
  ''' mysql start '''
  sudo('/etc/init.d/mysql start')

@roles('nginx')
@task
def nginx_start():
    ''' nginx start '''
    sudo('/etc/init.d/nginx start')

@roles('nginx')
@task
def nginx_stop():
    ''' nginx stop '''
    sudo('/etc/init.d/nginx stop')

@task
def echo():
    run('echo "hello,world"')
