import os
import logging

import discord
from discord.ext import commands
from transformers import pipeline, set_seed
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.INFO)

# Load environment variables from .env file
load_dotenv()

# Set up the Hugging Face pipeline for text generation
generator = pipeline('text-generation', model='gpt2')
set_seed(42)

# Set up discord.py bot with commands extension
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    logging.info(f'Logged in as {bot.user}')
    # Ensure your commands are registered with the Discord Developer Portal

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('!ask'):
        question = message.content[len('!ask'):].strip()
        logging.info(f"{question}")

        # Generate response using Hugging Face Transformers
        response = generator(question, max_length=50, num_return_sequences=1)
        reply = response[0]['generated_text'].strip()
        logging.info(f"AI response: {reply}")

        # Send AI's response
        await message.channel.send(reply)

if __name__ == "__main__":
    TOKEN = os.getenv("DISCORD_BOT_TOKEN")
    bot.run(TOKEN)
