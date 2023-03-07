# Third-party libraries
from flask import Flask, redirect, request, url_for, render_template, send_from_directory
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from oauthlib.oauth2 import WebApplicationClient
import requests
app = Flask(__name__)

@app.route("/")
def index():
    return send_from_directory('./', 'index.html')

@app.rout("/notification",methods=["POST"])
def push_notification():
    params = request.json
    response = {}
    try:
        print(request)
        # url = "http://192.168.101.33/5000/notification" #pi
        url = "http://169.231.106.37/5000/notification"
        resp = requests.post(f'{url}',verify=False)
        status = 200
    except Exception as e:
        print(f"Exception in notification: {e}")
        response["MESSAGE"] = f"Exception in notification {e}"
        status = 500
    return jsonify(response), status