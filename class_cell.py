import uuid

from class_banknote import BNote
from class_stamp import Stamp


class Cell:

    def __init__(self, id):
        self.id = id
        self.notes_sum = 0
        self.notes_list = []
        self.stamps_list = []

    def add_bnotes(self, qty, bn_nominal):
        bnote = BNote(qty, bn_nominal)
        self.notes_list.append(bnote)

    def count_notes_sum(self):
        self.notes_sum = 0
        for bn in self.notes_list:
            s = bn.qty * bn.bn_nominal
            self.notes_sum += s
        return self.notes_sum

    def get_all_bnotes(self):
        for bn in self.notes_list:
            print(f'{bn.qty} купюр по {bn.bn_nominal} руб.')

    def create_stamp_id(self):
        id = str(uuid.uuid4())
        return id

    def add_stamps(self):
        stamp = Stamp(self.create_stamp_id())
        self.stamps_list.append(stamp)

    def add_list_of_stamps(self, number):
        for n in range(number):
            self.add_stamps()

    def get_all_stamps(self):
        for m in self.stamps_list:
            print(m)

    def get_all_valuables(self):
        print(f'В вашей ячейке находятся:\n'
              f'Банкноты на сумму {self.count_notes_sum()} руб.\n'
              f'Следующего номинала:')
        self.get_all_bnotes()
        print(f'А также марки со следующими уникальными номерами:')
        self.get_all_stamps()

