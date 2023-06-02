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

### Project Goals

This code was written for educational purposes as part of an online course for web developers at [dvmn.org](https://dvmn.org/).
