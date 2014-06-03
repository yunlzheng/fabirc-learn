# coding: utf-8

import pprint

from fabric.api import *

pp = pprint.PrettyPrinter(indent=4)

tomcat_home = env.tomcat_dir + env.tomcat_folder


@task
def print_env():
    """
    打印环境配置文件
    """
    pp.pprint(env)


@task
def update_upgrade():
    """
    更新系统包
    """
    run("sudo apt-get update")


@task
def install_java():
    """
    安装Java JDK
    """
    with settings(warn_only=True):
        run("sudo apt-get install openjdk-7-jdk --fix-missing")


@task
def install_tomcat():
    """
    在远程服务器下载并安装Tomcat
    """
    with settings(warn_only=True):
        if run("test -d %s" % tomcat_home).failed:
            with cd("/tmp"):
                run("wget %s" % env.tomcat_source)
                run("mkdir %s" % env.tomcat_dir)
                run("tar -zxvf %s -C %s" % (env.tomcat_folder + ".tar.gz", env.tomcat_dir))
        else:
            print "tomcat already install "


@task
def install_requirements():
    """
    安装环境依赖
    """
    with settings(warn_only=True):
        if run("java -version").failed:
            install_java()
        
        if run("test -d %s" % tomcat_home).failed:
            install_tomcat()


@task
def tomcat_start():
    """
    启动远程Tomcat服务器
    """
    with cd(tomcat_home + "/bin"):
        run("./catalina.sh start")


@task
def tomcat_stop():
    """
    停止远程服务器
    """
    with cd(tomcat_home + "/bin"):
        run("./shutdown.sh")


@task
def tomcat_restart():
    """
    重启Tomcat服务器
    """
    tomcat_stop()
    tomcat_start()


@task
def tomcat_version():
    """
    获取当前Tomcat版本
    """
    with cd(tomcat_home + "/bin"):
        run("./catalina.sh version")


@task
def tomcat_logs():
    """
    打印Tomcat日志文件catalina.out
    """
    with cd(tomcat_home + "/logs"):
        run("tail -f catalina.out")


@task
def clean_install():
    """
    移除已安装的Tomcat
    """
    with settings(warn_only=True):
        with cd(env.tomcat_dir):
            with cd(env.tomcat_folder + "/bin"):
                run("sudo ./shutdown.sh")
            run("sudo rm -rf %s" % tomcat_home)
        with cd("/tmp"):
            run("sudo rm -rf apache-tomcat-*")
