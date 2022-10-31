# Pyrogrammers || GitHub.com/pyrogrammers || telegram.me/pyrogrammers 

# Importing required modules
from os import environ
import aiohttp, logging 
from pyrogram import Client, filters

# Defining global variables
API_ID = environ.get('API_ID')
API_HASH = environ.get('API_HASH')
BOT_TOKEN = environ.get('BOT_TOKEN')
SITE_URL = environ.get('SITE_URL')
API_KEY = environ.get('API_KEY')

# intialising logging
logging.basicConfig(
    level=logging.INFO, format="[%(levelname)s] %(asctime)s - %(message)s"
)
log = logging.getLogger("PYROGRAMMERS")

# Creating pyrogram client(I think telethon would be better, anyway will use telethon in next project.)
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

# Start message for welcome 
@app.on_message(filters.command('start') & filters.private)
async def start(event):
    await event.send_message(
        f"Hello {event.chat.first_name},\n"
        "I am multi shortener bot, i can short links of any website that uses Adlinkfly API Response.\n\nJust send your link i will give you shortened link.")

# Getting url using regex and trying to call convert function that is defined above
@app.on_message(filters.regex(r'https?://[^\s]+') & filters.private)
async def shortener(event):
    url = message.matches[0].group(0)
    try:
        short_url = await convert(url)
        await event.reply(f"Successfully generated your short link 👉 `{short_url}`,\n\n__Tap on link to copy it__")
    except Exception as e:
        await message.reply(f"An error occurred: `{str(e)}`, contact @pyroowner for support.")
