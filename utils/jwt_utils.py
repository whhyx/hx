import jwt

from flask import current_app
# 生成
def generate_jwt(payload,expire,secret_key=None):
    """

    :param payload: 表示用户的存储信息
    :param expire: jwt过期时间
    :param secret_key: 密钥
    :return:
    """
    _payload = {'exp': expire}
    _payload.update(payload)

    if not secret_key:
        secret_key = current_app.config['SECRET_KEY']
    token = jwt.encode(_payload,secret_key,algorithm='HS256')
    return token.decode('utf-8')
# 校验token值
def verify_jwt(token,secret_key=None):
    if not secret_key:
        secret_key = current_app.config['SECRET_KEY']

    try:
        payload = jwt.decode(token,secret_key,algorithms=['HS256'])
    except jwt.PyJWTError:
        payload = None
    return payload