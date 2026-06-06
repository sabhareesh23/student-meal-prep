from flask import Blueprint, render_template, jsonify, Response

main = Blueprint("main", __name__)


@main.route("/")
def index() -> str:
    return render_template("index.html")


@main.route("/api/meals")
def get_all_meals() -> Response:
    from app.data import WEEKLY_MEALS
    return jsonify(WEEKLY_MEALS)


@main.route("/api/meals/<day>")
def get_day_meals(day: str) -> Response:
    from app.data import WEEKLY_MEALS
    if day not in WEEKLY_MEALS:
        return jsonify({"error": "Day not found"}), 404
    return jsonify(WEEKLY_MEALS[day])