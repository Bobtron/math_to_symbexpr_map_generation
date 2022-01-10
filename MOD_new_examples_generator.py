import random
from pptree import *

"""
Borrowed from components.py

COMMUTABLE_OPERATORS = ["+", "*"]

# Format: [(Operator Name, Operator Symbol, (Argument Type, Return Type))]

# Unary Operators
UNARY_OPERATORS = [("NegOp", "-", (None, None))]

# Binary Operators
BINARY_OPERATORS = [("AddOp", "+", (None, None)),
       ("SubOp", "-", (None, None)),
       ("MulOp", "*", (None, None)),
       ("DivOp", "/", (None, None)),
       ("ModOp", "%", ("int", "int"))]

BINARY_BIT_OPERATORS = [("AndOp", "&", ("int", "int")),
       ("OrOp", "|", ("int", "int")),
       ("XorOp", "^", ("int", "int")),
       ("LshiftOp", "<<", ("int", "int")),
       ("RshiftOp", ">>", ("int", "int"))]

# Unary Functions
# https://en.wikibooks.org/wiki/C_Programming/math.h
UNARY_FUNCTIONS = [("AbsFunc", "abs", (None, None)),
       ("AcosFunc", "acos", (None, "double")),
       ("AsinFunc", "asin", (None, "double")),
       ("AtanFunc", "atan", (None, "double")),
       ("CeilFunc", "ceil", (None, "double")),
       ("CosFunc", "cos", (None, "double")),
       ("CoshFunc", "cosh", (None, "double")),
       ("CbrtFunc", "cbrt", (None, "double")),
       ("ExpFunc", "exp", (None, "double")),
       ("FabsFunc", "fabs", (None, "double")),
       ("FloorFunc", "floor", (None, "double")),
       ("LogFunc", "log", (None, "double")),
       ("Log10Func", "log10", (None, "double")),
       ("SinFunc", "sin", (None, "double")),
       ("SinhFunc", "sinh", (None, "double")),
       ("SqrtFunc", "sqrt", (None, "double")),
       ("TanFunc", "tan", (None, "double")),
       ("TanhFunc", "tanh", (None, "double")),
       ("AcoshFunc", "acosh", (None, "double")),
       ("AsinhFunc", "asinh", (None, "double")),
       ("AtanhFunc", "atanh", (None, "double")),
       ("AtanhFunc", "atanh", (None, "double")),
       ("Exp2Func", "exp2", (None, "double")),
       ("Log2Func", "log2", (None, "double")),
       ("TgammaFunc", "tgamma", (None, "double"))]
"""


class VarWrapper(object):
    def __init__(self, name, op_sym, *children):
        self.name = name
        self.op_sym = op_sym
        self.children = children

    def __str__(self):
        return self.name

    def get_equation(self):
        if len(self.children) == 0:
            return self.op_sym
        elif len(self.children) == 1:
            return f' ( {self.op_sym}{self.children[0].get_equation()} )'
        elif len(self.children) == 2:
            return f' ( {self.children[0].get_equation()} {self.op_sym} {self.children[1].get_equation()} ) '


float_two_op = [("AddOp", "+", (None, None)),
       ("SubOp", "-", (None, None)),
       ("MulOp", "*", (None, None)),
       ("DivOp", "/", (None, None))]

float_one_op = [("AbsFunc", "abs", (None, None)),
       ("AcosFunc", "acos", (None, "double")),
       ("AsinFunc", "asin", (None, "double")),
       ("AtanFunc", "atan", (None, "double")),
       ("CeilFunc", "ceil", (None, "double")),
       ("CosFunc", "cos", (None, "double")),
       ("CoshFunc", "cosh", (None, "double")),
       ("CbrtFunc", "cbrt", (None, "double")),
       ("ExpFunc", "exp", (None, "double")),
       ("FabsFunc", "fabs", (None, "double")),
       ("FloorFunc", "floor", (None, "double")),
       ("LogFunc", "log", (None, "double")),
       ("Log10Func", "log10", (None, "double")),
       ("SinFunc", "sin", (None, "double")),
       ("SinhFunc", "sinh", (None, "double")),
       ("SqrtFunc", "sqrt", (None, "double")),
       ("TanFunc", "tan", (None, "double")),
       ("TanhFunc", "tanh", (None, "double")),
       ("AcoshFunc", "acosh", (None, "double")),
       ("AsinhFunc", "asinh", (None, "double")),
       ("AtanhFunc", "atanh", (None, "double")),
       ("AtanhFunc", "atanh", (None, "double")),
       ("Exp2Func", "exp2", (None, "double")),
       ("Log2Func", "log2", (None, "double")),
       ("TgammaFunc", "tgamma", (None, "double"))]

int_two_op = [("AddOp", "+", (None, None)),
       ("SubOp", "-", (None, None)),
       ("MulOp", "*", (None, None)),
       ("DivOp", "/", (None, None)),
       ("ModOp", "%", ("int", "int")),
       ("AndOp", "&", ("int", "int")),
       ("OrOp", "|", ("int", "int")),
       ("XorOp", "^", ("int", "int")),
       ("LshiftOp", "<<", ("int", "int")),
       ("RshiftOp", ">>", ("int", "int"))]

int_one_op = [("NegOp", "-", (None, None)),
              ("BitnegOp", "~", (None, None))]


def generate_constant(largest_magnitude):
    select_mag = random.randrange(largest_magnitude)
    start = 10 ** select_mag
    end = 10 ** (select_mag + 1)
    return random.randrange(start, end)


var_names = ['a', 'b', 'c', 'd']

MIN_ARGS = 2
MAX_ARGS = 4
MAX_CONST_MAG = 6

# Change below to floats too
binary_op = int_two_op
unary_op = int_one_op

num_args = random.randint(MIN_ARGS, MAX_ARGS)
var_wrappers = []
for i in range(num_args):
    var_wrappers.append(VarWrapper(var_names[i], var_names[i]))

while len(var_wrappers) > 1:
    args = sorted([int(random.random() * len(var_wrappers)), int(random.random() * len(var_wrappers))])
    print(args)
    if args[0] == args[1]:
        if random.random() > 0.5:
            random_op = random.choice(binary_op)
            constant_on_left = True if random.random() > 0.5 else False
            constant = generate_constant(MAX_CONST_MAG)
            new_wrapper = None
            if constant_on_left:
                new_wrapper = VarWrapper(random_op[0], random_op[1], VarWrapper(str(constant), str(constant)), var_wrappers[args[0]])
            else:
                new_wrapper = VarWrapper(random_op[0], random_op[1], var_wrappers[args[0]], VarWrapper(str(constant), str(constant)))
            var_wrappers = var_wrappers[:args[0]] + var_wrappers[args[0] + 1:]
            var_wrappers.append(new_wrapper)
        else:
            random_op = random.choice(unary_op)
            new_wrapper = VarWrapper(random_op[0], random_op[1], var_wrappers[args[0]])
            var_wrappers = var_wrappers[:args[0]] + var_wrappers[args[0] + 1:]
            var_wrappers.append(new_wrapper)
    else:
        random_op = random.choice(binary_op)
        new_wrapper = VarWrapper(random_op[0], random_op[1], var_wrappers[args[0]], var_wrappers[args[1]])
        var_wrappers = var_wrappers[:args[0]] + var_wrappers[args[0] + 1: args[1]] + var_wrappers[args[1] + 1:]
        var_wrappers.append(new_wrapper)
    # break

print_tree(var_wrappers[0], "children")
print(var_wrappers[0].get_equation())

# for i in var_wrappers:
#     print(i)
