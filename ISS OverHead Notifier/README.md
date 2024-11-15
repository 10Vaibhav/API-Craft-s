# -ISS-Overhead-Notifier

## Description
This Python script checks if the International Space Station (ISS) is currently overhead and if it's nighttime at the user's location. If both conditions are met, it sends an email notification to look up and spot the ISS.

## Features
- Retrieves real-time ISS position data
- Calculates if the ISS is overhead based on user's coordinates
- Determines if it's currently nighttime at the user's location
- Sends email notifications when conditions are met

## Requirements
- Python 3.x
- `requests` library
- Internet connection for API calls
- Gmail account for sending notifications

## How it works
1. Fetches the current ISS position from the Open Notify API
2. Checks if the ISS is within ±5 degrees of the user's position
3. Determines if it's currently dark at the user's location using the Sunrise Sunset API
4. If both conditions are true, sends an email notification

## Note
This script is designed to run continuously. Make sure you have a stable internet connection and that your computer doesn't go to sleep while the script is running.

## Contributing
Contributions to this project are welcome!

## Disclaimer
Please ensure you're complying with your email provider's policies when using this script.
