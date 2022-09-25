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

class selfefficacy(Page):
    form_model = 'player'
    form_fields = ['efficacy1','check_slider_efficacy1','efficacy2','check_slider_efficacy2','efficacy3','check_slider_efficacy3','efficacy4','check_slider_efficacy4']

    def is_displayed(self):
            return self.round_number == 1

class barriers(Page):
    form_model = 'player'
    form_fields = ['educ_barrier1','check_slider_educ_barrier1','educ_barrier2','check_slider_educ_barrier2','educ_barrier3','check_slider_educ_barrier3','educ_barrier4','check_slider_educ_barrier4','educ_barrier5','check_slider_educ_barrier5','educ_barrier6','check_slider_educ_barrier6','educ_barrier7','check_slider_educ_barrier7']

    def is_displayed(self):
            return self.round_number == 1

class income(Page):
    form_model = 'player'
    form_fields = ['educ_inc1','check_slider_educ_inc1','educ_inc2','check_slider_educ_inc2','educ_inc3','check_slider_educ_inc3','educ_inc4','check_slider_educ_inc4','educ_inc5','check_slider_educ_inc5']

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

class instructions_transitions(Page):
    pass

class instructions_icfes(Page):
    pass

class transition1(Page):
    form_model = 'player'
    form_fields = ['l_study', 'l_militar', 'l_worker', 'l_selfemployed', 'l_nonwage', 'l_nini']
    
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        order = [0, 1, 2, 3, 4, 5]
        random.shuffle(order)
        shuffle_table = []
        for i in order:
            shuffle_table.append(Constants.table_options[i])
        return {
            "shuffle_table": shuffle_table
        }


class transition2(Page):
    form_model = 'player'
    form_fields = ['m_study', 'm_militar', 'm_worker', 'm_selfemployed', 'm_nonwage', 'm_nini']
    
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        order = [0, 1, 2, 3, 4, 5]
        random.shuffle(order)
        shuffle_table = []
        for i in order:
            shuffle_table.append(Constants.table_options[i])
        return {
            "shuffle_table": shuffle_table
        }

class transition3(Page):
    form_model = 'player'
    form_fields = ['h_study', 'h_militar', 'h_worker', 'h_selfemployed', 'h_nonwage', 'h_nini']
    
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        order = [0, 1, 2, 3, 4, 5]
        random.shuffle(order)
        shuffle_table = []
        for i in order:
            shuffle_table.append(Constants.table_options[i])
        return {
            "shuffle_table": shuffle_table
        }

class questions1(Page):
    form_model = 'player'
    form_fields = ['p_vocational', 'p_preicfes', 'p_sex', 'p_age', 'p_work', 'p_hwork', 'p_wage', 'p_desertion', 'p_years' ]
    def is_displayed(self):
        return self.round_number == 1
 

class questions2(Page):
    form_model = 'player'
    form_fields = ['p_internet', 'p_tinternet', 'p_care', 'p_family', 'p_rooms', 'p_poverty', 'p_migration', 'p_health', 'p_pension2', 'ocu_mother', 'ocu_father'] 
    def is_displayed(self):
        return self.round_number == 1


class time(Page):
    form_model = 'player'
    form_fields = ['p_risk','p_time','p_time2']
    def is_displayed(self):
        return self.round_number == 1


class thanks(Page):
    pass

page_sequence = [beliefs, efficacy, saber11, explicit,occupation, occupation2,  education, questions1, questions2, thanks]

#page_sequence = [occupation2, saber11, education, selfefficacy, barriers, income, instructions_transitions]

#

#transitions = [transition1, transition2, transition3]
#random.shuffle(transitions)

#for t in transitions:
#    page_sequence.append(t)

#for t in [instructions_icfes, icfes_m1, icfes_m2, icfes_l1, icfes_l2, icfes_s1, icfes_s2, icfes_n1, icfes_n2, time, questions1, questions2, thanks]:
#    page_sequence.append(t)

