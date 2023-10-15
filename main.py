import uuid

from class_bank import Bank
from class_banknote import Note
from class_cell import Cell
from class_mark import Mark

print("Привет! Это Банк 'Тысяча ячеек'! Рады приветствовать вас!")

bank = Bank()

while True:
    access = input("Если вы хотите получить доступ к существующей ячейке, нажмите 'y'\n"
                   "Если вы хотите создать новую ячейку, нажмите 'c'\n"
                   "Если вы хотите завершить работу программы, нажмите 'n'\n")
    if access == 'n':
        print('Приходите к нам еще!')
        break
    if access == 'c':
        cell_id = (input('Введите id для вашей новой ячейки '))
        cell = Cell(cell_id)
        bank.cell_list.append(cell)
        print('Готово! Новая ячейка создана!')
    if access == 'y':
        cell_id = input('Введите id вашей ячейки ')
        for cell in bank.cell_list:
            if cell.id == cell_id:
                print('Доступ разрешен. Ваша ячейка открыта.')
                while True:
                    choice = input("Что вы хотите положить в ячейку?\n"
                          "Если это банкноты, нажмите 'b'\n"
                          "Если это марки, нажмите 'm'\n"
                          "Если вы хотите выйти в предыдущее меню, нажмите 'n'\n")
                    if choice == 'b':
                        while True:
                            qty = int(input('Сколько банкнот вы хотели бы положить в ячейку?'))
                            bn_nominal = int(input('Введите номинал банкнот'))
                            note = Note(qty, bn_nominal)
                            cell.notes_dict[note.qty] = note.bn_nominal
                            cell.count_notes_sum()
                            print(f'Отлично! В вашей ячейке банкнот на сумму {cell.notes_sum}')
                            add_choice = input("Если вы хотите положить в ячейку еще банкноты, нажмите 'a'\n"
                                                   "Если вы хотите выйти в предыдущее меню, нажмите 'n'\n")
                            if add_choice == 'a':
                                continue
                            if add_choice == 'n':
                                break
                    if choice == 'm':
                        while True:
                            number = int(input('Сколько марок выхотели бы положить в ячейку?'))
                            for n in range(number):
                                mark_id = uuid.uuid4()
                                mark = Mark(mark_id)
                                cell.marks_list.append(mark)
                            print(f'Отлично! В вашей ячейке {len(cell.marks_list)} марок со следующими уникальными '
                                  f'номерами:')
                            for m in cell.marks_list:
                                print(m.id)
                            add_choice = input("Если вы хотите положить в ячейку еще марки, нажмите 'a'\n"
                                               "Если вы хотите выйти в предыдущее меню, нажмите 'n'\n")
                            if add_choice == 'a':
                                continue
                            if add_choice == 'n':
                                break
                    if choice == 'n':
                        break
            else:
                print('Такой ячейки не существует.')
                break


