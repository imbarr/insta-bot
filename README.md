# Instagram Bot

### Installation
1) Install Firefox and Geckodriver
2) Install packages (I recommend using virtualenv)

    `pip install -r requirements.txt`
    
    Note that requirements.txt contains link to my fork of InstaPy with some bugfixes. I might merge it into main repo later.
    
3) Copy and edit `config.yaml`. You should change login and password, rest should work out of the box. 

    `cp config/config-example.yaml config/config.yaml`

4) Edit `quota.py` (see below)

5) Run with `python3 run.py`

### Description
You should understand that this bot is very different from twitter-bot I made previously. It does not use instagram api, instead it operates through headless firefox browser using selenium driver. Most actions are slow to avoid suspicion, so it's recommended that it runs 24/7. In any case achieving good results will take some time because of strict limitations.

### Quota
You can change values inside `quota.py` which represent daily and hourly limits for follows, unfollows, likes and comments. Default values should be safe for a new account. From what I've read older accounts (>3 months) allow more actions, so you can try to increase those. If too many actions are made instagram may block you from doing that actions for some time or even ban you.

### Other info
InstaPy stores all data in `data` directory inside project root. You can restart this app at any time, all data will be saved (for example, users we already unfollowed in the past, so we will not follow them again)