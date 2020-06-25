from flask import Blueprint, jsonify, request, Response

from app.io.slacklife.extensions import redis_service
from app.io.slacklife.models.user.user_pb2 import User, Gender

user_bp = Blueprint('User', __name__)


@user_bp.route('/', methods=['GET'])
def get_user():
    redis_connection = redis_service.get_redis
    user_data = redis_connection.get(name='rgwrgedfgdfgrgeeg6677')
    user = User()
    user.ParseFromString(user_data)
    return user_data


@user_bp.route('/', methods=['PUT'])
def create_user() -> Response:
    user = User()
    req_data = request.json
    user.name = req_data.get('name')
    user.email = req_data.get('email')
    user.gender = Gender.MALE
    user.id = req_data.get('id')

    redis_connection = redis_service.get_redis

    redis_connection.set(name=req_data.get('id'), value=user.SerializeToString())
    return jsonify(req_data.get('id'))


@user_bp.after_request
def add_header(response):
    response.headers['Content-Type'] = 'application/octet-stream'
    response.headers['Cache-Control'] = 'private, no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    return response