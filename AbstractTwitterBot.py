"""AbstractTwitterBot.py
Class definition for twitter bot
"""


class AbstractTwitterBot:

    def __init__(self, twitter_api):
        """Initialize the bot with an api object
        """
        self.api = twitter_api
        self.running = False

    def start(self):
        """Initialize the twitter bot functionality
        """
        self.running = True

    def stop(self):
        """Halt the twitter bot from updating
        """
        self.running = False

    def loop(self):
        """If the bot has been started, perform the action specified by _loop
        """
        if self.running:
            self._loop()

    def _loop(self):
        """Perform the function of the twitter bot. Without affecting
        self.api or self.running. (Subtypes of
        AbstractTwitterBot must implement this function).
        :return:
        """
        raise NotImplementedError
