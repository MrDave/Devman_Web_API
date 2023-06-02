# Bitly URL shortener

This script allows to shorten links via Bitly and view their clicks statistics.

### How to install

To use the script, you'll need a Bitly account and your access token which can be gotten in the [API settings](https://app.bitly.com/settings/api/).
Your token will be a string of letters and numerals and look something like this:
```
abc12defg345hi6gk78lmn9op012qrs345tuvw6xyz
```
Store it in .env file in root folder of the project as "BITLY_TOKEN"

Python3 should already be installed. 
Use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Using the program

Run click_count.py  
```
python3 click_count.py
```
When asked, enter either a regular link or a bitlink
```
Enter your link: https://dvmn.org/
```
```
Enter your link: https://bit.ly/1a2b3c4
```

Get a shortened link
```
Your link wasn't a bitlink, but now it is!
Here is it: https://bit.ly/1a2b3c4
```
or a total click count of a bitlink
```
The link is a bitlink and was clicked exactly 4 time(s)
```
### Project Goals

This code was written for educational purposes as part of an online course for web developers at [dvmn.org](https://dvmn.org/).
