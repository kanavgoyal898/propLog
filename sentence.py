class Sentence():

    def evaluate(self, model):
        """Evaluates the logical sentence"""
        raise Exception("nothing to evaluate")
    
    def formula(self):
        """Returns string formula representing logical sentence"""
        return ""
    
    def symbols(self):
        """Returns a set of all symbols in the logical sentence"""
        return set()
    
    @classmethod
    def validate(cls, sentence):
        if not isinstance(sentence, Sentence):
            raise TypeError("must be a logical sentence")
        
    @classmethod
    def parenthesize(cls, s):
        """Parenthesizes an expression if not already parenthesized"""

        def balanced(s):
            """Checks if a string has balanced parentheses"""
            count = 0
            for c in s:
                if c == "(":
                    count += 1
                elif c == ")":
                    if count <= 0:
                        return False
                    count -= 1
            return count == 0
            
        if not len(s) or s.isalpha() or balanced(s[1:-1]):
            return s if s[0] == "(" and s[-1] == ")" else f"({s})"
        