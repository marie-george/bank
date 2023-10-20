import uuid

from class_bank import Bank
from class_banknote import BNote
from class_cell import Cell
from class_stamp import Stamp

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
        cell = bank.create_cell()
        bank.get_cell(cell)
    if access == 'y':
        cell_id = input('Введите id вашей ячейки ')
        if bank.check_cell(cell_id):
            while True:
                choice = input("Что вы хотите положить в ячейку?\n"
                      "Если это банкноты, нажмите 'b'\n"
                      "Если это марки, нажмите 'm'\n"
                      "Если вы хотите узнать содержимое ячейки, нажмите 'v'\n"
                      "Если вы хотите выйти в предыдущее меню, нажмите 'n'\n")
                if choice == 'b':
                    while True:
                        qty = int(input('Сколько банкнот вы хотели бы положить в ячейку?'))
                        bn_nominal = int(input('Введите номинал банкнот'))
                        cell.add_bnotes(qty, bn_nominal)
                        cell.count_notes_sum()
                        print(f'Отлично! В вашей ячейке банкнот на сумму {cell.notes_sum}, а именно:')
                        cell.get_all_bnotes()
                        add_choice = input("Если вы хотите положить в ячейку еще банкноты, нажмите 'a'\n"
                                               "Если вы хотите выйти в предыдущее меню, нажмите 'n'\n")
                        if add_choice == 'a':
                            continue
                        if add_choice == 'n':
                            break
                if choice == 'm':
                    while True:
                        number = int(input('Сколько марок выхотели бы положить в ячейку?'))
                        cell.add_list_of_stamps(number)
                        print(f'Отлично! В вашей ячейке {len(cell.stamps_list)} марок со следующими уникальными '
                              f'номерами:')
                        cell.get_all_stamps()
                        add_choice = input("Если вы хотите положить в ячейку еще марки, нажмите 'a'\n"
                                           "Если вы хотите выйти в предыдущее меню, нажмите 'n'\n")
                        if add_choice == 'a':
                            continue
                        if add_choice == 'n':
                            break
                if choice == 'v':
                    cell.get_all_valuables()
                    continue
                if choice == 'n':
                    break
        else:
            break
