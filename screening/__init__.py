from otree.api import *


doc = """
Basic screening app for online studies by Victor van Pelt
"""


class C(BaseConstants):
    NAME_IN_URL = 'screening'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class Captcha(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            participant_code=player.participant.label or player.participant.code,
            captcha_site_key="6LcHjv8iAAAAAAt9h-yoVQ7VqezK1NHGMJwNnoIv",
            pro_ip_api_key="05rqfk8VoTFZUuB"
        )


class Welcome(Page):
    pass


page_sequence = [Captcha, Welcome]
