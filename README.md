## Table of contents
* [MusicBot](#musicbot)
* [Setup](#setup)
* [Bot-commands](#bot-commands)
* [Packages](#packages)
* [Technologies](#technologies)
* [Status](#status)

## MusicBot
This project is a simple discord music bot. 

## Setup
Clone the repository to your desired directory

    git clone https://github.com/zaskul/Discord-MusicBot

To run the bot on your local machine first create a virtual environment:

    python -m virtualenv <name of your venv>

Install all the necessary packages

    pip install -r requirements.txt

If you want to use a service like Heroku follow their guide on how to deploy a Python app:

    https://devcenter.heroku.com/articles/getting-started-with-python

If you're working locally make sure you to declare two variables in `.env` file:

    TOKEN=<your Discord bot token>
    pathToBackendYoutubeDl=<path to backend_youtube_dl.py file>

If you're working with service like Heroku follow their guide on how to add config vars to your project:

    https://devcenter.heroku.com/articles/config-vars#local-setup

Example paths:

* if you want to run the bot locally:

    .\\Lib\\site-packages\\pafy\\backend_youtube_dl.py

* if you want to run the bot on a service like Heroku:

    .heroku/python/lib/python3.10/site-packages/pafy/backend_youtube_dl.py

It is needed due to an occuring bug involving the removal of dislikes by YouTube

## Bot commands
* ?join 
* ?play <URL or keyword> 
* ?leave
* ?queue
* ?skip


## Packages
* discord
* asyncio
* youtube_dl
* pafy
* dotenv
* PyNaCl

## Technologies
* Python 3.10.1

## Status
The project is still in development
