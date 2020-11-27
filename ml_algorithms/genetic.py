class Genetic:
    __correct_code: str
    __codes: list
    __offspring: int
    __max_steps: int

    def __init__(self, start_code, correct_code, offspring = 6, max_steps = 10):
        """ Initializes the genetic alorithm. """
        self.__correct_code = correct_code
        self.__offspring = offspring
        self.__max_steps = max_steps

        self.__codes.append(start_code)
    

    def execute(self):
        """ Runs the genetic algorithm. If true is returned, the algorithm found the correct code. """
        offspring = []
        i = 0

        # Run until it finds the correct code.
        while not self.satisfied() and i < self.__max_steps:
            i += 1
            offspring = []
            j = 0

            # Generate offspring.
            while len(offspring) < self.__offspring and j < self.__steps:
                j += 1
                code = self.crossover()
                code = self.mutate(code)

                if fitness(code) > 5:
                    offspring.append(code)

            # Make new generation from fit offspring of the former.
            if len(offspring) > 0:
                codes = offspring
        
        return self.satisfied()


    def crossover(self):
        """ Cross-over instructions (e.g., change + to *). """
        return self.__codes[0].replace("True1", "True")


    def mutate(self, code):
        """ Mutate the code (e.g., change the order of the instructions in the code). """
        return code.replace("False1", "False")


    def fitness(self, code):
        """ Fitness function for the given code. Score is returned (if -1, the code was malformed somewhere). """
        score = 0
        testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]

        # Write code to a python file.
        with open("seqGeneticSearch.py", "w") as file:
            file.write(code)

        # Scores the code based on expected outputs.
        try:
            import seqGeneticSearch

            if seqGeneticSearch.sequentialSearch(testlist, 13) == True:
                score += 1
            if seqGeneticSearch.sequentialSearch(testlist, 130) == False:
                score += 1
            if seqGeneticSearch.sequentialSearch(testlist, 19) == True:
                score += 1
            if seqGeneticSearch.sequentialSearch(testlist, 42) == True:
                score += 1
            if seqGeneticSearch.sequentialSearch(testlist, 81) == False:
                score += 1
            if seqGeneticSearch.sequentialSearch(testlist, 17) == True:
                score += 1
            if seqGeneticSearch.sequentialSearch(testlist, 14) == False:
                score += 1
            if seqGeneticSearch.sequentialSearch(testlist, 1) == True:
                score += 1
            if seqGeneticSearch.sequentialSearch(testlist, 420) == False:
                score += 1
            if seqGeneticSearch.sequentialSearch(testlist, 0) == True:
                score += 1
        except:
            score = -1

        return score


    def satisfied(self):
        """ Test if the program fulfills the requirements. """
        for str_code in self.__codes:
            if str_code == self.__correct_code:
                return True
        return False
