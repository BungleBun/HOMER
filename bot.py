#Testing to make sure my new git setup works after switching to linux
import os
import discord
from dotenv import load_dotenv

#TOKEN AND ID VARIABLES FROM ENV FILE
load_dotenv()
token = os.getenv("DISCORD_TOKEN")
id = os.getenv("USER_ID")

#BOT PERMISSIONS
intents = discord.Intents.default()
intents.message_content = True

#CLIENT
client = discord.Client(intents=intents)

#FUNCTION TO TEST IF IT WORKS
@client.event
async def on_ready():
    print(f"Logged in as {client.user.name}!")

    try:

        user = await client.fetch_user(id)
        await user.send(f"Hello {user.name}! Homer is online!")

    except discord.Forbidden:
        print("Could not send message")

    except Exception as e:
        print(f"error occurred {e}.")

if __name__ == "__main__":
    client.run(token)


