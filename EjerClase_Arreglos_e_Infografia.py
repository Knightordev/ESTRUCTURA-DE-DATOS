import random
class Alumno():
    def __init__(self, name, materias):
        self.name = name

        self.materias = materias
    def get_name(self):
        return self.name
    def get_materias(self):
        return self.materias
    def get_materia(self, materia_index):
        if materia_index < len(self.materias):
            return self.materias[materia_index]
        else:
            return "No valido"
def rand_mat():
    return random.choice(range(0, 100))

def materia(num):
    materias = []
    for i in range(num):
        materia = random.choice(range(0, 100))
        materias.append(materia)
    return materias

def add_alumno(num, num_mat):
    alumnos = []
    for i in range(num):
        materias_ = materia(num_mat)
        alumnos.append(Alumno(f"Alumno{i}", materias_))
        print(f"{alumnos[i].get_name()} materias: {alumnos[i].get_materias()}")
    

add_alumno(100, 100)
