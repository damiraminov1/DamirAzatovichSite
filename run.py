from app import create_app
from config import Config

app = create_app()
config = {'host': Config.HOST, 'debug': Config.DEBUG, 'port': Config.PORT}

if __name__ == '__main__':
    app.run(**config)
