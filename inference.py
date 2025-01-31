from sentence import *
from symbol import *
from operators import *
from model import *

people = ["Gilderoy", "Pomona", "Minerva", "Horace"]
houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

symbols = []

knowledge = AND()

for person in people:
    for house in houses:
        symbols.append(Symbol(f"{person}{house}"))

# Each person belongs to a house.
for person in people:
    knowledge.add(OR(
        Symbol(f"{person}Gryffindor"),
        Symbol(f"{person}Hufflepuff"),
        Symbol(f"{person}Ravenclaw"),
        Symbol(f"{person}Slytherin")
    ))

# Only one house per person.
for person in people:
    for h1 in houses:
        for h2 in houses:
            if h1 != h2:
                knowledge.add(
                    IMPLIES(Symbol(f"{person}{h1}"), NOT(Symbol(f"{person}{h2}")))
                )

# Only one person per house.
for house in houses:
    for p1 in people:
        for p2 in people:
            if p1 != p2:
                knowledge.add(
                    IMPLIES(Symbol(f"{p1}{house}"), NOT(Symbol(f"{p2}{house}")))
                )

knowledge.add(
    OR(Symbol("GilderoyGryffindor"), Symbol("GilderoyRavenclaw"))
)

knowledge.add(
    OR(Symbol("PomonaSlytherin"))
)

knowledge.add(
    Symbol("MinervaGryffindor")
)

model = Model()

print("KNOWLEDGE BASE:")
print(knowledge.formula())

print("\n")

print("INFERENCE: ")
for symbol in symbols:
    if model.model_check(knowledge, symbol):
        print(symbol)

