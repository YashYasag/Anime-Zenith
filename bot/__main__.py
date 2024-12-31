# oof
from datetime import datetime as dt
import os
from bot.plugins.call_back_button_handler import button
from bot.config import Config
from bot import (
    APP_ID,
    API_HASH,
    AUTH_USERS,
    DOWNLOAD_LOCATION,
    LOGGER,
    TG_BOT_TOKEN,
    BOT_USERNAME,
    SESSION_NAME,
    data,
    app,
    crf,
    resolution,
    audio_b,
    preset,
    codec,
    AUTH_USERS,
    name,
    size,
    acodec,
    metadata,
    metadata1,
    metadata2
)
from bot.helper_funcs.utils import add_task, on_task_complete
from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler, CallbackQueryHandler

from bot.plugins.incoming_message_fn import (
    incoming_start_message_f,
    incoming_compress_message_f,
    incoming_cancel_message_f
)

from bot.plugins.status_message_fn import (
    eval_message_f,
    exec_message_f,
    upload_log_file
)

from bot.commands import Command

sudo_users = "5487643307" 
crf.append("25")
codec.append("libx264")
resolution.append("1280x720")
preset.append("veryfast")
audio_b.append("40k")
acodec.append("libopus")
name.append("Anime Zenith")
metadata.append("Anime Zenith")
metadata1.append("Anime Zenith")
metadata2.append("Anime Zenith")
size.append("15")

uptime = dt.now()

def ts(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = (
        ((str(days) + "d, ") if days else "")
        + ((str(hours) + "h, ") if hours else "")
        + ((str(minutes) + "m, ") if minutes else "")
        + ((str(seconds) + "s, ") if seconds else "")
        + ((str(milliseconds) + "ms, ") if milliseconds else "")
    )
    return tmp[:-2]

if __name__ == "__main__" :
    # create download directory, if not exist
    if not os.path.isdir(DOWNLOAD_LOCATION):
        os.makedirs(DOWNLOAD_LOCATION)

    # STATUS ADMIN Command

    # START command
    incoming_start_message_handler = MessageHandler(
        incoming_start_message_f,
        filters=filters.command(["start", f"start@{BOT_USERNAME}"])
    )
    app.add_handler(incoming_start_message_handler)

    @app.on_message(filters.incoming & filters.command(["crf", f"crf@{BOT_USERNAME}"]))
    async def changecrf(app, message):
        if message.from_user.id in AUTH_USERS:
            cr = message.text.split(" ", maxsplit=1)[1]
            OUT = f"I will be using : {cr} crf"
            crf.insert(0, f"{cr}")
            await message.reply_text(OUT)
        else:
            await message.reply_text("Error")

    @app.on_message(filters.incoming & filters.command(["settings", f"settings@{BOT_USERNAME}"]))
    async def settings(app, message):
        if message.from_user.id in AUTH_USERS:
            video_settings = f"🏷 Video\n┏━━━━━━━━━━━━━━━━━\n┣ Codec  ➜ {codec[0]}\n┣ Crf  ➜ {crf[0]}\n┣ Resolution  ➜ {resolution[0]}\n┗━━━━━━━━━━━━━━━━━"
            audio_settings = f"🏷 Audio\n┏━━━━━━━━━━━━━━━━━\n┣ Audio  ➜ {acodec[0]}\n┣ Bitrates ➜ {audio_b[0]}\n┗━━━━━━━━━━━━━━━━━"
            watermark_settings = f"🏷 Watermark\n┏━━━━━━━━━━━━━━━━━\n┣ Size  ➜ {size[0]}\n┣ Text  ➜ {name[0]}\n┣ metadata ➜ {metadata[0]}\n┗━━━━━━━━━━━━━━━━━"
            speed_settings = f"🏷 Speed\n┏━━━━━━━━━━━━━━━━━\n┣ Preset ➜ {preset[0]}\n┗━━━━━━━━━━━━━━━━━"

            settings_message = f"<b>The current settings will be added to your video file:</b>\n\n{video_settings}\n\n{audio_settings}\n\n{watermark_settings}\n\n{speed_settings}"

            await message.reply_text(settings_message)

    @app.on_message(filters.incoming & filters.command(["resolution", f"resolution@{BOT_USERNAME}"]))
    async def changer(app, message):
        if message.from_user.id in AUTH_USERS:
            r = message.text.split(" ", maxsplit=1)[1]
            OUT = f"I will be using : {r} resolution"
            resolution.insert(0, f"{r}")
            await message.reply_text(OUT)
        else:
            await message.reply_text("Error")

    @app.on_message(filters.incoming & filters.command(["auth", f"auth@{BOT_USERNAME}"]))
    async def auth(app, message):
        if message.from_user.id in AUTH_USERS:
            cr = message.text.split(" ", maxsplit=1)[1]
            OUT = f"Look at this nigga using auth btw this {cr} added to Authorised users"
            auth = int(f'{cr}')
            Config.AUTH_USERS.append(auth)
            await message.reply_text(OUT)
        else:
            await message.reply_text("Error")

    @app.on_message(filters.incoming & filters.command(["acodec", f"acodec@{BOT_USERNAME}"]))
    async def changeac(app, message):
        if message.from_user.id in AUTH_USERS:
            ac = message.text.split(" ", maxsplit=1)[1]
            OUT = f"I will be using : {ac} Audio codec"
            acodec.insert(0, f"{ac}")
            await message.reply_text(OUT)
        else:
            await message.reply_text("Error")

    @app.on_message(filters.incoming & filters.command(["metadata", f"metadata@{BOT_USERNAME}"]))
    async def changemeta(app, message):
        if message.from_user.id in AUTH_USERS:
            meta = message.text.split(" ", maxsplit=1)[1]
            OUT = f"I will be using : {meta} metadata"
            metadata.insert(0, f"{meta}")
            await message.reply_text(OUT)
        else:
            await message.reply_text("Error")

    @app.on_message(filters.incoming & filters.command(["size", f"size@{BOT_USERNAME}"]))
    async def changesi(app, message):
        if message.from_user.id in AUTH_USERS:
            si = message.text.split(" ", maxsplit=1)[1]
            OUT = f"I will be using : {si} watermark size"
            size.insert(0, f"{si}")
            await message.reply_text(OUT)
        else:
            await message.reply_text("Error")

    @app.on_message(filters.incoming & filters.command(["name", f"name@{BOT_USERNAME}"]))
    async def changete(app, message):
        if message.from_user.id in AUTH_USERS:
            na = message.text.split(" ", maxsplit=1)[1]
            OUT = f"I will be using : {na} watermark name"
            name.insert(0, f"{na}")
            await message.reply_text(OUT)
        else:
            await message.reply_text("Error")

    @app.on_message(filters.incoming & filters.command(["preset", f"preset@{BOT_USERNAME}"]))
    async def changepr(app, message):
        if message.from_user.id in AUTH_USERS:
            pop = message.text.split(" ", maxsplit=1)[1]
            OUT = f"I will be using : {pop} preset"
            preset.insert(0, f"{pop}")
            await message.reply_text(OUT)
        else:
            await message.reply_text("Error")

    @app.on_message(filters.incoming & filters.command(["codec", f"codec@{BOT_USERNAME}"]))
    async def changecode(app, message):
        if message.from_user.id in AUTH_USERS:
            col = message.text.split(" ", maxsplit=1)[1]
            OUT = f"I will be using : {col} codec"
            codec.insert(0, f"{col}")
            await message.reply_text(OUT)
        else:
            await message.reply_text("Error")

    @app.on_message(filters.incoming & filters.command(["audio", f"audio@{BOT_USERNAME}"]))
    async def changea(app, message):
        if message.from_user.id in AUTH_USERS:
            aud = message.text.split(" ", maxsplit=1)[1]
            OUT = f"I will be using : {aud} audio bitrate"
            audio_b.insert(0, f"{aud}")
            await message.reply_text(OUT)
        else:
            await message.reply_text("Error")

    @app.on_message(filters.incoming & filters.command(["compress", f"compress@{BOT_USERNAME}"]))
    async def help_message(app, message):
        if message.chat.id not in AUTH_USERS:
            return await message.reply_text("You are not authorised to use this bot contact @TheBatmanShan")
        query = await message.reply_text("ᴀᴅᴅᴇᴅ ᴛᴏ ǫᴜᴇᴜᴇ...\nᴘʟᴇᴀsᴇ ʙᴇ ᴘᴀᴛɪᴇɴᴛ ʏᴏᴜ ᴇɴᴄᴏᴅᴇ ᴡɪʟʟ sᴛᴀʀᴛ sᴏᴏɴ", quote=True)
        data.append(message.reply_to_message)
        if len(data) == 1:
            await query.delete()
            await add_task(message.reply_to_message)

    @app.on_message(filters.incoming & filters.command(["restart", f"restart@{BOT_USERNAME}"]))
    async def restarter(app, message):
        if message.from_user.id in AUTH_USERS:
            await message.reply_text("ʀᴇsᴛᴀʀᴛɪɴɢ ᴛʜᴇ ʙᴏᴛ")
            quit(1)

    @app.on_message(filters.incoming & filters.command(["clear", f"clear@{BOT_USERNAME}"]))
    async def restarter(app, message):
        data.clear()
        await message.reply_text("✅ Successfully cleared Queue ...")

    @app.on_message(filters.incoming & (filters.video | filters.document))
    async def help_message(app, message):
        if message.chat.id not in AUTH_USERS:
            return await message.reply_text("You are not authorised to use this bot contact @ninja_naruto_sai_2")
        query = await message.reply_text("ᴀᴅᴅᴇᴅ ᴛᴏ ǫᴜᴇᴜᴇ...\nᴘʟᴇᴀsᴇ ʙᴇ ᴘᴀᴛɪᴇɴᴛ ʏᴏᴜ ᴇɴᴄᴏᴅᴇ ᴡɪʟʟ sᴛᴀʀᴛ sᴏᴏɴ", quote=True)
        data.append(message)
        if len(data) == 1:
            await query.delete()
            await add_task(message)

    @app.on_message(filters.incoming & (filters.photo))
    async def help_message(app, message):
        if message.chat.id not in AUTH_USERS:
            return await message.reply_text("You are not authorised to use this bot contact @NINJA_NARUTO_SAi_2")
        os.system('rm thumb.jpg')
        await message.download(file_name='/app/thumb.jpg')
        await message.reply_text('Thumbnail Added')

    @app.on_message(filters.incoming & filters.command(["cancel", f"cancel@{BOT_USERNAME}"]))
    async def help_message(app, message):
        await incoming_cancel_message_f(app, message)

    @app.on_message(filters.incoming & filters.command(["exec", f"exec@{BOT_USERNAME}"]))
    async def help_message(app, message):
        await exec_message_f(app, message)

    @app.on_message(filters.incoming & filters.command(["eval", f"eval@{BOT_USERNAME}"]))
    async def help_message(app, message):
        await eval_message_f(app, message)

    @app.on_message(filters.incoming & filters.command(["stop", f"stop@{BOT_USERNAME}"]))
    async def help_message(app, message):
        await on_task_complete()

    @app.on_message(filters.incoming & filters.command(["help", f"help@{BOT_USERNAME}"]))
    async def help_message(app, message):
        await message.reply_text("Hi, I am <b>Video Encoder bot</b>\n\n➥ Send me your telegram files\n➥ I will encode them one by one as I have <b>queue feature</b>\n➥ Just send me the jpg/pic and it will be set as your custom thumbnail \n➥ For ffmpeg lovers - u can change crf by /eval crf.insert(0, 'crf value')\n➥ Contact ☆ @ninja_naruto_sai_2 \n\n🏷<b>Maintained By : @ninja_naruto_sai_2 t</b>", quote=True)

    @app.on_message(filters.incoming & filters.command(["log", f"log@{BOT_USERNAME}"]))
    async def help_message(app, message):
        await upload_log_file(app, message)

    @app.on_message(filters.incoming & filters.command(["ping", f"ping@{BOT_USERNAME}"]))
    async def up(app, message):
        stt = dt.now()
        ed = dt.now()
        v = ts(int((ed - uptime).seconds) * 1000)
        ms = (ed - stt).microseconds / 1000
        p = f"🌋Pɪɴɢ = {ms}ms"
        await message.reply_text(v + "\n" + p)

    call_back_button_handler = CallbackQueryHandler(
        button
    )
    app.add_handler(call_back_button_handler)

    # run the APPlication
    app.run()

