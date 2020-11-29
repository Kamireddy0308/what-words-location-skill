from mycroft import MycroftSkill, intent_file_handler


class WhatWordsLocation(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('location.words.what.intent')
    def handle_location_words_what(self, message):
        self.speak_dialog('location.words.what')


def create_skill():
    return WhatWordsLocation()

