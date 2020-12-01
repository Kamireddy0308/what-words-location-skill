from mycroft import MycroftSkill, intent_file_handler
import requests
import json
from mycroft.utils.log import getLogger

LOGGER = getLogger(__name__)
def what_three_words():
    x = 'bricht'
    y = 'schach'
    z = 'bauen'
    value = requests.get(
        'https://api.what3words.com/v3/convert-to-coordinates?words=' + x + '.' + y + '.' + z + '&key=4WBPDAOJ',
        verify=False)
    json_value = value.json()
    response = json_value['nearestPlace']
    return response

class WhatWordsLocation(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('location.words.what.intent')
    def handle_location_words_what(self, message):
        output = what_three_words()
        LOGGER.debug(message)
        self.speak_dialog(output)


def create_skill():
    return WhatWordsLocation()


'''
from mycroft import MycroftSkill, intent_file_handler


class WhatWordsLocation(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('location.words.what.intent')
    def handle_location_words_what(self, message):
        self.speak_dialog('location.words.what')


def create_skill():
    return WhatWordsLocation()
'''

