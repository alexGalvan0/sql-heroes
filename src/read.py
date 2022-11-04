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


def deleteHero():
    hero_name = input('Hero name to delete: ')
    query = """
        DELETE FROM heroes
        WHERE name = %s
    """
    execute_query(query, (hero_name,))


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
    pp(list(execute_query(query,params)))


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
        add_hero()
        getProfile()

    if step1 == 'Login':
        getProfile(name)
    setep2 = input('What next? (get Heroes, Delete Profile, get abilities) ')
    if setep2 == 'get Heroes':
        getAllHeroes()
    elif setep2 == 'Delete Profile':
        deleteHero()
    elif setep2 == 'get abilities':
        getHeroAbilities(name)
    else:
        pp('that is not an optionLogin')


start()
