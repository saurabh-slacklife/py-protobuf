__author__ = "Saurabh Saxena from 3-Minute Tech"

from flask import Blueprint, jsonify

from app.io.slacklife.extensions import redis_service

health_bp = Blueprint('Health', __name__)


@health_bp.route('/', methods=['GET'])
def health_check():
    redis_conn = redis_service.get_redis
    return jsonify(redis_conn.info())


@health_bp.route('/datastore/', methods=['GET'])
def health_check_datastore():
    redis_conn = redis_service.get_redis
    return jsonify(redis_conn.connection_pool.make_connection().check_health())
