# codeing: utf-8
from fabric.api import *


def hello(name="world"):
    run('echo "hello,world"')


def who_am_i(name='yunlong'):
    """
    Who i am? Usage: 'fab who_am_i'
    """
    import pyttsx
    engine = pyttsx.init()
    engine.setProperty('rate', 110)

    voices = engine.getProperty('voices')
    for voice in voices:
        engine.setProperty('voice', voice.id)
        engine.say("Hi, I'm "+ name +", how are you?")
    engine.runAndWait()
