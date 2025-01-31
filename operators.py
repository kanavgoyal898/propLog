from propLog.sentence import Sentence
from propLog.sentence import Symbol

class NOT(Sentence):

    def __init__(self, operand):
        Sentence.validate(operand)
        self.operand = operand

    def __eq__(self, other):
        return isinstance(other, NOT) and self.operand == other.operand
    
    def __hash__(self):
        return hash(("not", hash(self.operand)))
    
    def __repr__(self):
        return f"NOT({self.operand})"
    
    def evaluate(self, model):
        return not self.operand.evaluate(model)
    
    def formula(self):
        return "¬" + Sentence.parenthesize(self.operand.formula())
    
    def symbols(self):
        return self.operand.symbols()
    
class AND(Sentence):

    def __init__(self, *conjuncts):
        for conjunct in conjuncts:
            Sentence.validate(conjunct)
        self.conjuncts = list(conjuncts)

    def __eq__(self, other):
        return isinstance(other, AND) and self.conjuncts == other.conjuncts
    
    def __hash__(self):
        return hash(("and", tuple(hash(conjunct) for conjunct in self.conjuncts)))
    
    def __repr__(self):
        conjunctions = ", ".join(str(conjunct) for conjunct in self.conjuncts)
        return f"AND({conjunctions})"
    
    def add(self, conjunct):
        Sentence.validate(conjunct)
        self.conjuncts.append(conjunct)

    def evaluate(self, model):
        return all(conjunct.evaluate(model) for conjunct in self.conjuncts)
    
    def formula(self):
        if len(self.conjuncts) == 1:
            return self.conjuncts[0].formula()
        return " ∧ ".join([Sentence.parenthesize(conjunct.formula()) for conjunct in self.conjuncts])
    
    def symbols(self):
        return set.union(*[conjunct.symbols() for conjunct in self.conjuncts])
    
class OR(Sentence):

    def __init__(self, *disjuncts):
        for disjunct in disjuncts:
            Sentence.validate(disjunct)
        self.disjuncts = list(disjuncts)

    def __eq__(self, other):
        return isinstance(other, OR) and self.disjuncts == other.disjuncts
    
    def __hash__(self):
        return hash("or", tuple(hash(disjunct) for disjunct in self.disjuncts))
    
    def __repr__(self):
        disjuncts = ", ".join(str(disjunct) for disjunct in self.disjuncts)
        return f"OR({disjuncts})"
    
    def evaluate(self, model):
        return any(disjunct.evaluate(model) for disjunct in self.disjuncts)
    
    def formula(self):
        if len(self.disjuncts) == 1:
            return self.disjuncts[0].formula()
        return " ∨ ".join([Sentence.parenthesize(disjunct.formula()) for disjunct in self.disjuncts])
    
    def symbols(self):
        return set.union(*[disjunct.symbols() for disjunct in self.disjuncts])
    
class IMPLIES(Sentence):

    def __init__(self, antecedent, consequent):
        Sentence.validate(antecedent)
        Sentence.validate(consequent)
        self.antecedent = antecedent
        self.consequent = consequent

    def __eq__(self, other):
        return isinstance(other, IMPLIES) and self.antecedent == other.antecedent and self.consequent == other.consequent
    
    def __hash__(self):
        return hash(("implies", hash(self.antecedent), hash(self.consequent)))
    
    def __repr__(self):
        return f"IMPLIES({self.antecedent}, {self.consequent})"
    
    def evaluate(self, model):
        return (not self.antecedent.evaluate(model)) or (self.consequent.evaluate(model))
    
    def formula(self):
        antecedent = Sentence.parenthesize(self.antecedent.formula())
        consequent = Sentence.parenthesize(self.consequent.formula())
        return f"{antecedent} → {consequent}"
    
    def symbols(self):
        return set.union(self.antecedent.symbols(), self.consequent.symbols())
    
class IFF(Sentence):
    
    def __init__(self, left, right):
        Sentence.validate(left)
        Sentence.validate(right)
        self.left = left
        self.right = right

    def __eq__(self, other):
        return isinstance(other, IFF) and self.left == other.left and self.right == other.right
    
    def __hash__(self):
        return hash(("iff", hash(self.left), hash(self.right)))
    
    def __repr__(self):
        return f"IFF({self.left}, {self.right})"
    
    def evaluate(self, model):
        return (self.left.evaluate(model) and self.right.evaluate(model)) or (not self.left.evaluate(model) and not self.right.evaluate(model))
    
    def formula(self):
        return f"{self.left.formula()} ↔ {self.right.formula()}"
    
    def symbols(self):
        return set.union(self.left.symbols(), self.right.symbols())

    
