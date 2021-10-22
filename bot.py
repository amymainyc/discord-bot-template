import os
from discord.ext import commands


token = "INSERT TOKEN HERE"
client = commands.Bot(command_prefix="!", case_insensitive=True, help_command=None)

def loadCogs():
    for file in os.listdir("cogs"):
        if file.endswith(".py"):
            name = file[:-3]
            client.load_extension(f"cogs.{name}")
            print(f"Loaded cogs.{name}")


loadCogs()

client.run(token)
