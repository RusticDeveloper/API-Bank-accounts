from decouple import config #para obtener las variables de entorno

class Config:
    SECRET_KEY=config('SECRET_KEY')

class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'development':DevelopmentConfig
}