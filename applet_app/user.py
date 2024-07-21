from flask import Blueprint, render_template, request, redirect

user_bp = Blueprint('user_bp', __name__,url_prefix='/users')

@user_bp.route('/')
def index():
    return "你好,用户模块"