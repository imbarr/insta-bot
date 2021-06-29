import random
from instapy import InstaPy


def get_sleep_delay():
    return random.randint(500, 600)


def set_quota(session: InstaPy):
    session.set_quota_supervisor(enabled=True,
                                 sleep_after=["likes", "comments", "follows", "server_calls"],
                                 sleepyhead=True,
                                 stochastic_flow=True,
                                 notify_me=False,
                                 peak_likes_hourly=10,
                                 peak_likes_daily=250,
                                 peak_comments_hourly=5,
                                 peak_comments_daily=10,
                                 peak_follows_hourly=5,
                                 peak_follows_daily=150,
                                 peak_unfollows_hourly=5,
                                 peak_unfollows_daily=150,
                                 peak_server_calls_hourly=200,
                                 peak_server_calls_daily=2500)
