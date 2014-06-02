# coding: utf-8
from fabric.decorators import task


@task
def install_requirements():
    pass


@task
def sync_project():
    pass


@task
def start():
    pass


@task
def stop():
    pass


@task
def restart():
    pass


@task(default=True)
def full_install():
    pass