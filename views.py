from flask import Blueprint, render_template, request,jsonify, redirect, url_for


views = Blueprint(__name__, 'views')

@views.route('/')
def home():
    return render_template('index.html',name='Dio', age=23)

# Query parameters
# @views.route('/profile')
# def profile():
#     args = request.args
#     name = args.get('name')
#     return render_template('index.html', name=name)



# Returning json parameters
@views.route('/json')
def get_json():
    return jsonify({'name': 'tim', 'coolness': 10})

# Getting Json
@views.route('/data')
def get_data():
    data = request.json
    return jsonify(data)

# Redirect
@views.route('/go-to-json')
def go_to_json():
    return redirect(url_for('views.get_json'))

# Adding Javascript
#====================

# template inherit
@views.route('/profile')
def profile():
    return render_template('profile.html')