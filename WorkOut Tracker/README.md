# Workout Tracker

A command-line application that tracks workouts using Nutritionix API for exercise data and Sheety API for Google Sheets integration.

## Features

- Natural language exercise input processing
- Automatic calorie calculation based on exercise type and user metrics
- Records date, time, exercise name, duration, and calories burned
- Stores data in Google Sheets for tracking

## Setup

### Prerequisites
- Python 3.6+
- Nutritionix API account
- Sheety account
- Google account

### Installation
```bash
pip install requests python-dotenv
```

### Environment Configuration
Create a `.env` file with:
```
APP_ID=your_nutritionix_app_id
API_KEY=your_nutritionix_api_key
TOKEN=Bearer your_sheety_api_token
SHEET_URL=your_sheety_api_endpoint
```

## API Configuration

1. **Nutritionix API**: Register at [nutritionix.com/business/api](https://www.nutritionix.com/business/api) to obtain APP_ID and API_KEY
2. **Sheety API**: Set up at [sheety.co](https://sheety.co/) with Google Sheet containing columns: Date, Time, Exercise, Duration, Calories

## Usage

```bash
python workout_tracker.py
```

When prompted, enter your exercise in natural language:
```
Tell Me Which Exercise You Did: ran 3 miles
```

The app will calculate calories and log the workout to your Google Sheet.

## Customization

Modify user parameters in the script to match your personal metrics (weight, height, age).