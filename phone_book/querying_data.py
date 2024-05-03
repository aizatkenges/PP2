import psycopg2

config = psycopg2.connect(
    host = 'localhost',
    database='phonebook',
    user='postgres',
    password='zzzz06'
)
current = config.cursor()#Этот инструмент позволяет нам взаимодействовать с данными в базе данных

# запрос id, name, number по отсортированному имени 
sql1 = '''
    SELECT phone_number_id, name, surname, number_value FROM phone_number ORDER BY name ASC
'''
# запрос номера телефона определенного человека 
sql2 = '''
    SELECT number_value FROM phone_number WHERE name = 'Aizat'
'''
sql3 = '''
    SELECT * FROM phone_number WHERE surname='Zholdasov'
'''
current.execute(sql3)

final = current.fetchall()
print(final)
current.close()
config.commit()
config.close()