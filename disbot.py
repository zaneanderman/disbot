#!/usr/bin/python3

import discord
from discord.ext import commands
import sys
import os
from modules import calc 

bot = commands.Bot(command_prefix='~')
nsp = calc.NumericStringParser()

@bot.command()
async def ping(ctx):
	await ctx.send(f"{int(bot.latency*1000)} ms")

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
	calculation = "".join(args)
	await ctx.send(nsp.eval(calculation))

@bot.command()
async def whois(ctx, user:str):
	message = ""
	for person in ctx.guild.members:
		if person.display_name.lower().find(user.lower()) != -1:
			message = f"{message}id: {person}, server name: {person.display_name}\n"
	if message != "":
		await ctx.send(message)
	else:
		await ctx.send("There is no user of that name!")

@bot.command()
async def updatetext(ctx, text:str):
	previousvalue = read("savetext.txt")
	with open("savetext.txt", "w") as file:
		file.write(text)
	await ctx.send(f"Updated text file! \nThe previous text was: {previousvalue}")

@bot.command()
async def echo(ctx, *args):
	sendstring = ""
	for i in args:
		sendstring = f"{sendstring} {i}" 
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
async def chocolate(ctx):
	await ctx.send("The bot eats some chocolate and leaves none for you")

@bot.command()
async def whoami(ctx):
	await ctx.send(ctx.author)

token = read("./token.txt")
bot.run(token)