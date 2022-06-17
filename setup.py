from setuptools import setup

setup(
   name='dcmusicbot',
   version='1.0',
   description='A simple Discord MusicBot',
   author='zaskul',
   packages=['dcmusicbot'],
   install_requires=['discord', 'asyncio', 'youtube-dl', 'pafy', 'dotenv', 'PyNaCl'],
)
