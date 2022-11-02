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


def updateHero():
    heroId = input('Hero Id to Update: ')
    updateField = input('What do you want to update? (name, about_me, biography): ')
    updateValue = input(f'What do you want to update {updateField} to? ')

    params = (updateField,updateValue,heroId)

    query = """
        UPDATE heroes
        SET %s = %s
        WHERE id = %s
    """
    execute_query(query,params)
updateHero()



def start():
    step1 = input('What do you want to do?, (Create, Read, Update, Delete): ')

    if step1 == 'Create':
        add_hero()
    elif (step1 == 'Delete'):
        deleteHero()
    elif(step1 == 'Update'):
        updateHero()
    else:
        pp('That is not an Option')



