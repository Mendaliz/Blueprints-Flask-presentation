from flask import Blueprint, render_template, jsonify

user_bp = Blueprint('user', __name__, 
                    template_folder='templates',
                    static_folder='static')

@user_bp.before_request
def before_api_request():
    print("Запрос к API")

@user_bp.route('/500')
def error_creator():
    print("error")
    return jsonify(error = "my error"), 500

@user_bp.errorhandler(500)
def not_found(error):
    print("ERROROROOROROROR")
    return jsonify({'error': 'Not found this thing'}), 500

@user_bp.route('/')
def index():
    return render_template('index.html')

@user_bp.route('/profile')
def profile():
    return render_template('user/profile.html')