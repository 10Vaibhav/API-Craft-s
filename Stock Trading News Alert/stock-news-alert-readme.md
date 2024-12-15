# Stock News Alert Application

## Project Overview

This is a Python-based stock tracking and news alert application that:
- Retrieves daily stock price information for a specific company (Tesla in this example)
- Calculates stock price changes
- Fetches relevant news articles when significant price movements occur
- Sends SMS alerts with stock performance and news headlines using Twilio

## Features

- Tracks daily stock prices using Alpha Vantage API
- Monitors stock price percentage changes
- Retrieves latest news articles using News API
- Sends SMS notifications via Twilio when stock price changes exceed 5%

## Prerequisites

Before running the application, you'll need to install the following:

### Python Libraries
- `requests`
- `twilio`

### API Accounts
You must obtain API keys from:
1. Alpha Vantage (Stock Price Data)
2. NewsAPI (News Articles)
3. Twilio (SMS Sending)

## Installation

1. Install required libraries:
```bash
pip install requests twilio
```

2. Set up your API keys:
- Replace `Stock_API_Key` with your Alpha Vantage API key
- Replace `News_API_Key` with your NewsAPI key
- Replace `account_sid` and `auth_token` with your Twilio credentials
- Replace the `from_` number with your Twilio phone number
- Replace the `to` number with the phone number where you want to receive alerts

## Configuration

You can customize the following variables:
- `STOCK_NAME`: Stock symbol (e.g., "TSLA")
- `COMPANY_NAME`: Full company name (e.g., "Tesla Inc")
- Percentage threshold for sending alerts (currently set at 5%)
- Number of news articles to retrieve

## How It Works

1. Fetches daily stock prices for the specified stock
2. Calculates price difference and percentage change
3. If percentage change exceeds 5%:
   - Retrieves top 3 recent news articles about the company
   - Sends SMS with stock performance and news headlines

## Security Notes

- Never commit your API keys to version control
- Use environment variables or a separate configuration file to store sensitive information

## Disclaimer

This application is for educational purposes. Always consult financial professionals before making investment decisions.

