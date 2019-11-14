from os.path import join, dirname, realpath

class Config(object):
    DEBUG = False
    SECRET_KEY = "B\xb2?.\xdf\x9f\xa7m\xf8\x8a%,\xf7\xc4\xfa\x91"

    STORAGE_PATH = join(dirname(realpath(__file__)), '../storage')

    SESSION_COOKIE_SECURE = True

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True
