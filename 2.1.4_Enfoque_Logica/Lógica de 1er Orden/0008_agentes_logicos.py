

from pyDatalog import pyDatalog

# Definir las reglas y hechos lógicos
pyDatalog.create_terms('padre, madre, abuelo, hermano, hermana, X, Y, Z')

+padre('Juan', 'Pedro')
+madre('María', 'Pedro')
+padre('Pedro', 'Luis')
+madre('Ana', 'Luis')

abuelo(X, Y) <= padre(X, Z) & padre(Z, Y)
hermano(X, Y) <= padre(Z, X) & padre(Z, Y) & (X != Y)
hermana(X, Y) <= madre(Z, X) & madre(Z, Y) & (X != Y)

# Consultas
print("Abuelos:")
print(abuelo(X, Y))
print()

print("Hermanos:")
print(hermano(X, Y))
print()

print("Hermanas:")
print(hermana(X, Y))
