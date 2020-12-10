from flask import Flask, jsonify
import os
from dotenv import load_dotenv

from .services.user_activity import make_user_contribution_call
from .services.repo_activity import get_total_changes_on_commits


load_dotenv(".env")
app = Flask(__name__)

app_settings = os.getenv("APP_SETTINGS")
app.config.from_object(app_settings)


@app.route("/sanity", methods=["GET"])
def ping_pong():
    return jsonify({
        "status": "success",
        "message": "check!"
    })


@app.route("/active/<user>", methods=["GET"])
def is_user_active(user):
    contribution_days = make_user_contribution_call(user)
    if not contribution_days and type(contribution_days) != int:
        return jsonify({
            "status": 400,
            "message": f"{user} not found."
        })
    return jsonify({
        "is_active_since_yesterday": contribution_days > 0
    })


@app.route("/downwards/<repo>", methods=["GET"])
def is_repo_downgraded(repo):
    total_changes_last_week = get_total_changes_on_commits(repo)
    if not total_changes_last_week and type(total_changes_last_week) != int:
        return jsonify({
            "status": 400,
            "message": f"{repo} is not unique or not found."
        })
    return jsonify({
        "is_repo_downwarded_since_last_week": True if total_changes_last_week < 0 else False
    })
