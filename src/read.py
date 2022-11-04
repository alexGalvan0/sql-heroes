from database.connection import execute_query
from pprint import pprint as pp


def select_all():
    query = """
        SELECT * from heroes
    """

    list_of_heroes = execute_query(query).fetchall()
    for record in list_of_heroes:
        pp(record[1])


def add_hero(name):
    about_me = input('Tell me about yourself: ')
    bio = input('Tell me how you became super: ')
    params = (name, about_me, bio)
    query = """ 
        INSERT INTO heroes(name,about_me,biography) VALUES(%s,%s,%s)
    """
    execute_query(query, params)


def deleteHero(name):

    query = """
        DELETE FROM heroes
        WHERE name = %s
    """
    execute_query(query, (name,))


def updateHero(name):
    updateValue = input(f'What do you want to update name to? ')

    query = """
    UPDATE heroes
    SET name = %s
    WHERE name = %s
    """
    params = (updateValue, name)

    execute_query(query, params)


def getProfile(name):
    name = (name,)
    query = """
    SELECT 
        name,
        biography,
        about_me
    FROM heroes
    WHERE name = %s
    """
    data = execute_query(query, name).fetchall()
    pp(data)


def getHeroAbilities(name):
    params = (name,)
    query = """
    SELECT 
    heroes.name,
    ability_types.name

    FROM heroes 
    JOIN 
        abilities ON heroes.id = abilities.hero_id
    JOIN 
        ability_types ON ability_types.id = abilities.ability_type_id

    WHERE heroes.name = %s
    """
    pp(list(execute_query(query, params)))

def addHeroAbilities(name):
    params = (name, )
    query = """
    INSERT INTO abilities(hero_id,ability_type_id)VALUES(17,5)    
    """



def getAllHeroes():
    query = """
    SELECT 
        names
    FROM
        heroes
    """
    data = execute_query(query)
    pp(data)


def start():
    print("""
    ___ ___  _ __ ___ (_) ___ ___ 
  / __/ _ \| '_ ` _ \| |/ __/ __|
 | (_| (_) | | | | | | | (__\__ /
  \___\___/|_| |_| |_|_|\___|___/

    """)
    step1 = input('What do you want to do?, (SignUp, Login): ')
    name = input('What is your name? ')

    if step1 == 'SignUp':
        add_hero(name)
        getProfile(name)

    if step1 == 'Login':
        getProfile(name)
    else:
        pp('Not an Option')

    step2 = input('What next? (profile, friendships, abilities) ')
    if step2 == 'profile':
        step3 = input('Profile Options (delete, update) ')


    if step2 == 'abilities':
        step3 = input('get, add, delete ')
        if step3 == 'get':
            getHeroAbilities(name)
        if step3 == 'add':
            addHeroAbilities(name)

    if step3 == 'delete':
        step4 = input('Do you want to delete your profile?(y,n)')
        if step4 == 'y':
            deleteHero(name)
        else:
            pass


start()
