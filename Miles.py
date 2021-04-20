import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>')
#client = discord.Client

@bot.command()
async def ping(ctx):#simple command for testing if the bot is alive
    await ctx.send('pong')
    pass

@bot.command()
async def vote(ctx, *, arg):
    msg = await ctx.send("New vote from " + ctx.author.display_name + ": \n > " + arg)
    react = await msg.add_reaction("\N{THUMBS UP SIGN}")
    react2 = await msg.add_reaction("\N{RAISED HAND}")
    react3 = await msg.add_reaction("\N{THUMBS DOWN SIGN}")
    delete = await ctx.message.delete()
    pass

@bot.command()
async def echo(ctx, *, arg):#repeats the text a user sends
    await ctx.send(arg)
    pass

@bot.command()
async def shutdown(ctx):
    if await bot.is_owner(ctx.message.author):
        await ctx.send("Shutting down...")
        await bot.logout()
    else:
        await ctx.send("<@"+str(ctx.message.author.id)+">, you do not have permission to use that command. This incident has been logged.")
        print(str(ctx.message.author)+" has tried to run a restricted command.")
    pass

@bot.command()
async def feedbackMode(ctx):
    if await bot.is_owner(ctx.message.author):
        await ctx.send("Awaiting input:")
        while True:
            text = input(">")
            if text == "stop":
                print("Aborting...")
                break
            else:
                await ctx.send(text)
        print("Aborted.")
        await ctx.send("Feedback mode aborted.")
    else:
        await ctx.send("<@"+str(ctx.message.author.id)+">"+", you do not have permission to use that command. This incident has been logged.")
        print(str(ctx.message.author)+" has tried to run a restricted command.")
    pass

#@bot.command()
#async def join(ctx):
#    """Joins a voice channel"""
 #   voice_channel = client.get_channel(701585271665459233)
#
 #   await voice_channel.connect()

print("Running Miles...")
bot.run("BotKeyHere")
