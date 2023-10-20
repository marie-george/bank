import uuid

from class_cell import Cell


class Bank:

    def __init__(self):
        self.cell_list = []

    def add_new_cell(self, cell):
        self.cell_list.append(cell)

    def create_cell(self):
        cell = Cell(self.create_id())
        self.add_new_cell(cell)
        print('Готово! Новая ячейка создана!')
        return cell

    def create_id(self):
        id = str(uuid.uuid4())
        return id

    def get_cell(self, cell):
        id = cell.id
        print(f'Ключ к вашей ячейке {id}. Пожалуйста, запомните его!')

    def check_cell(self, id):
        for c in self.cell_list:
            if c.id == id:
                print("Доступ разрешен. Ваша ячейка открыта")
                return True
            else:
                print("Доступ запрещен!")
                return False
