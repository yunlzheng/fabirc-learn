# coding: utf-8
from fabric.api import *


def hello(name="world"):
    run('echo "hello,world"')


def who_am_i(name='Fabric'):
    """
    Who i am? Usage: 'fab who_am_i'
    """

    intro = "Fabric is a Python library and command-line tool for streamlining the use of SSH for application deployment or systems administration tasks."

    import pyttsx
    engine = pyttsx.init()
    engine.setProperty('rate', 120)

    voices = engine.getProperty('voices')
    voice = voices[2]
    engine.setProperty('voice', voice.id)
    engine.say("Hi, I'm "+ name +", "+ intro)
    engine.runAndWait()
