from flask import Flask, jsonify
import os
from dotenv import load_dotenv

from .services.user_activity import make_user_contribution_call


load_dotenv(".env")
app = Flask(__name__)

app_settings = os.getenv("APP_SETTINGS")
app.config.from_object(app_settings)


@app.route("/ping", methods=["GET"])
def ping_pong():
    return jsonify({
        "status": "success",
        "message": "pong!"
    })


@app.route("/active/<user>", methods=["GET"])
def is_user_active(user):
    contribution_days = make_user_contribution_call(user)
    return jsonify({
        "was_active_since_yesterday": contribution_days > 0
    })
