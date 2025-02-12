# File Sharing Ultra V1

![Image](https://github.com/user-attachments/assets/ede171ae-66bb-45f8-aded-ce2f0dd5782d)

## 🚀 A Telegram File Sharing Bot
Easily access files through specific links!

---

## ✨ Features
- 🔹 Fully customizable
- 🔹 Two Force Sub Channels
- 🔹 Change ForceSub & Admins via commands
- 🔹 Custom welcome & ForceSub messages
- 🔹 Customizable images
- 🔹 Multiple posts in one link
- 🔹 Deployable on **Heroku** & **Koyeb**

---

## ⚙️ Setup
- Add the bot to **Database Channel** with all permissions
- Add the bot to **ForceSub Channel** as Admin with "Invite Users via Link" permission (if enabled)

---

## 🚀 Installation
### 📌 Deploy on Heroku
**Fork the repo & rename it before deploying!**

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

### 📌 Deploy on Render
**Fork the repo, edit config, create new web service, add variables, and add monitor.**

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com)

---

### 📌 Deploy in VPS
```bash
# Clone repo
git clone https://github.com/<github-username>/<repo-name>
cd <repo-name>

# Install dependencies
pip3 install -r requirements.txt

# Add values in config.py
python3 main.py
```

### 📌 Deploy in VPS (Private Repo)
```bash
git clone https://<your-github-private-token>:x-oauth-basic@github.com/<github-username>/<repo-name>
cd <repo-name>
pip3 install -r requirements.txt
python3 main.py
```

---

## 🔥 Admin Commands
```bash
start - Start the bot or get posts
batch - Create links for multiple posts
nbatch - Advanced batch processing
genlink - Create link for one post
users - View bot statistics
broadcast - Broadcast messages to users
stats - Check bot uptime
add_admin - Add admins
del_admin - Remove admins
admins - View admin list
forcesub1 - Change ForceSub Channel 1
forcesub2 - Change ForceSub Channel 2
```

---

## 🔑 Environment Variables
* `API_HASH` - API Hash from [my.telegram.org](https://my.telegram.org)
* `APP_ID` - API ID from [my.telegram.org](https://my.telegram.org)
* `TG_BOT_TOKEN` - Bot token from [@BotFather](https://t.me/BotFather)
* `OWNER_ID` - Your Telegram ID
* `CHANNEL_ID` - Your Channel ID (e.g., `-100xxxxxxxx`)
* `DB_URL` - MongoDB URL
* `DB_NAME` - MongoDB session name
* `ADMINS` - (Optional) Space-separated list of admin user IDs
* `START_MSG` - (Optional) Custom start message
* `FORCE_SUB_MESSAGE` - (Optional) Custom ForceSub message
* `FORCE_CHANNEL` - (Optional) ForceSub Channel ID (set `0` to disable)
* `FORCE_CHANNEL2` - (Optional) Second ForceSub Channel ID
* `PROTECT_CONTENT` - (Optional) Set `True` to prevent file forwarding

---

## 🎨 Extra Variables
* `CUSTOM_CAPTION` - Custom caption for documents
* `DISABLE_CHANNEL_BUTTON` - Set `True` to disable channel share button (default `False`)
* `BOT_STATS_TEXT` - Custom text for `/stats` command
* `USER_REPLY_TEXT` - Custom reply text for user messages

---

## 🛠️ Fillings
### 🔹 START_MESSAGE | FORCE_SUB_MESSAGE
* `{first}` - User first name
* `{last}` - User last name
* `{id}` - User ID
* `{mention}` - Mention user
* `{username}` - Username

### 🔹 CUSTOM_CAPTION
* `{filename}` - File name
* `{previouscaption}` - Original caption

### 🔹 CUSTOM_STATS
* `{uptime}` - Bot uptime

---

⭐ **Star this Repo if you Liked it!** ⭐⭐⭐
