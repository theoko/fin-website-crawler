class CompoundAverage:
    sum = 0.0
    total = 0

    @staticmethod
    def add(amount):
        CompoundAverage.sum = CompoundAverage.sum + amount
        CompoundAverage.total = CompoundAverage.total + 1

    @staticmethod
    def get_average():
        if CompoundAverage.total != 0:
            return CompoundAverage.sum / CompoundAverage.total
        else:
            return 0
