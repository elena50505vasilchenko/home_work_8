class DivisionByNull:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    @staticmethod
    def divide_by_null(num_1, num_2):
        try:
            return num_1 / num_2
        except:
            return f"На ноль делить нельзя!"


div = DivisionByNull(36, 0)
print(DivisionByNull.divide_by_null(36, 0))
print(DivisionByNull.divide_by_null(36, 2))
print(div.divide_by_null(80, 0))
