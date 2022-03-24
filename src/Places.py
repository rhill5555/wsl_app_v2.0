########################################################################################################################
# Places Class Hierarchy
# FileName: Places.py

########################################################################################################################
# Select Continents
from mysql.connector import MySQLConnection

import gui


class Continent:
    @staticmethod
    def continent(mysql_connection: MySQLConnection):
        mycursor = mysql_connection.cursor()
        mycursor.execute("select continent from wsl.continents")
        result = mycursor.fetchall()

        continent_list = []
        for x in result:
            continent_list.append(x[0])

        return sorted(continent_list, key=str.lower)


# Countries from Continents
class Country(Continent):
    @staticmethod
    def country(mysql_connection: MySQLConnection, continent: str):
        mycursor = mysql_connection.cursor()
        mycursor.execute(f"""select country
                            from wsl.countries countries
                            join wsl.continents continents
                                on countries.continent_id = continents.id
                            where continent = '{continent}'
                        """)

        result = mycursor.fetchall()

        country_list = []
        for x in result:
            country_list.append(x[0])

        return sorted(country_list, key=str.lower)

# Regions from Country
class Region(Country):
    @staticmethod
    def region(mysql_connection: MySQLConnection, country: str):
        mycursor = mysql_connection.cursor()
        mycursor.execute(f"""select region
                            from wsl.regions regions
                            join wsl.countries countries
                                on regions.country_id = countries.id
                            where country = '{country}'
                        """)

        result = mycursor.fetchall()

        region_list = []
        for x in result:
            region_list.append(x[0])

        return sorted(region_list, key=str.lower)


# Cities from Region
# class City(Region):
#     def __init__(self, region: str, country: str, continent: str):
#         Country.__init__(self, continent=continent)
#         Region.__init__(self, country=country)
#         self.region = region
#
#     # return cities that are in selected region
#     def select_city(self):
#         # Select cities from wsl.regions
#         pass
#
#
# # Breaks from region
# class Break(Region):
#     def __init__(self, region: str, country: str, continent: str):
#         Country.__init__(self, continent=continent)
#         Region.__init__(self, country=country)
#         self.region = region
#
#     # return breaks that are in select region
#     def select_break(self):
#         # Select break from wsl.regions
#         pass