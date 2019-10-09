#!/usr/bin/env python3

from omxplayer.player import OMXPlayer
from time import sleep

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class PlayerManager(object):
   __metaclass__ = Singleton
   def __init__(self):
      self.playerAlive=false

   def createPlayer(self):
      STREAM_URI = './video.mp4'
      self.player = OMXPlayer(STREAM_URI)
      self.playerAlive=true

   def getPlayer(self):
      if(not self.playerAlive):
         self.createPlayer();
      return self.player
