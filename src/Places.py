########################################################################################################################
# Places Class Hierarchy
# FileName: Places.py

########################################################################################################################

# Countries from Continents
class Country:
    def __init__(self, continent: str):
        self.continent = continent

    # return countries that are in selected continents
    def select_country(self):
        # Select country from wsl.continents
        pass


# Regions from Country
class Region(Country):
    def __init__(self, country: str, continent: str):
        Country.__init__(self, continent=continent)
        self.country = country

    # return regions that are in selected country
    def select_region(self):
        # Select region from wsl.countries
        pass


# Cities from Region
class City(Region):
    def __init__(self, region: str):
        self.region = region

    # return cities that are in selected region
    def select_city(self):
        # Select cities from wsl.regions
        pass


# Breaks from region
class Break(Region):
    def __init__(self, region: str):
        self.region = region

    # return breaks that are in select region
    def select_break(self):
        # Select break from wsl.regions
        pass