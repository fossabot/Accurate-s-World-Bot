# Accurate's World Bot [![CodeFactor](https://www.codefactor.io/repository/github/shadawcraw/accurate-s-world-bot/badge)](https://www.codefactor.io/repository/github/shadawcraw/accurate-s-world-bot)

This bot is used in the Accurate's World Discord Server

# Cloning

To run and host the bot on your machine, there are a few steps to take.

## Dependencies

Here is a list of the bot dependencies:

1. Discord&#46;py python module (pip install discord&#46;py)
2. termcolor module (pip install termcolor)

## Python interpreter

This bot requires python 3.6 or higher to run.

## Config file

There are several included with the bot which are not included by default.

### SECRET&#46;json

This file contains the client token.

Steps to create this file:

1. create a file named 'SECRET.json' (caps matter!) in the `src` folder.
2. copy paste the following code inside it: </br> `{ "token": "TOKEN HERE" }`
3. replace 'TOKEN HERE' by your own token. (don't know how to get it? <a href="https://www.writebots.com/discord-bot-token/"> Here. </a>)
4. then, create a file named 'levels.json' in the extensions folder (src/extensions), you can leave it empty.
5. There! You're done, run main.py (run the python src/main.py command in the root folder) Bye!

## Server

Psst! One last thing, join the discord server the bot was made for! https://discord.gg/PUxVyEaj26
