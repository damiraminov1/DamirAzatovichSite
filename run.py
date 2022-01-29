from app import create_app
from config import Config

app = create_app()
config = {'host': Config.HOST, 'port': Config.PORT, 'debug': Config.DEBUG}

if __name__ == '__main__':
    app.run(**config)
