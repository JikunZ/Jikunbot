import discord, asyncio
from discord.ext.commands import Bot
from discord import Server
p = Bot(command_prefix='j/')

#komendy zwykłe
@p.command()
async def commands():
    await p.say('``[Add "j/" before a command] List of commands - commands, info, invite, ping, ban, kick, avatar, delete (+amount)``')
	
@p.command()
async def ping():
	await p.say('Pong :ping_pong:')
	
@p.command()
async def info():
    await p.say('``Jikun Bot (Currently in Pre-Beta) is an Open-Source project to make fast, and easy-to-use bot. Documents of this bot will be published soon on GitHub``')
	
@p.command(pass_context=True)
async def avatar(ctx):
	await p.say(ctx.message.author.avatar_url)
	
@p.command(pass_context=True)
async def delete(ctx, amount):
    amount = int(amount)
    await p.purge_from(ctx.message.channel, limit=amount)
	
@p.command()
async def invite():
	await p.say('https://discordapp.com/oauth2/authorize?&client_id=303531537457086465&scope=bot&permissions=0')
#__________________________________________________________________________________________________________________________________
	
#komendy moderacyjne
@p.command()
async def gggame(ctx, *, a):
    await p.change_presence(game=discord.Game(name=a, type=1, url='https://www.twitch.tv/nocopyrightsounds'))
	
@p.command()
async def ssstream(ctx, *, a):
    await p.change_presence(game=discord.Game(name=a, type=0, url='https://www.twitch.tv/nocopyrightsounds'))
	
@p.command(pass_context=True)
async def kick(ctx, user: discord.Member = None):
	try:
		if ctx.message.author.id == '216134373345460224' or '326401460906622978':
			await p.kick(user)
	except Exception as e:
		await p.send_message(ctx.message.channel, "" + e + "")
		
@p.command(pass_context=True)
async def ban(ctx, user: discord.Member = None):
	try:
		if ctx.message.author.id == '216134373345460224' or '326401460906622978':
			await p.ban(user)
	except Exception as e:
		await p.send_message(ctx.message.channel, "" + e + "")
	

	
p.run('MzAzNTMxNTM3NDU3MDg2NDY1.DIAsYg.Z9eUghVGXmm8aw2nxTYHEOE8OIs')