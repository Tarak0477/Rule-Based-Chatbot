# Simple Chatbot using Traditional Approaches

A rule-based chatbot built with Microsoft Bot Framework that demonstrates traditional natural language processing techniques.

## Features

This chatbot implements the following capabilities:

1. **Greet users and respond to greetings** - Recognizes various greeting patterns (hello, hi, hey, good morning, etc.)
2. **Answer questions about itself** - Responds to identity questions like "who are you" or "what are you"
3. **Provide weather information** - Simulated weather responses
4. **Tell the current time and date** - Returns system time and date
5. **Perform basic calculations** - Handles addition, subtraction, multiplication, and division
6. **Tell jokes** - Shares programming-related humor
7. **List capabilities** - Type 'help' or 'what can you do' to see all features
8. **Handle malformed input** - Gracefully manages unrecognized or invalid input

## Requirements

- Python 3.8.2
- Microsoft Bot Framework SDK
- Bot Framework Emulator (for local testing)

## Installation

### 1. Create Anaconda Environment

```bash
conda create --name MSAI631_MBF python==3.8.2
conda activate MSAI631_MBF
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Install Bot Framework Emulator

Download from: https://github.com/microsoft/BotFramework-Emulator/releases

## Running the Bot

### Start the Bot Server

```bash
python app.py
```

The bot will start on `http://localhost:3978`

### Connect with Bot Framework Emulator

1. Open Bot Framework Emulator
2. Click "Open Bot"
3. Enter the bot URL: `http://localhost:3978/api/messages`
4. Click "Connect"

**Important:** Make sure to include `/api/messages` in the URL, otherwise you'll get 500 errors.

## Usage Examples

Try these commands with the bot:

- **Help:** "help", "what can you do", "capabilities"
- **Greetings:** "hello", "hi", "good morning"
- **Identity:** "who are you", "what are you"
- **Weather:** "what's the weather"
- **Time:** "what time is it", "tell me the time"
- **Date:** "what's the date", "what's today's date"
- **Jokes:** "tell me a joke", "something funny"
- **Calculations:** "5 + 3", "what is 10 * 2", "15 / 3"
- **Farewell:** "bye", "goodbye"

## Architecture

The chatbot uses a traditional rule-based approach with pattern matching:

- **Pattern Matching:** Uses keyword detection and regular expressions
- **Intent Recognition:** Identifies user intent through predefined patterns
- **Response Generation:** Returns appropriate responses based on matched patterns
- **Error Handling:** Gracefully handles unrecognized input with helpful suggestions

### Key Components

- `app.py` - Main application entry point and web server setup
- `bots/echo_bot.py` - Core chatbot logic with pattern matching and response generation
- `config.py` - Configuration settings for the bot
- `requirements.txt` - Python dependencies

## Extension Possibilities

This bot is designed to be easily extended with:

- Azure Cognitive Services integration
- Natural Language Understanding (NLU)
- Machine Learning models
- Database connectivity
- External API integrations
- Multi-turn conversations with state management

## Troubleshooting

### Common Issues

1. **Import Error with cffi:**
   ```bash
   pip -vvv install --upgrade --force-reinstall cffi
   ```

2. **500 Errors in Emulator:**
   - Ensure you're connecting to `http://localhost:3978/api/messages`
   - Verify the bot is running (`python app.py`)

3. **Python Version Issues:**
   - Must use Python 3.8.2 specifically
   - Verify with: `python --version`

## License

This project uses the Microsoft Bot Framework which is licensed under the MIT License.

## References

- Microsoft Bot Framework: https://dev.botframework.com/
- Bot Builder Samples: https://github.com/microsoft/BotBuilder-Samples
- Anaconda Documentation: https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
