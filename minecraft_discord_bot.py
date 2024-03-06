from decouple import config
import discord
from discord.ext import commands
import subprocess
from datetime import datetime

TOKEN = config("DISCORD_TOKEN")
bot = commands.Bot(intents=discord.Intents.all(), command_prefix='!')
bot.help_command = commands.DefaultHelpCommand()

@bot.command()
async def restart(ctx: commands.Context):
    """
    Restarts the minecraft server container (hard stop)
    """
    now = datetime.now()
    exec_time = (now.strftime("%b-%d %I:%M %p"))
    await ctx.send("Restart command has been received. The server should do a full restart shortly")
    subprocess.run(("./server_commands.sh","0"), capture_output=True)
    msg = (f"{ctx.author.mention} restarted the server at {exec_time}")
    user = await bot.fetch_user(532684925208363017) #finds me
    await user.send(msg)
@bot.command()
async def stop(ctx: commands.Context):
    """
    Stops the minecraft server; Saves the server files (graceful stop)
    """
    now = datetime.now()
    exec_time = (now.strftime("%b-%d %I:%M %p"))
    await ctx.send("Stop command has been received. Please wait 5 minutes to allow the server time to save the files. You can check periodically for the servers status by using the `!status` command. If the command returns that the server is no longer running. You can restart it with the `!restart` command")
    subprocess.run(("./server_commands.sh","1"), capture_output=True)
    msg = (f"{ctx.author.mention} stopped the server at {exec_time}")
    user = await bot.fetch_user(532684925208363017) #finds me
    await user.send(msg) #sends me who reset the button

    return 0
@bot.command()
async def status(ctx: commands.Context):
    """
    Returns the status of the server
    """
    message = subprocess.check_output(["./server_commands.sh","3"])
    await ctx.send(message.decode().strip())
bot.run(TOKEN)