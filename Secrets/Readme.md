# Random Secrets Web Application

A Node.js/Express application that displays random secrets fetched from the Secrets API.

## Features

- Serves static files
- Fetches random secrets from external API
- Renders data using EJS templating

## Prerequisites

- Node.js
- npm

## Installation

```bash
npm install express axios body-parser ejs
```

## Configuration

The server runs on port 3000 by default.

## Project Structure

```
├── public/         # Static files
├── views/          # EJS templates
│   └── index.ejs
└── server.js       # Main application file
```

## API

The application fetches data from `secrets-api.appbrewery.com/random`

## Usage

Start the server:

```bash
node server.js
```

Access the application at `http://localhost:3000`

## Error Handling

The application includes basic error logging for API request failures.
