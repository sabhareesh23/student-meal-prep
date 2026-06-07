import os
from dotenv import load_dotenv
from google import genai
from flask import Blueprint, render_template, jsonify, Response, request

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

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


@main.route("/api/suggest", methods=["POST"])
def suggest_meal() -> Response:
    user_input = request.json.get("preference", "")
    prompt = f"""You are a student meal assistant. 
    Suggest a simple, affordable meal based on: {user_input}
    
    Format your response exactly like this:
    🍽️ Meal Name: [name]
    
    📝 Ingredients: [list ingredients]
    
    👨‍🍳 Instructions:
    1. [step 1]
    2. [step 2]
    3. [step 3]
    
    💰 Estimated Cost: $[amount]
    
    Keep it short, practical and student-friendly!"""
    
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    return jsonify({"suggestion": response.text})
