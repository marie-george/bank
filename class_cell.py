class Cell:

    def __init__(self, id):
        self.id = id
        self.notes_sum = 0
        self.notes_dict = {}
        self.marks_list = []

    def count_notes_sum(self, qty, bn_nominal):
        self.notes_sum += qty * bn_nominal
