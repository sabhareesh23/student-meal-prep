# Student Meal Prep App

A Flask web app that helps students plan weekly meals and get AI-powered meal suggestions.

## Team
- Partner A (Sabhareesh) - Backend
- Partner B (Pranav)- Frontend

## What it does
- Weekly meal dashboard (click a day to see meals)
- Shows ingredients and daily cost per day
- Tracks total weekly spending
- AI meal suggester powered by Google Gemini

## Technologies
- Python & Flask
- HTML, CSS, JavaScript
- Google Gemini AI
- Docker
- Pytest
- Git & GitHub

## How to run

```bash
git clone https://github.com/sabhareesh23/student-meal-prep.git
cd student-meal-prep
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
echo "GEMINI_API_KEY=your_key_here" > .env
python run.py
```

Visit http://127.0.0.1:5000

## API Endpoints
- GET /api/meals - all meals
- GET /api/meals/<day> - meals for a day
- POST /api/suggest - AI meal suggestion

## Tests
```bash
python -m pytest tests/test_routes.py -v
```

## Docker
```bash
docker build -t student-meal-prep .
docker run -p 5000:5000 -e GEMINI_API_KEY=your_key student-meal-prep
```
