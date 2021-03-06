import discord 
from discord.ext import commands 
import aiohttp

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents = intents)
API_KEY = "Your Random Stuff API Key" 
headervar = {"authorization": API_KEY, "x-rapidapi-host": "random-stuff-api.p.rapidapi.com", "x-rapidapi-key": "Your Rapid Api Key"}
URL = "https://random-stuff-api.p.rapidapi.com/ai" 

@bot.event
async def on_ready():
    print('Successfully Logged')

@bot.event 
async def on_message(message): 
	if message.author.bot: 
		return
	if message.channel.id != "Your Channel Id": 
		return
	try: 
		datavar = {'msg':message.content}
		async with aiohttp.ClientSession(headers = headervar) as session: 
			async with session.get(url=URL, params = datavar) as reply: 
				output = await reply.json() 
				msg = output["AIResponse"]  
				await message.reply(msg) 
	except: #If it fails, Then do this
		await message.reply("An error has occured.") 

	
bot.run("Your Bot Token")
