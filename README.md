# propLog: Propositional Logic Evaluation Library

`propLog` is a Python-based implementation of propositional logic, designed to handle logical operations, model checking, and entailment. Inspired by lessons from the CS50x AI course, this project provides classes and methods to represent and evaluate logical sentences and formulas. It implements common logical operations such as NOT, AND, OR, IMPLIES, IFF, and XOR. The project supports the evaluation of logical expressions based on a model and checks if a knowledge base entails a query.

<div style="text-align: center;">
  <img src="./demo.jpg" alt="propLog" style="width: 100%;">
</div>

## Features

- **Logical Sentences**: Represents propositional sentences such as symbols and logical operations.
- **Logical Operations**: Supports operations like NOT (¬), AND (∧), OR (∨), IMPLIES (→), IFF (↔), and XOR (⊕).
- **Model Checking**: Checks if a knowledge base entails a specific query.
- **Symbol Handling**: Supports logical symbols and evaluates their truth value within a model.
- **Parenthesization**: Automatically formats logical expressions with parentheses where necessary.

## Classes and Methods

### `Model`

The `Model` class is responsible for checking whether a knowledge base entails a given query.

#### Methods:
- **`model_check(knowledge, query)`**: Checks if the knowledge base entails the query by evaluating all possible truth assignments for the symbols involved.

### `Sentence` (Base Class)

The `Sentence` class is an abstract base class for all logical sentences, providing common methods for all derived logical operations.

#### Methods:
- **`evaluate(model)`**: Evaluates the logical sentence based on the given model.
- **`formula()`**: Returns the string representation of the logical sentence.
- **`symbols()`**: Returns a set of symbols involved in the logical sentence.
- **`validate(sentence)`**: Ensures that a given sentence is a valid logical sentence.
- **`parenthesize(s)`**: Adds parentheses around a formula if necessary.

### Logical Operations

Each logical operation is implemented as a class that inherits from `Sentence`. These operations represent basic propositional logic operations, such as NOT, AND, OR, IMPLIES, IFF, and XOR.

#### `NOT`
Represents the logical negation (¬) of a sentence.
- **Methods**:
  - **`evaluate(model)`**: Evaluates the negation of the operand in the model.
  - **`formula()`**: Returns the string representation of the negation.
  - **`symbols()`**: Returns the set of symbols in the negation.

#### `AND`
Represents the logical conjunction (∧) of one or more sentences.
- **Methods**:
  - **`evaluate(model)`**: Evaluates the conjunction of all operands in the model.
  - **`formula()`**: Returns the string representation of the conjunction.
  - **`symbols()`**: Returns the set of symbols involved in the conjunction.

#### `OR`
Represents the logical disjunction (∨) of one or more sentences.
- **Methods**:
  - **`evaluate(model)`**: Evaluates the disjunction of all operands in the model.
  - **`formula()`**: Returns the string representation of the disjunction.
  - **`symbols()`**: Returns the set of symbols involved in the disjunction.

#### `IMPLIES`
Represents the logical implication (→) between two sentences.
- **Methods**:
  - **`evaluate(model)`**: Evaluates the implication in the model.
  - **`formula()`**: Returns the string representation of the implication.
  - **`symbols()`**: Returns the set of symbols involved in the implication.

#### `IFF`
Represents the logical biconditional (↔) between two sentences.
- **Methods**:
  - **`evaluate(model)`**: Evaluates the biconditional in the model.
  - **`formula()`**: Returns the string representation of the biconditional.
  - **`symbols()`**: Returns the set of symbols involved in the biconditional.

#### `XOR`
Represents the logical exclusive OR (⊕) between two sentences.
- **Methods**:
  - **`evaluate(model)`**: Evaluates the exclusive OR in the model.
  - **`formula()`**: Returns the string representation of the exclusive OR.
  - **`symbols()`**: Returns the set of symbols involved in the exclusive OR.

### `Symbol`

The `Symbol` class represents a propositional symbol (variable), which is evaluated based on a model.

#### Methods:
- **`evaluate(model)`**: Evaluates the truth value of the symbol in the given model.
- **`formula()`**: Returns the string representation of the symbol.
- **`symbols()`**: Returns a set containing the symbol itself.

## Usage Example

```python
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
```

## Requirements

- Python 3.x
- No external dependencies required.
