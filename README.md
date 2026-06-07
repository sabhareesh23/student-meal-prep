# StudentMealPrep AI

## Overview

StudentMealPrep AI is a Flask-based web application designed to help international students plan affordable, healthy, and easy-to-cook meals based on their budget and dietary preferences. The application uses Google Gemini AI to generate personalized meal plans, grocery shopping lists, estimated costs, and cooking instructions.

## Problem Statement

Many international students face challenges such as:

- Limited food budgets
- Lack of meal planning experience
- Limited cooking time
- Difficulty finding affordable and healthy meals
- Managing grocery shopping efficiently

StudentMealPrep AI helps students make informed meal decisions while saving time and money.

## Features

### Frontend Features
- Home page
- AI Meal Planner page
- Recipes page
- Grocery List page
- About page

### Backend Features
- Flask web application
- REST API endpoints
- Gemini AI integration
- SQLite database support

### AI Meal Planning
Users can provide:
- Weekly budget
- Dietary preference (Vegetarian, Vegan, Non-Vegetarian)
- Number of days

The AI generates:
- Breakfast suggestions
- Lunch suggestions
- Dinner suggestions
- Grocery shopping list
- Estimated food cost
- Meal preparation instructions

### API Endpoint

Generate meal plans through the API:


## Technologies Used

- Python
- Flask
- Flask-SQLAlchemy
- Google Gemini AI
- HTML
- CSS
- SQLite
- Docker
- Pytest

## Project Structure

student-meal-prep-ai/

├── app/

│   ├── __init__.py

│   ├── routes.py

│   ├── api.py

│   ├── models.py

│   ├── ai_service.py

│   ├── templates/

│   └── static/

├── tests/

├── run.py

├── requirements.txt

├── Dockerfile

├── .gitignore

├── .env

└── README.md

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd student-meal-prep-ai
