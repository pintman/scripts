from mastodon import Mastodon
import os

CLIENT_CRED_FILE='mastodon_poster_clientcred.secret'

API = os.environ.get('MASTODON_API')
USER = os.environ.get('MASTODON_USER')
PASSWORD = os.environ.get('MASTODON_PASSWORD')
TO = os.environ.get('MASTODON_TO')
MSG = os.environ.get('MASTODON_MSG')

def register_app():
    'run this only once to register the app'
    Mastodon.create_app(
        'mastodon_poster',
        api_base_url=API,
        to_file=CLIENT_CRED_FILE
    )

def main():
    if not USER or not PASSWORD:
        print('Username/Password missing in env')
        exit()

    if not TO:
        print('no target for message found')
        exit()

    mastodon = Mastodon(
        client_id=CLIENT_CRED_FILE,
        api_base_url=API
    )
    mastodon.log_in(username=USER, password=PASSWORD)

    mastodon.status_post(f'@{TO} {MSG}', visibility='direct')


if __name__ == '__main__':  
    main()
