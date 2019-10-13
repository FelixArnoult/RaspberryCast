#!/usr/bin/env python3

from omxplayer.player import OMXPlayer
import omxplayer.keys as OMXkeys
from time import sleep

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class PlayerManager(OMXPlayer, metaclass=Singleton):
    SHORT_SEEK = 10
    LONG_SEEK = 60
    VOLUME_STEP = 0.5
    def __init__(self, stream_uri):
        OMXPlayer.__init__(self, stream_uri)
        self.SHORT_SEEK = 10
        self.LONG_SEEK = 60
        self.VOLUME_STEP = 0.5

    def decrease_volume(self):
        self.set_volume(self.volume() - self.VOLUME_STEP)

    def increase_volume(self):
        self.set_volume(self.volume() + self.VOLUME_STEP)

    def short_forward(self): #TODO check when remain duratiSHORT_SEEK
        if(self.can_seek()):
            self.seek(self.position() + self.SHORT_SEEK)

    def short_backward(self):
        if(self.can_seek()):
            self.seek(self.position() - self.SHORT_SEEK)

    def long_forward(self): #TODO check when remain duration < self.SHORT_SEEK
        if(self.can_seek()):
            self.seek(self.position() +self. LONG_SEEK)

    def long_backward(self):
        if(self.can_seek()):
            self.seek(self.position() -self. LONG_SEEK)
