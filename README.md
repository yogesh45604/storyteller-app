# Storyteller App

A FastAPI-based web service that generates stories and images using AI models. Users can specify genre, characters, and number of sections, and receive a story with AI-generated images.

## Features

- Generate creative stories based on user prompts
- Create images for each story section using AI
- REST API with `/generate` endpoint
- Static file serving for generated images

## Project Structure
storyteller-app/ ├── app.py ├── deepinfra_api.py ├── main.py ├── models.py ├── requirements.txt ├── utils.py ├── static/ └── pycache/

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yogesh45604/storyteller-app.git
   cd storyteller-app