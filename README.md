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
python gemini.py

💬 Support
If you have any questions or run into issues, please open an Issue on this repository.
