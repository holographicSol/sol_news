GDAC Defcon and World News data stored and displayed. Designed for use on Android Sony Xperia Tablet Z as a dedicated Sol News Device.
Written by Benjamin Jack Cullen - All rights reserved.

Note: Writes to console are formatted specifically for Sony Xperia Tablet Z screen geometry.

On Android (recommended display 1920x1080):
1. install & open termux
2. command line:
    pkg install requests
    pkg install bs4
    pkg install colorama
3. git clone https://github.com/holographicSol/sol_news
4. cd sol_news
5. python sol_news.py


To use with displays smaller than 1920x1080 modify the char_limit variable to anything you like, although you may need to perform
other formatting too.

Developed on Windows 10 using Python version 3.9 for Windows/Linux and Android namely for Sony Xperia Tablet Z.

The news articles are not meant to be read except in internet/power down events where information could help. The rest of the time
the tablet/device serves as a low power (ideally) device displaying and storing potentially critical data.
Use a CLI wizard or file browser to read the articles, find articles from certain time or find articles containing foobar.

![DEMO IMAGE](/Demo.png)
