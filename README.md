
# MyAnimeList-discord-bot
A python bot made to surf MyAnimeList website from discord.
# Overview 
A discord bot made to surf the MyAnimeList website on discord with the help of the [Jikan REST API](https://github.com/jikan-me/jikan-rest). View the information about any anime, manga, character etc. using advanced search commands. Look into the pictures of your favourite character from any anime or manga using a single search command. 
# Planned
| Commands      | Description |
| ----------- | ----------- |
| `+top <type>`   | To view rankings of characters, animes and mangas.        |
# Commands 
## Search
| Commands | Description | Examples|
| --- | ----------- |---------|
| `+anime <name>` | Get information about an anime. |+anime Hyouka, +anime NHK ni Youkoso!|
|`+manga <name>` | Get information about a manga. |+manga attack on titan, +manga Omniscient Reader|

### Screenshot
![anime search](https://media.discordapp.net/attachments/870414758006911036/884551943505211473/github_anime.gif)

## Character
| Commands | Description | Examples|
| --- | ----------- |---------|
| `+char <name>` | Get Information about the requested character. |+character Mikasa, +char Oreki|
|`+images <name>` | Get images for the requested character. |+images Mikasa, +im Eru Chitanda|

### Screenshots
![char search](https://media.discordapp.net/attachments/870414758006911036/884554644972523520/github_char.gif)
![char images](https://media.discordapp.net/attachments/870414758006911036/884558109664751636/github_img.gif)

## User 
| Command | Description | Flags | Examples |
| --- | ----------- |---------|----|
| `+user <name>` | Shows information about a user's list or their profile. |`manga` <br /> `reading` <br /> `plantoread` <br /> `completed` <br /> `dropped` <br /> `onhold` <br /> `plantowatch` <br /> `watching`| `+user wildcyclotron` <br /> `+user wildcyclotron --watching` <br />  `+u wildcyclotron --completed` <br />  `+u wildcyclotron --onhold` <br />  `+u wildcyclotron --ptw `<br /> ` +u wildcyclotron --dropped` <br />` +u wildcyclotron --completed --m `<br /> ` +u wildcyclotron --dropped --m `<br />`  +u wildcyclotron --onhold --m `<br /> `+u wildcyclotron --reading` <br /> ` +u wildcyclotron --ptr` |

### Screenshots
![user info](https://media.discordapp.net/attachments/870414758006911036/885517666608091157/user_info.gif)
![user status](https://media.discordapp.net/attachments/870414758006911036/885523201625583626/user_status.gif)
# Installing
* Make sure to get Python 3.8 or higher.

* Set up venv
```
python3.8 -m venv venv
```
* Install dependencies
```
pip install -U -r requirements.txt
```

* To install the development version, do the following:
```
$ git clone https://github.com/WildCyclotron/MyAnimeList-discord-bot.git
```
# Running 
* Edit `main.py` and replace the `'Token'` with the your bot's actual token.
* Save your changes and run the `main.py` file.
```
python main.py 
```

# DISCLAIMER
Please be respectful towards MyAnimeList's [Terms Of Service](https://myanimelist.net/about/terms_of_use).


