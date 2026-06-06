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
    user_input = request.json.get("preference", "").lower()
    suggestions = {
        "spicy": "🌶️ Spicy Chicken Fried Rice\nIngredients: chicken, rice, soy sauce, chili, garlic\nEstimated Cost: $6.50",
        "cheap": "🥚 Egg Fried Rice\nIngredients: eggs, rice, soy sauce, onion\nEstimated Cost: $3.00",
        "healthy": "🥗 Grilled Chicken Salad\nIngredients: chicken breast, lettuce, tomato, cucumber\nEstimated Cost: $7.00",
        "sweet": "🍌 Banana Oat Pancakes\nIngredients: banana, oats, egg, honey\nEstimated Cost: $4.00",
        "vegetarian": "🥘 Paneer Curry\nIngredients: paneer, tomato, onion, spices, cream\nEstimated Cost: $8.00",
        "chicken": "🍗 Grilled Chicken & Rice\nIngredients: chicken breast, rice, garlic, olive oil, herbs\nEstimated Cost: $7.50",
        "paneer": "🧀 Paneer Tikka Wrap\nIngredients: paneer, tortilla, yogurt, spices, onion\nEstimated Cost: $6.00",
        "egg": "🍳 Masala Omelette\nIngredients: eggs, onion, tomato, green chili, spices\nEstimated Cost: $2.50",
        "rice": "🍚 Vegetable Fried Rice\nIngredients: rice, mixed vegetables, soy sauce, egg\nEstimated Cost: $4.00",
        "pasta": "🍝 Creamy Pasta\nIngredients: pasta, cream, garlic, parmesan, herbs\nEstimated Cost: $5.50",
    }
    for key in suggestions:
        if key in user_input:
            return jsonify({"suggestion": suggestions[key]})
    return jsonify({"suggestion": "🍱 Student Special: Rice + Dal + Salad\nIngredients: rice, lentils, mixed vegetables\nEstimated Cost: $4.50"})
