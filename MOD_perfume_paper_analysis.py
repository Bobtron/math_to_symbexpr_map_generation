import angr
import argparse
import claripy
import logging
import os
from symbolic_execution.symbolic_expression_extraction import SymbolicExpressionExtractor
import random
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng()

logging.getLogger('angr').disabled = True
logging.getLogger('angr').propagate = False
logging.getLogger('cle').disabled = True
logging.getLogger('cle').propagate = False


def generate_constant(largest_magnitude):
    select_mag = random.randrange(largest_magnitude)
    start = 10 ** select_mag
    end = 10 ** (select_mag + 1)
    return random.randrange(start, end)


def generate_random_numbers_magnitude_equal(num_to_generate, total_magnitudes):
    return_this = []
    for i in range(num_to_generate):
        return_this.append(generate_constant(total_magnitudes))
    return return_this


def sample_one_var_function(symexpr: any, length: int):
    ast = symexpr.symex_expr
    # print(ast)
    # in_sym = symexpr.symex_to_infix()
    # # print("")
    # print("".join(in_sym))
    # print()
    return_this = []

    a_var, = symexpr.symvars
    # print(a_var)
    solver = claripy.Solver()
    for i in range(0, length):
        # solver.add(a_var == i)
        return_this.append(solver.eval(ast, 1, extra_constraints=[a_var == i])[0])
    return return_this


def main():
    elf_path = 'MOD_new_examples'
    see  = SymbolicExpressionExtractor(elf_path)
    #fib_map = (0x400878, ('fib', ('int',), 'int'))


    #short_circuit_calls=dict((fib_map,))

    short_circuit_calls = {}


    """
    extracted_symexpr = see.extract('f_001', ['a', 'b'], ['float', 'float'], 'float', simplified=False, short_circuit_calls=short_circuit_calls)
    print(extracted_symexpr)
    ast = extracted_symexpr.symex_expr
    print(ast)
    in_sym = extracted_symexpr.symex_to_infix()
    print(in_sym)
    # print("")
    print("".join(in_sym))

    # for var in extracted_symexpr.symvars:
    #     print(var)

    a_var, b_var = extracted_symexpr.symvars
    print(a_var)
    print(b_var)
    print(claripy.FPV(3.2, claripy.fp.FSORT_DOUBLE))

    solver = claripy.Solver()
    solver.add(a_var == claripy.FPV(3.2, claripy.fp.FSORT_DOUBLE))
    solver.add(b_var == claripy.FPV(1.0, claripy.fp.FSORT_DOUBLE))
    # solver.add(a_var == 3.2)
    # solver.add(b_var == 0.0)
    print(solver.constraints)

    result = solver.eval(ast, 10)

    print(result)
    # print(claripy.BVV(result, 64))
    for i in result:
        print(claripy.BVV(i, 64).raw_to_fp())
        print()
        # print(claripy.fpToFP(i, claripy.fp.FSORT_DOUBLE))
        # print(claripy.fpToFP(claripy.BVV(i, 128), claripy.fp.FSORT_DOUBLE))

    # print(solver.eval(ast, 1, extra_constraints=[var == 1.0 for var in extracted_symexpr.symvars]))
    # print(solver.eval(ast, 1, extra_constraints=[var == 2.0 for var in extracted_symexpr.symvars]))
    # print(solver.eval(ast, 1, extra_constraints=[var == 3.0 for var in extracted_symexpr.symvars]))

    print()

    return

    

    extracted_symexpr = see.extract('f_002', ['a', 'b'], ['float', 'int'], 'float', simplified=False, short_circuit_calls=short_circuit_calls)
    ast = extracted_symexpr.symex_expr
    print(ast)
    in_sym = extracted_symexpr.symex_to_infix()
    # print("")
    print("".join(in_sym))
    print()

    extracted_symexpr = see.extract('f_003', ['a', 'b', 'c'], ['float', 'float', 'float'], 'float', simplified=False, short_circuit_calls=short_circuit_calls)
    ast = extracted_symexpr.symex_expr
    print(ast)
    in_sym = extracted_symexpr.symex_to_infix()
    # print("")
    print("".join(in_sym))
    print()

    extracted_symexpr = see.extract('f_004', ['a', 'b', 'c'], ['float', 'float', 'float'], 'float', simplified=False, short_circuit_calls=short_circuit_calls)
    ast = extracted_symexpr.symex_expr
    print(ast)
    in_sym = extracted_symexpr.symex_to_infix()
    # print("")
    print("".join(in_sym))
    print()
    
    """
    
    extracted_symexpr = see.extract('f_005', ['a', 'b'], ['int', 'int'], 'int', simplified=False, short_circuit_calls=short_circuit_calls)
    ast = extracted_symexpr.symex_expr
    print(ast)
    in_sym = extracted_symexpr.symex_to_infix()
    # print("")
    print("".join(in_sym))
    print()

    """

    a_var, b_var = extracted_symexpr.symvars
    print(a_var)
    print(b_var)
    print(claripy.BVV(25, 64))

    solver = claripy.Solver()
    solver.add(a_var == 25)
    # solver.add(b_var == 6)
    print(solver.eval(ast, 10))

    rand_nums = generate_random_numbers_magnitude_equal(25, 6)
    print(rand_nums)
    for i in rand_nums:
        print(solver.eval(ast, 2, extra_constraints=[b_var == i]))

    return

    """

    # extracted_symexpr = see.extract('f_006', ['a', 'b'], ['float', 'float'], 'float', simplified=False, short_circuit_calls=short_circuit_calls)
    # ast = extracted_symexpr.symex_expr
    # print(ast)
    # in_sym = extracted_symexpr.symex_to_infix()
    # # print("")
    # print("".join(in_sym))
    # print()


# for two known functions that are similar, see if it is useful
    # assumptions, same sampling rate

    extracted_symexpr = see.extract('f_plus_001', ['a'], ['int'], 'int', simplified=False, short_circuit_calls=short_circuit_calls)
    ast = extracted_symexpr.symex_expr
    print(ast)
    in_sym = extracted_symexpr.symex_to_infix()
    # print("")
    print("".join(in_sym))
    print()

    # a_var, = extracted_symexpr.symvars
    # print(a_var)
    # solver = claripy.Solver()
    # for i in range(0, 10):
    #     # solver.add(a_var == i)
    #     print(solver.eval(ast, 1, extra_constraints=[a_var == i]))

    plus_five = sample_one_var_function(extracted_symexpr, 100)

    extracted_symexpr = see.extract('f_plus_002', ['a'], ['int'], 'int', simplified=False,
                                    short_circuit_calls=short_circuit_calls)
    ast = extracted_symexpr.symex_expr
    print(ast)
    in_sym = extracted_symexpr.symex_to_infix()
    # print("")
    print("".join(in_sym))
    print()

    plus_ten = sample_one_var_function(extracted_symexpr, 100)

    fig, (ax_plus_five, ax_plus_ten, ax_corr) = plt.subplots(3, 1, sharex=True)
    ax_plus_five.plot(plus_five)
    ax_plus_five.set_title("f(x) = x + 5")
    ax_plus_five.set_xlabel("X")
    ax_plus_ten.plot(plus_ten)
    ax_plus_ten.set_title("f(x) = x + 10")
    ax_plus_ten.set_xlabel("X")

    corr = signal.correlate(plus_five, plus_ten)
    # lags = signal.correlation_lags(len(plus_five), len(plus_ten))
    # corr /= np.max(corr)
    ax_corr.plot(corr)
    ax_corr.set_title('Cross-correlated signal')
    # ax_corr.set_xlabel('Lag')

    fig.tight_layout()
    plt.show()

    """

    sig = np.repeat([0., 1., 1., 0., 1., 0., 0., 1.], 128)
    sig_noise = sig + rng.standard_normal(len(sig))
    corr = signal.correlate(sig_noise, np.ones(128), mode='same') / 128

    clock = np.arange(64, len(sig), 128)
    fig, (ax_orig, ax_noise, ax_corr) = plt.subplots(3, 1, sharex=True)
    ax_orig.plot(sig)
    ax_orig.plot(clock, sig[clock], 'ro')
    ax_orig.set_title('Original signal')
    ax_noise.plot(sig_noise)
    ax_noise.set_title('Signal with noise')
    ax_corr.plot(corr)
    ax_corr.plot(clock, corr[clock], 'ro')
    ax_corr.axhline(0.5, ls=':')
    ax_corr.set_title('Cross-correlated with rectangular pulse')
    ax_orig.margins(0, 0.1)
    fig.tight_layout()
    plt.show()
    
    """


    extracted_symexpr = see.extract('f_piecewise_001', ['a'], ['int'], 'int', simplified=False,
                                    short_circuit_calls=short_circuit_calls)
    ast = extracted_symexpr.symex_expr
    print(ast)
    in_sym = extracted_symexpr.symex_to_infix()
    # print("")
    print("".join(in_sym))
    print()

    piecewise = sample_one_var_function(extracted_symexpr, 100)

    fig, (ax_plus_five, ax_piecewise, ax_corr) = plt.subplots(3, 1, sharex=True)
    ax_plus_five.plot(plus_five)
    ax_plus_five.set_title("f(x) = x + 5")
    ax_plus_five.set_xlabel("X")
    ax_piecewise.plot(piecewise)
    ax_piecewise.set_title("f(x) = 0 if x < 50 else x + 10")
    ax_piecewise.set_xlabel("X")

    corr = signal.correlate(plus_five, piecewise)
    # lags = signal.correlation_lags(len(plus_five), len(plus_ten))
    # corr /= np.max(corr)
    ax_corr.plot(corr)
    ax_corr.set_title('Cross-correlated signal')
    # ax_corr.set_xlabel('Lag')

    fig.tight_layout()
    plt.show()

    # extracted_symexpr = see.extract('f_new_001', ['a', 'b', 'c'], ['int', 'int', 'int'], 'int', simplified=False, short_circuit_calls=short_circuit_calls)
    # ast = extracted_symexpr.symex_expr
    # print(ast)
    # in_sym = extracted_symexpr.symex_to_infix()
    # # print("")
    # print("".join(in_sym))
    # print()

    # extracted_symexpr = see.extract('f_new_002', ['a', 'b', 'c'], ['int', 'int', 'int'], 'int', simplified=False, short_circuit_calls=short_circuit_calls)
    # ast = extracted_symexpr.symex_expr
    # print(ast)
    # in_sym = extracted_symexpr.symex_to_infix()
    # # print("")
    # print("".join(in_sym))
    # print()

    # extracted_symexpr = see.extract('f_new_003', ['a', 'b', 'c'], ['int', 'int', 'int'], 'int', simplified=False, short_circuit_calls=short_circuit_calls)
    # ast = extracted_symexpr.symex_expr
    # print(ast)
    # in_sym = extracted_symexpr.symex_to_infix()
    # # print("")
    # print("".join(in_sym))
    # print()

    #print(solver.eval(ast, 1, extra_constraints=[var == 1.0 for var in extracted_symexpr.symvars]))
    #print(ast)
    #print(extracted_symexpr.symvars)
    #print(solver.eval(ast, 1, extra_constraints=[var == claripy.ast.fp.FPV(2.0 + i, sort=claripy.FSORT_DOUBLE) for i, var in enumerate(extracted_symexpr.symvars)]))

    #print(ast.eval({var: 1 for var in extracted_symexpr.symvars}))
    #print(ast)

    # in_sym = extracted_symexpr.symex_to_infix()
    # print("")
    # print("".join(in_sym))


if __name__ == '__main__':
    main()
