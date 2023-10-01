import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID","18732851"))
API_HASH = getenv("API_HASH","0a409e0d80850704667d887f3849a936")
BOT_TOKEN = getenv("BOT_TOKEN","")

MONGO_DB_URI = getenv("MONGO_DB_URI", "")

LOGGER_ID = int(getenv("LOGGER_ID", "-1001907995111"))

GBAN_LOG_ID = int(getenv("GBAN_LOG", "-1001800713917"))

BOT_NAME = getenv("BOT_NAME", "˹Zᴀʀᴀ ꭙ Mᴜsɪᴄ[🇮🇳]")
OWNER_ID = list(
    map(int, getenv("OWNER_ID", "5971645819").split())
)
    
SUPPORT_CHANNEL = getenv(
    "SUPPORT_CHANNEL", "https://t.me/BOTS_SUPPORTTT")
SUPPORT_GROUP = getenv(
    "SUPPORT_GROUP", "https://t.me/RANA_societyyyy")

DURATION_LIMIT_MIN = int(
    getenv("DURATION_LIMIT", "900000")
)
SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180000")
)

HEROKU_API_KEY = getenv("HEROKU_API_KEY")

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Sahilxopp/Noobxmusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")

GIT_TOKEN = getenv("GIT_TOKEN", "")

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True")

AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "54000")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "6"))

GITHUB_REPO = getenv("GITHUB_REPO", "https://te.legra.ph/file/fa898291a360b85acb1ab.mp4")

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "29a1991c889f4beab0cbbb6a097ac7a6")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "516f0dbf510045c98f32401750de82f7")

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "10")
)

TG_AUDIO_FILESIZE_LIMIT = int(
    getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600")
)
TG_VIDEO_FILESIZE_LIMIT = int(
    getenv("TG_VIDEO_FILESIZE_LIMIT", "2073741824")
)


STRING1 = getenv("STRING_SESSION", "")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "Opxlogs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv("https://te.legra.ph/file/77924dbacd7167cc546d7.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://te.legra.ph/file/f5bee35c2a17ff3ac17eb.jpg",
)

PLAYLIST_IMG_URL = "https://telegra.ph/file/075610fd1519afd9ed467.png"

GLOBAL_IMG_URL = "https://telegra.ph/file/d531b3f0827db188acc33.png"

STATS_IMG_URL = "https://telegra.ph/file/d531b3f0827db188acc33.png"

TELEGRAM_AUDIO_URL = "https://telegra.ph/file/98b8aabf1bfda012d6dc7.png"

TELEGRAM_VIDEO_URL = "https://telegra.ph/file/98b8aabf1bfda012d6dc7.png"

STREAM_IMG_URL = "https://telegra.ph/file/98b8aabf1bfda012d6dc7.png"

SOUNCLOUD_IMG_URL = "https://telegra.ph/file/98b8aabf1bfda012d6dc7.png"

YOUTUBE_IMG_URL = "https://telegra.ph/file/98b8aabf1bfda012d6dc7.png"

SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/98b8aabf1bfda012d6dc7.png"

SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/98b8aabf1bfda012d6dc7.png"

SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/98b8aabf1bfda012d6dc7.png"


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)

if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            print(
                "[ERROR] - Your PING_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if PLAYLIST_IMG_URL:
    if PLAYLIST_IMG_URL != "assets/Playlist.jpeg":
        if not re.match("(?:http|https)://", PLAYLIST_IMG_URL):
            print(
                "[ERROR] - Your PLAYLIST_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if GLOBAL_IMG_URL:
    if GLOBAL_IMG_URL != "assets/Global.jpeg":
        if not re.match("(?:http|https)://", GLOBAL_IMG_URL):
            print(
                "[ERROR] - Your GLOBAL_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if STATS_IMG_URL:
    if STATS_IMG_URL != "assets/Stats.jpeg":
        if not re.match("(?:http|https)://", STATS_IMG_URL):
            print(
                "[ERROR] - Your STATS_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if TELEGRAM_AUDIO_URL:
    if TELEGRAM_AUDIO_URL != "assets/Audio.jpeg":
        if not re.match("(?:http|https)://", TELEGRAM_AUDIO_URL):
            print(
                "[ERROR] - Your TELEGRAM_AUDIO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if STREAM_IMG_URL:
    if STREAM_IMG_URL != "assets/Stream.jpeg":
        if not re.match("(?:http|https)://", STREAM_IMG_URL):
            print(
                "[ERROR] - Your STREAM_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if SOUNCLOUD_IMG_URL:
    if SOUNCLOUD_IMG_URL != "assets/Soundcloud.jpeg":
        if not re.match("(?:http|https)://", SOUNCLOUD_IMG_URL):
            print(
                "[ERROR] - Your SOUNCLOUD_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if YOUTUBE_IMG_URL:
    if YOUTUBE_IMG_URL != "assets/Youtube.jpeg":
        if not re.match("(?:http|https)://", YOUTUBE_IMG_URL):
            print(
                "[ERROR] - Your YOUTUBE_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if TELEGRAM_VIDEO_URL:
    if TELEGRAM_VIDEO_URL != "assets/Video.jpeg":
        if not re.match("(?:http|https)://", TELEGRAM_VIDEO_URL):
            print(
                "[ERROR] - Your TELEGRAM_VIDEO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()
