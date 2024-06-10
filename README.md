# Pensa Bot

[![GitHub issues](https://img.shields.io/github/issues/dom557/pensa-bot)](https://github.com/dom557/pensa-bot/issues)
[![GitHub forks](https://img.shields.io/github/forks/dom557/pensa-bot)](https://github.com/dom557/pensa-bot/network)
[![GitHub stars](https://img.shields.io/github/stars/dom557/pensa-bot)](https://github.com/dom557/pensa-bot/stargazers)
[![GitHub license](https://img.shields.io/github/license/dom557/pensa-bot)](https://github.com/dom557/pensa-bot/blob/main/LICENSE)

Pensa Bot is a Discord chat bot powered by the GPT-2 model from Hugging Face. Start a conversation with it using the command `!ask` followed by your query. This bot is designed to facilitate engaging and interactive discussions on your Discord server.

## Example Usage

To start a conversation with Pensa Bot, use the command:
```
!ask What do you want to talk about?
```

## Getting Started

Follow these instructions to set up and run Pensa Bot on your local machine for development and testing purposes.

### Prerequisites

Ensure you have the following installed:
- Python 3.8+
- pip

### Installation

1. Clone the repo:
    ```bash
    git clone https://github.com/dom557/pensa-bot.git
    ```
2. Navigate to the project directory:
    ```bash
    cd pensa-bot
    ```
3. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
4. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5. Create a `.env` file in the root directory and add the required environment variables:
    ```plaintext
    DISCORD_BOT_TOKEN=your_discord_bot_token
    ```

### Running the Bot

Start the bot by running:
```bash
python bot.py
```

## Feedback

If you have any feedback, please reach out to me [mail](kingmohaemed@gmail.com).

## FAQ

#### How do I start a conversation with Pensa Bot?
Use the command `!ask` followed by your question or topic. For example:
```
!ask How's the weather today?
```

#### What model does Pensa Bot use?
Pensa Bot uses the GPT-2 model from Hugging Face to generate responses.

## Authors

- [@dom557](https://github.com/dom557)
