import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Erika')
API_ID = int(environ['API_ID', '10162913'])
API_HASH = environ['API_HASH', '7f3e8e035cc59e7d6f03d2d115ba22fa']
BOT_TOKEN = environ['BOT_TOKEN', "5963514962:AAFnRQNJIzqzwI00oPSnHfHwF7PIJi9J2Vw"]

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
PICS = (environ.get('PICS', 'https://telegra.ph/file/84d06b09397b89875f763.jpg')).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1357877025').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001929896769').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://vimarsharya1087:Vimarsh@cluster0.md8m1lw.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "ErikaBot")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Others
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001953623068'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'ShadowSupport12')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), False)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "⚡<b>File uploaded by [Shadow Movies](https://t.me/ShadowUpdates12)</b>⚡\n\nName: {file_caption} \n\n⚙️ <b>Size: </b><code>{file_size}</code>\n\n\n🔥  ↭ <b>Join Now [Shadow Movies](https://t.me/ShadowUpdates12)</b> ↭  🔥")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", "⚡<b>File uploaded by [Shadow Movies](https://t.me/ShadowUpdates12)</b>⚡\n\nName: {file_caption} \n\n⚙️ <b>Size: </b><code>{file_size}</code>\n\n\n🔥  ↭ <b>Join Now [Shadow Movies](https://t.me/ShadowUpdates12)</b> ↭  🔥")
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>Your Query: {query}</b> \n‌‌‌‌IMDb: Data by: @ShadowUpdates12 \n\n🏷 Tɪᴛʟᴇ : {title}\n🌟 Rᴀᴛɪɴɢ : {rating}/10\n🎭 Gᴇɴʀᴇs : {genres}\n📆 Rᴇʟᴇᴀsᴇ Iɴғᴏ : {year}\n⏰ Rᴜɴᴛɪᴍᴇ : {runtime}\n🎙️ Lᴀɴɢᴜᴀɢᴇs : {languages}\n🔖 Pʟᴏᴛ : {plot}\n\n💛 Pʟᴇᴀsᴇ Sᴜᴘᴘᴏʀᴛ Us 💛\n\n⚠️ᴛʜɪs ᴍᴇssᴀɢᴇ ᴡɪʟʟ ᴅᴇʟᴇᴛᴇ ᴀғᴛᴇʀ 5 ᴍɪɴᴜᴛᴇs")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), False)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1001962810800')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "True")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "False")), False)

#LazyRenamer Configs
FLOOD = int(environ.get("FLOOD", "10"))
LAZY_MODE = bool(environ.get("LAZY_MODE"))
#Add user id of the user in this field those who you want to be Authentic user for file renaming features
lazy_renamers = [int(lazrenamers) if id_pattern.search(lazrenamers) else lazrenamers for lazrenamers in environ.get('LAZY_RENAMERS', '').split()]
LAZY_RENAMERS = (lazy_renamers + ADMINS) if lazy_renamers else []
REQ_CHANNEL = int(environ.get('REQ_CHANNEL', '-1001671185048'))

#ai
AI = is_enabled((environ.get("AI","True")), False)
OPENAI_API = environ.get("OPENAI_API","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")
LAZY_AI_LOGS = int(environ.get("LAZY_AI_LOGS","-1001954000385")) #GIVE YOUR NEW LOG CHANNEL ID TO STORE MESSAGES THAT THEY SEARCH IN BOT PM.... [ i have added this to keep an eye on the users message, to avoid misuse of LazyPrincess ]
# Requested Content template variables ---
ADMIN_USRNM = environ.get('ADMIN_USRNM','Sad_Nobita') # WITHOUT @
MAIN_CHANNEL_USRNM = environ.get('MAIN_CHANNEL_USRNM','ShadowUpdates12') # WITHOUT @
DEV_CHANNEL_USRNM = environ.get('DEV_CHANNEL_USRNM','ShadowUpdates12') # WITHOUT @
LAZY_YT_HANDLE = environ.get('LAZY_YT_HANDLE','')  # WITHOUT @ [  add only handle - don't add full url  ] 
MOVIE_GROUP_USERNAME = environ.get('MOVIE_GROUP_USERNAME', "ShadowSupport12") #[ without @ ]

# Url Shortner
URL_MODE = is_enabled((environ.get("URL_MODE","True")), False)
URL_SHORTENR_WEBSITE = environ.get('URL_SHORTENR_WEBSITE', 'omegalinks.in') #Always use website url from api section 
URL_SHORTNER_WEBSITE_API = environ.get('URL_SHORTNER_WEBSITE_API', 'd24d5a6f0b68680b4a48910894363b225ebd5605')
LZURL_PRIME_USERS = [int(lazyurlers) if id_pattern.search(lazyurlers) else lazyurlers for lazyurlers in environ.get('LZURL_PRIME_USERS', '5965340120').split()]

# Auto Delete For Group Message (Self Delete) #
SELF_DELETE_SECONDS = int(environ.get('SELF_DELETE_SECONDS', 300))
SELF_DELETE = is_enabled((environ.get('SELF_DELETE','True')), True)

# Download Tutorial Button #
DOWNLOAD_TEXT_NAME = "📥 HOW TO DOWNLOAD 📥"
DOWNLOAD_TEXT_URL = "https://t.me/ShadowUpdates12"

# Custom Caption Under Button #
CAPTION_BUTTON = "Get Updates"
CAPTION_BUTTON_URL = "https://t.me/ShadowUpdates12"

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
