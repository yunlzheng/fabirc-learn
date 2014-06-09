Simple As Fabric- 角色管理
========================

## 角色管理

在服务器管理或者应用部署过程中，经常会对服务器进行分组：

系统管理：

* 数据库服务器
* 负载均衡服务器

应用部署:

* 开发环境
* 测试环境
* 验收环境


## 演示时间

* Ubuntu-Server-01: ssh -p 3001 ubuntu@127.0.0.1
* Ubuntu-Server-02: ssh -p 3002 ubuntu@127.0.0.1
* Ubuntu-Server-03: ssh -p 3003 ubuntu@127.0.0.1

__代码__：

```
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

```