from otree.api import *



doc = """
this is a course
"""


class C(BaseConstants):
    NAME_IN_URL = 'webapp'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    '''kept = models.CurrencyField(
        doc="""Amount dictator decided to keep for himself""",
        min=0,
        max=C.ENDOWMENT,
        label="I will keep",
    )'''
    pass


class Player(BasePlayer):
    pass


# FUNCTIONS
def set_payoffs(group: Group):
    p1 = group.get_player_by_id(1)
    p2 = group.get_player_by_id(2)
    p1.payoff = group.kept
    p2.payoff = C.ENDOWMENT - group.kept


# PAGES
class Introduction(Page):
    @staticmethod
    def live_method(player, data):
        print("data: ",data)
        return {0: data}
    


class Offer(Page):
#    form_model = 'group'
#    form_fields = ['kept']
#
#    @staticmethod
#    def is_displayed(player: Player):
#        return player.id_in_group == 1

    pass

class ResultsWaitPage(WaitPage):
#    after_all_players_arrive = set_payoffs
    pass

class Results(Page):
#    @staticmethod
#    def vars_for_template(player: Player):
#        group = player.group
#
#        return dict(offer=C.ENDOWMENT - group.kept)
    pass


page_sequence = [Introduction, Results]
