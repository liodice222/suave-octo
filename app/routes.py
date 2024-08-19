from flask import render_template, request, jsonify
import subprocess
from app import app

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout if result.returncode == 0 else result.stderr

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_user', methods=['POST'])
def add_user():
    username = request.form['username']
    command = f'sudo bash scripts/user_management.sh add {username}'
    output = run_command(command)
    return jsonify({'result': output})

@app.route('/modify_user', methods=['POST'])
def modify_user():
    username = request.form['username']
    shell = request.form['shell']
    command = f'sudo bash scripts/user_management.sh modify {username} {shell}'
    output = run_command(command)
    return jsonify({'result': output})

@app.route('/delete_user', methods=['POST'])
def delete_user():
    username = request.form['username']
    command = f'sudo bash scripts/user_management.sh delete {username}'
    output = run_command(command)
    return jsonify({'result': output})