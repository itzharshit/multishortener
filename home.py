# Pyrogrammers || GitHub.com/pyrogrammers || telegram.me/pyrogrammers 

# Importing required modules
from os import environ
import aiohttp, logging 
from pyrogram import Client, filters
import pyshorteners

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
s = pyshorteners.Shortener(api_key='API_KEY', user_id='USER_ID', domain='SITE_URL', group_id=12, type='int')

# Start message for welcome 
@app.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(
        f"Hello {message.chat.first_name},\n"
        "I am multi shortener bot, i can short links of any website that uses Adlinkfly API Response.\n\nJust send your link i will give you shortened link.")

# Getting url using regex and trying to call the function that is defined above
@app.on_message(filters.regex(r'https?://[^\s]+') & filters.private)
async def shortener(bot, message):
    url = message.matches[0].group(0)
    try:
        short_url = s.adfly.short(url)
        await message.reply(f"Successfully generated your short link 👉 `{short_url}`,\n\n__Tap on link to copy it__")
    except Exception as e:
        await message.reply(f"An error occurred: `{str(e)}`, contact @pyroowner for support.")

# Running client
app.run()
