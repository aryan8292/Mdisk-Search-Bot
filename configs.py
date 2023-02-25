# (c) @AM_ROBOTS

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "c33b2f280810fc2f60a6387a4c4217f2")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5015404755:AAE58laq-OGoqxkKth7TjVzyKYBTa4zs7oc")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "MdiskSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -1001711211283))
    BOT_USERNAME = os.environ.get("Arymovies_bot")
    BOT_OWNER = int(os.environ.get("5079629749")
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Aryan6969:Aryan6969@cluster0.krhmwhe.mongodb.net/?retryWrites=true&w=majority")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    ABOUT_BOT_TEXT = """<b>This is Mdisk Search Bot.
    
    
    
🤖 My Name: <a href='https://t.me/Official_Movies_Group'>Mdisk Search Robot</a>

📝 Language : <a href='https://www.python.org'> Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'> Pyrogram</a>

📡 Server: <a href='https://heroku.com'>Heroku</a>

👨‍💻 Created By: <a href='https://t.me/Am_RoBots'>ᎯℕUℛᎯᎶ</a></b>
"""

    ABOUT_HELP_TEXT = """<b>👨‍💻 Developer : <a href='https://t.me/Am_RoBots'>ᎯℕUℛᎯᎶ</a>

If You Want Your Own Bot Like This Then You Can Contact Our Developer.</b>
"""

    HOME_TEXT = """
<b>Hey! {}😅,

I'm Mdisk Search Robot.🤖</a>

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @Am_RoBots</a></b>
"""


    START_MSG = """
<b>Hey! {}😅,

I'm Mdisk Search Robot.🤖</a>

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @Am_RoBots</a></b>
"""

