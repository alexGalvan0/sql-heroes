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
    name = input('what is your Super Heroe Name? ')
    about_me = input('Tell me about yourself: ')
    bio = input('Tell me how you became super: ')
    params = (name, about_me, bio)
    query = """ 
        INSERT INTO heroes(name,about_me,biography) VALUES(%s,%s,%s)
    """
    execute_query(query, params)


def deleteHero():
    hero_name = input('Hero name to delete: ')
    query = """
        DELETE FROM heroes
        WHERE name = %s
    """
    execute_query(query, (heroId,))


def updateHero():
    heroId = input('Hero Id to Update: ')
    updateField = input(
        'What do you want to update? (name, about_me, biography): ')
    updateValue = input(f'What do you want to update {updateField} to? ')

    params = (updateValue, heroId)

    query = """
    UPDATE heroes
    SET name = %s
    WHERE id = %s
    """
    execute_query(query, params)


def getProfile():
    hero_name = input('What is your name? ')
    params = (hero_name,)
    query = """
    SELECT 
        name,
        biography,
        about_me
    FROM heroes
    WHERE name = %s
    """
    profile = execute_query(query, params).fetchall()
    pp(profile)


def getHeroAbilities():
    query = """
        SELECT 
        abilities.id AS ABSID,
        ability_types.name AS SUPNAME,
        abilities.hero_id HERID

        FROM ability_types
        JOIN abilities ON abilities.ability_type_id = ability_types.id
       
    """
    params = (1,)
    pp(list(execute_query(query)))



def start():
    print("""
    ___ ___  _ __ ___ (_) ___ ___ 
  / __/ _ \| '_ ` _ \| |/ __/ __|
 | (_| (_) | | | | | | | (__\__ /
  \___\___/|_| |_| |_|_|\___|___/

    """)
    step1 = input('What do you want to do?, (SignUp, Login): ')

    if step1 == 'SignUp':
        add_hero()
    if step1 == 'Login':
        getProfile()
        step2 = input('What would you like to update? (profile, abilities, friends)')
        if step2 == 'profile':
            updateHero()
        
start()
