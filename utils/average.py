class Average:
    # Compound, negative, neutral, positive
    sums = [0.0, 0.0, 0.0, 0.0]
    totals = [0, 0, 0, 0]

    @staticmethod
    def add(amount, sumPos, totalPos):
        Average.sums[sumPos] = Average.sums[sumPos] + amount
        Average.totals[totalPos] = Average.totals[totalPos] + 1

    @staticmethod
    def get_average(sumPos, totalPos):
        if Average.totals[totalPos] != 0:
            return Average.sums[sumPos] / Average.totals[totalPos]
        else:
            return 0

    @staticmethod
    def add_compound(amount):
        Average.add(amount, 0, 0)

    @staticmethod
    def get_average_compound():
        return Average.get_average(0, 0)

    @staticmethod
    def add_neg(amount):
        Average.add(amount, 1, 1)

    @staticmethod
    def get_average_neg():
        return Average.get_average(1, 1)

    @staticmethod
    def add_neu(amount):
        Average.add(amount, 2, 2)

    @staticmethod
    def get_average_neu():
        return Average.get_average(2, 2)

    @staticmethod
    def add_pos(amount):
        Average.add(amount, 3, 3)

    @staticmethod
    def get_average_pos():
        return Average.get_average(3, 3)
