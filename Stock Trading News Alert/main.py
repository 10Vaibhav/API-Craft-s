import requests as r
from twilio.rest import Client

STOCK_NAME = "TSLA"

COMPANY_NAME = "Tesla Inc"

News_API_Key = "" # Use Your Own News API_Key

Stock_API_Key = "" # Use Your Own Stock API_Key

Twilio_API_Key = ""# Use Your Own Twilio API_Key


account_sid = '' # Use Your Own Sid
auth_token = '' # Use Your Own Auth Token

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey={Stock_API_Key}"

json_data = r.get(url)
data = json_data.json()

Daily_data = data["Time Series (Daily)"]

closing_price = [date["4. close"] for date in Daily_data.values()]
# print(closing_price)

LastDay_closing_price = round(float(closing_price[0]))
print(f"Last Day Stock Closing Time : {LastDay_closing_price}.")

SecondLastDay_closing_price = int(float(closing_price[1]))
print(f"Second Last Day Stock Closing Time : {SecondLastDay_closing_price}.")

price_diff = LastDay_closing_price - SecondLastDay_closing_price
up_down = None
if price_diff > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

print(f"price difference between 1 Day : {price_diff}")


percentage_price_diff = round(((price_diff/SecondLastDay_closing_price)*100))

print(f"Percentage Difference of 1 day: {percentage_price_diff}%")


if percentage_price_diff > 5 :
    url = f"https://newsapi.org/v2/everything?apiKey={News_API_Key}&q={COMPANY_NAME}&language=en&sortBy=publishedAt&pageSize=10&page=1"

    response = r.get(url)
    News = response.json()
    articles = News["articles"][0:3]

    for article in articles:
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            from_ = "", # Use Your Twilio Number
            body=f"{STOCK_NAME} : {up_down}{percentage_price_diff}%\nHeadline:  {article["title"]}\nBrief: {article["description"]}",
            to = "" # Use Your Personal Number
        )

        print(message.sid)



