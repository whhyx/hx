from config import config_dict
from flask_migrate import Migrate
from model import db
from applet_app import create_applet_app


app = create_applet_app(config_dict['base'])

# 数据库迁移脚本
migrate = Migrate(app, db)


@app.route('/')
def hello_world():  # put application's code here
    print(app.config['SECRET_KEY'])
    return 'Hello World!'




print(app.url_map)
