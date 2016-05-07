

class Fitness(object):
    def __init__(self, decoder_func, goal):
        self.decoder = decoder_func
        self.goal = goal

    def fitness_score(self, chrom):
        """
        Calculates distance of chromosome from goal
        :param chrom: Chromosome to calculate fitness score
        :return: Fitness score of given chromosome in values > 0. Return 0 if perfect (solution found)
        """
        if self.goal == self.decoder(chrom):
            return 0
        return 1.0 / (abs(self.goal - self.decoder(chrom)))
