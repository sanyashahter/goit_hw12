from collections import UserDict
from datetime import date
import pickle

class Field:
    def __init__(self) -> None:
        pass

class AdressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def save_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.data, file)
        print("Адресну книгу збережено на диск.")

    def load_from_file(self, filename):
        with open(filename, 'rb') as file:
            self.data = pickle.load(file)
        print("Адресну книгу відновлено з диска.")

    def search(self, query):
        results = []
        for name, record in self.data.items():
            if query.lower() in name.lower() or query in record.phone.value:
                results.append(record)
        return results

    def show_all(self):
        for name, record in self.data.items():
            print(f"{name}")
            print(f"{record}")
            print()  

    def __str__(self):
        return f'AdressBOOK = {str(self.data)}'
    
class Name(Field):
    def __init__(self, value):
        self.value = value

    # def __str__(self):
    #     return str(self.value)
      
    def __repr__(self):
        return f'Имя  === {str(self.value)}'
    
class Birthday:
    def __init__(self, birthday):
        self.birthday = birthday
    
    def to_date(self):
        date_split = self.birthday.split(".")
        a = int(date_split[0])
        b = int(date_split[1])
        c = int(date_split[2])
        return date(a, b, c)
    
    def days_to_birthday(self):
        if self.birthday is None:
            return None
        date2 = date.today()
        date_birthday = self.to_date()
        if date_birthday < date2:
            date_birthday = date(date2.year + 1, date_birthday.month, date_birthday.day)
        days_left = (date_birthday - date2).days
        return f'{days_left} '
       
class Phone(Field):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return f'Телефон = {self.value}'


class Record():                                   
    def __init__(self, name, phone, birthday = None):
        self.name = Name(name)
        self.phone = Phone(phone)
        self.birthday = Birthday(birthday)
        self.phones = []
    
    def add_phone(self, phone):
        phone = Phone(phone)
        self.phones.append(phone)
        print(f"Телефон {phone} добавлен в список телефонов")

    
    def days_to_birthday(self):  # принимаем дату в формате гггг.мм.дд
       
        if self.birthday is None:
            return None
        else:
            return self.birthday.days_to_birthday()
       
    def edit_phone(self, old_phone, new_phone):
        for i in self.phones:
            if i == old_phone:
                index = self.phones.index(old_phone)
                self.phones[index] = new_phone
                print(f"Старый номер телефона {old_phone} заменено на новый {new_phone}")

    def del_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)
        else:
            print("Такого телефона не существует")
    
    def __repr__(self):
        days_left = self.days_to_birthday()
        if days_left is None:
            return f'Данные о учетной записи: ({repr(self.name)}, {repr(self.phone)})'
        return f'Данные о учетной записи: ({repr(self.name)}, {repr(self.phone)}, до дня рождения осталось {days_left} дней)'


    # def __repr__(self):
    #     if self.birthday is None:
    #         return f'Данные о учетной записи: ({repr(self.name)}, {repr(self.phone)})'
    #     else:
    #         return f'Данные о учетной записи: ({repr(self.name)}, {repr(self.phone)}, {self.days_to_birthday()})' if self.days_to_birthday() else f'Данные о учетной записи: ({repr(self.name)}, {repr(self.phone)})'
        # return f'Данные о учетной записи :  ({repr(self.name)}, {repr(self.phone)}, до дня рождения осталось {self.days_to_birthday()}дня)'   

# res_name = str(add_classes_1(['', "Bill", "0962893087"]))
# res_phone = str(add_classes_2(['', "Bill", "0962893087"]))
# print(res_name, res_phone)
# name = Name(res_name)
# phone = Phone(res_phone)
# rec = Record(name, phone)
# ab = AdressBook()
# ab.add_record(rec)
# print(ab)

# # text = ['', "Bill", "0962893087"]

 # def __repr__(self):
    #     phone_strings = ', '.join([str(phone) for phone in self.phones])
    #     return f'Name - {str(self.name)}  Запись - {phone_strings}'
# rec = Record('Bill',"0962893087", "2023.06.24")
# print(rec)