class BNote:

    def __init__(self, qty, bn_nominal):
        self.qty = qty
        self.bn_nominal = bn_nominal

    def __str__(self):
        return f'{self.qty} купюр по {self.bn_nominal} руб.'
