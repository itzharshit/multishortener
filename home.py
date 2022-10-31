# importing required modules
from os import environ
import aiohttp
from pyrogram import Client, filters

# defining global variables
API_ID = environ.get('API_ID')
API_HASH = environ.get('API_HASH')
BOT_TOKEN = environ.get('BOT_TOKEN')
SITE_URL = environ.get('SITE_URL')

# Creating pyrogram client
app = Client(
    "multishortener",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

# Defining function for shortening links
async def convert(link):
    url = f'{SITE_URL}/api'
    params = {'api': API_KEY, 'url': link}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, raise_for_status=True) as response:
            data = await response.json()
            return data["shortenedUrl"]

# start message for welcome 
@app.on_message(filters.command('start') & filters.private)
async def start(event):
    await event.send_message(
        f"Hello {event.chat.first_name},\n"
        "I am multi shortener bot, i can short links of any website that uses Adlinkfly API Response.\n\nJust send your link i will give you shortened link.")

# getting url using regex and trying to call convert function that is defined above
@app.on_message(filters.regex(r'https?://[^\s]+') & filters.private)
async def shortener(event):
    url = message.matches[0].group(0)
    try:
        short_link = await convert(url)
        await event.reply(f"Successfully generated your short link 👉 `{short_link}`,\n\n__Tap on link to copy it__")
    except Exception as e:
        await message.reply(f"An error occurred: `{str(e)}`, contact @pyroowner for support.")
