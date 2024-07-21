from utils import generate_key

class BaseConfig:
    key = generate_key.generate_key()
    SECRET_KEY = key
    # 配置数据库连接信息
    SQLALCHEMY_DATABASE_URI = 'mysql://wu:666@localhost:3306/hkwx'

config_dict = {
    'base': BaseConfig
}