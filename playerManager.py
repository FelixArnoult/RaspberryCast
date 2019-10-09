#!/usr/bin/env python3

from omxplayer.player import OMXPlayer
from time import sleep

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class PlayerManager(OMXPlayer, metaclass=Singleton):
   def __init__(self):
      self.playerAlive=False

   def createPlayer(self):
      STREAM_URI = './video.mp4'
      self.player = OMXPlayer(STREAM_URI)
      self.playerAlive=True

   def getPlayer(self):
      if(not self.playerAlive):
         self.createPlayer();
      return self.player
