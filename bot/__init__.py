import logging
import configparser
from telegram.ext import Updater
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

config = configparser.ConfigParser()
config.read('bot/config.ini')


def getConfig(name: str):
    return config['DEFAULT'][name]


LOGGER = logging.getLogger(__name__)

try:
    if bool(config['DEFAULT']['_____REMOVE_THIS_LINE_____']):
        logging.ERROR('The README.md file there to be read! Exiting now!')
        exit()
except KeyError:
    pass

DOWNLOAD_DIR = None
BOT_TOKEN = None
try:
    BOT_TOKEN = getConfig('BOT_TOKEN')
    CLIENT_ID = getConfig('G_DRIVE_CLIENT_ID')
    CLIENT_SECRET = getConfig('G_DRIVE_CLIENT_SECRET')
    parent_id = getConfig('GDRIVE_FOLDER_ID')
    DOWNLOAD_DIR = getConfig('DOWNLOAD_DIR')
    if DOWNLOAD_DIR[-1] != '/' or DOWNLOAD_DIR[-1] != '\\':
        DOWNLOAD_DIR = DOWNLOAD_DIR + '/'
    DOWNLOAD_STATUS_UPDATE_INTERVAL = int(getConfig('DOWNLOAD_STATUS_UPDATE_INTERVAL'))
    download_list = {}

except KeyError as e:
    LOGGER.error("One or more env variables missing! Exiting now")
    exit(1)

updater = Updater(token=BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher