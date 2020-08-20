import datetime






def decorator(function_to_decorate):

    def wrapper(*args, **kwargs):
        print('Начало работы программы:', datetime.datetime.now())
        start = datetime.datetime.now()
        function_to_decorate(*args, **kwargs)
        log_string = f'Дата и время запуска программы: {start}  \nНазвание программы: {function_to_decorate.__name__} \nАргументы: {args} {kwargs}'
        with open('log.txt', 'w', encoding='UTF-8') as file:
            file.write(log_string)
        print(log_string)
    return wrapper


@decorator
def say(name, surname, age):
    print('Привет', name, surname, age)




say(input("Введите имя:"),input('Введите фамилию:'), input('Введите возраст:'))




