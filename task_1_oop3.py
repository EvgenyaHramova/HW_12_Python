# Создайте класс студента.
# - Используя дескрипторы проверяйте ФИО
# на первую заглавную букву и наличие только букв.


class Name_verification:

    def __set_name__(self, owner, name):
        self.param_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)
    
    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    # проверка на валидацию
    def validate(self, value: str):
        if value[0].isupper() == False:
        #if value.istitle() == False:
            raise ValueError(f'Слово "{value}" должно начинаться с заглавной буквы!')
        if value.isalpha() == False:
            raise ValueError(f'В данном слове не должно быть цифр')

class Student:
    surname = Name_verification()
    name = Name_verification()
    patronymic = Name_verification()

    def __init__(self, surname, name, patronymic):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic

    def __repr__(self):
        return f'Студент: фамилия - {self.surname}, имя - {self.name}, отчество - {self.patronymic})'

if __name__ == '__main__':
    student_1 = Student('Иванов', 'Иван', 'Иванович')
    print(student_1)
