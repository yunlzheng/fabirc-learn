from fabric.api import *
env.hosts = ['127.0.0.1:3001', '127.0.0.1:3002', '27.0.0.1:3003']
env.user = 'ubuntu'
env.password = '123456'

@task
def echo():
    run('echo "hello,world"')
