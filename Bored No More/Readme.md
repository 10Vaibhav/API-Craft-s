# BoredNoMore 🎯

A web application that helps cure boredom by suggesting activities based on type and number of participants. Never run out of things to do again!

## Features 🌟

- Get random activity suggestions
- Filter activities by type (education, charity, recreational, etc.)
- Filter by number of participants (1-4)
- Clean and intuitive user interface
- Error handling for invalid combinations

## Technologies Used 💻

- Node.js
- Express.js
- EJS (Embedded JavaScript templating)
- Axios for API calls
- Body-parser for parsing POST requests
- Custom CSS for styling

## Installation 🚀

1. Install dependencies:
```bash
npm install
```

2. Start the server:
```bash
node index.js
```

3. Open your browser and navigate to:
```
http://localhost:3000
```

## Usage 📝

1. Visit the homepage to get a random activity suggestion
2. Use the dropdown menus to filter:
   - Activity type (education, charity, recreational, etc.)
   - Number of participants (1-4 people)
3. Click "Go" to get a filtered suggestion
4. If no activities match your criteria, you'll receive an error message

## API Reference 🔗

This project uses the Bored API with the following endpoints:
- Random activity: `GET /random`
- Filtered activity: `GET /filter?type={type}&participants={participants}`

## File Structure 📁

```
bored-no-more/
├── public/
│   └── styles/
│       └── main.css
├── views/
│   └── index.ejs
├── index.js
├── package.json
└── README.md
```

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments 👏

- Thanks to the Bored API for providing activity data
- The App Brewery for the API endpoint
