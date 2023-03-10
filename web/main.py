import os
import datetime

from flask import Flask, request, json, render_template, make_response, session, send_from_directory, send_file

from web.api_v1 import api_v1_bp

# Flask App
App = Flask(__name__)
# App.config['JSON_AS_ASCII'] = False
# App.secret_key = os.urandom(24)
# App.permanent_session_lifetime = datetime.timedelta(days=30)

# API注册
App.register_blueprint(api_v1_bp, url_prefix="/api/v1")

if __name__ == '__main__':
    App.run(debug=True)
