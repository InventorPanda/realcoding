import discord
from discord.ext import commands
from discord.utils import get
import datetime
import random

TOKEN = 'NzExMDM2ODM0NDMxNjMxNDUw.XsW02g.Yx1OwO1pSBNKKYIA9kA3Kl1U9zM'

description = '''George's Personal Discord Bot'''
bot = commands.Bot(command_prefix='--', description=description)

announcements = 12


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    
#@bot.event
#async def on_reaction_add(reaction, user):
#    emojiyes = discord.utils.get(guild.emojis, name='thumbsup')
#    if Reaction.message.id == 711686849881440297:
#        if Reaction.emoji == emojiyes:
#            Reaction.user
       

@bot.event
async def on_member_join(member):
    #712011973855936583
    channel = bot.get_channel(712011973855936583)
    await channel.send(str(member.name) + " Joined the Server. Did they come back, or are they new???")

@bot.event
async def on_member_remove(member):
    #712011973855936583
    channel = bot.get_channel(712011973855936583)
    await channel.send(member.name + " Left the Server. Will they come back?")
@bot.event
async def on_user_update(before, after):
    #712011973855936583
    channel = bot.get_channel(712011973855936583)
    if before.name != after.name:
        await channel.send("From " + before.name + " to " + after.name + ", an update occurred!")
    if before.avatar != after.avatar:
        await channel.send("User "+ str(after.name) + " Updated their avatar!!!")

@bot.command()
async def hello(ctx):
    """Tests the main functionality"""
    await ctx.send("hello world!!!")

@bot.command()
async def roll(ctx, die):
    """Rolls a dice with die as the number of sides"""
    await ctx.send("Rolled a " + (random.randint(1, die)) + " out of "+ str(die))


@bot.command()
async def stats(ctx, accountPing):
    """Discord Account stats, accountPing is the @ for your account"""
    await ctx.send("Stats for user " + str(accountPing))
    await ctx.send("Sorry, panda broke this command by forgetting to finish it before playing D&D")
@bot.command()
async def announce(context, rol, annc):
    channel = bot.get_channel(711286405212667948)
    """Announces something, but only when Panda does it. If you need to make an announcement, DM Him!!!"""
    global announcements
    announcements = announcements + 1
    await channel.send("**Announcement No. " + str(announcements) + "**")
    await channel.send(rol + ": ")
    await channel.send('`' + annc + '`')
    await channel.send("Don't blame Panda for the ping, but sorry anyways :P")

@bot.command()
async def listbanned(ctx, guild):
    """Lists ban logs"""
    async for entry in guild.audit_logs(action=discord.AuditLogAction.ban):
            context.say('{0.user} banned {0.target}'.format(entry))
@bot.command(pass_context=True)
async def no_pings(ctx):
    member = ctx.message.author
    role = get(member.server.roles, name="Ping Me! I'm Cool with it")
    role2 = get(member.server.roles, name="no pings")
    role3 = get(member.server.roles, name="Announcement Pings")
    await bot.add_roles(member, role2)
    await bot.remove_roles(member, role3)
    await bot.remove_roles(member, role1)
@bot.command(pass_context=True)
async def announcement_pings(ctx):
    member = ctx.message.author
    role = get(member.server.roles, name="Ping Me! I'm Cool with it")
    role2 = get(member.server.roles, name="no pings")
    role3 = get(member.server.roles, name="Announcement Pings")
    await bot.add_roles(member, role3)
    await bot.remove_roles(member, role1)
    await bot.remove_roles(member, role2)

@bot.command(pass_context=True)
async def yes_pings(ctx):
    member = ctx.message.author
    role = get(member.server.roles, name="Ping Me! I'm Cool with it")
    role2 = get(member.server.roles, name="no pings")
    role3 = get(member.server.roles, name="Announcement Pings")
    await bot.add_roles(member, role)
    await bot.remove_roles(member, role3)
    await bot.remove_roles(member, role2)
@bot.command()
async def message_panda(ctx, message):
    await ctx.send("Messaging Pandaboy (George) through the power of Python")
    print(message)
bot.run(TOKEN)