AIgor - Multifunctional Telegram Bot
AIgor is a powerful and versatile Telegram bot built on a modular architecture that leverages multiple external APIs to handle a wide range of user requests. From generating text and images to searching the web and managing notes, AIgor provides a seamless and intelligent user experience.

https://img.shields.io/badge/Telegram-Bot-blue?logo=telegram
https://img.shields.io/badge/Python-3.10%252B-yellow?logo=python
https://img.shields.io/badge/License-MIT-green.svg

https://github.com/user-attachments/assets/48e28e76-300a-45b8-8d12-1987c4e52bad

✨ Features
Multimodal Input/Output: Supports text, image, and audio generation.

Natural Language Processing: Understands and processes complex user requests using the Gemini model.

Web Search: Finds relevant information online using the Google Search API.

Map Search: Retrieves geographic data and locations via OpenStreetMap.

Text-to-Speech: Converts text responses into audio messages using Edge TTS.

Smart Command Routing: Intelligently parses user intent and routes requests to the appropriate service.

Reminder Notes: Create and manage notes with reminders (implementation details in code).

🏗️ System Architecture
The bot is designed as a sophisticated request-processing pipeline:

User Input: A user sends a message via the Telegram API.

Request Reception: The Telegram Bot server receives and forwards the request.

Intent Recognition: The heart of the system. The user's prompt, along with context, is sent to a lightweight LLM (e.g., Gemini Flash 1.5 8B) to determine the user's intent and the specific command to execute.

API Routing: Based on the parsed command, the bot routes the request to the appropriate specialized API:

Gemini Pro/Flas h - For advanced text generation and conversation.

Kandinsky - For image generation.

Google Search API - For fetching information from the web.

OpenStreetMap (Nominatim) - For geocoding and map data.

Edge TTS - For converting text to speech.

Response Handling: The bot receives the response from the external API, formats it, and sends the final result back to the user through the Telegram API.

This architecture allows for efficient and scalable handling of diverse and complex user queries by leveraging the best tools for each task.

🚀 Getting Started
Prerequisites
Python 3.10 or higher

A Telegram Bot Token from @BotFather

API keys for the services you plan to use (Google Gemini, Google Search, etc.)

Installation
Clone the repository:

bash
git clone https://github.com/FabulousGitHub/aigor-bot.git
cd aigor-bot
Create a virtual environment and activate it:

bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install the required dependencies:

bash
pip install -r requirements.txt
Configure environment variables:
Create a .env file in the root directory and add your API keys:

ini
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
GEMINI_API_KEY=your_gemini_api_key_here
GOOGLE_SEARCH_API_KEY=your_google_search_api_key_here
GOOGLE_CSE_ID=your_custom_search_engine_id_here
# Add other API keys as needed
Run the bot:

bash
python main.py
📁 Project Structure
text
aigor-bot/
├── main.py                 # Main application entry point
├── bot/
│   ├── __init__.py
│   ├── core.py            # Core bot logic and handler setup
│   ├── command_router.py  # Intent recognition and command routing
│   └── handlers/          # Modules for handling different commands
│       ├── text_generation.py
│       ├── image_generation.py
│       ├── web_search.py
│       ├── maps.py
│       └── tts.py
├── utils/                 # Helper functions (API clients, formatters)
├── .env.example          # Example environment variables file
├── requirements.txt      # Project dependencies
└── README.md
🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request

📜 License
This project is distributed under the MIT License. See the LICENSE file for more information.

⚠️ Disclaimer
This bot is intended for educational and personal use. Please ensure you comply with the Terms of Service for all integrated APIs (Google, Telegram, etc.) and use the bot responsibly.

💬 Support
If you have any questions or run into issues, please open an Issue on this repository.
