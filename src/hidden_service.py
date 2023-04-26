import os

from stem.control import Controller
from dotenv import load_dotenv

load_dotenv()

PORT = os.getenv('FLASK_PORT', 2512)
HS_DIR = '/var/lib/tor/hidden_service/'

def start():
    with Controller.from_port() as controller:
        controller.authenticate()

        controller.set_options([
            ('HiddenServiceDir', HS_DIR),
            ('HiddenServicePort', f'80 127.0.0.1:{PORT}')
        ])

    TOR_URL = open(f'{HS_DIR}/hostname').read().strip()
    print(f'Successfully registered hidden service: {TOR_URL}')

    with open('logs/_hidden_service.txt', 'w') as f:
        f.write(TOR_URL)

if __name__ == '__main__':
    start()
