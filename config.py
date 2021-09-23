from strictyaml import load, Map, Str, Int, Seq, Float, Bool, EmptyList, Optional, Enum
import logging

schema = Map({
    'app': Map({
        'log_level': Str(),
        'main_cycle_rate_minutes': Float(),
        'headless_browser': Bool()
    }),
    'instagram': Map({
        'login': Str(),
        'password': Str()
    }),
    'instapy': Map({
        Optional('skip_actions', default=[]): Seq(Enum([
            'pods',
            'accept_follow',
            'follow_users',
            'follow_tags',
            'unfollow',
            'interact_feed',
            'interact_tags'
        ])) | EmptyList(),

        'follow_count': Int(),
        'unfollow_count': Int(),
        'like_count': Int(),

        Optional('skip_private', default=False): Bool(),

        'follow_user_followers': Seq(Str()) | EmptyList(),
        'follow_tags': Seq(Str()) | EmptyList(),
        'unfollow_after_hours': Float(),

        'like_tags': Seq(Str()) | EmptyList(),
        'comment_percentage': Int(),
        'comments': Seq(Str()) | EmptyList(),
        'comment_media': Str(),

        'ignore': Seq(Str()) | EmptyList(),
    })

})

cfg: schema


def fetch_config_unsafe():
    global cfg
    with open('config/config.yaml', 'r') as file:
        config = load(file.read(), schema=schema)
        _validate(config)
        cfg = config.data


def fetch_config_safe():
    try:
        fetch_config_unsafe()
    except Exception as e:
        logging.error(f'Failed to fetch config, using last version instead: {e}')


def _validate(config: schema):
    pass
