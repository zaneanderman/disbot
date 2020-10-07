#!/usr/bin/python3

import discord
from discord.ext import commands
import sys

bot = commands.Bot(command_prefix='~')

@bot.command()
async def ping(ctx):
	await ctx.send(str(bot.latency) + " milliseconds")

@bot.command()
async def calculate(ctx, *args):
	await Calculate(ctx, *args)

@bot.command()
async def calc(ctx, *args):
	await Calculate(ctx, *args)

def read(filename):
	with open(filename) as x:
		returnvalue = x.read()
	return returnvalue

def num(number):
	if int(number) == float(number):
		return int(number)
	else:
		return float(number)

async def Calculate(ctx, *args):
	if args[1] in ["+","-","*","/","&","^","**",] and (isinstance(num(args[0]), int) or isinstance(num(args[0]), float)) and (isinstance(num(args[2]), int) or isinstance(num(args[2]), float)):
		if args[1] == "+":
			returnvalue = num(args[0]) + num(args[2])
		if args[1] == "*":
			returnvalue = num(args[0]) * num(args[2])
		if args[1] == "/":
			returnvalue = num(args[0]) / num(args[2])
		if args[1] == "-":
			returnvalue = num(args[0]) - num(args[2])
		if args[1] == "**":
			returnvalue = num(args[0]) ** num(args[2])
		if args[1] == "&":
			returnvalue = num(args[0]) & num(args[2])
		if args[1] == "^":
			returnvalue = num(args[0]) ^ num(args[2])

	elif args[1] == "help":
		returnvalue = "This help page is currently unavailable. Look at the code to find out how to use this command."
	else:
		returnvalue = "That's not a valid calculation! Syntax: \n~calculate ([number 1] [operater] [number 2]) | help"
	await ctx.send(returnvalue)

@bot.command()
async def whois(ctx, user:str):
	message = ""
	for person in ctx.guild.members:
		if person.display_name.lower().find(user.lower()) != -1:
			message = message+"id: "+str(person)+", "+"server name: "+person.display_name+"\n"
	if message != "":
		await ctx.author.send(message)
		await ctx.send("I have dm'ed you the id's of all users who's names contain that string")
	else:
		await ctx.send("There is no user of that name!")

@bot.command()
async def updatetext(ctx, text:str):
	previousvalue = read("savetext.txt")
	with open("savetext.txt", "w") as file:
		file.write(text)
	await ctx.send("Updated text file! \nThe previous text was: %s"%previousvalue)

@bot.command()
async def echo(ctx, *args):
	sendstring = ""
	for i in args:
		print(i)
		sendstring = sendstring + "%s "%i 
	await ctx.send(sendstring)

@bot.command()
async def invite(ctx):
	await ctx.send("https://discord.com/oauth2/authorize?client_id=753258454713630730&scope=bot")

@bot.command()
async def code(ctx, *args):
	codecontents = read(sys.argv[0])
	brokencontents = [codecontents[i:i+1000] for i in range(0, len(codecontents), 1000)]
	for chunk in brokencontents:
		await ctx.author.send(chunk)
	await ctx.author.send("Dependencies: all imported modules, python 3, possibly linux")
	await ctx.send("I have dm'ed you my source code. Feel free to use it. Alternatively, you can view the bot on github at https://github.com/zaneanderman/disbot")

@bot.command()
async def whoami(ctx):
	await ctx.send(ctx.author)






token = read("./token.txt")
bot.run(token)