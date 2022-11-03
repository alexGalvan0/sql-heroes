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
    execute_query(query, (hero_name,))


def updateHero():
    heroName = input('Hero name to Update: ')
    updateValue = input(f'What do you want to update name to? ')

    query = """
    UPDATE heroes
    SET name = %s
    WHERE name = %s
    """
    params = (updateValue, heroName)


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
    data = execute_query(query, params).fetchall()
    pp(data)



def getHeroAbilities():
    heroId  = input('What is your Id? ')
    query = """
        SELECT 
        ability_types.name,
        abilities.hero_id
        WHERE 

        FROM ability_types
        JOIN abilities ON abilities.ability_type_id = ability_types.id   
    """
    params = (1,)
    pp(list(execute_query(query)))

def getAllHeroes():
    query = """
    SELECT 
        name
    FROM 
        heroes
    """
    data = execute_query(query).fetchall()
    pp(data)


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
        getProfile()

    if step1 == 'Login':
        getProfile()
    setep2 = input('What next? (get Heroes, Delete Profile, get abilities) ')
    if setep2 == 'get Heroes':
        getAllHeroes()
    elif setep2 == 'Delete Profile':
        deleteHero()
    elif setep2 == 'get abilities':
        getHeroAbilities()
    else:
        pp('that is not an optionLogin')
start()
