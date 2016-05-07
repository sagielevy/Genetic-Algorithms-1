import Simulator
import operator
import logging

gene_pool = {"0000": 0, "0001": 1, "0010": 2, "0011": 3, "0100": 4, "0101": 5, "0110": 6,
             "0111": 7, "1000": 8, "1001": 9, "1010": "+", "1011": "-", "1100": "*", "1101": "/"}
ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.div}
chrom_size = 20
goal = 1000
members = 500


def decode_fitness(chrom):
    valid_first_int = None
    valid_op = None

    for i in xrange(chrom_size):
        curr_bin = chrom[i * 4:(i * 4) + 4]
        curr_val = int(curr_bin, 2)

        if valid_first_int is None and curr_val <= 9:
            valid_first_int = gene_pool[curr_bin]

        elif valid_first_int is not None and valid_op is None and 10 <= curr_val <= 13:
            valid_op = gene_pool[curr_bin]

        elif valid_first_int is not None and valid_op is not None and curr_val <= 9 \
                and not (valid_op == "/" and gene_pool[curr_bin] == 0):
            valid_first_int = ops[valid_op](valid_first_int, gene_pool[curr_bin])
            valid_op = None

    return valid_first_int


def decode_display(chrom):
    result = ""

    for i in xrange(chrom_size):
        if chrom[i * 4:(i * 4) + 4] in gene_pool:
            result += str(gene_pool[chrom[i * 4:(i * 4) + 4]]) + " "
        else:
            result += "n/a "

    return result


def validate(chrom):
    pass

if __name__ == "__main__":
    Simulator.Simulator(members, decode_fitness, goal, gene_pool, chrom_size, generation_lim=500,
                        validate_chrom=validate, decoder_display=decode_display,
                        log_level=logging.DEBUG, mutation_rate=0.01).simulate()
