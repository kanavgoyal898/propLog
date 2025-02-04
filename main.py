from src.model import *
from src.sentence import Sentence
from src.symbol import Symbol
from src.operators import *

# Create symbols
p = Symbol("p")
q = Symbol("q")

# Create logical sentences
not_p = NOT(p)
conjunction = AND(p, q)
implication = IMPLIES(p, q)

# Create a knowledge base and a query
knowledge = AND(p, NOT(q))
query = implication

# Check if knowledge entails the query
print("Inference by Model Checking:")
result = ModelCheckInference.model_check(knowledge, query)
print(f"Does knowledge entail query? {result}")
