

class Contact:
    def __init__(self, *args, favourite_contact=False, **kwargs: "email, social, other"):
        self.name, self.surname, self.phone_number = args
        self.favourite_contact = favourite_contact
        self.additional_info = kwargs
        self.main_info = self.name + " " + self.surname + " " + self.phone_number

    def list_additional_info(self):
        additional_info = []
        for i, f in self.additional_info.items():
            additional_info.append(f'{i}:{f}')
        return additional_info


    def __str__(self):
        sep = f'\n{" "*5}'
        return f'Имя: {self.name}\nФамилия: {self.surname}\nТелефон: {self.phone_number}' \
               f'\nВ избранных: {str(self.favourite_contact).replace("True", "да").replace("False", "нет")}' \
               f'\nДополнительная информация: {sep}{sep.join(self.list_additional_info())}'


# jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
# print(jhon)