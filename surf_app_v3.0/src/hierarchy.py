########################################################################################################################
# Places Class Hierarchy
# FileName: hierarchy.py

########################################################################################################################
# Select Continents

import mysql
from mysql.connector import MySQLConnection
from mysql.connector.cursor import MySQLCursor
from typing import Optional, List, Callable


class CommonSQL:
    # This is a class variable for the mysql_connection.
    # This variable has a default value of None and will be assigned a value by the function below.
    MYSQL__CONNECTION: Optional[MySQLConnection] = None
    SQL_HOST: Optional[str] = None
    SQL_USER: Optional[str] = None
    SQL_PASSWORD: Optional[str] = None
    MY_CURSOR: Optional[MySQLCursor] = None

    # We need some information passed to this class when an instance is created.
    # We will give these variables default values because
    # We want to create an instance of the class but define some or all of those values later.
    def __init__(self,
                 host_name: Optional[str] = None,
                 user_name: Optional[str] = None,
                 password: Optional[str] = None):

        # Define the class variable for the host name.
        if CommonSQL.SQL_HOST is None:
            CommonSQL.SQL_HOST = host_name

        # Define the instance variable for the username.
        if CommonSQL.SQL_USER is None:
            CommonSQL.SQL_USER = user_name

        # Define the instance variable for the password.
        if CommonSQL.SQL_PASSWORD is None:
            CommonSQL.SQL_PASSWORD = password

    # This is a special function (property) that does NOT allow inputs, besides self, but REQUIRES a returned value.
    # This property will return the class variable __mysql__connection. When it is first accessed it will be None,
    # so the function will create a mysql connection and set the class variable equal to that connection.
    @property
    def mysql_connection(self) -> Optional[MySQLConnection]:

        # First we need to check if the class variable is set to None. If so we need to create the connection.
        # We can access the class variable by CommonSQL.__mysql__connection or the self operator.
        if CommonSQL.MYSQL__CONNECTION is None:

            # Now, we need to check that the following instance variables were not None.
            # If that is the case then trying to create a connection will lead to an error.
            condition_1 = CommonSQL.SQL_HOST is not None
            condition_2 = CommonSQL.SQL_USER is not None
            condition_3 = CommonSQL.SQL_PASSWORD is not None
            if condition_1 and condition_2 and condition_3:

                # We can create the mysql connection, Wrapping this in a try except to help with debugging.
                try:
                    CommonSQL.MYSQL__CONNECTION = mysql.connector.connect(
                        host=CommonSQL.SQL_HOST,
                        user=CommonSQL.SQL_USER,
                        password=CommonSQL.SQL_PASSWORD
                    )
                except Exception as e:
                    # Print the official exception info.
                    print(e)
                    print()
                    print(f"You're a fucking piece of shit idiot and can't even fucking connect to mysql correctly.")
                    # Insert a popup dialog later so that the program doesn't have to shut down.
                    raise ValueError

        # Return the value of the class variable, regardless of whether it is equal to None.
        return CommonSQL.MYSQL__CONNECTION

    @property
    def mycursor(self) -> MySQLCursor:

        if SqlCommands.MY_CURSOR is None:
            SqlCommands.MY_CURSOR = self.mysql_connection.cursor()

        return SqlCommands.MY_CURSOR

    # Return a hierarchy list and sort it alphabetically
    def return_hierarchy(self, mysql_command: str, sort_key: Callable = str.lower) -> List:

        # Define a temporary local list to store the places that are returned.
        hierarchy: List = []

        # Okay, so, lets do some smart error handling. We are going to use self.mysql_connection to return the mysql
        # connection, but right now it could return None, which will lead to a most likely fatal error that crashes the
        # app, we want to prevent this. So, first we will check if it returns None, if it does return an empty list
        # and print some useful info, to help you debug this error.

        # We are using self.mysql_connection to return the mysql connection.
        # Right now it could return None which could lead to an error that crashes the app.
        # If None will be returned then return the empty list above with a useful print statement
        if self.mysql_connection is None:
            print(f"OH NOOOO!!! Butters made a boo boo. Butters tried to return the places and the mysql_connection "
                  f"returned None. Check everything is correct with settings relating to connection to mysql.")
            return hierarchy

        # Make sure the mysql_command is a string.
        if not isinstance(mysql_command, str):
            print("DAMN IT, the mysql_command is not a string when you passed it to return_places.")
            return hierarchy

        # Wrap this next part into a try except, just in case this causes an error.
        try:
            mycursor = self.mysql_connection.cursor()
            mycursor.execute(mysql_command)
            result = mycursor.fetchall()

            # For error debugging lets print what you got that way if an error occurs after this point, we will know it
            # was due to the loop code.
            print(f"The mysql results for the command {mysql_command} is: {result}")
            print()

            # Since mysql returns it in the list of tuple format, you take care of this with a for loop.
            for item in result:

                # Append the modified version of the current item into the hierarchy list created above.
                hierarchy.append(
                    item[0]
                )

            # Sort the hierarchy list alphabetically
            return sorted(hierarchy, key=sort_key)

        except Exception as e:
            print(e)
            print()
            print("OH No Cartman was right, the red head infected your code!!!!! There was an error fetching the "
                  f"the places with the mysql_command: {mysql_command} and for the love of god, check that the sql"
                  f"syntax has not been infected with the red head gene, aka bad sql syntax. NO REALLY. HEY, HEY, Don't"
                  f"IGNORE ME, PUT THAT SHIT IN THE SQL COMMAND LINE THING AND CHECK IT, JESUS.")
            return hierarchy

    # def return_event_hier(self, mysql_command: str, sort_key: Callable = str.lower) -> List:
    #
    #     # Define a temporary local list to store the event hier that are returned.
    #     event_hier_list: List = []
    #
    #     # Okay, so, lets do some smart error handling. We are going to use self.mysql_connection to return the mysql
    #     # connection, but right now it could return None, which will lead to a most likely fatal error that crashes the
    #     # app, we want to prevent this. So, first we will check if it returns None, if it does return an empty list
    #     # and print some useful info, to help you debug this error.
    #     if self.mysql_connection is None:
    #         print(f"OH NOOOO!!! Butters made a boo boo. Butters tried to return the event types and the mysql_connection "
    #               f"returned None. Check everything is correct with settings relating to connection to mysql.")
    #         return event_hier_list
    #
    #     # Okay, another error check, because we know you like to mistype things and shit. Make sure the mysql_command
    #     # is a string. We can later add more advanced checks with regular expressions, if you want to.
    #     if not isinstance(mysql_command, str):
    #         print("DAMN IT, the mysql_command is not a string when you passed it to return_event_hier.")
    #         return event_hier_list
    #
    #     # Okay, so let's wrap this next part into a try except, just in case this causes an error.
    #     try:
    #
    #         # Define the mycursor object.
    #         mycursor = self.mysql_connection.cursor()
    #
    #         # Define the execute command inside the mycursor object, by passing in the variable, mysql_command.
    #         mycursor.execute(mysql_command)
    #
    #         # Grab the results of this.
    #         result = mycursor.fetchall()
    #
    #         # For error debugging lets print what you got that way if an error occurs after this point, we will know it
    #         # was due to the loop code.
    #         print(f"The mysql results for the command {mysql_command} is: {result}")
    #         print()
    #
    #         # Since, mysql returns it in the list of tuple format, you take care of this.
    #         for item in result:
    #
    #             # Append the modified version of the current item into the places_list list.
    #             event_hier_list.append(
    #                 str(item[0])
    #             )
    #
    #         # Okay, so now we sort the place_list, by using the sort key passed to this function. In most cases, we will
    #         # use the default value, which is a string function, str.lower. You could use lambda to pass in your own
    #         # function, or pass in a reference to another function. For now, just use str.lower. Also, notice that when
    #         # you pass a reference to a function into another function you omit the parenthesis, which you use when you
    #         # call that function. If you don't omit the parenthesis, it would pass the value returned by the function
    #         # and not a reference to use to call the function. Again, if this doesn't make complete sense, that is okay
    #         # for now, just remember the rule, if I need to pass a reference to a function to use later than no
    #         # parenthesis and if I want it to evaluate and return the value of the function then use parenthesis.
    #         return sorted(event_hier_list, key=sort_key)
    #
    #     except Exception as e:
    #         # Print the official error.
    #         print(e)
    #         # Print a blank space.
    #         print()
    #         # Print a usable error message
    #         print("OH No Cartman was right, the red head infected your code!!!!! There was an error fetching the "
    #               f"the places with the mysql_command: {mysql_command} and for the love of god, check that the sql"
    #               f"syntax has not been infected with the red head gene, aka bad sql syntax. NO REALLY. HEY, HEY, Don't"
    #               f"IGNORE ME, PUT THAT SHIT IN THE SQL COMMAND LINE THING AND CHECK IT, JESUS.")
    #         # return
    #         return event_hier_list


class SqlCommands(CommonSQL):
    def __init__(self,
                 sql_host_name: Optional[str] = None,
                 sql_user_name: Optional[str] = None,
                 sql_password: Optional[str] = None):
        # Call the constructor for the inherited class, CommonSQL. Remember this runs the constructor function in the
        # CommonSQL class and all the instance variables of that class are now instance variables of this class.
        # It also inherits all the functions.
        CommonSQL.__init__(
            self,
            host_name=sql_host_name,
            user_name=sql_user_name,
            password=sql_password
        )

    def insert_to_table(self, table: str, columns: str, fields: str):
        self.mycursor.execute(f"""INSERT INTO {table} ({columns}) VALUES ({fields});""")
        self.mysql_connection.commit()

    def select_a_column(self, table: str, column: str, col_filter: str):
        query = f"""SELECT {column} FROM {table} {col_filter}"""

        self.mycursor.execute(query)

        result = self.mycursor.fetchall()

        # Since, mysql returns it in the list of tuple format, you take care of this.
        result_list = []
        for item in result:
            # Append the modified version of the current item into the result_list list.
            result_list.append(
                item[0]
            )

        return result_list

    def update_table_record(self):
        pass


class Continent(CommonSQL):
    # We are going to assign default values of None to all the values passed into the constructor,
    # so we can create an instance of this class without having that information at the time of creating the instance.
    def __init__(self,
                 sql_host_name: Optional[str] = None,
                 sql_user_name: Optional[str] = None,
                 sql_password: Optional[str] = None,
                 selected_continent: Optional[str] = None):

        # Call the constructor for the inherited class, CommonSQL.
        CommonSQL.__init__(
            self,
            host_name=sql_host_name,
            user_name=sql_user_name,
            password=sql_password
        )

        # This is the instance variable for the selected continent, which is equal to the passed value.
        self.selected_continent: Optional[str] = selected_continent

    # Define a function to return a list of the continents to populate the combobox at startup.
    def return_continents(self) -> List:

        print("We are discovering all continents...")
        sql_command: str = "select continent from wsl.continent"

        # Use the return_hierarchy function from the CommonSQL class to return the lsit of continents
        return self.return_hierarchy(
            mysql_command=sql_command
        )

    # Define a function to return a list of the countries to populate the combobox.
    def return_countries(self) -> List:
        print(f"We are discovering all countries in {self.selected_continent}...")
        countries_list: List = []

        # Create an instance of this class.
        # We most likely will not have a value to pass for selected_continent so None is set by default.
        # If it is None or if it is not a string return the empty list.
        condition_1 = self.selected_continent is None
        condition_2 = isinstance(self.selected_continent, str)
        if condition_1 or not condition_2:
            print("Beep Boop Bot... Oh No... You were trying to return a list of countries, but the selected continent"
                  f"is None or not a string. It has a type of: {type(self.selected_continent)}")
            return countries_list

        sql_command: str = f"""select country.country
                                from wsl.country country
                                join wsl.continent continent
                                    on country.continent_id = continent.continent_id
                                where continent = '{self.selected_continent}'
                            """

        # Use the return_hierarchy function from the CommonSQL class to return the list of countries.
        return self.return_hierarchy(
            mysql_command=sql_command
        )


class Country(Continent):
    # We are going to assign default values of None to all the values passed into the constructor,
    # so we can create an instance of this class without having that information at the time of creating the instance.
    def __init__(self,
                 sql_host_name: Optional[str] = None,
                 sql_user_name: Optional[str] = None,
                 sql_password: Optional[str] = None,
                 selected_country: Optional[str] = None):

        Continent.__init__(
            self,
            sql_host_name=sql_host_name,
            sql_user_name=sql_user_name,
            sql_password=sql_password
        )

        self.selected_country: Optional[str] = selected_country

        # This is the instance variable for the country_id that we can add in later.
        self.selected_country_id: Optional[int] = None

    # Define a function to return a list of regions to place into the combobox.
    def return_regions(self) -> List:
        print(f"We are disovering all regions in {self.selected_country}...")
        regions_list: List = []

        # When an instance of this class is created we most likely will not know the value so the default will be used.
        # Check to see if that value is None and whether or not it is a string.
        condition_1 = self.selected_country is None
        condition_2 = isinstance(self.selected_country, str)
        if condition_1 or not condition_2:
            print("Beep Boop Bot... Oh No... You were trying to return a list of regions, but the selected country"
                  f"is None or not a string. It has a type of: {type(self.selected_country)}")
            return regions_list

        sql_command: str = f"""select region.region
                                from wsl.region region
                                join wsl.country country
                                    on region.country_id = country.country_id
                                where country = '{self.selected_country}'
                            """

        # Return the regions, by calling the return_places function from the CommonSQL Class.
        return self.return_hierarchy(
            mysql_command=sql_command
        )


class Region(Country):
    # We are going to assign default values of None to all the values passed into the constructor,
    # so we can create an instance of this class without having that information at the time of creating the instance.
    def __init__(self,
                 sql_host_name: Optional[str] = None,
                 sql_user_name: Optional[str] = None,
                 sql_password: Optional[str] = None,
                 selected_region: Optional[str] = None):

        Country.__init__(
            self,
            sql_host_name=sql_host_name,
            sql_user_name=sql_user_name,
            sql_password=sql_password
        )

        self.selected_region: Optional[str] = selected_region
        self.selected_region_id: Optional[int] = None

    # Define a function to return a list of the cities so they can be place in the combobox.
    def return_cities(self) -> List:
        print(f"We are discovering all the cities in {self.selected_region}...")
        cities_list: List = []

        # When an instance of this class is created we most likely will not know the value so the default will be used.
        # Check to see if that value is None and whether or not it is a string.
        condition_1 = self.selected_region is None
        condition_2 = isinstance(self.selected_region, str)
        if condition_1 or not condition_2:
            print("Beep Boop Bot... Oh No... You were trying to return a list of cities, but the selected region"
                  f"is None or not a string. It has a type of: {type(self.selected_region)}")
            return cities_list

        sql_command: str = f"""select city.city
                                from wsl.city city
                                join wsl.region region
                                    on city.region_id = region.region_id
                                where region = '{self.selected_region}'
                            """

        return self.return_hierarchy(
            mysql_command=sql_command
        )

    # Define a function to return a list of the breaks to add to the combobox.
    def return_breaks(self) -> List:
        print(f"We are discovering all breaks in {self.selected_region}...")
        breaks_list: List = []

        # When an instance of this class is created we most likely will not know the value so the default will be used.
        # Check to see if that value is None and whether or not it is a string.
        condition_1 = self.selected_region is None
        condition_2 = isinstance(self.selected_region, str)
        if condition_1 or not condition_2:
            print("Beep Boop Bot... Oh No... You were trying to return a list of cities, but the selected region"
                  f"is None or not a string. It has a type of: {type(self.selected_region)}")
            return breaks_list

        sql_command: str = f"""select break.break
                                from wsl.break break
                                join wsl.region region
                                    on break.region_id = regions.region_id
                                where region = '{self.selected_region}'
                            """

        return self.return_hierarchy(
            mysql_command=sql_command
        )

    # This function sets all the instance variables that dealing with selected locations back to None.
    def set_everything_to_none(self) -> None:
        self.selected_region = None
        self.selected_country = None
        self.selected_continent = None


########################################################################################################################


class TourYear(CommonSQL):
    # We are going to assign default values of None to all the values passed into the constructor,
    # so we can create an instance of this class without having that information at the time of creating the instance.
    def __init__(self,
                 sql_host_name: Optional[str] = None,
                 sql_user_name: Optional[str] = None,
                 sql_password: Optional[str] = None,
                 selected_tour_year: Optional[str] = None):

        # Call the constructor for the inherited class, CommonSQL.
        CommonSQL.__init__(
            self,
            host_name=sql_host_name,
            user_name=sql_user_name,
            password=sql_password
        )

        self.selected_tour_year: Optional[str] = selected_tour_year

    # Define a function to return tour years for the combobox
    def return_tour_years(self) -> List:
        print("We are returning tour years...")

        sql_command: str = "select distinct year from wsl.tour"

        return self.return_hierarchy(
            mysql_command=sql_command
        )

    # Define a function to return all possible round names since that does not depend on anything else
    def return_all_rounds(self) -> List:
        print("We are returning the list of all round names...")

        sql_command: str = "select distinct round from wsl.round"

        return self.return_hierarchy(
            mysql_command=sql_command
        )

    # Define a function to return a list of tour names for the combobox
    def return_tours(self) -> List:
        print(f"We are returning the tours from {self.selected_tour_year}...")
        tour_list: List = []

        # Create an instance of this class.
        # We most likely will not have a value to pass for selected_tour_name so None is set by default.
        # If it is None or if it is not a string return the empty list.
        condition_1 = self.selected_tour_year is None
        condition_2 = isinstance(self.selected_tour_year, str)
        if condition_1 or not condition_2:
            print("Beep Boop Bot... Oh No... You were trying to return a list of tour names, "
                  "but the selected tour year"
                  f"is None or not a string. It has a type of: {type(self.selected_tour_year)}")
            return tour_list

        sql_command: str = f"""select tour.tour_name
                                from wsl.tour tour
                                where tour.year = '{self.selected_tour_year}'
                            """

        return self.return_hierarchy(
            mysql_command=sql_command
        )


class TourName(TourYear):
    # We are going to assign default values of None to all the values passed into the constructor,
    # so we can create an instance of this class without having that information at the time of creating the instance.
    def __init__(self,
                 sql_host_name: Optional[str] = None,
                 sql_user_name: Optional[str] = None,
                 sql_password: Optional[str] = None,
                 selected_tour_name: Optional[str] = None):

        TourYear.__init__(
            self,
            sql_host_name=sql_host_name,
            sql_user_name=sql_user_name,
            sql_password=sql_password
        )

        self.selected_tour_name: Optional[str] = selected_tour_name

    # Define a function to return a list of events for the combobox.
    def return_events(self) -> List:
        print(f"We are returning the events from {self.selected_tour_name}...")
        events_list: List = []

        # Check to see if tourname is None and make sure it is a string
        condition_1 = self.selected_tour_name is None
        condition_2 = isinstance(self.selected_tour_name, str)
        if condition_1 or not condition_2:
            print("Beep Boop Bot... Oh No... You were trying to return a list of events, but the selected tourname"
                  f"is None or not a string. It has a type of: {type(self.selected_tour_name)}")
            return events_list

        sql_command: str = f"""select event.event_name
                                    from wsl.event event
                                    join wsl.tour tour
                                        on event.tour_id = tour.tour_id
                                    where tour_name = '{self.selected_tour_name}'
                                """

        return self.return_hierarchy(
            mysql_command=sql_command
        )


class EventRound(TourName):
    # We are going to assign default values of None to all the values passed into the constructor,
    # so we can create an instance of this class without having that information at the time of creating the instance.
    def __init__(self,
                 sql_host_name: Optional[str] = None,
                 sql_user_name: Optional[str] = None,
                 sql_password: Optional[str] = None,
                 selected_event: Optional[str] = None):

        TourName.__init__(
            self,
            sql_host_name=sql_host_name,
            sql_user_name=sql_user_name,
            sql_password=sql_password
        )

        self.selected_event: Optional[str] = selected_event

    # Define a function to return a list of the round for the combobox
    def return_rounds(self) -> List:
        print(f"We are returning the round in {self.selected_event} in the{self.selected_tour_name}...")
        round_list: List = []

        # Check to see if tourname is None and make sure it is a string
        condition_1 = self.selected_event is None
        condition_2 = isinstance(self.selected_event, str)
        if condition_1 or not condition_2:
            print("Beep Boop Bot... Oh No... You were trying to return a list of rounds, but the selected event"
                  f"is None or not a string. It has a type of: {type(self.selected_event)}")
            return round_list

        sql_command: str = f"""select distinct round.round
                                from wsl.event_round event_round
                                join wsl.event event
                                    on event_round.event_id = event.event_id
                                join wsl.round round
                                    on event_round.round_id = round.round_id
                                join wsl.tour tour
                                    on tour.tour_id = event.tour_id
                                where event.event_name = {self.selected_event}
                                and tour.tour_name = {self.selected_tour_name}
                            """

        # Return the cities, by calling the return_places function from the CommonSQL Class.
        return self.return_hierarchy(
            mysql_command=sql_command
        )


class Heat(EventRound):
    # This is the constructor class for the region class. We will assign default values of None to all values passed to
    # the constructor, so that we can create an instance of this class without having all information at the time of
    # of creating the instance. Values will be assigned later during use.
    def __init__(self,
                 sql_host_name: Optional[str] = None,
                 sql_user_name: Optional[str] = None,
                 sql_password: Optional[str] = None,
                 selected_heat: Optional[str] = None,
                 selected_surfer: Optional[str] = None):
        # Call the constructor for the inherited class, Country. Remember, this runs the constructor function in the
        # CommonSQL class and all the instance variables of that class are now instance variables of this class.
        # It also inherits all the functions.
        TourName.__init__(
            self,
            sql_host_name=sql_host_name,
            sql_user_name=sql_user_name,
            sql_password=sql_password
        )

        # This is the instance variable for the selected region, which is equal to the passed value.
        self.selected_heat: Optional[str] = selected_heat
        self.selected_surfer: Optional[str] = selected_surfer

        # This is the instance variable for the region_id. I assume this has something to do with the SQL key stuff.
        # Just going to set its default to None.
        self.selected_heat_id: Optional[int] = None

    # Define a function to return a list of the cities, so you can use it to place it in the
    # Combo box after the region is selected.
    def return_surfers(self) -> List:
        # Let's print that we are in this function, so it makes debugging easier.
        print("We are returning the surfers...")

        # Create a temporary list for the countries.
        surfer_list: List = []

        # Okay, since we inherited the return_places function from the CommonSQL class, we use it here to grab the
        # list of cities and return it. First, let's create a temporary string with the sql command.
        sql_command: str = f"""select surfers.surfer 
                                from wsl.heat_surfers surfers 
                                join wsl.heats heats 
                                    on surfers.heat_id = heats.id
                                join wsl.rounds rounds
                                    on heats.round_id = rounds.id
                                join wsl.events events
                                    on heats.event_id = events.id
                                join wsl.tour_type tour
                                    on events.tour_type_id = tour.id
                                where heats.heat_nbr = {self.selected_heat}
                                and rounds.round_name = '{self.selected_round}'
                                and events.event_name = '{self.selected_event}'
                                and tour.tour_name = '{self.selected_tourname}'
                            """

        # Return the cities, by calling the return_places function from the CommonSQL Class.
        return self.return_event_hier(
            mysql_command=sql_command
        )

        # # This function sets all the instance variables that dealing with selected places back to None.
        # def set_everything_to_none(self) -> None:
        #     self.selected_round = None
        #     self.selected_event = None
        #     self.selected_tour_name = None
        #     self.selected_round = None


    def return_heat_and_surfer(self) -> List:
        # Let's print that we are in this function, so it makes debugging easier.
        print("We are returning the heat and surfer...")

        # Create a temporary list for the countries.
        heat_and_surfer_list: List = []

        # Okay, since we inherited the return_places function from the CommonSQL class, we use it here to grab the
        # list of cities and return it. First, let's create a temporary string with the sql command.
        sql_command: str = f"""select surfers.id 
                                from wsl.heat_surfers surfers 
                                join wsl.heats heats 
                                    on surfers.heat_id = heats.id
                                join wsl.rounds rounds
                                    on heats.round_id = rounds.id
                                join wsl.events events
                                    on heats.event_id = events.id
                                join wsl.tour_type tour
                                    on events.tour_type_id = tour.id
                                where heats.heat_nbr = {self.selected_heat}
                                and surfers.surfer = '{self.selected_surfer}'
                                and rounds.round_name = '{self.selected_round}'
                                and events.event_name = '{self.selected_event}'
                                and tour.tour_name = '{self.selected_tourname}'
                            """

        # Return the cities, by calling the return_places function from the CommonSQL Class.
        return self.return_event_hier(
            mysql_command=sql_command
        )


    # This function sets all the instance variables that dealing with selected places back to None.
    def set_everything_to_none(self) -> None:
        self.selected_round = None
        self.selected_event = None
        self.selected_tourname = None
        self.selected_round = None




########################################################################################################################


if __name__ == '__main__':
    # Create an instance of the Continent Class
    inst_cont: Continent = Continent(
        sql_host_name="localhost",
        sql_password="#LAwaItly19",
        sql_user_name="Heather"
    )

    # Print the continents out.
    print(inst_cont.return_continents())

    # Set the selected_continent to North America
    inst_cont.selected_continent = "North America"

    # Print the countries out.
    print(inst_cont.return_countries())
    ####################################################################################################################
    # # Create an instance of the Country class
    # inst_country: Country = Country(
    #     sql_host_name="localhost",
    #     SQL_PASSWORD="#LAwaItly19",
    #     sql_user_name="Heather"
    # )
    #
    # # Print the continents out.
    # print(inst_country.return_continents())
    #
    # # Set the selected_continent to North America
    # inst_country.selected_continent = "North America"
    #
    # # Print the countries out.
    # print(inst_country.return_countries())
    #
    # # Set the selected_country to "USA".
    # inst_country.selected_country = "USA"
    #
    # # Print the regions out.
    # print(inst_country.return_regions())
    ####################################################################################################################
    # # Create an instance of the Region class
    # inst_region: Region = Region(
    #     sql_host_name="localhost",
    #     SQL_PASSWORD="#LAwaItly19",
    #     sql_user_name="Heather"
    # )
    #
    # # Print the continents out.
    # print(inst_region.return_continents())
    #
    # # Set the selected_continent to North America
    # inst_region.selected_continent = "North America"
    #
    # # Print the countries out.
    # print(inst_region.return_countries())
    #
    # # Set the selected_country to "USA".
    # inst_region.selected_country = "USA"
    #
    # # Print the regions out.
    # print(inst_region.return_regions())
    #
    # # Set the selected_region to Florida
    # inst_region.selected_region = "Florida"
    #
    # # Print the cities out.
    # print(inst_region.return_cities())
    #
    # # Print the breaks out.
    # print(inst_region.return_breaks())



