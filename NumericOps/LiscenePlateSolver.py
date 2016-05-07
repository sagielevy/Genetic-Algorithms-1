import Simulator
import operator
import logging
import random

gene_pool = {"00": "+", "01": "-", "10": "*", "11": "/"}
ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.div}
members = 100


def gen_number(size=7):
    result = ""

    for i in xrange(size):
        result += str(random.randint(0, 9))

    return result


def select_goal():
    equals = None
    while equals is None:
        equals = input("Where to place equals? (by index) for {0}-{1}-{2}\n".
                       format(plate_number[:2], plate_number[2:5], plate_number[5:]))

        if not (isinstance(equals, int) and 1 <= equals <= 6):
            equals = None

    return equals


def decode_fitness_no_order(chrom):
    left_side_equation = plate_number[:equal_index]
    result = int(left_side_equation[0])

    for i in xrange(len(left_side_equation) - 1):
        # Invalid operation (division by 0), return 0 as this is an invalid chromosome
        if gene_pool[chrom[i * 2: (i * 2) + 2]] is "/" and int(left_side_equation[i + 1]) == 0:
            return 0

        result = ops[gene_pool[chrom[i * 2: (i * 2) + 2]]](result, int(left_side_equation[i + 1]))

    return result


def decode_fitness_with_order(chrom):
    result = 0
    try:
        result = eval(decode_display(chrom))
    except ZeroDivisionError:
        pass
    return result


def decode_display(chrom):
    result = plate_number[0] + " "

    for i in xrange(chrom_size):
        if chrom[i * 2:(i * 2) + 2] in gene_pool:
            result += str(gene_pool[chrom[i * 2:(i * 2) + 2]]) + " " + plate_number[i + 1] + " "

    return result


plate_number = gen_number()
equal_index = select_goal()
goal = int(plate_number[equal_index:])
chrom_size = equal_index - 1

if __name__ == "__main__":
    Simulator.Simulator(members, decode_fitness_with_order, goal, gene_pool, chrom_size, generation_lim=500,
                        decoder_display=decode_display, log_level=logging.DEBUG, mutation_rate=0.01).simulate()
