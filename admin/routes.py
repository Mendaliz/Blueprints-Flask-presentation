from flask import Blueprint, render_template, jsonify

admin_bp = Blueprint('admin', __name__,
                     template_folder='templates',
                     static_folder='static')

@admin_bp.before_request
def before_api_request():
    print("Запрос к API")

@admin_bp.route('/500')
def error_creator():
    print("error")
    return jsonify(error = "my error"), 500

@admin_bp.errorhandler(500)
def not_found(error):
    print("ERROROROOROROROR")
    return jsonify({'error': 'Not found this thing'}), 500

@admin_bp.route('/')
def index():
    return render_template('admin/index.html')

@admin_bp.route('/profile')
def profile():
    return render_template('admin/profile.html')

@admin_bp.route('/users')
def users():
    user_list = ['John', 'Carla', 'Mathew']
    return render_template('admin/users.html', users=user_list)