# DharaaBot

An AI-powered chatbot application built with Flask backend and interactive frontend, powered by Google's Gemini API.

## Overview

DharaaBot is a conversational chatbot that provides intelligent responses using Google's Gemini AI model. The application features a clean, modern web interface with a fixed chatbot widget and a robust backend API.

## Features

- 🤖 AI-powered responses using Google Gemini API
- 💬 Real-time chat interface
- 🎨 Modern, responsive UI built with Tailwind CSS
- 🔄 CORS-enabled for cross-origin requests
- 🛡️ Environment-based configuration for secure API key management
- 📱 Mobile-friendly chat widget

## Tech Stack

### Backend
- **Framework**: Flask
- **Language**: Python
- **Dependencies**:
  - `flask` - Web framework
  - `flask-cors` - Cross-Origin Resource Sharing
  - `python-dotenv` - Environment variable management
  - `requests` - HTTP requests library

### Frontend
- **HTML5** - Markup
- **Tailwind CSS** - Styling
- **Vanilla JavaScript** - Interactivity
- **Material Icons** - UI icons

## Project Structure

```
DharaaBot/
├── backend/
│   ├── app.py              # Flask application and API routes
│   └── requirement.txt      # Python dependencies
├── frontend/
│   └── index.html          # Chat interface
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

## Installation

### Prerequisites
- Python 3.8+
- Git
- Google Gemini API Key

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/DharaaBot.git
   cd DharaaBot
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r backend/requirement.txt
   ```

4. **Configure environment variables**
   Create a `.env` file in the project root:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## Usage

1. **Start the backend server**
   ```bash
   python backend/app.py
   ```
   The Flask server will run on `http://localhost:5000`

2. **Open the frontend**
   - Open `frontend/index.html` in your web browser
   - Click the chatbot widget to start chatting

## API Endpoints

### POST `/chat`
Sends a message to the chatbot and returns an AI-generated response.

**Request:**
```json
{
  "message": "Hello, how are you?"
}
```

**Response:**
```json
{
  "reply": "I'm doing well, thank you for asking!"
}
```

## Environment Variables

- `GEMINI_API_KEY` - Your Google Gemini API key (required)

## Getting Started with Gemini API

1. Visit [Google AI Studio](https://aistudio.google.com)
2. Create a new API key
3. Add it to your `.env` file

## Contributing

Feel free to submit issues and enhancement requests!


## Contact

For questions or support, please open an issue on GitHub.

---

