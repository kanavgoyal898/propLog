from sentence import Sentence
from symbol import Symbol

class NOT(Sentence):
    """
    Represents a logical NOT operation on a given operand.
    
    Methods:
        __init__(operand): Initializes the NOT operation with the given operand.
        __eq__(other): Checks equality between two NOT objects.
        __hash__(): Returns a hash value for the NOT object.
        __repr__(): Returns a string representation of the NOT object.
        evaluate(model): Evaluates the NOT operation based on a given model.
        formula(): Returns a string representation of the formula using logical notation.
        symbols(): Returns a set of symbols involved in the operand.
    """

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
    """
    Represents a logical AND operation on multiple conjuncts.
    
    Methods:
        __init__(*conjuncts): Initializes the AND operation with one or more conjuncts.
        __eq__(other): Checks equality between two AND objects.
        __hash__(): Returns a hash value for the AND object.
        __repr__(): Returns a string representation of the AND object.
        add(conjunct): Adds a conjunct to the AND operation.
        evaluate(model): Evaluates the AND operation based on a given model.
        formula(): Returns a string representation of the formula using logical notation.
        symbols(): Returns a set of symbols involved in the conjuncts.
    """

    def __init__(self, *conjuncts):
        for conjunct in conjuncts:
            Sentence.validate(conjunct)
        self.conjuncts = list(conjuncts)

    def __eq__(self, other):
        return isinstance(other, AND) and self.conjuncts == other.conjuncts
    
    def __hash__(self):
        return hash(("and", tuple(hash(conjunct) for conjunct in self.conjuncts)))
    
    def __repr__(self):
        conjunctions = ", ".join([str(conjunct) for conjunct in self.conjuncts])
        return f"AND({conjunctions})"
    
    def add(self, conjunct):
        Sentence.validate(conjunct)
        self.conjuncts.append(conjunct)

    def evaluate(self, model):
        return all(conjunct.evaluate(model) for conjunct in self.conjuncts)
    
    def formula(self):
        if len(self.conjuncts) == 1:
            return self.conjuncts[0].formula()
        return f" ∧ ".join([Sentence.parenthesize(conjunct.formula()) for conjunct in self.conjuncts])
    
    def symbols(self):
        return set.union(*[conjunct.symbols() for conjunct in self.conjuncts])
    
class OR(Sentence):
    """
    Represents a logical OR operation on multiple disjuncts.
    
    Methods:
        __init__(*disjuncts): Initializes the OR operation with one or more disjuncts.
        __eq__(other): Checks equality between two OR objects.
        __hash__(): Returns a hash value for the OR object.
        __repr__(): Returns a string representation of the OR object.
        evaluate(model): Evaluates the OR operation based on a given model.
        formula(): Returns a string representation of the formula using logical notation.
        symbols(): Returns a set of symbols involved in the disjuncts.
    """

    def __init__(self, *disjuncts):
        for disjunct in disjuncts:
            Sentence.validate(disjunct)
        self.disjuncts = list(disjuncts)

    def __eq__(self, other):
        return isinstance(other, OR) and self.disjuncts == other.disjuncts
    
    def __hash__(self):
        return hash(("or", tuple(hash(disjunct) for disjunct in self.disjuncts)))
    
    def __repr__(self):
        disjuncts = ", ".join([str(disjunct) for disjunct in self.disjuncts])
        return f"OR({disjuncts})"
    
    def evaluate(self, model):
        return any(disjunct.evaluate(model) for disjunct in self.disjuncts)
    
    def formula(self):
        if len(self.disjuncts) == 1:
            return self.disjuncts[0].formula()
        return f" ∨ ".join([Sentence.parenthesize(disjunct.formula()) for disjunct in self.disjuncts])
    
    def symbols(self):
        return set.union(*[disjunct.symbols() for disjunct in self.disjuncts])
    
class IMPLIES(Sentence):
    """
    Represents a logical implication (→) between an antecedent and a consequent.
    
    Methods:
        __init__(antecedent, consequent): Initializes the implication with an antecedent and a consequent.
        __eq__(other): Checks equality between two IMPLIES objects.
        __hash__(): Returns a hash value for the IMPLIES object.
        __repr__(): Returns a string representation of the IMPLIES object.
        evaluate(model): Evaluates the implication based on a given model.
        formula(): Returns a string representation of the formula using logical notation.
        symbols(): Returns a set of symbols involved in the antecedent and consequent.
    """

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
    """
    Represents a logical biconditional (↔) operation between two operands.
    
    Methods:
        __init__(left, right): Initializes the IFF operation with two operands.
        __eq__(other): Checks equality between two IFF objects.
        __hash__(): Returns a hash value for the IFF object.
        __repr__(): Returns a string representation of the IFF object.
        evaluate(model): Evaluates the IFF operation based on a given model.
        formula(): Returns a string representation of the formula using logical notation.
        symbols(): Returns a set of symbols involved in both operands.
    """
    
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
    
class XOR(Sentence):
    """
    Represents a logical exclusive OR (⊕) operation between two operands.
    
    Methods:
        __init__(left, right): Initializes the XOR operation with two operands.
        __eq__(other): Checks equality between two XOR objects.
        __hash__(): Returns a hash value for the XOR object.
        __repr__(): Returns a string representation of the XOR object.
        evaluate(model): Evaluates the XOR operation based on a given model.
        formula(): Returns a string representation of the formula using logical notation.
        symbols(): Returns a set of symbols involved in both operands.
    """

    def __init__(self, left, right):
        Sentence.validate(left)
        Sentence.validate(right)
        self.left = left
        self.right = right

    def __eq__(self, other):
        return isinstance(other, XOR) and self.left == other.left and self.right == other.right
    
    def __hash__(self):
        return hash(("xor", hash(self.left), hash(self.right)))
    
    def __repr__(self):
        return f"XOR({self.left}, {self.right})"
    
    def evaluate(self, model):
        return (self.left.evaluate(model) and not self.right.evaluate(model)) or (not self.left.evaluate(model) and self.right.evaluate(model))
    
    def formula(self):
        return f"{self.left.formula()} ⊕ {self.right.formula()}"
    
    def symbols(self):
        return set.union(self.left.symbols(), self.right.symbols())
    