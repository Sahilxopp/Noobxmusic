@app.on_message(filters.command(VARS_COMMAND) & SUDOERS)
async def varsFunc(client, message):
    mystic = await message.reply_text(
        "Pʟᴇᴀsᴇ ᴡᴀɪᴛ... Gᴇᴛᴛɪɴɢ ʏᴏᴜʀ ᴄᴏɴғɪɢ ᴠᴀʀɪᴀʙʟᴇs...!"
    )
    v_limit = await get_video_limit()
    bot_name = config.BOT_NAME
    up_r = f"[ʀᴇᴩᴏ]({config.UPSTREAM_REPO})"
    up_b = config.UPSTREAM_BRANCH
    auto_leave = config.AUTO_LEAVE_ASSISTANT_TIME
    yt_sleep = config.YOUTUBE_DOWNLOAD_EDIT_SLEEP
    tg_sleep = config.TELEGRAM_DOWNLOAD_EDIT_SLEEP
    playlist_limit = config.SERVER_PLAYLIST_LIMIT
    fetch_playlist = config.PLAYLIST_FETCH_LIMIT
    song = config.SONG_DOWNLOAD_DURATION
    play_duration = config.DURATION_LIMIT_MIN
    cm = config.CLEANMODE_DELETE_MINS
    if config.AUTO_LEAVING_ASSISTANT == str(True):
        ass = "Yᴇs"
    else:
        ass = "Nᴏ"
    if config.PRIVATE_BOT_MODE == str(True):
        pvt = "Yᴇs"
    else:
        pvt = "Nᴏ"
    if config.AUTO_DOWNLOADS_CLEAR == str(True):
        down = "Yᴇs"
    else:
        down = "Nᴏ"

    if not config.GITHUB_REPO:
        git = "Nᴏ"
    else:
        git = f"[Rᴇᴩᴏ]({config.GITHUB_REPO})"
    if not config.START_IMG_URL:
        start = "Nᴏ"
    else:
        start = f"[Iᴍᴀɢᴇ]({config.START_IMG_URL})"
    if not config.SUPPORT_CHANNEL:
        s_c = "Nᴏ"
    else:
        s_c = f"[Cʜᴀɴɴᴇʟ]({config.SUPPORT_CHANNEL})"
    if not config.SUPPORT_GROUP:
        s_g = "Nᴏ"
    else:
        s_g = f"[Sᴜᴩᴩᴏʀᴛ]({config.SUPPORT_GROUP})"
    if not config.GIT_TOKEN:
        token = "Nᴏ"
    else:
        token = "Yᴇs"
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        sotify = "Nᴏ"
    else:
        sotify = "Yᴇs"
    owners = [str(ids) for ids in config.OWNER_ID]
    owner_id = " ,".join(owners)
    tg_aud = convert_bytes(config.TG_AUDIO_FILESIZE_LIMIT)
    tg_vid = convert_bytes(config.TG_VIDEO_FILESIZE_LIMIT)
    text = f"""**Mᴜsɪᴄ Bᴏᴛ Cᴏɴғɪɢ Vᴀʀɪᴀʙʟᴇs :**

<u>Bᴀsɪᴄ Vᴀʀɪᴀʙʟᴇs:</u>
MUSIC_BOT_NAME : {bot_name}
DURATION_LIMIT : {play_duration} ᴍɪɴᴜᴛᴇs
SONG_DOWNLOAD_DURATION_LIMIT : {song} ᴍɪɴᴜᴛᴇs
OWNER_ID : {owner_id}
    
<u>Rᴇᴩᴏsɪᴛᴏʀʏ Vᴀʀɪᴀʙʟᴇs :</u>

UPSTREAM_REPO : {up_r}
UPSTREAM_BRANCH : {up_b}
GITHUB_REPO : {git}
GIT_TOKEN : {token}


<u>Bᴏᴛ Vᴀʀɪᴀʙʟᴇs :</u>

AUTO_LEAVING_ASSISTANT : {ass}
ASSISTANT_LEAVE_TIME : {auto_leave} sᴇᴄᴏɴᴅs
AUTO_DOWNLOADS_CLEAR : {down}
PRIVATE_BOT_MODE : {pvt}
YOUTUBE_EDIT_SLEEP : {yt_sleep} sᴇc.
TELEGRAM_EDIT_SLEEP : {tg_sleep} sᴇᴄ.
CLEANMODE_MINS : {cm} ᴍɪɴ.
VIDEO_STREAM_LIMIT : {v_limit} ᴄʜᴀᴛ
SERVER_PLAYLIST_LIMIT : {playlist_limit}
PLAYLIST_FETCH_LIMIT : {fetch_playlist}

<u>Sᴩᴏᴛɪғʏ Vᴀʀɪᴀʙʟᴇs :</u>

SPOTIFY_CLIENT_ID : {sotify}
SPOTIFY_CLIENT_SECRET : {sotify}

<u>Pʟᴀʏsɪᴢᴇ Vᴀʀs :</u>

TG_AUDIO_FILESIZE_LIMIT : {tg_aud}
TG_VIDEO_FILESIZE_LIMIT : {tg_vid}

<u>Exᴛʀᴀ Vᴀʀɪᴀʙʟᴇs :</u>

SUPPORT_CHANNEL : {s_c}
SUPPORT_GROUP :  {s_g}
START_IMG_URL :  {start}
    """
    await asyncio.sleep(1)
    await mystic.edit_text(text)
