## Table of contents
* [MusicBot](#musicbot)
* [Setup](#setup)
* [Bot-commands](#bot-commands)
* [Packages](#packages)
* [Technologies](#technologies)
* [Status](#status)

## MusicBot
This project is a simple discord music bot 

## Setup
Clone the repository to your desired directory

    git clone https://github.com/zaskul/Discord-MusicBot

Create `.env` file that contains a token to your discord bot in the following format

    TOKEN=<your token>

Install all the necessary packages

Make sure to comment line 54

    self._dislikes = self._ydl_info['dislike_count']
    
in

    \Lib\site-packages\pafy\backend_youtube_dl.py
    
due to a bug caused by YouTube removing dislikes

Run the `main.py` file

    python main.py

## Bot commands
* ?play <URL or keyword> 
* ?join
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
The project is incomplete
