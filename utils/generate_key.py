import secrets
import string

def generate_key(length=32):
    # 大小写字母 + 数字 + 标点字符串
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for i in range(length))