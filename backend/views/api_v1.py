from flask import Blueprint

api = Blueprint('api', __name__)

@api.route('/')
def root():
    return """
        {
            "hello": "world"
        }
    """