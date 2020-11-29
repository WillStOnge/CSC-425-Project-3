import random

class Genetic:
    __correct_code: str
    __codes: list
    __offspring: int
    __max_steps: int

    def __init__(self, start_codes: list, correct_code: str, offspring = 2, max_steps = 10):
        """ Initializes the genetic alorithm. """
        self.__correct_code = correct_code
        self.__offspring = offspring
        self.__max_steps = max_steps
        self.__codes = start_codes
    

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
            while len(offspring) < self.__offspring and j < self.__max_steps:
                j += 1
                code = self.__crossover(self.__codes[0], self.__codes[1], len(offspring))
                code = self.__mutate(code)

                if self.__fitness(code) > 5:
                    offspring.append(code)

            # Make new generation from fit offspring of the former.
            if len(offspring) > 0:
                self.__codes = offspring
        
        return self.satisfied()


    def __crossover(self, parent1, parent2, num):
        if num == 0:
            return parent1[0:int(len(parent1)/2)] + parent2[int(len(parent1)/2):len(parent2)]
        return parent2[0:int(len(parent2)/2)] + parent1[int(len(parent2)/2):len(parent1)]


    def __mutate(self, code):
        if random.randint(0, 99) < 30:
            selectMutation = random.randint(0, 2)
            if selectMutation == 0:
                if "==" in code:
                    code.replace("==", "!=")
                else:
                    code.replace("!=", "==")
            elif selectMutation == 1:
                if "<" in code:
                    code.replace("<", ">")
                else:
                    code.replace(">", "<")
            else:
                if "*2" in code:
                    code.replace("*2", "+1")
                else:
                    code.replace("+1", "*2")
        return code


    def __fitness(self, code):
        """ Fitness function for the given code. Score is returned (if -1, the code was malformed somewhere). """
        score = 0
        testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]

        # Write code to a python file.
        with open("seq_genetic_search.py", "w") as file:
            file.write(code)

        # Scores the code based on expected outputs.
        try:
            import seq_genetic_search

            if seq_genetic_search.sequentialSearch(testlist, 13) == True:
                score += 1
            if seq_genetic_search.sequentialSearch(testlist, 130) == False:
                score += 1
            if seq_genetic_search.sequentialSearch(testlist, 19) == True:
                score += 1
            if seq_genetic_search.sequentialSearch(testlist, 42) == True:
                score += 1
            if seq_genetic_search.sequentialSearch(testlist, 81) == False:
                score += 1
            if seq_genetic_search.sequentialSearch(testlist, 17) == True:
                score += 1
            if seq_genetic_search.sequentialSearch(testlist, 14) == False:
                score += 1
            if seq_genetic_search.sequentialSearch(testlist, 1) == True:
                score += 1
            if seq_genetic_search.sequentialSearch(testlist, 420) == False:
                score += 1
            if seq_genetic_search.sequentialSearch(testlist, 0) == True:
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
