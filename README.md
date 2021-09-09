
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
| Command | Brief  | Flags | 
| --- | ----------- |---------|
| `+user <name>` | Shows information about an user. |`manga` <br /> `reading` <br /> `plantoread` <br /> `completed` <br /> `dropped` <br /> `onhold` <br /> `plantowatch` <br /> `watching`| 

### Usage
```
+user <name> [--manga] [--reading] [--ptr] [--completed] [--dropped] [--onhold] [--ptw] [--watching]
```

### Description 
* Shows detailed information about MyAnimeList user's list or sends you the general profile information about their profile. 
* Use flag `--m` or `--manga` to specify if you need manga list of a particular status.
* For example, if you want to look into completed manga(s) of user wildcyclotron: 
```
+user wildcyclotron --completed --m
```
* For flags like `--reading` or `--ptr`(or `--plantoread`), you may or may not pass the `--manga` because it's obvious that they belong to manga list.
* The position of flags doesn't matter i.e `--dropped --m` is same as `--m --dropped`

### Examples 
```
+user wildcyclotron
+user wildcyclotron --watching
+u wildcyclotron --completed 
+u wildcyclotron --onhold
+u wildcyclotron --ptw
+u wildcyclotron --dropped
+u wildcyclotron --completed --m
+u wildcyclotron --dropped --m
+u wildcyclotron --onhold --m
+u wildcyclotron --reading
+u wildcyclotron --ptr
```

### Screenshots
![user info](https://media.discordapp.net/attachments/870414758006911036/885517666608091157/user_info.gif)
![user status](https://media.discordapp.net/attachments/870414758006911036/885538284892209172/user_list.gif)

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


