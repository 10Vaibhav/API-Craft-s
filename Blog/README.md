# BlogForge: Modern Express Blog Platform

A robust and elegant full-stack blogging platform built with Node.js, Express, and EJS templating engine. BlogForge provides a seamless writing and publishing experience through its clean interface and efficient client-server architecture.

## Features

- Create, read, update, and delete blog posts (CRUD operations)
- Clean and responsive user interface
- Server-side rendering with EJS templates
- RESTful API architecture
- In-memory data storage

## Project Structure

```
blogforge/
├── index.js          # API server
├── server.js         # Frontend server
├── views/
│   ├── index.ejs     # Main blog page
│   └── modify.ejs    # Create/Edit post page
├── public/
│   └── styles/
│       └── main.css  # Stylesheet
```

## Technical Stack

- **Backend**: Node.js & Express
- **Frontend**: EJS templates, HTML, CSS
- **API Communication**: Axios
- **Data Storage**: In-memory JavaScript array

## Setup and Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   npm install express body-parser axios ejs
   ```
3. Start the API server:
   ```bash
   node index.js
   ```
4. In a separate terminal, start the frontend server:
   ```bash
   node server.js
   ```
5. Access the application at `http://localhost:3000`

## API Endpoints

### Posts API (Running on port 4000)

- `GET /posts` - Retrieve all posts
- `GET /posts/:id` - Retrieve a specific post
- `POST /posts` - Create a new post
- `PATCH /posts/:id` - Update a specific post
- `DELETE /posts/:id` - Delete a specific post

### Frontend Server (Running on port 3000)

- `GET /` - Home page showing all posts
- `GET /new` - Page for creating a new post
- `GET /edit/:id` - Page for editing an existing post
- `POST /api/posts` - Handle new post creation
- `POST /api/posts/:id` - Handle post updates
- `GET /api/posts/delete/:id` - Handle post deletion

## Post Object Structure

```javascript
{
  id: Number,
  title: String,
  content: String,
  author: String,
  date: String (ISO format)
}
```

## Development

The project uses two separate servers:
- API Server (port 4000): Handles data operations and serves JSON
- Frontend Server (port 3000): Handles rendering and user interface

This separation allows for:
- Clear separation of concerns
- Independent scaling of frontend and backend
- Possibility to create multiple frontends using the same API

## Notes

- The current implementation uses in-memory storage, so data will be reset when the server restarts
- The frontend server proxies requests to the API server
- All dates are stored in ISO format
- Form validation is handled through HTML5 attributes

