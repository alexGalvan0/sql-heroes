from database.connection import execute_query
from pprint import pprint as pp


def select_all():
    query = """
        SELECT * from heroes
    """

    list_of_heroes = execute_query(query).fetchall()
    for record in list_of_heroes:
        pp(record[1])


def add_hero():
    name = input('what is the Super Heroe Name? ')
    about_me = input('Super Heroe Bio: ')
    bio = input('Super Heroe bio: ')
    params = (name, about_me, bio)
    query = """ 
        INSERT INTO heroes(name,about_me,biography) VALUES(%s,%s,%s)
    """
    execute_query(query, params)

def deleteHero():
    heroId = input('Hero Id to delete: ')
    query = """
        DELETE FROM heroes
        WHERE id = %s
    """
    execute_query(query, (heroId,))




def start():
    step1 = input('What do you want to do?, (Create, Read, Update, Delete): ')
    
    if step1 == 'Create':
        add_hero()
    elif(step1 == 'Delete'):
        deleteHero()
    else:
        pp('That is not an Option')

start()
