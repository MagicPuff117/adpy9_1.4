import datetime




def print_function():
    print('Привет')

def decorator(function_to_decorate):
    def wrapper():
        start = datetime.datetime.now()
        function_to_decorate()
        log_string = f'Дата и время запуска программы: {start}  \nНазвание программы: {function_to_decorate.__name__}'
        with open('log.txt', 'w', encoding='UTF-8') as file:
            file.write(log_string)
        print(log_string)
    return wrapper()












if __name__ == '__main__':
    decorator(print_function)

