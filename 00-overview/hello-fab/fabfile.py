# coding: utf-8
from fabric.api import *


def hello(name="world"):
    """
    Usage: 'fab -c example.fabricc hello' 在配置文件制定的服务器上运行echo
    """
    run('echo "hello,world"')

def ls(local_dir='/Users/ylzheng', remote_dir='/home/vagrant'):
    """
    Usage: 'fab remote_ls:\,\' 显示本地以及远程服务器的目录信息
    """
    with cd(remote_dir):
      run('ls -l')
    with lcd(local_dir):
      local('ls -l')

def upload(source, target="/home/vagrant"):
    """
    Usage: 'fab -c example.fabricrc upload:/Users/ylzheng/test/i_am_file_in_local.txt' 上传本地文件到服务器
    """
    put(source, target)


def who_am_i(name='Fabric'):
    """
    Usage: 'fab who_am_i' Fabric的自我介绍
    """

    intro = """Fabric is a Python library and command-line tool
    for streamlining the use of SSH for application deployment
    or systems administration tasks.
    """

    import pyttsx
    engine = pyttsx.init()
    engine.setProperty('rate', 120)

    voices = engine.getProperty('voices')
    voice = voices[2]
    engine.setProperty('voice', voice.id)
    engine.say("Hi, I'm "+ name +", "+ intro)
    engine.runAndWait()
