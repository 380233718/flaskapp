from flask import Flask
from config import config


app = Flask(__name__)
app.config.from_object(config)


@app.route('/')
def hello_world():
    return 'Hello World! change'


if __name__ == '__main__':
    app.run()
