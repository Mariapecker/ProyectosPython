import copy
empleados = [
    ["Pedro",["Python","SQL"]],
    ["Manolo",["Java", "C++", "JavaScript"]],
    ["Alejandro",["HTML", "CSS", "JavaScript"]]
]

empleados1 = empleados.copy()
empleados2 = copy.deepcopy(empleados)

empleados[0][1].append("C++")

print("Copia original modificada: \n" + str(empleados) + "\n \n")
print("Copia hecha con método copy: \n" + str(empleados1) + "\n \n")
print("Copia hecha con método deepcopy: \n" + str(empleados2))
