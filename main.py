from os import environ
import discord

bot = discord.Client()

counter = 0

@bot.event
async def on_ready():
    guild_count = 0

    for guild in bot.guilds:
        print(f"- {guild.id} (name: {guild.name})")
        guild_count += 1

    print(f"Bot is in {guild_count} guilds")

@bot.event
async def on_message(message):
    msg = message.content
    channel = message.channel.name
    if channel == "bot-testing":
        print(f"Got message: {msg}")
        for char in msg:
            action = parse_command(char)
            print(action)

def parse_command(cmd):
    global counter
    counter += 1 

    match cmd.lower():
        case "w":
            return f"{counter}: Forward"
        case "a":
            return f"{counter}: Left"
        case "s":
            return f"{counter}: Backward"
        case "d":
            return f"{counter}: Right"
        case _:
            return f"{counter}: Invalid"

bot.run(environ.get("DISCORD_TOKEN"))
