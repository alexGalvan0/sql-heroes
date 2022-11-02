from database.connection import execute_query
from pprint import pprint as pp





heroes = execute_query("""
SELECT name
FROM heroes
""")

pp(list(heroes))