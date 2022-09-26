from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random

class occupation2(Page):
    form_model = 'player'
    form_fields = ['educ_type', "educ_university", "educ_university2"]

    def is_displayed(self):
        return self.round_number == 1

class saber11(Page):
    form_model = 'player'
    form_fields = ['prueba_20000', 'prueba_15000', 'prueba_10000', 'prueba_5000', 'puntaje_20000', 'puntaje_15000', 'puntaje_10000', 'puntaje_5000', 'prefer_20000', 'prefer_15000', 'prefer_10000', 'prefer_5000', 'predic_20000', 'predic_15000', 'predic_10000', 'predic_5000', 'grupo_puntaje_global']

    def is_displayed(self):
            return self.round_number == 1

class education(Page):
    form_model = 'player'
    form_fields = ['educsup', 'check_slider_educsup']

    def is_displayed(self):
        return self.round_number == 1

class beliefs(Page):
    form_model = 'player'
    form_fields = ['p_science1','p_science2','p_science3','p_science4','p_science5','p_gender1','p_gender2','p_gender3','p_gender4','p_gender5']

    def is_displayed(self):
        return self.round_number == 1

class group(Page):
    form_model = 'player'
    form_fields = ['i_mat','i_spa','i_sci','i_soc']

    def is_displayed(self):
        return self.round_number == 1

class explicit(Page):
    form_model = 'player'
    form_fields = ['e_tec','e_sci','e_mat','e_spa','e_soc','e_art']

    def is_displayed(self):
        return self.round_number == 1

class efficacy(Page):
    form_model = 'player'
    form_fields = ['p_math1','p_math2','p_math3','p_math4','p_jobsci1','p_jobsci2','p_jobsci3']

    def is_displayed(self):
        return self.round_number == 1

class occupation(Page):
    form_model = 'player'
    form_fields = ['occupation_1', 'time_occupation_1', 'occupation_2', 'time_occupation_2', 'occupation_3', 'time_occupation_3', 'time_init_occupation']

    def is_displayed(self):
        return self.round_number == 1

class subjects(Page):
    form_model = 'player'
    form_fields = ['l_mat','l_art','l_soc','l_spa','l_sci','l_tec','p_sci','p_tec','p_spa','p_soc','p_art','p_mat']

    def is_displayed(self):
        return self.round_number == 1

class careers(Page):
    form_model = 'player'
    form_fields = ['career1','career2','career3','career4','career5','career6','career7','career8','career9','career10','career11','career12','career13','career14','career15','career16','career17','career18','career19','career20']

    def is_displayed(self):
        return self.round_number == 1

class time(Page):
    form_model = 'player'
    form_fields = ['p_risk','p_time','p_time2']
    def is_displayed(self):
        return self.round_number == 1

class questions1(Page):
    form_model = 'player'
    form_fields = ['p_vocational', 'p_sex', 'p_age', 'p_colombian', 'p_urban', 'p_tech', 'p_desertion', 'p_years', 'p_internet', 'p_lavadora' ]

    def is_displayed(self):
        return self.round_number == 1
 

class questions2(Page):
    form_model = 'player'
    form_fields = [ 'p_care', 'p_family', 'p_siblings', 'p_rooms', 'p_estrato', 'p_pension2', 'edu_father', 'edu_mother', 'career_father', 'career_mother','ocu_mother', 'ocu_father'] 
    def is_displayed(self):
        return self.round_number == 1

class thanks(Page):
    form_model = 'player'
    form_fields = [ 'comments'] 

page_sequence = [beliefs, efficacy, group, saber11, explicit, subjects, occupation, occupation2, careers, education, time, questions1, questions2, thanks]