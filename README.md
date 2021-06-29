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

### Quota
You can change values inside `quota.py` which represent daily and hourly limits for follows, unfollows, likes and comments. Default values should be safe for a new account. From what I've read older accounts allow more actions, so you can try to increase those. If too many actions are made instagram may block you from doing that actions for some time or even ban you.

### Other info
InstaPy stores all data in `data` directory inside project root. You can restart this app at any time, all data will be saved (for example, users we already unfollowed in the past, so we will not follow them again)