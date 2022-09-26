from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import random

author = 'Your name here'

doc = """
Your app description
"""

class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1
    table_options = {
        0: {'label': 'Estudiando', 'name': '_study'},
        1: {'label': 'Prestando servicio militar', 'name': '_militar'},
        2: {'label': 'Trabajando por un salario para un empleador', 'name': '_worker'},
        3: {'label': 'Trabajando por cuenta propia', 'name': '_selfemployed'},
        4: {'label': 'Trabajando con familiares sin remuneración', 'name': '_nonwage'},
        5: {'label': 'No este trabajando, ni estudiando', 'name': '_nini'}
    }


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    prueba_20000 = models.StringField();
    prueba_15000 = models.StringField();
    prueba_10000 = models.StringField();
    prueba_5000 = models.StringField();

    puntaje_20000 = models.IntegerField();
    puntaje_15000 = models.IntegerField();
    puntaje_10000 = models.IntegerField();
    puntaje_5000 = models.IntegerField();

    prefer_20000 = models.IntegerField();
    prefer_15000 = models.IntegerField();
    prefer_10000 = models.IntegerField();
    prefer_5000 = models.IntegerField();

    predic_20000 = models.IntegerField();
    predic_15000 = models.IntegerField();
    predic_10000 = models.IntegerField();
    predic_5000 = models.IntegerField();

    grupo_puntaje_global = models.IntegerField();

    educ_type = models.IntegerField(
    choices=[
        [1,'Técnica'],
        [2,'Tecnológica'],
        [3,'Profesional'],
        [4,'Ninguna']
    ], label="¿Para hacer lo que más le gusta es necesaria una carrera?")

    educ_university = models.StringField(label="Escriba el nombre de la institución educativa en la que desea estudiar. También puede escribir NO SÉ")
    educ_university2 = models.StringField(label="¿Tiene una segunda opción? En caso de que sí, escriba el nombre de la institución educativa donde también le gustaría estudiar. También puede escribir NO SÉ o NO TENGO SEGUNDA OPCIÓN:")

    educsup =  models.IntegerField()
    check_slider_educsup=  models.IntegerField()



    p_vocational = models.IntegerField(
    choices=[
        [1, 'Sí'],
        [2, 'No'],
    ], label="1. ¿Ha participado antes en alguna actividad de orientación vocacional/profesional?")

    p_sex = models.IntegerField(
    choices=[
        [0, 'Hombre'],
        [1, 'Mujer'],
    ], label="2. ¿Cuál es su sexo?")

    p_age = models.IntegerField(label="3. ¿Cuántos años cumplidos tiene?")

    p_colombian = models.IntegerField(
    choices=[
        [1, 'Colombia'],
        [2, 'Otro país'],
    ], label="4. País de nacimiento:")

    p_urban = models.IntegerField(
    choices=[
        [1, 'Rural'],
        [2, 'Urbana'],
    ], label="5. Área de residencia:")

    p_tech = models.IntegerField(
    choices=[
        [1, 'Actividad física y deporte.'],
        [2, 'Administración empresarial.'],
        [3, 'Dibujo técnico.'],
        [4, 'Electricidad y electrónica.'],
        [5, 'Mecánica automotriz.'],
        [6, 'Mecánica industrial.'],
        [7, 'Sistemas.'],
        [8, 'Otra.']
    ], label="6. Seleccione la especialidad en la cual actualmente se encuentra")

    p_desertion = models.IntegerField(
    choices=[
        [1, 'No.'],
        [2, 'Sí, por dificultades académicas.'],
        [3, 'Sí, por dificultades en el colegio con compañeros, docentes o directivos.'],
        [4, 'Sí, por enfermedad.'],
        [5, 'Sí, por falta de interés en estudiar.'],
        [6, 'Sí, por razones económicas.'],
        [7, 'Sí, por razones de seguridad (nivel de violencia en la zona).'],
    ], label="7. ¿Alguna vez tuvo que suspender sus estudios?")

    p_years = models.IntegerField(
    choices=[
        [0, 'No, no he perdido ningún año.'],
        [1, 'Sí, estudié y no aprobé los exámenes.'],
        [2, 'Sí, por dificultades en el colegio con compañeros, docentes o directivos.'],
        [3, 'Sí, por enfermedad.'],
        [4, 'Sí, no me interesaban los temas.'],
        [5, 'Sí, por razones económicas.'],
        [6, 'Sí, tenía poco tiempo después del colegio para estudiar.'],
        [7, 'Sí, por razones de seguridad (nivel de violencia en la zona).']
    ], label="8. ¿Ha reprobado algún año?")

    p_internet = models.IntegerField(
    choices=[
        [0, 'No.'],
        [1, 'Sí, al menos un teléfono móvil con datos.'],
        [2, 'Sí, un computador portátil con conexión a internet.'],
        [3, 'Sí, un computador de escritorio con conexión a internet.'],
    ], label="9. ¿En su hogar cuenta con acceso o conexión a internet?")

    p_lavadora = models.IntegerField(
    choices=[
        [0, 'No.'],
        [1, 'Sí'],
    ], label="10. ¿Su hogar cuenta con una máquina lavadora de ropa?") 

    p_care = models.IntegerField(
    choices=[1, 2, 3, 4, 5],
    widget=widgets.RadioSelectHorizontal,
    label="11. De 1 (nada) a 5 (completamente), ¿qué tanto cree que ayudar en su casa dificulta su proceso de aprendizaje?")

    p_family = models.IntegerField(min=0, max=15, label="12. ¿Cuántas personas conforman el hogar donde vive actualmente, incluido usted? ")

    p_siblings = models.IntegerField(min=0, max=10, label="13. ¿Cuántas hermanas y hermanos tiene usted en total? ")

    p_rooms = models.IntegerField(min=0, max=10, label="14.	En total, ¿en cuántos cuartos duermen las personas de su hogar?")

    p_estrato = models.IntegerField(min=0, max=6, label="15.Según el recibo de energía ¿Cuál es el estrato de la vivienda en la que reside con sus padres o núcleo familiar?  (Escriba un número entre 0 y 6, donde cero es igual a sin estrato) ")

    p_pension2 = models.IntegerField(
    choices=[
        [1,'Aportando en un fondo de pensiones obligatorias'],
        [2,'Aportando en un fondo de pensiones voluntarias (por ejemplo, BEPS)'],
        [3,'Ahorrando'],
        [4,'Haciendo inversiones'],
        [5,'Pagando un seguro por su cuenta'],
        [6,'Preparando a los hijos para que puedan ayudarlos en su vejez'],
        [7,'Nada'],
    ], label="16. ¿Qué están haciendo (hicieron) sus padres para mantenerse económicamente en la vejez?")

    edu_father = models.IntegerField(
    choices=[
        [1,'Ninguno'],
        [2,'Primaria'],
        [3,'Secundaria (Bachillerato)'],
        [4,'Técnico o tecnológico'],
        [5,'Pregrado (Universitario)'],
        [6,'Posgrado (Especialización, Maestría o Doctorado)'],
        [7,'No sabe'],
    ], label="17. ¿Cuál es el nivel educativo más alto alcanzado por su padre")

    edu_mother = models.IntegerField(
    choices=[
        [1,'Ninguno'],
        [2,'Primaria'],
        [3,'Secundaria (Bachillerato)'],
        [4,'Técnico o tecnológico'],
        [5,'Pregrado (Universitario)'],
        [6,'Posgrado (Especialización, Maestría o Doctorado)'],
        [7,'No sabe'],
    ], label="18. ¿Cuál es el nivel educativo más alto alcanzado por su madre")

    career_father= models.StringField(label="19.Escriba el nombre de la profesión de su padre")

    career_mother= models.StringField(label="20.Escriba el nombre de la profesión de su madre")

    comments= models.StringField(label="Comentario")

    ocu_father = models.IntegerField(
    choices=[
        [1,'Es agricultor, pesquero o jornalero.'],
        [2,'Es dueño de un negocio grande, tiene un cargo de nivel directivo o gerencial.'],
        [3,'Es dueño de un negocio pequeño (tiene pocos empleados o no tiene, por ejemplo, tienda, papelería, etc.'],
        [4,'Es operario de máquinas o conduce vehículos (taxista, chofer).'],
        [5,'Es vendedor o trabaja en atención al público.'],
        [6,'Tiene un trabajo de tipo auxiliar administrativo (por ejemplo, secretario o asistente)'],
        [7,'Trabaja como personal de limpieza, mantenimiento, seguridad o construcción. '],
        [8,'Trabaja como profesional (por ejemplo, médico, abogado, ingeniero).'],
        [9,'Trabajadora por cuenta propia'],
        [10,'Trabaja en el hogar (por ejemplo, actividades del hogar o cuidado de personas)'],
        [11,'Trabaja por cuenta propia (por ejemplo, plomero, electricista).'],
        [12,'Pensionado.'],
        [13,'No trabaja o estudia.'],
        [14,'No sabe'],
        [15,'No responde'],
    ], label="21. Ocupación u oficio del padre")

    ocu_mother= models.IntegerField(
    choices=[
        [1,'Es agricultora, pesquera o jornalera.'],
        [2,'Es dueña de un negocio grande, tiene un cargo de nivel directivo o gerencial.'],
        [3,'Es dueña de un negocio pequeño (tiene pocos empleados o no tiene, por ejemplo, tienda, papelería, etc.'],
        [4,'Es operaria de máquinas o conduce vehículos (taxista, chofer).'],
        [5,'Es vendedora o trabaja en atención al público.'],
        [6,'Tiene un trabajo de tipo auxiliar administrativo (por ejemplo, secretario o asistente)'],
        [7,'Trabaja como personal de limpieza, mantenimiento, seguridad o construcción. '],
        [8,'Trabaja como profesional (por ejemplo, médico, abogado, ingeniero).'],
        [9,'Trabajadora por cuenta propia'],
        [10,'Trabaja en el hogar (por ejemplo, actividades del hogar o cuidado de personas)'],
        [11,'Trabaja por cuenta propia (por ejemplo, plomero, electricista).'],
        [12,'Pensionada.'],
        [13,'No trabaja o estudia.'],
        [14,'No sabe'],
        [15,'No responde'],
    ], label="22. Ocupación u oficio del madre")
    
    occupation_1 = models.StringField();
    occupation_2 = models.StringField();
    occupation_3 = models.StringField();
    time_init_occupation = models.FloatField();
    time_occupation_1 = models.FloatField();
    time_occupation_2 = models.FloatField();
    time_occupation_3 = models.FloatField();

    e_tec = models.IntegerField(choices=[[0, 'Hombre'],[1, 'Mujer']], widget=widgets.RadioSelectHorizontal, label="Informática y Tecnología")
    e_sci = models.IntegerField(choices=[[0, 'Hombre'],[1, 'Mujer']], widget=widgets.RadioSelectHorizontal, label="Naturales (Biología, Física y Química)")
    e_mat = models.IntegerField(choices=[[0, 'Hombre'],[1, 'Mujer']], widget=widgets.RadioSelectHorizontal, label="Matemáticas")
    e_spa = models.IntegerField(choices=[[0, 'Hombre'],[1, 'Mujer']], widget=widgets.RadioSelectHorizontal, label="Español")
    e_soc = models.IntegerField(choices=[[0, 'Hombre'],[1, 'Mujer']], widget=widgets.RadioSelectHorizontal, label="Sociales (Geografía, Historia y Democracia)")
    e_art = models.IntegerField(choices=[[0, 'Hombre'],[1, 'Mujer']], widget=widgets.RadioSelectHorizontal, label="Artes")

    i_sci = models.IntegerField(choices=[[0, 'Hombres'],[1, 'Mujeres']], widget=widgets.RadioSelectHorizontal, label="Ciencias Naturales")
    i_mat = models.IntegerField(choices=[[0, 'Hombres'],[1, 'Mujeres']], widget=widgets.RadioSelectHorizontal, label="Matemáticas")
    i_spa = models.IntegerField(choices=[[0, 'Hombres'],[1, 'Mujeres']], widget=widgets.RadioSelectHorizontal, label="Lectura Crítica")
    i_soc = models.IntegerField(choices=[[0, 'Hombres'],[1, 'Mujeres']], widget=widgets.RadioSelectHorizontal, label="Sociales y Ciudadanas")

    p_science1 = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Requieren muchos años de estudio."
                                       )
    p_science2 = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Son monótonos."
                                       )
    p_science3 = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Son solitarios."
                                       )
    p_science4 = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Pagan salarios altos."
                                       )
    p_science5 = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Hacen difícil el balance familia-trabajo."
                                       )
    p_gender1 = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Los hombres nacen con habilidades diferentes a las mujeres."
                                       )
    p_gender2 = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Las mujeres son mejores en matemáticas que los hombres."
                                       )    
    p_gender3 = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Los hombres son mejores científicos que las mujeres."
                                       )
    p_gender4 = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Las mujeres son mejores programadoras que los hombres."
                                       )    
    p_gender5 = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Las ingenierías son profesiones para hombres."
                                       )
    p_math1 = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Me gusta la ciencia en general."
                                       )
    p_math2 = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Me siento perdida o perdido cuando trato de resolver un problema de matemáticas."
                                       )    
    p_math3 = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name=" menudo me preocupa que tendré dificultades en la clase de matemáticas. "
                                       )
    p_math4 = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Si me esfuerzo lo suficiente, puedo hacerlo bien en las materias de ciencias."
                                       )  
    p_jobsci1 = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Algunos trabajos en ciencia son interesantes."
                                       )
    p_jobsci2 = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Podría verme trabajando en un trabajo relacionado con la ciencia más adelante en la vida."
                                       )    
    p_jobsci3 = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Las perspectivas de carrera y de ingresos juegan un papel importante en mi elección de estudio."
                                       )
    l_mat = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Matemáticas"
                                       )
    l_spa = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Español"
                                       )
    l_tec = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Informática y Tecnología"
                                       )     
    l_art = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Artes"
                                        )  
    l_sci = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Naturales (Biología, Física y Química)"
                                       )    
    l_soc = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Sociales (Geografía, Historia y Democracia)"
                                       )                                     
    p_mat = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Matemáticas"
                                       )
    p_spa = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Español"
                                       )
    p_tec = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Informática y Tecnología"
                                       )     
    p_art = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Artes"
                                        )  
    p_sci = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Naturales (Biología, Física y Química)"
                                       )    
    p_soc = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Sociales (Geografía, Historia y Democracia)"
                                       )
    career1 = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Administración, Contaduría Pública, Economía."
                                       )      
    career2 = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Agronomía, Veterinaria, Zootecnia."
                                       )      
    career3 = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Antropología, Psicología, Historia."
                                       )      
    career4 = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Artes Plásticas, Visuales y Artes Afines."
                                       )      
    career5 = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Biología, Física, Química."
                                       )      
    career6 = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Deportes, Educación Física, Recreación."
                                       )      
    career7 = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Derecho, Filosofía, Ciencia Política."
                                       ) 
    career8 = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Diseño, Publicidad."
                                       )          
    career9 = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Educación."
                                       )      
    career10 = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Estadística."
                                       )      
    career11 = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Ingeniería de Sistemas, Telemática y Afines."
                                       )      
    career12 = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Ingeniería Electrónica, Telecomunicaciones y Afines."
                                       )      
    career13 = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Ingeniería Mecánica, Industrial, Civil."
                                       )      
    career14 = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Ingeniería Química, Metalúrgica, Petróleos."
                                       ) 
    career15 = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Lenguas Modernas."
                                       )      
    career16 = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Licenciaturas."
                                       )      
    career17 = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Literatura."
                                       )      
    career18 = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Matemáticas."
                                       )      
    career19 = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Medicina, Enfermería, Bacteriología."
                                       )      
    career20 = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Odontología, Optometría, Instrumentación Quirúrgica."
                                       )
    p_risk = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="¿Qué tan dispuesto (a) está o no está usted a tomar riesgos?"
                                       )
    p_time = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="¿Qué tan dispuesto está a renunciar a algo que es beneficioso para usted en este momento a fin de obtener mayores beneficios en el futuro?"
                                       )
    p_time2 = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="¿Qué tan dispuesto está a posponer las tareas, incluso cuando sabe que sería mejor hacerlas de inmediato?"
                                       )