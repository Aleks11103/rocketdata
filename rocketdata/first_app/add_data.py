from psycopg2 import OperationalError, connect


def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection

connection = create_connection('rocketdatadb', 'rocketdatauser', 'password', 'localhost', '')

employees = [
    # (fio, position, date_of_employment, salary_amount, salary_paid, chief, level)
    ('Иванов Иван Иванович', 'Директор', '2021-05-14', 4000, 200, None, 1),
    ('Степанов Иван Петрович', 'Зам. по финансам', '2018-03-03', 1200, 150, 1, 2),
    ('Ионов Максим Вадимович', 'Зам. по основной деятельности', '2015-01-15', 1300, 300, 1, 2),
    ('Федорова Ирина Геннадьевна', 'Секретарь', '2020-08-01', 900, 150, 1, 3),
    ('Лепёхин Иван Андреевич', 'senior разработчик', '2019-11-10', 2500, 500, 1, 3),
]

employees_records = ', '.join(['%s'] * len(employees))

insert_query = (
    f'INSERT INTO first_app_employee (fio, position, date_of_employment, salary_amount, salary_paid, chief_id, level) VALUES {employees_records}'
)

connection.autocommit = True
cursor = connection.cursor()
cursor.execute(insert_query, employees)