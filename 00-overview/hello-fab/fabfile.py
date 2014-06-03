# codeing: utf-8
from fabric.api import *


def hello(name="world"):
    print("Hello %s!" % name)
    run('echo "hello,world"')


def who_am_i(name='yunlong'):
    """
    Who i am? Usage: 'fab who_am_i'
    """
    import pyttsx
    engine = pyttsx.init()
    engine.setProperty('rate', 70)

    voices = engine.getProperty('voices')
    for voice in voices:
        print "Using voice:", repr(voice)
        engine.setProperty('voice', voice.id)
        engine.say("Hi, I'm "+ name +", how are you?")
    engine.runAndWait()
