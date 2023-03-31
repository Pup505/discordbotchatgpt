import os
import discord
import openai
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

TOKEN = os.getenv('DISCORD_TOKEN')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
BOT_PREFIX = "!gpt "

client = discord.Client()

# Set up OpenAI API
openai.api_key = OPENAI_API_KEY
model_engine = "text-davinci-002"

# Function to generate response from OpenAI API
def generate_response(prompt):
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = response.choices[0].text
    return message.strip()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(BOT_PREFIX):
        prompt = message.content[len(BOT_PREFIX):].strip()
        response = generate_response(prompt)
        await message.channel.send(response)

client.run(TOKEN)
