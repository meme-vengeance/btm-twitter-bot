"""TextSpamBot.py
Prints lines of text from a given file
"""

import tweepy
from AbstractTwitterBot import AbstractTwitterBot


class TextSpamBot(AbstractTwitterBot):
    def __init__(self, twitter_api, text_file):
        with open(text_file, 'r') as f:
            self.lines = f.readlines()
        self._iter_lines = iter(self.lines)
        super(TextSpamBot, self).__init__(twitter_api=twitter_api)

    def _loop(self):
        this_line = next(self._iter_lines)
        assert isinstance(self.api, tweepy.API)
        self.api.update_status(this_line)
