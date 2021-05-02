import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print("works")


@client.event
async def on_member_join(member):
    guild = member.guild
    if guild.system_channel is not None:
        to_send = 'Welcome {0.mention} to {1.name}!'.format(member, guild)
        await guild.system_channel.send(to_send)


@client.event
async def on_message(message):
    if message.author.id == client.user.id:
        return
    msg = message.content.lower()
    if msg.startswith('hello') or msg.startswith('hi') or msg.startswith('hey'):
        await message.reply('hello ' + message.author.name, mention_author=True)
    await client.process_commands(message)


@client.command(aliases=["8ball"])
async def _8ball(ctx, *, question):
    answers = [" As I see it, yes.", "Ask again later.", "Better not tell you now.", "Cannot predict now.",
               "Concentrate and ask again.", "Don’t count on it.", "It is certain.", "It is decidedly so.",
               "Most likely.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Outlook good.",
               "Reply hazy, try again.", "Signs point to yes.", "Very doubtful.", "Without a doubt.", "Yes.",
               "Yes – definitely.", "You may rely on it."]
    await ctx.send(random.choice(answers))


@client.command()
async def ping(ctx: commands.Context):
    await ctx.send(f'{round(client.latency * 1000)}ms')


client.run('ODM4MjA1NjM1MzIwNjEwODU3.YI3t1A.LLF3zuqnpZPEo_rAoREoIyXS7cY')
