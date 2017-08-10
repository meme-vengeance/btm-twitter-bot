"""TextSpamBot.py
Prints lines of text from a given file
"""

import tweepy
from AbstractTwitterBot import AbstractTwitterBot


class TextSpamBot(AbstractTwitterBot):
    def __init__(self, twitter_api, text_file):
        """Initiate a twitter spam bot that tweets lines from text_file
        one at a time in the order they are printed.
        Requires:
            + text_file contains at least one line
        """
        with open(text_file, 'r') as f:
            self.lines = list(f.readlines())
        self.pos = 0
        super(TextSpamBot, self).__init__(twitter_api=twitter_api)

    def _loop(self):
        if self.pos >= len(self.lines):
            self.pos = 0
        this_line = self.lines[self.pos].strip()
        assert isinstance(self.api, tweepy.API)
        self.api.update_status(this_line)
