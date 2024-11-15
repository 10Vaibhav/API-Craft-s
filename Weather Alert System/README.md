# Weather-Alert-System
This Python script checks the weather forecast for a specific location and sends a message if rain is expected. 


## Requirements

To run this script, you'll need:

- Python 3.7+
- requests library
- twilio library
  
## Security Considerations

1. API keys and tokens should not be hardcoded in the script. Use environment variables instead.
3. Implement proper error handling and logging.
4. Be cautious when sharing code publicly to avoid exposing sensitive information.
   
## How It Works

1. API Setup:
   - The script uses OpenWeatherMap API for weather data and Twilio API for sending messages.
   - API keys and credentials are stored as environment variables.

2. Weather Data Retrieval:
   - A GET request is sent to the OpenWeatherMap API with location parameters.
   - The API returns weather forecast data for the specified location.

3. Weather Analysis:
   - The script parses the JSON response from the API.
   - It checks weather condition codes for the next few time periods.
   - Weather codes below 700 typically indicate rain or precipitation.

4. Rain Check:
   - If any upcoming weather condition has a code less than 700, 'will_rain' is set to True.

5. Sending Alert:
   - If rain is expected, the script uses the Twilio API to send a message.
   - The message warns about rain and reminds to bring an umbrella.

## Contributing

Contributions to improve the Weather Alert System are welcome.
