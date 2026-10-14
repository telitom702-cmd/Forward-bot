# VJ Forward Bot

<b>Auto Restart All User Forwarding After Bot Restarted.</b>

![Typing SVG](https://readme-typing-svg.herokuapp.com/?lines=Welcome+To+VJ+Forward+Bot+!)

## How To Deploy [Video Tutorial](https://youtu.be/A-iIh_5WAlk)

## Features

- [x] Public Forward (Bot)
- [x] Private Forward (User Bot)
- [x] Custom Caption
- [x] Custom Button
- [x] Skip Duplicate Messages
- [x] Skip Messages Based On Extensions & Keywords & Size
- [x] Filter Type Of Messages
- [x] Auto Restart Pending Task After Bot Restart

<b>To Know About All Features, Join My <a href='https://t.me/VJ_Botz'>Update Channel</a>.</b>

## Commands

```text
/start       - check I'm alive
/forward     - forward messages
/unequify    - delete duplicate media messages in chats
/settings    - configure your settings
/stop        - stop your ongoing tasks
/reset       - reset your settings
/restart     - restart server (owner only)
/resetall    - reset all users settings (owner only)
/broadcast   - broadcast a message to all your users (owner only)
```

## Run

The bot and its HTTP health-check server are started together by `bot.py`. Run locally with:

```bash
python bot.py
```

The Procfile uses the same entry point as the Docker image. The HTTP server listens on `PORT` (default `8080`) and responds at `/` and `/health`.

## Environment variables

- `API_ID` - Telegram API ID from my.telegram.org (required)
- `API_HASH` - Telegram API hash from my.telegram.org (required)
- `BOT_TOKEN` - Bot token from @BotFather (required)
- `DATABASE_URI` - MongoDB connection URI (required)
- `DATABASE_NAME` - MongoDB database name (default: `vj-forward-bot`)
- `BOT_SESSION` - Pyrogram session name (default: `vjbot`)
- `BOT_OWNER` - Telegram account ID for owner-only commands
- `PORT` - HTTP health-check port (default: `8080`; usually set by the host)

## Credits

- <b>[Tech VJ](https://youtube.com/@Tech_VJ)</b>
