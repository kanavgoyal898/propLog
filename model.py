from sentence import Sentence
from symbol import Symbol
from operators import *

class Model():

    def __init__(self, knowledge, query):
        self.knowledge = knowledge
        self.query = query
    
        # Get all symbols in both knowledge and query
        self.symbols = set.union(knowledge.symbols(), query.symbols())
    
    def model_check(self, knowledge, query):
        """Checks if knowledge base entails query."""

        def check_model(knowledge, query, symbols, model):
            """Checks if knowledge base entails query, given a particular model."""

            # If model has an assignment for each symbol
            if not symbols:
                # If knowledge base is true in model, then query must also be true
                if knowledge.evaluate(model):
                    return query.evaluate(model)
                # If knowledge base is false in model, then query can be either true or false
                return True
            
            # Choose one of the remaining unused symbols
            symbols_ = symbols.copy()
            symbol = symbols_.pop()

            # Create a model where the symbol is true
            model_true = model.copy()
            model_true[symbol] = True

            # Create a model where the symbol is false
            model_false = model.copy()
            model_false[symbol] = False
            
            # Ensure entailment holds in both models
            return (check_model(knowledge, query, symbols_, model_true) and
                    check_model(knowledge, query, symbols_, model_false))

        # Check that knowledge entails query
        return check_model(knowledge, query, self.symbols, {})
