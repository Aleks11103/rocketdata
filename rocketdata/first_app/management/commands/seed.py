from django.core.management.base import BaseCommand
import random
from first_app.models import Employee

class Command(BaseCommand):
    help = 'Заполнение базы случайными значениями'

    def handle(self, *args, **options):
        self.stdout.write('Заполнение данными...')
        run_seed(self)
        self.stdout.write('Выполнено')

    
def first_rec():
    if Employee.objects.count() < 1:
        e = Employee(
            fio='Иванов Иван Иванович',
            position='Директор',
            date_of_employment='2015-01-12',
            salary_amount=10000,
            salary_paid=500.25,
            chief=None,
            level=1
        )
        e.save()


def create_employee(position, salary_amount, level):
    # (fio, position, date_of_employment, salary_amount, salary_paid, chief, level)
    # Мужские фамилии
    man_last_names = ['Антонов', 'Архипов', 'Белоусов', 'Бердник', 'Беспалов', 'Виноградов', 'Городецкий', 'Гуляев', 'Дзюба', 'Евдокимов', 'Жданов', 'Карпов', 'Коваленко', 'Кудряшов', 'Кузнецов', 'Лукин', 'Маслов', 'Осипов', 'Панов', 'Петренко', 'Пономарёв', 'Сафонов', 'Селезнёв', 'Соловьёв', 'Субботин', 'Тимофеев', 'Тягай', 'Хитрук', 'Чикольба', 'Щукин']
    # Мужские имена
    man_names = ['Александр', 'Артур', 'Борис', 'Владислав', 'Геннадий', 'Георгий', 'Денис', 'Дмитрий', 'Кирилл', 'Константин', 'Макар', 'Максим', 'Марат', 'Марк', 'Мирослав', 'Михаил', 'Никита', 'Николай', 'Павел', 'Пётр', 'Ростислав', 'Руслан', 'Святослав', 'Семён', 'Тимур', 'Фёдор', 'Эдуард', 'Юлиан', 'Юрий', 'Ян', 'Яромир', 'Ярослав']
    # Мужские отчества
    man_patronymics = ['Александрович', 'Алексеевич', 'Анатолиевич', 'Артёмович', 'Богданович', 'Борисович', 'Брониславович', 'Вадимович', 'Валериевич', 'Васильевич', 'Викторович', 'Виталиевич', 'Владимирович', 'Григорьевич', 'Данилович', 'Дмитриевич', 'Евгеньевич', 'Иванович', 'Леонидович', 'Львович', 'Максимович', 'Петрович', 'Платонович', 'Романович', 'Сергеевич', 'Станиславович', 'Фёдорович', 'Эдуардович']
    # Женские фамилии
    woman_last_names = ['Афанасьева', 'Беспалова', 'Богданова', 'Бондаренко', 'Гамула', 'Голубева', 'Гребневска', 'Гусева', 'Данилова', 'Жданова', 'Жукова', 'Журавлёва', 'Зуева', 'Котовска', 'Лазарева', 'Логинова', 'Моисеева', 'Одинцова', 'Панова', 'Пахомова', 'Пономаренко', 'Предыбайло', 'Саксаганска', 'Сасько', 'Соболева', 'Сыпченко', 'Чернова', 'Шумейко', 'Юдина']
    # Женские имена
    woman_names = ['Алина', 'Алёна', 'Анастасия', 'Анна', 'Беатриса', 'Белла', 'Борислава', 'Бронислава', 'Валентина', 'Валерия', 'Виктория', 'Владлена', 'Галина', 'Евгения', 'Екатерина', 'Жанна', 'Злата', 'Зоя', 'Инесса', 'Ирина', 'Лада', 'Лариса', 'Лидия', 'Лилия', 'Людмила', 'Марина', 'Марта', 'Олеся', 'Пелагея', 'Полина', 'Рената', 'Светлана', 'София', 'Софья', 'Тамара', 'Татьяна', 'Ульяна', 'Элеонора', 'Юлия', 'Яна']
    # Женские отчества
    woman_patronymics = ['Александровна', 'Алексеевна', 'Анатолиевна', 'Артёмовна', 'Богдановна', 'Борисовна', 'Брониславовна', 'Вадимовна', 'Валериевна', 'Васильевна', 'Викторовна', 'Виталиевна', 'Владимировна', 'Григорьевна', 'Даниловна', 'Ивановна', 'Леонидовна', 'Львовна', 'Максимовна', 'Михайловна', 'Петровна', 'Романовна', 'Сергеевна', 'Станиславовна', 'Фёдоровна', 'Эдуардовна', 'Ярославовна']
    
    count = Employee.objects.count()
    if random.randint(1,2) == 1:
        fio = random.choice(man_last_names) + ' ' + random.choice(man_names) + ' ' + random.choice(man_patronymics)
    else:
        fio = random.choice(woman_last_names) + ' ' + random.choice(woman_names) + ' ' + random.choice(woman_patronymics)
    if count <= 1:
        id_chief = 1
    else:
        id_chief = random.randint(1, count)
    employee = Employee(
        fio=fio,
        position=position,
        date_of_employment=str(random.randint(2010, 2020)) + '-' + str(random.randint(1, 12)) + '-' + str(random.randint(1, 28)),
        salary_amount=salary_amount,
        salary_paid=random.randint(100, salary_amount),
        chief_id=id_chief,
        level=level
    )
    employee.save()


def run_seed(self):
    first_rec()
    for i in range(2):
        create_employee('Заместитель директора', 5000, 2)
    for i in range(5):
        create_employee('Начальник отдела', 3500, 3)
    for i in range(5):
        create_employee('Заместитель начальник отдела', 1500, 4)
    for i in range(40):
        create_employee('Работник', 800, 5)