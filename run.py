import config
import quota
import time
import sys
import os
import logging
import schedule
from instapy import InstaPy, smart_run, Settings


session: InstaPy


def main():
    try:
        config.fetch_config_unsafe()
    except Exception as e:
        logging.fatal(f'Failed to fetch config: {e}')
        sys.exit(1)

    logging.basicConfig(
        stream=sys.stdout,
        level=config.cfg["app"]["log_level"],
        format=f'[%(asctime)s] InstaBot: %(levelname)s - %(message)s'
    )

    Settings.log_location = "data"
    Settings.database_location = os.path.join("data", "instapy.db")

    global session
    session = InstaPy(
        username=config.cfg['instagram']['login'],
        password=config.cfg['instagram']['password'],
        headless_browser=config.cfg['app']['headless_browser'],
        show_logs=False
    )

    quota.set_quota(session)

    cycle_rate = config.cfg['app']['main_cycle_rate_minutes']
    cycle_rate_seconds = int(cycle_rate * 60)
    schedule.every(cycle_rate_seconds).seconds.do(main_cycle)

    with smart_run(session):
        schedule.run_all()
        while True:
            schedule.run_pending()
            time.sleep(1)


def main_cycle():
    logging.info('Starting main cycle')
    config.fetch_config_safe()
    set_session_settings()
    follow_activity()
    interact_activity()
    logging.info('Main cycle finished')


def set_session_settings():
    session.set_skip_users(skip_private=config.cfg['instapy']['skip_private'])
    session.set_dont_like(config.cfg['instapy']['ignore'])
    media = config.cfg['instapy']['comment_media']
    session.set_comments(config.cfg['instapy']['comments'],
                         media=None if media.lower() == 'all' else media)
    percentage = config.cfg['instapy']['comment_percentage']
    session.set_do_comment(enabled=True, comment_liked_photo=True, percentage=percentage)
    session.join_pods('fashion', engagement_mode='no_comments')


def follow_activity():
    if config.cfg['instapy']['unfollow_all']:
        logging.info('Unfollowing all users')
        session.unfollow_users(amount=100, allFollowing=True,
                               style="FIFO", unfollow_after=None,
                               sleep_delay=quota.get_sleep_delay())
        return

    logging.info('Accepting follow requests')
    session.accept_follow_requests(amount=50)

    logging.info('Following user followers')
    session.follow_user_followers(usernames=config.cfg['instapy']['follow_user_followers'],
                                  amount=config.cfg['instapy']['follow_count'],
                                  randomize=False, interact=False, sleep_delay=quota.get_sleep_delay())

    logging.info('Following by tags')
    session.follow_by_tags(tags=config.cfg['instapy']['follow_tags'],
                           randomize=False, amount=config.cfg['instapy']['follow_count'])

    unfollow_after = int(config.cfg['instapy']['unfollow_after_hours'] * 60 * 60)
    logging.info(f'Setting unfollow action after {unfollow_after} seconds')
    session.unfollow_users(amount=config.cfg['instapy']['follow_count'], nonFollowers=True, style="FIFO",
                           unfollow_after=unfollow_after, sleep_delay=quota.get_sleep_delay())


def interact_activity():
    session.like_by_tags(tags=config.cfg['instapy']['like_tags'],
                         amount=config.cfg['instapy']['like_count'], interact=False)
    session.like_by_feed(amount=config.cfg['instapy']['like_count'],
                         interact=True, randomize=False, unfollow=False)


if __name__ == '__main__':
    main()
