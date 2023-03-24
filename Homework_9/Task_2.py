# Реализовать дескрипторы для любых двух классов

class IsStr:

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("Значение должно быть строкой")
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Worker:
    name = IsStr()
    surname = IsStr()
    position = IsStr()
    _income = {'wage': 0, 'bonus': 0}

    def __init__(self, input_name, input_surname, input_position, input_wage,
                 input_bonus):
        self.name = input_name
        self.surname = input_surname
        self.position = input_position
        self._income['wage'] = input_wage
        self._income['bonus'] = input_bonus

    def __str__(self):
        return f"Worker: {self.name} {self.surname} " \
               f"\nincome: " \
               f"{int(self._income['wage']) + int(self._income['bonus'])}"


first_worker = Worker('Иван', 'Сидоров', 'Разработчик', 100000, 40000)
second_worker = Worker('Андрей', 1234567890, 'Аналитик', 90000, 30000)

print(Worker.__str__(first_worker))
print(Worker.__str__(second_worker))

