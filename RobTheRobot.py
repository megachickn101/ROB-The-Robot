import sqlite3
import random
import discord
from discord.ext import commands
from discord.utils import get
import datetime
import asyncio
import time
import praw
import json
import os

client = commands.Bot(command_prefix = 'r.')
client.remove_command('help')

reddit = praw.Reddit(client_id='4fqBCl9I0Cc2KQ',
					client_secret='xS0C9f2q3P3hnSeUJZnUlsYHPKg',
					user_agent='A meme scraper For Another Bot (by /u/megachickn)')

def is_it_me(ctx):
	return ctx.author.id == 601881016461819907

@client.event
async def on_ready():
	await client.change_presence(status=discord.Status.idle, activity=discord.Game('With Power'))
	print('ROB Is Online')

@client.event
async def on_member_join(member):
	print(f'{member} has joined the server.')

@client.event
async def on_member_remove(member):
	print(f'{member} has left the server.')

@client.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		await ctx.send("Hey! Just Telling You That That's Not A Command. Try r.help If You Forgot It")
		print('An Incorrect Command Was Used')

	elif isinstance(error, commands.MissingRequiredArgument):
		await ctx.send(f'Umm Hey,You Kinda Forgot To Add An Argument')
		print('Someone Did Not Ask A Question')

	elif isinstance(error, commands.MissingPermissions):
		await ctx.send(f'Hey! You Arent Supposed To Be Using That Command!')
		print('Someone Tried To Use A Command That They Did Not Have Permissions To Do')

	else:
  		raise error

@client.command()
async def calibrate(ctx):
	await ctx.author.send('Calibration Registered')
	print('Calibration Registered')
	return

#WARNING CHEAT CODES/ EASTER EGGS

@client.command()
async def NintendoSwitch(ctx, amount=1):
	conn = sqlite3.connect('blacklist.db')
	c = conn.cursor()
	user = ctx.author.id
	c.execute("SELECT * FROM blacklist WHERE user_id=?", (user,))
	result = c.fetchone()
	if result is None:
		await ctx.channel.purge(limit=amount)
		await ctx.author.send('SW-4344-5684-9895')
		await ctx.author.send('Yay! You Uncovered Our Easter Egg!!! That Doesnt Mean You Can Screw It Up For Everyone Else And Spoil The Suprise. So Again, Congrats For Uncovering Our Secret, Be Sure To Uncover More :D')
		print('Command Used: EE:NintendoSwitch')
		return
		c.close()
		conn.close()

	else:
		await ctx.send("Ok! Wait... I Never Saw You. My Creator Doesn't Want You To Use Me")
		c.close()
		conn.close()

@client.command()
async def AprilTwentySeven(ctx, amount=1):
	conn = sqlite3.connect('blacklist.db')
	c = conn.cursor()
	user = ctx.author.id
	c.execute("SELECT * FROM blacklist WHERE user_id=?", (user,))
	result = c.fetchone()
	if result is None:
		await ctx.channel.purge(limit=amount)
		await ctx.author.send('https://i.ytimg.com/vi/ykHAwUhjjGE/maxresdefault.jpg')
		await ctx.author.send('Yay! A Birthday')
		await ctx.author.send('Yay! You Uncovered Our Easter Egg!!! That Doesnt Mean You Can Screw It Up For Everyone Else And Spoil The Suprise. So Again, Congrats For Uncovering Our Secret, Be Sure To Uncover More :D')
		print('Command Used: EE:AprilTwentySeven')
		return
		c.close()
		conn.close()

	else:
		await ctx.send("Ok! Wait... I Never Saw You. My Creator Doesn't Want You To Use Me")
		c.close()
		conn.close()

@client.command()
async def ANGRYGOOSE(ctx, amount=1):
	conn = sqlite3.connect('blacklist.db')
	c = conn.cursor()
	user = ctx.author.id
	c.execute("SELECT * FROM blacklist WHERE user_id=?", (user,))
	result = c.fetchone()
	if result is None:
		await ctx.channel.purge(limit=amount)
		await ctx.author.send('https://samperson.itch.io/desktop-goose')
		await ctx.author.send('Yay! You Uncovered Our Easter Egg!!! That Doesnt Mean You Can Screw It Up For Everyone Else And Spoil The Suprise. So Again, Congrats For Uncovering Our Secret, Be Sure To Uncover More :D')
		print('Command Used: EE:ANGRYGOOSE')
		return
		c.close()
		conn.close()

	else:
		await ctx.send("Ok! Wait... I Never Saw You. My Creator Doesn't Want You To Use Me")
		c.close()
		conn.close()

@client.command()
async def ResearchSucks(ctx, amount=1):
	conn = sqlite3.connect('blacklist.db')
	c = conn.cursor()
	user = ctx.author.id
	c.execute("SELECT * FROM blacklist WHERE user_id=?", (user,))
	result = c.fetchone()
	if result is None:
		await ctx.channel.purge(limit=amount)
		await ctx.author.send('https://discord.gg/MVW5SgG')
		await ctx.author.send('Yay! You Uncovered Our Easter Egg!!! That Doesnt Mean You Can Screw It Up For Everyone Else And Spoil The Suprise. So Again, Congrats For Uncovering Our Secret, Be Sure To Uncover More :D')
		print('Command used: EE:ResearchSucks')
		c.close()
		conn.close()

	else:
		await ctx.send("Ok! Wait... I Never Saw You. My Creator Doesn't Want You To Use Me")
		c.close()
		conn.close()

@client.command()
async def AdVeNtUrE(ctx, amount=1):
	conn = sqlite3.connect('blacklist.db')
	c = conn.cursor()
	user = ctx.author.id
	c.execute("SELECT * FROM blacklist WHERE user_id=?", (user,))
	result = c.fetchone()
	if result is None:
		await ctx.channel.purge(limit=amount)
		await ctx.author.send ('This Game For The Atari Was Fundemental For Easter Eggs')
		await ctx.author.send('Yay! You Uncovered Our Easter Egg!!! That Doesnt Mean You Can Screw It Up For Everyone Else And Spoil The Suprise. So Again, Congrats For Uncovering Our Secret, Be Sure To Uncover More :D')
		print('Command Used: EE:AdVeNtUrE')
		c.close()
		conn.close()

	else:
		await ctx.send("Ok! Wait... I Never Saw You. My Creator Doesn't Want You To Use Me")
		c.close()
		conn.close()

@client.command()
async def PeppaChicken(ctx, amount=1):
	conn = sqlite3.connect('blacklist.db')
	c = conn.cursor()
	user = ctx.author.id
	c.execute("SELECT * FROM blacklist WHERE user_id=?", (user,))
	result = c.fetchone()
	if result is None:
		await ctx.channel.purge(limit=amount)
		await ctx.author.send ('DISCUSTANG')
		await ctx.author.send('Yay! You Uncovered Our Easter Egg!!! That Doesnt Mean You Can Screw It Up For Everyone Else And Spoil The Suprise. So Again, Congrats For Uncovering Our Secret, Be Sure To Uncover More :D')
		print('Command Used: EE:PeppaChicken')
		c.close()
		conn.close()

	else:
		await ctx.send("Ok! Wait... I Never Saw You. My Creator Doesn't Want You To Use Me")
		c.close()
		conn.close()

	#Fun Stuff--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#r.8ball/_8ball Question
@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
	conn = sqlite3.connect('blacklist.db')
	c = conn.cursor()
	user = ctx.author.id
	c.execute("SELECT * FROM blacklist WHERE user_id=?", (user,))
	result = c.fetchone()
	if result is None:
		responses = ['Yes', 'No', 'Maybe', 'Try Again Later']
		await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')
		print('Command Used: 8ball')
		return
		c.close()
		conn.close()

	else:
		await ctx.send("Ok! Wait... I Never Saw You. My Creator Doesn't Want You To Use Me")
		c.close()
		conn.close()


@client.command()
async def say(ctx, *, message, amount=1):
	conn = sqlite3.connect('blacklist.db')
	c = conn.cursor()
	user = ctx.author.id
	c.execute("SELECT * FROM blacklist WHERE user_id=?", (user,))
	result = c.fetchone()
	if result is None:
		username = ctx.author.name
		await ctx.channel.purge(limit=amount)
		await ctx.send(f'{message}\n')
		await ctx.send(f'-{username}')
		print(f'Command Used: say {message}')
		return
		c.close()
		conn.close()

	else:
		await ctx.send("Ok! Wait... I Never Saw You. My Creator Doesn't Want You To Use Me")
		c.close()
		conn.close()

#r.askRob Question
@client.command(aliases=['NintendoSucksJK'])
async def askROB(ctx, *, question):
	conn = sqlite3.connect('blacklist.db')
	c = conn.cursor()
	user = ctx.author.id
	c.execute("SELECT * FROM blacklist WHERE user_id=?", (user,))
	result = c.fetchone()
	if result is None:
		responses = ['Yes', 'No', 'Maybe', 'Uhhhh SHUT DOWN', 'BUY FROM NINTENDO!!!', 'NINTENDO!!!!', 'Gyromite', 'NES!!!!', 'FAMILY FRIENDLY!!!!!!']
		await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')
		print('Command Used: askRob')
		return
		c.close()
		conn.close()

	else:
		await ctx.send("Ok! Wait... I Never Saw You. My Creator Doesn't Want You To Use Me")
		c.close()
		conn.close()

#r.dice
@client.command(aliases=['Gambling'])
async def dice(ctx):
	conn = sqlite3.connect('blacklist.db')
	c = conn.cursor()
	user = ctx.author.id
	c.execute("SELECT * FROM blacklist WHERE user_id=?", (user,))
	result = c.fetchone()
	if result is None:
		options = ['1','2','3','4','5','6']
		await ctx.send(f'{random.choice(options)}')
		print('Command Used: dice')
		return
		c.close()
		conn.close()

	else:
		await ctx.send("Ok! Wait... I Never Saw You. My Creator Doesn't Want You To Use Me")
		c.close()
		conn.close()

@client.command()
async def roast(ctx):
	conn = sqlite3.connect('blacklist.db')
	c = conn.cursor()
	user = ctx.author.id
	c.execute("SELECT * FROM blacklist WHERE user_id=?", (user,))
	result = c.fetchone()
	if result is None:
		options = ['You look like something that I would draw with my left hand.', 'I refuse to have a battle of wits with somebody who is unarmed!', 'If I ever said anything to offend you, it was purely intentional.', 'Im not saying that I hate you, but I would unplug your life support to charge my phone.', 'In spite of what it did to you, dont you love nature?', 'Ive seen someone like you before, but I had to pay admission.', 'You have the perfect face for radio!', 'Youre not as bad as people say. Youre a whole lot worse.', 'Im not sure what your problem is, but Id be wiling to bet that its hard to pronounce.', 'Its pretty easy to figure out when youre lying. Your lips are moving.', 'Wow! You look like a before picture!', 'I wanted to give you a nasty look, but you already had one.', 'I dont think youre un-intelligent. You just have bad luck when it comes to thinking.', 'Brains arent everything. And, in your case, theyre nothing.', 'Its looks like your face caught on fire and somebody tried to extinguish it with a hammer.', 'Its really great to see how you dont let your education get in the way of your ignorance.', 'They say that we all sprang from apes. As it stands, you didnt seem to spring far enough.', 'Im really jealous of everyone that hasnt met you!', 'Most people live and learn. Apparently you just live.', 'There is only one problem with your face...I can see it.', 'So a thought crossed your mind? Well, that journey must have been long and lonely.', 'Its amazing what youve done with your hair! How did you manage to grow it out of your nostrils like that?', 'Hey, theres something on your chin. No, no...the third one down.', 'They say that laughter is the medicine. Seems like your face is curing the world!', 'You were born on a highway right? Because that’s where most accidents happen.']
		await ctx.send(f'{random.choice(options)}')
		print('Command Used: roast')
		return
		c.close()
		conn.close()

	else:
		await ctx.send("Ok! Wait... I Never Saw You. My Creator Doesn't Want You To Use Me")
		c.close()
		conn.close()


#r.coinflip
@client.command(aliases=['Bet', 'Heads Or Tails'])
async def coinflip(ctx):
	conn = sqlite3.connect('blacklist.db')
	c = conn.cursor()
	user = ctx.author.id
	c.execute("SELECT * FROM blacklist WHERE user_id=?", (user,))
	result = c.fetchone()
	if result is None:
		options = ['Heads', 'Tails']
		await ctx.send(f'You Flipped Your Lucky Penny, It Landed On {random.choice(options)}')
		print('Command Used: Coinflip')
		return
		c.close()
		conn.close()

	else:
		await ctx.send("Ok! Wait... I Never Saw You. My Creator Doesn't Want You To Use Me")
		c.close()
		conn.close()


@client.command(aliases=['unspiration'])
async def inspiration(ctx):
	conn = sqlite3.connect('blacklist.db')
	c = conn.cursor()
	user = ctx.author.id
	c.execute("SELECT * FROM blacklist WHERE user_id=?", (user,))
	result = c.fetchone()
	if result is None:
		options = ['https://static.boredpanda.com/blog/wp-content/uploads/2018/11/BYY1f3gBqKS-png__700.jpg', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/Untitled-1-5bea92837351f-png__700.jpg', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/BfkCPE6hZdd-png__700.jpg', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/BZO4Kt2B4Y7-png__700.jpg', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/BhxRQCQDBr7-png__700.jpg', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/BebkoyEhLyw-png__700.jpg', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/Untitled-1-5bea92fb7b707-png__700.jpg', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/BmhWhnqAu6b-1-png__700.jpg', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/BXWR4fLh0ul-4-png__700.jpg', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/Bdga2TSh4hK-png__700.jpg', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/BgsjL9Sh4PD-png__700.jpg', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/Bmbf4AtAQiB-1-png__700.jpg', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/BfYwkP0h9pO-png__700.jpg', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/BkYLpXqgr8Q-1-png__700.jpg', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/BYT4wNBhYZZ-png__700.jpg', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/BhWpmTjji0x-png__700.jpg', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/BlGkANAgLu_-1-png__700.jpg', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/BprziFAjOkz-png__700.jpg', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/BaUunaxBYzl-png__700.jpg', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/BmUdHbZACXi-1-png__700.jpg', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/Bghul-ghD4r-png__700.jpg', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/BiDDUkkAmsD-png__700.jpg', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/Bhj-PZyDby9-png__700.jpg', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/BhR_xqdjaLc.png', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/BZWYLLVBYL--png__700.jpg', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/BpGwEYRjeRm-png__700.jpg', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/BY_TBEch0Fp-png__700.jpg', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/BmB9zZHADDl-1-png__700.jpg', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/BgUHn6vBNNV.png', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/BbK2xTahu0k-png__700.jpg', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/BoVHwjKDmWx-png__700.jpg', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/Untitled-1-5bea93b04eb26.png', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/BYOroNphG7g-png__700.jpg', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/Bmo9zkYgtFZ-1-png__700.jpg', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/BncYXxfAcym-png__700.jpg', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/BpIM9qoDXQ6-png__700.jpg', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/BYOWZI-hdHf.png', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/BbZ3jQnhTUe-png__700.jpg', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/Untitled-1-5bea9372c2c6b-png__700.jpg', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/BaZVb2mBe78-png__700.jpg', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/BjbmR7bAqKC.png', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/BlMZXQYgQAh-1-png__700.jpg', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/Bpne5uWjbaf-png__700.jpg', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/Bk01uowgc4s-png__700.jpg', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/BgNAwdMhMS9-png__700.jpg', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/Bik3LRYgpZJ-png__700.jpg', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/Bm4tj5DAuxR-png__700.jpg', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/Bn4AyciAet4-png__700.jpg', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/BZcBQDEBgFC-png__700.jpg', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/Bic3EWTATdA-png__700.jpg', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/BmO2_VygQrG-1-png__700.jpg', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/Untitled-3-5bea94177610a__700.jpg', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/BlOgroQg47f-1-png__700.jpg', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/BeoTEeIh8vj-png__700.jpg', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/BaFzAm3hNsD-png__700.jpg', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/BhKqG9ahyh3-png__700.jpg', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/BkRkHHXAZa2-1-png__700.jpg', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/BfrE-okhtPF-png__700.jpg', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/BfMboifBsZZ-png__700.jpg', 'https://static.boredpanda.com/blog/wp-content/uploads/2018/11/BcGGe-oB-Bw-png__700.jpg']
		await ctx.send(f'{random.choice(options)}')
		print('Command Used: BadQuotes')
		return
		c.close()
		conn.close()

	else:
		await ctx.send("Ok! Wait... I Never Saw You. My Creator Doesn't Want You To Use Me")
		c.close()
		conn.close()

#r.meme
@client.command()
async def ROBmemes(ctx):
	conn = sqlite3.connect('blacklist.db')
	c = conn.cursor()
	user = ctx.author.id
	c.execute("SELECT * FROM blacklist WHERE user_id=?", (user,))
	result = c.fetchone()
	if result is None:
		ROBmeme = ['https://cdn.discordapp.com/attachments/651218357747449906/699708725992226866/3vxp8f.jpg',
		'https://cdn.discordapp.com/attachments/651218357747449906/699708731323056138/3vxpdn.jpg',
		'https://cdn.discordapp.com/attachments/651218357747449906/699708736411009064/3vxpka.jpg',
		'https://cdn.discordapp.com/attachments/651218357747449906/699708755662864484/3vxpq5.jpg',
		'https://cdn.discordapp.com/attachments/651218357747449906/699708761530433668/3vxpxn.jpg',
		'https://cdn.discordapp.com/attachments/651218357747449906/699708761530433668/3vxpxn.jpg',
		'https://cdn.discordapp.com/attachments/651218357747449906/699708773329141891/3vxq17.jpg',
		'https://cdn.discordapp.com/attachments/651218357747449906/699708779247435927/3vxqge.jpg',
		'https://cdn.discordapp.com/attachments/651218357747449906/699708785068867725/3vxqvq.jpg',
		'https://cdn.discordapp.com/attachments/651218357747449906/699708790769188995/3vxr31.jpg',
		'https://cdn.discordapp.com/attachments/651218357747449906/699708795927920680/3vxra5.jpg',
		'https://cdn.discordapp.com/attachments/651218357747449906/699708800759758878/3vxri2.jpg',
		'https://cdn.discordapp.com/attachments/651218357747449906/699708806699024444/3vxrms.jpg',
		'https://cdn.discordapp.com/attachments/651218357747449906/699708812751274096/3vxrtz.jpg',
		'https://cdn.discordapp.com/attachments/651218357747449906/699708816463233108/3vxs66.jpg'
		]
		await ctx.send(f'{random.choice(ROBmeme)}')
		return
		c.close()
		conn.close()

	else:
		await ctx.send("Ok! Wait... I Never Saw You. My Creator Doesn't Want You To Use Me")
		c.close()
		conn.close()

@client.command(aliases=['meme'])
async def memes(ctx):
	conn = sqlite3.connect('blacklist.db')
	c = conn.cursor()
	user = ctx.author.id
	c.execute("SELECT * FROM blacklist WHERE user_id=?", (user,))
	result = c.fetchone()
	if result is None:
		memes_submissions = reddit.subreddit('memes').hot()
		post_to_pick = random.randint(1, 100)
		for i in range(0, post_to_pick):
			submission = next(x for x in memes_submissions if not x.stickied)

			embed = discord.Embed(title=submission.title, colour=discord.Color.blue(), url= 'https://reddit.com')
			embed.set_footer(text='All Memes Are Taken From r/memes', icon_url=ctx.author.avatar_url)
			embed.set_image(url=submission.url)

		await ctx.send(embed=embed)
		print('Command Used:Memes')
		c.close()
		conn.close()

	else:
		await ctx.send("Ok! Wait... I Never Saw You. My Creator Doesn't Want You To Use Me")
		c.close()
		conn.close()


#r.pun
@client.command(aliases=['StandupComedy'])
async def pun(ctx):
	conn = sqlite3.connect('blacklist.db')
	c = conn.cursor()
	user = ctx.author.id
	c.execute("SELECT * FROM blacklist WHERE user_id=?", (user,))
	result = c.fetchone()
	if result is None:
		puns = ['Light travels faster than sound. Thats why some people appear bright until you hear them speak', 'I was wondering why the ball was getting bigger. Then it hit me', 'I have a few jokes about unemployed people, but none of them work', 'I have a split personality, said Tom, being frank.', 'When life gives you melons, youre dyslexic', 'How do you make holy water? You boil the hell out of it', 'I Renamed my iPod The Titanic, so when I plug it in, it says “The Titanic is syncing.', 'Will glass coffins be a success? Remains to be seen', 'Last night, I dreamed I was swimming in an ocean of orange soda. But it was just a Fanta sea', 'Its hard to explain puns to kleptomaniacs because they always take things literally', 'I lost my job at the bank on my very first day. A woman asked me to check her balance, so I pushed her over', 'What’s the difference between a hippo and a zippo? One is really heavy and the other is a little lighter', 'Two windmills are standing in a wind farm. One asks, “What’s your favorite kind of music?” The other says, “I’m a big metal fan.”', 'Did you hear about the guy whose whole left side was cut off? He’s all right now', 'I can’t believe I got fired from the calendar factory. All I did was take a day off', 'The man who survived pepper spray and mustard gas is now a seasoned veteran', 'My dad farted in an elevator, it was wrong on so many levels', 'I went to buy some camouflage trousers yesterday but couldnt find any', 'What do you call a bee that can’t make up its mind? A maybe', 'Hear about the new restaurant called Karma? Theres no menu - you get what you deserve', 'I tried to sue the airline for losing my luggage. I lost my case', 'England doesnt have a kidney bank, but it does have a Liverpool', 'All chemists know that alcohol is always a solution', 'Jill broke her finger today, but on the other hand she was completely fine', 'A police officer just knocked on my door and told me my dogs are chasing people on bikes. That’s ridiculous. My dogs don’t even own bikes', 'When everything is coming your way, youre in the wrong lane', 'She had a photographic memory but never developed it', 'The furniture store keeps calling me to come back. But all I wanted was one night stand', 'A cross-eyed teacher couldn’t control his pupils', 'When the past, present, and future go camping they always argue. Its intense tense in tents', 'A mean crook going down stairs = A condescending con, descending', 'What did the janitor say when he jumped out of the closet? SUPPLIES!', 'Is it ignorance or apathy thats destroying the world today? I dont know and dont really care', 'Let me tell you about my grandfather. He was a good man, a brave man. He had the heart of a lion, and a lifetime ban from the zoo', 'My dad, unfortunately, passed away when we couldn’t remember his blood type… His last words to us were, “Be positive!”', 'What do you call the wife of a hippie? A Mississippi', 'Which country’s capital has the fastest-growing population? Ireland. Every day it’s Dublin.', 'I wasn’t originally going to get a brain transplant, but then I changed my mind', 'There was a kidnapping at school yesterday. Don’t worry, though - he woke up', 'What do you get when you mix alcohol and literature? Tequila mockingbird', 'How do you throw a space party? You planet', 'How does an attorney sleep? First he lies on one side, then he lies on the other', 'My ex-wife still misses me. But her aim is starting to improve', 'What washes up on tiny beaches? Microwaves', 'What are the strongest days of the week? Saturday and Sunday, the rest are weekdays', 'What’s the difference between a poorly dressed man on a bicycle and a nicely dressed man on a tricycle? A tire', 'Two fish are in a tank, one says to the other "how do you drive this thing?"', 'I was going to make a chemistry joke, but since Im kinda late to the thread, the good ones argon', 'I hate how funerals are always at 9 a.m. I’m not really a mourning person', 'I saw an ad for burial plots, and I thought: “That’s the last thing I need!”', 'Uhhhhh NINTENDO!! Sorry I Have No Good Puns Right Now']
		await ctx.send(f'{random.choice(puns)}')
		print('Command Used: pun')
		return
		c.close()
		conn.close()

	else:
		await ctx.send("Ok! Wait... I Never Saw You. My Creator Doesn't Want You To Use Me")
		c.close()
		conn.close()

@client.command()
async def rps(ctx, *, message):
	conn = sqlite3.connect('blacklist.db')
	c = conn.cursor()
	user = ctx.author.id
	c.execute("SELECT * FROM blacklist WHERE user_id=?", (user,))
	result = c.fetchone()
	if result is None:

		if message == "s":
			options = ['I Chose Rock! You Lose!', 'I Chose Scissors. We Tied.', 'I Chose Paper... I Lost...']
			await ctx.send(f'{random.choice(options)}')
			return
			c.close()
			conn.close()

		elif message == 'p':
			options = ['I Chose Scissors! You Lose!', 'I Chose Paper. We Tied.', 'I Chose Rock... I Lost...']
			await ctx.send(f'{random.choice(options)}')
			return
			c.close()
			conn.close()

		elif message == "r":
			options = ['I Chose Paper! You Lose!', 'I Chose Rock. We Tied.', 'I Chose Scissors... I Lost...']
			await ctx.send(f'{random.choice(options)}')
			return
			c.close()
			conn.close()

		else:
			await ctx.send(f'Uhh... What? That Is Not An Option')
			c.close()
			conn.close()

	else:
		await ctx.send("Ok! Wait... I Never Saw You. My Creator Doesn't Want You To Use Me")
		c.close()
		conn.close()

@client.command()
async def orderROB(ctx):
	conn = sqlite3.connect('blacklist.db')
	c = conn.cursor()
	user = ctx.author.id
	c.execute("SELECT * FROM blacklist WHERE user_id=?", (user,))
	result = c.fetchone()
	if result is None:
		await ctx.author.send(f'bots.ondiscord Invite: https://bots.ondiscord.xyz/bots/636726747165098026')
		await ctx.author.send(f'discord.bots Invite: https://discord.bots.gg/bots/636726747165098026')
		print('A ROB Found A New Home')
		c.close()
		conn.close()

	else:
		await ctx.send("Ok! Wait... I Never Saw You. My Creator Doesn't Want You To Use Me")
		c.close()
		conn.close()

@client.command()
async def memeknuckles(ctx, *, meme):
	conn = sqlite3.connect('blacklist.db')
	c = conn.cursor()
	user = ctx.author.id
	c.execute("SELECT * FROM blacklist WHERE user_id=?", (user,))
	result = c.fetchone()
	if result is None:
		memeapproved = ['https://cdn.discordapp.com/attachments/651218357747449906/711729129724051629/Meme_approved_sorta.mp4',
		'https://cdn.discordapp.com/attachments/651218357747449906/711729131213029426/Meme_Approved_or_is_it_Denied_Knuckles_cant_decide.mp4',
		'https://cdn.discordapp.com/attachments/651218357747449906/711729135990472714/NO_Meme_Approved_Knuckles_Meme.mp4',
		'https://cdn.discordapp.com/attachments/651218357747449906/711729140084244531/Meme_approved..._I_guess..mp4',
		'https://cdn.discordapp.com/attachments/651218357747449906/711729140264468490/Sonic_Adventure_2_Knuckles_Approves_Your_Meme.mp4',
		'https://cdn.discordapp.com/attachments/651218357747449906/711729141019443320/Meme_Denied_Knuckles.mp4',
		'https://cdn.discordapp.com/attachments/651218357747449906/711729144886460526/Wrong_Meme_Approved.mp4',
		'https://cdn.discordapp.com/attachments/651218357747449906/711729144844517426/Meme_Approved.mp4',
		'https://cdn.discordapp.com/attachments/651218357747449906/711729221239832586/knuckles_meme_approver_but_its_spamming.mp4',
		'https://cdn.discordapp.com/attachments/651218357747449906/711729227682021406/Meme_Approved_Knuckles_2_Electric_Boogaloo.mp4',
		'https://cdn.discordapp.com/attachments/651218357747449906/711729237782036500/Meme_Approved_Knuckles_but_he_stamped_too_hard.mp4',
		'https://cdn.discordapp.com/attachments/651218357747449906/711729242999750746/Knuckles_wont_approve_your_meme_until_your_number..mp4',
		'https://cdn.discordapp.com/attachments/651218357747449906/711729244878929980/Meme_Approved_Knuckles.mp4',
		'https://cdn.discordapp.com/attachments/651218357747449906/711729247495913472/Meme_Approved_Knuckles_but_knuckles_is_the_man_behind_the_slaughter.mp4',
		'https://cdn.discordapp.com/attachments/651218357747449906/711729251082043522/Meme_Approved_Knuckles_but_its_completely_messed_up.mp4',
		'https://cdn.discordapp.com/attachments/651218357747449906/711729251598204998/Knuckles_Really_Likes_Your_Meme.mp4',
		'https://cdn.discordapp.com/attachments/651218357747449906/711729254500532274/Meme_Approved_Knuckles_but_he_is_a_Robot.mp4',
		'https://cdn.discordapp.com/attachments/651218357747449906/711729293943767060/Excellent_Meme_Approved.mp4',
		'https://cdn.discordapp.com/attachments/651218357747449906/711729297383227412/knuckles_but_he_doesnt_like_your_meme.mp4',
		'https://cdn.discordapp.com/attachments/651218357747449906/711729306694582352/Knuckles_meme_approval_disapproval_but_vibe_check.mp4',
		'https://cdn.discordapp.com/attachments/651218357747449906/711729316286693376/knuckles_meme_approved_meme.mp4',
		'https://cdn.discordapp.com/attachments/651218357747449906/711729320791506984/4_Knuckles_decide_your_meme.mp4',
		'https://cdn.discordapp.com/attachments/651218357747449906/711729322934927501/Knuckles_Disapproves..mp4',
		'https://cdn.discordapp.com/attachments/651218357747449906/711729323148836914/Knuckles_Meme_Approved.mp4',
		'https://cdn.discordapp.com/attachments/651218357747449906/711729329293361203/Knuckles_bans_all_memes_from_the_Internet....mp4']

		await ctx.send(f'{random.choice(memeapproved)}')
		c.close()
		conn.close()

	else:
		await ctx.send("Ok! Wait... I Never Saw You. My Creator Doesn't Want You To Use Me")
		c.close()
		conn.close()

#r.add
@client.command()
async def add(ctx, left : int, right : int):
	conn = sqlite3.connect('blacklist.db')
	c = conn.cursor()
	user = ctx.author.id
	c.execute("SELECT * FROM blacklist WHERE user_id=?", (user,))
	result = c.fetchone()
	if result is None:
		await ctx.send(left + right)
		print('Command Used: add')
		c.close()
		conn.close()

	else:
		await ctx.send("Ok! Wait... I Never Saw You. My Creator Doesn't Want You To Use Me")
		c.close()
		conn.close()

#r.subtract
@client.command()
async def subtract(ctx, left : int, right : int):
	conn = sqlite3.connect('blacklist.db')
	c = conn.cursor()
	user = ctx.author.id
	c.execute("SELECT * FROM blacklist WHERE user_id=?", (user,))
	result = c.fetchone()
	if result is None:
	    await ctx.send(left - right)
	    print('Command Used: subtract')
	    return
	    c.close()
	    conn.close()

	else:
		await ctx.send("Ok! Wait... I Never Saw You. My Creator Doesn't Want You To Use Me")
		c.close()
		conn.close()

#r.multiply
@client.command()
async def multiply(ctx, left : int, right : int):
	conn = sqlite3.connect('blacklist.db')
	c = conn.cursor()
	user = ctx.author.id
	c.execute("SELECT * FROM blacklist WHERE user_id=?", (user,))
	result = c.fetchone()
	if result is None:
	    await ctx.send(left * right)
	    print('Command Used: multiply')
	    return
	    c.close()
	    conn.close()

	else:
		await ctx.send("Ok! Wait... I Never Saw You. My Creator Doesn't Want You To Use Me")
		c.close()
		conn.close()

#r.divide
@client.command()
async def divide(ctx, left : int, right : int):
	conn = sqlite3.connect('blacklist.db')
	c = conn.cursor()
	user = ctx.author.id
	c.execute("SELECT * FROM blacklist WHERE user_id=?", (user,))
	result = c.fetchone()
	if result is None:
	    await ctx.send(left / right)
	    print('Command Used: divide')
	    return
	    c.close()
	    conn.close()

	else:
		await ctx.send("Ok! Wait... I Never Saw You. My Creator Doesn't Want You To Use Me")
		c.close()
		conn.close()

#Vital Stuff------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@client.command()
async def help(ctx, option='.'):

	conn = sqlite3.connect('blacklist.db')
	c = conn.cursor()
	user = ctx.author.id
	c.execute("SELECT * FROM blacklist WHERE user_id=?", (user,))
	result = c.fetchone()
	if result is None:
		if option == 'fun':
			embed = discord.Embed(title='Fun Commands', description='ROB The Robot - By: megachickn101', colour=discord.Color.blue(), url= 'https://www.google.com')
			embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
			embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
			embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/651218357747449906/690971263803588648/ROB_DX.png')

			embed.add_field(name='8ball<Question>', value='Check Your Future!!')
			embed.add_field(name='askROB<Question>', value='Ask ROB Anything!')
			embed.add_field(name='orderROB', value='Order Your Very Own ROB Classic Edition!')
			embed.add_field(name='say<message>', value='Get ROB Say Anything!')
			embed.add_field(name='dice', value='Roll A Dice!')
			embed.add_field(name='roast', value='Get Burned')
			embed.add_field(name='coinflip', value='Flip A Coin')
			embed.add_field(name='inspiration', value='Get Your Daily Dose Of Sadness')
			embed.add_field(name='ROBmemes', value='Get Some Good ROB Made Memes')
			embed.add_field(name='memes', value='Get Some Memes Straight From r/memes')
			embed.add_field(name='pun', value='Get Some Punny Pun')
			embed.add_field(name='rps<options>', value='Play Rock, Paper, Scissors - Options: r, p, s')
			embed.add_field(name='memeknuckles', value='Get Your Meme Reviewed')
			await ctx.send(embed=embed)
			print('Command Used: help fun')
			c.close()
			conn.close()

		elif option == 'math':
			embed = discord.Embed(title='Math Commands', description='ROB The Robot - By: megachickn101', colour=discord.Color.blue(), url= 'https://www.google.com')
			embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
			embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
			embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/651218357747449906/690971263803588648/ROB_DX.png')

			embed.add_field(name='add', value='Do Some Math')
			embed.add_field(name='subtract', value='Do Some Math')
			embed.add_field(name='multiply', value='Do Some Math')
			embed.add_field(name='divide', value='Do Some Math')
			await ctx.send(embed=embed)
			print('Command Used: help math')
			return
			c.close()
			conn.close()

		elif option == 'mod':
			embed = discord.Embed(title='Mod Commands', description='ROB The Robot - By: megachickn101', colour=discord.Color.blue(), url= 'https://www.google.com')
			embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
			embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
			embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/651218357747449906/690971263803588648/ROB_DX.png')

			embed.add_field(name='terminate<@user>', value='Bans A Person')
			embed.add_field(name='clear<#>', value='Will Delete 10000000000 Messages')
			embed.add_field(name='kickout<@user>', value='Kick A Person')

			await ctx.send(embed=embed)
			print('Command Used: help mod')
			return
			c.close()
			conn.close()

		elif option == 'admin':
			embed = discord.Embed(title='Admin Commands', description='ROB The Robot - By: megachickn101', colour=discord.Color.blue(), url= 'https://www.google.com')
			embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
			embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
			embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/651218357747449906/690971263803588648/ROB_DX.png')

			embed.add_field(name='unterminate<user#Tag>', value='Unbans A Person')

			await ctx.send(embed=embed)
			print('Command Used: help')
			return
			c.close()
			conn.close()

		elif option == 'misc':
			embed = discord.Embed(title='Miscellaneous Commands', description='ROB The Robot - By: megachickn101', colour=discord.Color.blue(), url= 'https://www.google.com')
			embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
			embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
			embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/651218357747449906/690971263803588648/ROB_DX.png')

			embed.add_field(name='ping', value='Check The Speed Of The Bot')
			embed.add_field(name='copyright', value='Check Your Copyright')
			embed.add_field(name='thanks', value='Some Thank Yous')
			embed.add_field(name='suggest<Suggestion>', value='Get Anonymous Feedback Sent Directly To My DMs Anonymously!')
			embed.add_field(name='time', value='Tells The Day, And Time In A 24Hr Format')

			await ctx.send(embed=embed)
			print('Command Used: help misc')
			return
			c.close()
			conn.close()

		else:
			embed = discord.Embed(title='Command Categories', description='ROB The Robot - By: megachickn101', colour=discord.Color.blue(), url= 'https://www.google.com')
			embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
			embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
			embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/651218357747449906/690971263803588648/ROB_DX.png')

			embed.add_field(name='Fun', value='Memes, 8ball, etc - Use ```r.help fun```')
			embed.add_field(name='Math', value='Add, Subtract, etc - Use ```r.help math```')
			embed.add_field(name='Moderation', value='Kick, Ban, etc - Use ```r.help mod``` - Needs The Ban Permission')
			embed.add_field(name='Admin', value='unterminate - Use ```r.help admin``` - Needs The Admin Permission')
			embed.add_field(name='Misc', value='ping, suggest, etc - Use ```r.help misc``` - Needs The Admin Permission')

			await ctx.send(embed=embed)
			print('Command Used: help')
			return
			c.close()
			conn.close()

	else:
		await ctx.send("Ok! Wait... I Never Saw You. My Creator Doesn't Want You To Use Me")
		c.close()
		conn.close()

@client.command()
async def suggest(ctx, *, message):
	conn = sqlite3.connect('blacklist.db')
	c = conn.cursor()
	user = ctx.author.id
	c.execute("SELECT * FROM blacklist WHERE user_id=?", (user,))
	result = c.fetchone()
	if result is None:
		user = client.get_user(601881016461819907)
		await ctx.send('Thank You For Sending Feedback! Keep In Mind That This Command Is Anonymous So megachickn101 Will Not Know Who Sent It!')
		await user.send('Suggestion:')
		await user.send(message)
		c.close()
		conn.close()

	else:
		await ctx.send("Ok! Wait... I Never Saw You. My Creator Doesn't Want You To Use Me")
		c.close()
		conn.close()


#r.thanks
@client.command()
async def thanks(ctx):
	conn = sqlite3.connect('blacklist.db')
	c = conn.cursor()
	user = ctx.author.id
	c.execute("SELECT * FROM blacklist WHERE user_id=?", (user,))
	result = c.fetchone()
	if result is None:
		await ctx.send(f'Thank You To MegaNinja101 for being a reliable and awesome tester!!!! :)')
		print('Command Used: thanks')
		return
		c.close()
		conn.close()

	else:
		await ctx.send("Ok! Wait... I Never Saw You. My Creator Doesn't Want You To Use Me")
		c.close()
		conn.close()


#r.ping
@client.command()
async def ping(ctx):
	conn = sqlite3.connect('blacklist.db')
	c = conn.cursor()
	user = ctx.author.id
	c.execute("SELECT * FROM blacklist WHERE user_id=?", (user,))
	result = c.fetchone()
	if result is None:
		await ctx.send(f'Pong! {round(client.latency * 1000)}ms. You Happy Now You Stat Nerd?!')
		print('Command Used: ping')
		return
		c.close()
		conn.close()

	else:
		await ctx.send("Ok! Wait... I Never Saw You. My Creator Doesn't Want You To Use Me")
		c.close()
		conn.close()

@client.command()
async def time(ctx):
	conn = sqlite3.connect('blacklist.db')
	c = conn.cursor()
	user = ctx.author.id
	c.execute("SELECT * FROM blacklist WHERE user_id=?", (user,))
	result = c.fetchone()
	if result is None:
		x = datetime.datetime.now()
		await ctx.send(x)
		print("Command Used: Time")
		c.close()
		conn.close()

	else:
		await ctx.send("Ok! Wait... I Never Saw You. My Creator Doesn't Want You To Use Me")
		c.close()
		conn.close()

@client.command()
@commands.check(is_it_me)
async def blacklist(ctx, user: discord.Member):
	user_id = user.id
	conn = sqlite3.connect('blacklist.db')
	c = conn.cursor()
	c.execute("INSERT INTO blacklist VALUES(?)", (user_id,))
	conn.commit()
	await ctx.send(f'Blacklisted {user.mention}. Serves Them Right!')

#r.shutdown
@client.command()
@commands.check(is_it_me)
async def shutdown(ctx):
	await client.close()

@client.command()
@commands.check(is_it_me)
async def fshutdown(ctx):
	await client.close()

#r.clear(#)
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=2):
	conn = sqlite3.connect('blacklist.db')
	c = conn.cursor()
	user = ctx.author.id
	c.execute("SELECT * FROM blacklist WHERE user_id=?", (user,))
	result = c.fetchone()
	if result is None:
		await ctx.channel.purge(limit=amount)
		print('Command Used: clear')
		c.close()
		conn.close()

	else:
		await ctx.send("Ok! Wait... I Never Saw You. My Creator Doesn't Want You To Use Me")
		c.close()
		conn.close()



#r.kickout @member#0000
@client.command()
@commands.has_permissions(kick_members=True)
async def kickout(ctx, member : discord.Member, *, reason=None):
	await member.kick(reason=reason)
	await ctx.send(f'kicked {member.mention}')
	print('Command Used: kickout')
	return

#r.terminate @member#0000
@client.command()
@commands.has_permissions(ban_members=True)
async def terminate(ctx, member : discord.Member, *, reason=None):
	await member.ban(reason=reason)
	await ctx.send(f'banned {member.mention}')
	print('Command Used: terminate')
	return

#r.unterminate member#0000
@client.command()
@commands.has_permissions(administrator=True)
async def unterminate(ctx, *, member):
	banned_users = await ctx.guild.bans()
	member_name, member_discriminator = member.split('#')

	for ban_entry in banned_users:
		user = ban_entry.user

		if (user.name, user.discriminator) == (member_name, member_discriminator):
			await ctx.guild.unban(user)
			await ctx.send(f'Unbanned {user.mention}')
			return

client.run("Insert Token")
