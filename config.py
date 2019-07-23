import os

class Config(object):
    DEBUG = False
    ENVIROMENT = 'prod'

class Produccion(Config):
    DEBUG = False
    ENVIROMENT = 'prod'

class Development(Config):
    DEBUG = True
    ENVIROMENT = 'dev'