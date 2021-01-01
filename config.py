# Just copy this file to config.py and change it to your info.
from pyrogram import filters
from helpers import get_banned_users

# Get these two from https://my.telegram.org
API_ID = 1366324
API_HASH = "0d0274833b354d9223ca60b3e2f1e7c8"

# Get this from @Botfather
TOKEN = "1437099346:AAGyH2twmU12MW3EXtYarNCJ4c0vkx1FloQ"

# The IDs of the users which can stream, skip, pause and change volume
SUDO_USERS = [
    829327264,
    1356608073,
    1302101407,
]

# A group ID to send messages to when a song starts playing
# Example group ID: -1001477743244
LOG_GROUP = None  # Just keep it like this if you are not going to use one

# Choose the preferred language for your bot. If English leave as it is, or change to the code of any supported language.
LANG = "en"

# Max video duration allowed for downloads in minutes
DUR_LIMIT = 5

# Show a small credit for @su_Bots in the start message
CREDIT = False

# No need to touch the following.
SUDO_FILTER = filters.user(SUDO_USERS)
BANNED = filters.user(get_banned_users())
