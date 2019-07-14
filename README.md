# PinBot - A bot that pins message(s)

This bot is written in Python and is used to pin message(s) that have certain amounts of specified Reactions.

Please note that it is only for Python 3.

The usage is pretty straightforward:

````sh
pip3 install discord
````

````sh
python3 pin_bot.py
````

You might have to insert your secret key into the script before using:

````python
if __name__ == '__main__':
  client.run('YOUR_KEY_HERE')
````
