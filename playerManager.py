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
    def __init__(self):
        STREAM_URI = './video.mp4'
        OMXPlayer.__init__(self, STREAM_URI)

    def decrease_volume(self):
        self.set_volume(self.volume() - VOLUME_STEP)

    def increase_volume(self):
        self.set_volume(self.volume() + VOLUME_STEP)

    def short_forward(self): #TODO check when remain duratiSHORT_SEEK
        if(self.can_seek()):
            self.seek(self.position() + SHORT_SEEK)

    def short_backward(self):
        if(self.can_seek()):
            self.seek(self.position() - SHORT_SEEK)

    def long_forward(self): #TODO check when remain duration < SHORT_SEEK
        if(self.can_seek()):
            self.seek(self.position() + LONG_SEEK)

    def long_backward(self):
        if(self.can_seek()):
            self.seek(self.position() - LONG_SEEK)
