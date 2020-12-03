'''
Permite construir expresiones logicas,
se obtiene como resultado falso o veradero
'''
'''
AND(CONJUNCION) AND
OR(DISYUNCION) OR
NEGACION NOT
'''
'''
AND:
true and true = true
true and false = false
false and true = false
false and false = false

OR:
true or true = true
true or false = true
false or true = true
false or false = false

NOT:
Not(True) = false
Not(false) = true

PRioridad:
NOT
AND
OR
'''
a = 10
b = 12
c = 13
d = 10
print(((a > b) or (a < c)) and ((a == c) or (a >= b)))

e = 10
f = 15
g = 20
resultado = ((e < f) and (f < g))
print(resultado)
