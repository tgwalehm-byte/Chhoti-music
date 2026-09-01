from ThakurxMusic.core.bot import Thakur
from ThakurxMusic.core.dir import dirr
from ThakurxMusic.core.git import git
from ThakurxMusic.core.userbot import Userbot
from ThakurxMusic.misc import dbb, heroku
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Thakur()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

