class Profesor:
    def __init__(self, nombre_profesor, email_profesor):
        self.__nombre__ = nombre_profesor
        self.__email__ = email_profesor

    def dame_tu_nombre(self):
        return self.__nombre__ 

class Alumno:
    def __init__(self, nombre_alumno, mail_alumno):
        self.__nombre__ = nombre_alumno
        self.__email__ = mail_alumno
        self.__inasistencias__ = 0
        self.__dieta__ = ""
        self.__mentor__ = None

    def mentoria(self, profesor):
        self.__mentor__ = profesor
    

    def falta(self):
        self.__inasistencias__  += 1

    def esta_libre(self):
        if self.__inasistencias__>= 5:
            return "ESTAS LIBRE"
        else:
            return "OK"
        
    def elegir_dieta(self,la_dieta):
        self.__dieta__ = la_dieta

    def es_vegano(self):
        self.__dieta__ = "es vegano"

profe_Elio = Profesor("Elio", "elio@gmail.com")
profe_Gabi = Profesor("Gabriel", "gabriel@gmail.com")

""" print (profe_Elio.dame_tu_nombre())
print (profe_Gabi.dame_tu_nombre()) """

alumno_Zowi = Alumno("Zoe", "zoe@gmail.com")
alumno_Carli = Alumno("Carla", "carla@gmail.com")

alumno_Carli.falta()
alumno_Carli.falta()
alumno_Carli.falta()
alumno_Carli.falta()
alumno_Carli.falta()
alumno_Carli.falta()

print(profe_Gabi.__nombre__)
print(profe_Elio.__nombre__)
print(alumno_Carli.__email__)
print(profe_Gabi)
print(alumno_Zowi.__inasistencias__)
print (alumno_Carli.__inasistencias__)
print (alumno_Carli.esta_libre())

alumno_Zowi.elegir_dieta("vegetariana")
print(alumno_Zowi.__dieta__)

alumno_Carli.mentoria(profe_Gabi)
print(alumno_Carli.__mentor__)

#def __unit__ (self)
#self.__atributo__ = 0
#¿como creo un objeto?- objeto = MiClase(par1, par2)[objeto]
