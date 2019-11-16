from flask import (
    Blueprint
)

api_blueprint = Blueprint('api', __name__, url_prefix='/api')


@api_blueprint.route('/users', methods=['GET'])
def get_users():
    return 'users'


@api_blueprint.route('/users', methods=['POST'])
def post_user():
    pass
