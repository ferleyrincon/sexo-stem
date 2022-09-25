"""
Implicit Association Test (IAT) experiment -- models.

Dynamic data points for IAT trials are collected in custom data model "Trial". See Konrad 2018 [1] for an article
on collection dynamic data with oTree.

[1] https://doi.org/10.1016/j.jbef.2018.10.006

November 2019
Markus Konrad <markus.konrad@wzb.eu>

Updated December 2020
Christoph Semken <dev@csemken.eu>
"""

import random

# required for custom data models:
from otree.db.models import Model, ForeignKey
from otree.export import sanitize_for_csv
from otreeutils.admin_extensions import custom_export

from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Markus Konrad <markus.konrad@wzb.eu>'

doc = """
IAT – Implicit Association Test Gender-STEM
Adapted from: https://github.com/WZBSocialScienceCenter/otree_iat/blob/master/iat/models.py
"""

#
# configuration of stimuli: attribute and concept levels and stimuli words
# these are just made up stimuli; fill in your own
#

STIMULI = {
    'attributes': {
        'woman': ['mamá', 'mujer', 'chica', 'femenina', 'hija'],
        'man':   ['papá', 'hombre', 'chico', 'masculino', 'hijo']
    },
    'concepts': {
        'stem':    ['matemáticas', 'naturales'  , 'informática' , 'ingenierías', 'química'  ],
        'no_stem': ['español'    , 'sociales'   , 'artes'       , 'humanidades', 'filosofía']
    }
}

STIMULI_LABELS = {
    ('attributes', 'woman'): 'Mujer',
    ('attributes', 'man'): 'Hombre',
    ('concepts', 'stem'): ' Números (STEM)',
    ('concepts', 'no_stem'): 'Letras (No STEM)',
}

# Images of the attributes and concepts
IMAGES = {
    ('attributes', 'woman'): 'mujer.png',
    ('attributes', 'man'): 'hombre.png',
    ('concepts', 'stem'): 'numeros.png',
    ('concepts', 'no_stem'): 'a-b-c.png',
}

#
# configuration of practice and Prueba blocks
#

BLOCKS = [
    {   # 1
        'label': 'Practica 1',
        'n': 10,      # this must match the number of stimuli per side
        'left': [('concepts', 'no_stem')],
        'right': [('concepts', 'stem')],
        'is_practice': True
    },
    {   # 2
        'label': 'Practica 2',
        'n': 10,
        'left': [('attributes', 'man')],
        'right': [('attributes', 'woman')],
        'is_practice': True
    },
    {   # 3
        'label': 'Prueba 1',
        'n': 20,
        'left': [
            ('attributes', 'man'),
            ('concepts', 'no_stem'),
        ],
        'right': [
            ('attributes', 'woman'),
            ('concepts', 'stem'),
        ]
    },
    {   # 4: same as 3
        'label': 'Prueba 2',
        'n': 20,
        'left': [
            ('attributes', 'man'),
            ('concepts', 'no_stem'),
        ],
        'right': [
            ('attributes', 'woman'),
            ('concepts', 'stem'),
        ]
    },
    {   # 5
        'label': 'Practica 3 (invertida)',
        'n': 10,
        'left': [('concepts', 'stem')],
        'right': [('concepts', 'no_stem')],
        'is_practice': True,
        'notice': 'CUIDADO, ¡Las categorías cambiaron de lado!',
    },
    {  # 6
        'label': 'Prueba 3',
        'n': 20,
        'left': [
            ('attributes', 'man'),
            ('concepts', 'stem'),
        ],
        'right': [
            ('attributes', 'woman'),
            ('concepts', 'no_stem'),
        ]
    },
    {  # 7: same as 6
        'label': 'Prueba 4',
        'n': 20,
        'left': [
            ('attributes', 'man'),
            ('concepts', 'stem'),
        ],
        'right': [
            ('attributes', 'woman'),
            ('concepts', 'no_stem'),
        ]
    },
]

class Constants(BaseConstants):
    name_in_url = 'iat'
    players_per_group = None
    num_rounds = len(BLOCKS)                  # number of blocks to play
    capture_keycodes = {'left': ('KeyE', 'E'),
                        'right': ('KeyI', 'I')}
    next_trial_delay_ms = 250                 # delay between trials in millisec.


class Subsession(BaseSubsession):
    def set_id_players(self):
        for j in self.get_players():
            j.set_id()

    def creating_session(self):
        """
        Prepare trials for each round. Generates Trial objects.
        """

        # iterate through all players in all rounds
        trials = []
        for p in self.get_players():
            block_num = p.round_number - 1
            block_def = BLOCKS[block_num]    # get block definition for this round

            # create stimuli: class (attrib./concept) and level (e.g. woman./man.) for left and right side
            stimuli = []
            for side in ('left', 'right'):
                for stim_class, stim_lvl in block_def[side]:
                    stim_vals = STIMULI[stim_class][stim_lvl]   # concrete stimuli words
                    n_vals = len(stim_vals)
                    stimuli.extend(zip([side] * n_vals, [stim_class] * n_vals, [stim_lvl] * n_vals, stim_vals))

            # randomize order
            random.shuffle(stimuli)

            if len(stimuli) != block_def['n']:
                raise ValueError('the number of stimuli (%d) and the number of repetitions in the block definition '
                                 '(n=%d) do not match' % (len(stimuli), block_def['n']))

            # generate Trial object for each stimulus
            for trial_i, stim_def in enumerate(stimuli):
                side, stim_class, stim_lvl, stim = stim_def

                trials.append(Trial(
                    block=p.round_number,
                    trial=trial_i+1,
                    stimulus=stim,
                    stimulus_class=stim_class,
                    stimulus_level=stim_lvl,
                    player=p
                ))

        Trial.objects.bulk_create(trials)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    identificador = models.StringField(label='Recuerde que su código de participante está compuesto por las iniciales de su primer nombre y apellido seguido de su fecha de nacimiento. Por ejemplo, si usted se llama Andres Carrillo y usted nació el 11 de febrero de 2005, su código será AC11022005. Para iniciar por favor ingrese su código, escriba todo en mayúscula. Este código es importante para asegurar su participación en el resto de la actividad.')
    treatment = models.IntegerField(
    choices=[
        [0, 'C'],
        [1, 'T'],
    ], label="Por favor seleccione el grupo al que fue asignado")

    def set_id(self):
        self.participant.vars['identificador'] = self.in_round(1).identificador


class Trial(Model):
    """
    Trial model holds all information for a single trial made by a player.
    This is a "custom data model" in a 1:n relationship between Player and Trial.
    It uses an otreeutils "CustomModelConf" for monitoring and exporting the collected data from this model.
    """
    block = models.IntegerField()  # block number (-> round number)
    trial = models.IntegerField()  # trial number in that round for that participant

    stimulus = models.StringField()          # shown word or name
    stimulus_class = models.StringField()    # words or names
    stimulus_level = models.StringField()    # woman/man or tr/dt

    response_key = models.StringField()       # response: key that was pressed by participant
    response_correct = models.BooleanField()  # records whether response was correct
    response_time_ms = models.IntegerField()  # time it took until key was pressed since word/name was shown

    player = ForeignKey(Player, on_delete=models.CASCADE)  # make a 1:n relationship between Player and Trial

    class CustomModelConf:
        """
        Configuration for otreeutils admin extensions.
        """
        data_view = {  # define this attribute if you want to include this model in the live data view
            'exclude_fields': ['player'],
            'link_with': 'player'
        }
        export_data = {  # define this attribute if you want to include this model in the data export
            'exclude_fields': ['player_id'],
            'link_with': 'player'
        }


try:
    from otreeutils.admin_extensions import custom_export
except ImportError:
    def custom_export(players):
        print("Error de importación")
        """
        Export all IAT trials together with the standard fields `session` and `participant_code`
        """
        fields_to_export = ['block', 'trial', 'stimulus', 'stimulus_class', 'stimulus_level',
                            'response_key', 'response_correct', 'response_time_ms']
        yield ['session', 'participant_code'] + fields_to_export
        print("fields to export", fields_to_export)
        for trial in Trial.objects.all():
            yield [trial.player.session.code, trial.player.participant.code] \
                + [sanitize_for_csv(getattr(trial, f)) for f in fields_to_export]
