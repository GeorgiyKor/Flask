from User import User


class Teacher(User):
    def __int__(self, name, surname):
        super().__init__(name, surname)

    def showPage(self):
        html = '<h1>Страница преподавателя</h1>'
        html += f'Фамилия: {self.surname}<br>'
        html += f'Имя: {self.name}<br>'

        return html
