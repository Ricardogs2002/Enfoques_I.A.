

# Definimos una clase para representar las reglas de la gramática
class Rule:
    def __init__(self, lhs, rhs):
        self.lhs = lhs  # El lado izquierdo de la regla es un símbolo no terminal
        self.rhs = rhs  # El lado derecho de la regla es una lista de símbolos terminales y no terminales

    def __str__(self):
        return self.lhs + " -> " + " ".join(self.rhs)

# Definimos una clase para representar la gramática
class Grammar:
    def __init__(self):
        self.rules = []  # La gramática está compuesta por una lista de reglas

    # Método para agregar una regla a la gramática
    def add_rule(self, lhs, rhs):
        self.rules.append(Rule(lhs, rhs))

    # Método para obtener las reglas que tienen un símbolo no terminal específico en el lado izquierdo
    def get_rules_for_lhs(self, lhs):
        return [rule for rule in self.rules if rule.lhs == lhs]

# Definimos la gramática causal definida
def define_causal_grammar():

    # Creamos una instancia de la clase Grammar
    grammar = Grammar()

    # Agregamos las reglas de la gramática
    grammar.add_rule("S", ["cause", "E", "then", "E"])
    grammar.add_rule("S", ["E"])

    grammar.add_rule("E", ["verb", "N"])
    grammar.add_rule("E", ["verb"])

    grammar.add_rule("N", ["noun"])
    grammar.add_rule("N", ["adj", "noun"])

    # Devolvemos la gramática
    return grammar

#Este programa define una gramática causal definida que se compone de dos símbolos
# no terminales: "S" y "E". Las reglas de la gramática se definen como instancias de 
# la clase Rule, que tiene un lado izquierdo (lhs) que es un símbolo no terminal y 
# un lado derecho (rhs) que es una lista de símbolos terminales y no terminales. La 
# gramática se define como una instancia de la clase Grammar, que tiene una lista de 
# reglas.


#El método add_rule se utiliza para agregar una regla a la gramática. El método
 #get_rules_for_lhs se utiliza para obtener todas las reglas que tienen un símbolo
 #no terminal específico en el lado izquierdo.

#La gramática causal definida se define en el método define_causal_grammar. En este 
#método, creamos una instancia de la clase Grammar y agregamos las reglas de la 
#gramática. Las reglas de la gramática se definen de acuerdo con las reglas de la 
#gramática causal definida, donde "S" representa una oración causal, "E" representa 
#una expresión, "verb" representa un verbo, "N" representa un sustantivo y "adj" 
#representa un adjetivo.

#Este programa proporciona una forma sencilla de definir y trabajar con gramáticas en
# Python, lo que puede ser útil en tareas de procesamiento de lenguaje natural.
