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
            captcha_site_key="ENTER CAPTCHA SITE KEY HERE",
            pro_ip_api_key="ENTER PRO IP API KEY HERE"
        )


class Welcome(Page):
    pass


page_sequence = [Captcha, Welcome]
