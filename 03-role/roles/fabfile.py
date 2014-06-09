from fabric.api import *
from fabric.context_managers import *

env.hosts = ['ubuntu@127.0.0.1:3001', 'ubuntu@127.0.0.1:3002', 'ubuntu@127.0.0.1:3003']

env.passwords = {
    'ubuntu@127.0.0.1:3001': '123456',
    'ubuntu@127.0.0.1:3002': '123456',
    'ubuntu@127.0.0.1:3003': '123456'
}

env.roledefs = {
  'nginx': ['ubuntu@127.0.0.1:3001', 'ubuntu@127.0.0.1:3002'],
  'mysql': ['ubuntu@127.0.0.1:3003']
  }

@roles('nginx')
@task
def nginx_start():
    ''' nginx start '''
    run('echo "nginx start"')

@roles('nginx')
@task
def nginx_stop():
    ''' nginx stop '''
    run('echo "nginx stop"')

@roles('mysql')
@task
def mysql_start():
    ''' mysql start '''
    run('echo "mysql start"')

@roles('mysql')
@task
def mysql_stop():
    ''' mysql stop '''
    run('echo "mysql stop"')

@task
def echo():
    run('echo "hello,world"')
