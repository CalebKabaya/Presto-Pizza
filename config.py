import os

class Config:
    # UPLOADED_PHOTOS_DEST ='app/static/photos'

    # API_KEY = os.environ.get('API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://lynne:lynne2022@localhost/pizza'

    





    


# class TestConfig(Config):
#     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://'

class ProdConfig(Config):
    pass


class DevConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://venecia:12345@localhost/pizza'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
# 'test':TestConfig
}
