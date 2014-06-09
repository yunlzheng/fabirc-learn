Simple As Fabric -认证
=================

## 认证方式 = SSH的认证方式

* 基于用户名密码的认证
* 基于SSH公钥的认证

## Fabric 环境变量

```
* env.hosts
* env.user
* env.password
* env.passwords
* env.key_filename
```

## Password

两个常见的场景： 

场景一：

一堆服务器，用户名相同，密码相同

```
from fabric.api import *
env.hosts = ['127.0.0.1:3001', '127.0.0.1:3002', '27.0.0.1:3003']
env.user = 'ubuntu'
env.password = '123456'

@task
def echo():
    run('echo "hello,world"')
```

场景二：

一堆服务器，用户名相同，密码不同

```
from fabric.api import *
env.hosts = ['127.0.0.1:3001', '127.0.0.1:3002', '27.0.0.1:3003']
env.user = 'ubuntu'
env.passwords = {
    'ubuntu@127.0.0.1:3001': '123456',
    'ubuntu@127.0.0.1:3002': '123456',
    'ubuntu@127.0.0.1:3003': '123456'
}

@task
def echo():
    run('echo "hello,world"')
```

场景三：

一堆服务器，用户名不同，密码不同

```
from fabric.api import *
env.hosts = ['ubuntu@127.0.0.1:3001', 'ubuntu@127.0.0.1:3002', 'ubuntu@127.0.0.1:3003']
env.passwords = {
    'ubuntu@127.0.0.1:3001': '123456',
    'ubuntu@127.0.0.1:3002': '123456',
    'ubuntu@127.0.0.1:3003': '123456'
}

@task
def echo():
    run('echo "hello,world"')
```


## SSH公钥认证

当然更安全的方式：基于SSH的认证

### 本地

__生成 SSH Private Key__

```
ssh-keygen
```

__提交 SSH公钥到服务器__

```
scp -P 2222 id_rsa.pub vagrant@127.0.0.1:~/.ssh/
```

### 服务器端

```
cat id_rsa.pub >> authorized_keys
```

### 演示时间

```
from fabric.colors import *
from fabric.api import *


env.hosts = ['vagrant@127.0.0.1:2222']

env.key_filename = "~/.ssh/id_rsa"


@task
def ls():
    print(green("I'm server  /home/vagrant"))
    with cd('/home/vagrant'):
        run('ls -l')


@task
def put():
    print(green("I'm put local's test file to 10 and 12"))
    put('/Users/ylzheng/test','/home/vagrant/')
    print(yellow("I'm 10 or 12 /home/vagrant/test"))
    with cd('/home/vagrant/test'):
        run('ls -l')


@task
def deploy():
    execute(ls)
    execute(put)

```
