########################################################################################################################
# Project: wsl_app_v2.0
# FileName: main_widget.py
# Main Python Code for GUI
########################################################################################################################
import datetime
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog

from gui.common_widget.dialog_widget import add_tourtype_popup
from gui.common_widget.dialog_widget.add_location_popup import AddLocation
from gui.main.ui_to_py.wsl_analytics_ui_v2 import Ui_Form
from src.Places import Region, TourType
from src import Places, Validations


########################################################################################################################


class MainWidget(QMainWindow, Ui_Form):
    def __init__(self) -> object:
        # Call the constructor for the inherited QWidget class.
        QMainWindow.__init__(self)

        # Call the setupUi function that adds all the pyqt stuff to this class, that was designed in the designer.
        # This function is inherited from the Ui_Form class.
        self.setupUi(self)

        # Call the connect_slots function to connect all the event-handlers to functions in this class.
        self.connect_slots()

        # Sql Connection Variables
        self.__sql_user: str = "Heather"
        self.__sql_password: str = "#LAwaItly19"
        self.__sql_host: str = "localhost"

        # Instance of the Region Class.
        self.add_break_region_instance: Region = Region(
            sql_host_name=self.__sql_host,
            sql_password=self.__sql_password,
            sql_user_name=self.__sql_user
        )

        # Instance of TourType Class.
        self.add_tour_instance: TourType = TourType(
            sql_host_name=self.__sql_host,
            sql_password=self.__sql_password,
            sql_user_name=self.__sql_user
        )

        # Call to setup everything on the gui.
        self.on_startup()

    # This defines the event handlers for everything on the Main Widget
    def connect_slots(self):

        # Slots for Add Event Tab
        self.cb_addevent_continent.currentIndexChanged.connect(self.slot_cb_addevent_continent_on_index_change)
        self.cb_addevent_country.currentIndexChanged.connect(self.slot_cb_addevent_country_on_index_change)
        self.cb_addevent_region.currentIndexChanged.connect(self.slot_cb_addevent_region_on_index_change)
        self.pb_addevent_newtour.clicked.connect(self.slot_pb_addevent_newtour_clicked)
        self.pb_addevent_clear.clicked.connect(self.slot_pb_addevent_clear_clicked)
        self.pb_addevent_submit.clicked.connect(self.slot_pb_addevent_submit_clicked)

        # Slots for Add Break Tab
        self.cb_addbreak_continent.currentIndexChanged.connect(self.slot_cb_addbreak_continent_on_index_change)
        self.cb_addbreak_country.currentIndexChanged.connect(self.slot_cb_addbreak_country_on_index_change)
        self.pb_addbreak_clear.clicked.connect(self.slot_pb_addbreak_clear_clicked)
        self.pb_addbreak_newloc.clicked.connect(self.slot_pb_addbreak_newloc_clicked)
        self.pb_addbreak_submit.clicked.connect(self.slot_pb_addbreak_submit_clicked)

        # Slots for Add Surfer Tab
        self.cb_addsurfer_continent.currentIndexChanged.connect(self.slot_cb_addsurfer_continent_on_index_change)
        self.cb_addsurfer_hcontinent.currentIndexChanged.connect(self.slot_cb_addsurfer_hcontinent_on_index_change)
        self.cb_addsurfer_hcountry.currentIndexChanged.connect(self.slot_cb_addsurfer_hcountry_on_index_change)
        self.cb_addsurfer_hregion.currentIndexChanged.connect(self.slot_cb_addsurfer_hregion_on_index_change)
        self.pb_addsurfer_clear.clicked.connect(self.slot_pb_addsurfer_clear_clicked)
        self.pb_addsurfer_newloc.clicked.connect(self.slot_pb_addsurfer_newloc_clicked)
        self.pb_addsurfer_submit.clicked.connect(self.slot_pb_addsurfer_submit_clicked)

    ####################################################################################################################

    # Everything that should happen when the app has started up
    def on_startup(self):

        # Add Event Tab
        self.cb_addevent_continent.addItems([''] + self.add_break_region_instance.return_continents())
        self.cb_addevent_tourtype.addItems([''] + self.add_tour_instance.return_tours())

        # Add Break Tab
        self.cb_addbreak_continent.addItems(['']+self.add_break_region_instance.return_continents())

        # Add Surfer Tab
        self.cb_addsurfer_continent.addItems(['']+self.add_break_region_instance.return_continents())
        self.cb_addsurfer_hcontinent.addItems(['']+self.add_break_region_instance.return_continents())


    ####################################################################################################################
    # Event Handler Functions for Add Event Tab

    def slot_cb_addevent_continent_on_index_change(self):
        # Set all the instance variables in the instance of the Region class to None, by calling a function in the
        # add_break_region_instance instance.
        self.add_break_region_instance.set_everything_to_none()

        # Clear the country combo boxs.
        self.cb_addevent_country.clear()

        # Set the current value of the selected_continent variable in add_break_region_instance to the current text in the continent
        # combo box.
        self.add_break_region_instance.selected_continent = self.cb_addevent_continent.currentText()

        # Add the countries to the country combo box.
        self.cb_addevent_country.addItems([''] + self.add_break_region_instance.return_countries())

    def slot_cb_addevent_country_on_index_change(self):
        # Clear the add_break_region_instance combo boxs.
        self.cb_addevent_region.clear()

        # Set the current value of the selected_country variable in add_break_region_instance to the current text
        # in the country combo box.
        self.add_break_region_instance.selected_country = self.cb_addevent_country.currentText()

        # Add the regions to the add_break_region_instance combo box.
        self.cb_addevent_region.addItems([''] + self.add_break_region_instance.return_regions())

    def slot_cb_addevent_region_on_index_change(self):
        # Clear the add_break_region_instance combo boxs.
        self.cb_addevent_break.clear()

        # Set the current value of the selected_country variable in add_break_region_instance to the current text
        # in the country combo box.
        self.add_break_region_instance.selected_region = self.cb_addevent_region.currentText()

        # Add the regions to the add_break_region_instance combo box.
        self.cb_addevent_break.addItems([''] + self.add_break_region_instance.return_breaks())

    def slot_pb_addevent_newtour_clicked(self):
        dialog = add_tourtype_popup.AddTourType(title="Add a Tour Type to database.")

        if dialog.exec() == QDialog.Accepted:
            tour_type = dialog.line_tourtype.text()

            # Check to see if Tour Name is Blank for Label and LineEdit
            if dialog.line_tourtype.text() == '':
                print(f"You can't add a blank tour type. Just make something up.")
                raise ValueError

            # Check to see if Year is Blank for the Label and LineEdit
            if dialog.line_year.text() == '':
                print (f"You have to tell us the year...")
                raise ValueError

                # Insert new tour type into  tour type table
            try:
                # Tour Type Description
                tour_type = dialog.line_tourtype.text()

                # Tour Year
                year = dialog.line_year.text()
                inst = Validations.NumCheck(input_num=year)
                inst.year_check()

                # Check to see whether Men or Women was checked
                if dialog.chkbox_men.isChecked():
                    if dialog.chkbox_women.isChecked():
                        print(f"You checked both Male and Female. If it's both don't check anything.")
                    else:
                        gender = 'Men'
                elif dialog.chkbox_women.isChecked():
                    gender = 'Women'
                else:
                    gender = ''

                print(f"{year} {gender}'s {tour_type}")

                # Insert into Country Table
                table = 'wsl.tour_type'
                columns = f"gender, year, tour_name"
                fields = f"'{gender}', {year}, '{tour_type}'"
                inst = Places.SqlCommands()
                inst.insert_to_table(table=table,
                                     columns=columns,
                                     fields=fields
                                     )
            except:
                print('I went to the fucking except')
                raise ValueError

    def slot_pb_addevent_clear_clicked(self):
        self.cb_addevent_tourtype.clear()
        self.line_addevent_name.clear()
        self.line_addevent_stop.clear()
        self.line_addevent_open.clear()
        self.line_addevent_close.clear()
        self.cb_addevent_continent.clear()
        self.cb_addevent_continent.addItems([''] + self.add_break_region_instance.return_continents())
        self.cb_addevent_country.clear()
        self.cb_addevent_region.clear()
        self.cb_addevent_break.clear()

    def slot_pb_addevent_submit_clicked(self):
        # Check to make sureTour Type have data
        condition_1 = self.cb_addevent_tourtype.currentText() == ''
        if not condition_1:
            print("Tour Added.")
        else:
            print("You need to enter a Tour.")
            raise ValueError

        # Grab Tour Type and Name
        tour_type = self.cb_addevent_tourtype.currentText()
        event_name = self.line_addevent_name.text()

        # Grab Stop Nbr and check to make sure it's and integer
        stop_num = self.line_addevent_stop.text()
        inst = Validations.NumCheck(input_num=stop_num)
        stop_num = inst.int_check()

        # Grab Date Open and Date close and check that they are in the correct format
        open_date = self.line_addevent_open.text()
        inst = Validations.DateCheck(input_dt=open_date)
        inst.date_check()
        close_date = self.line_addevent_close.text()
        inst.date_check()

        # Grab Location Data
        continent = self.cb_addevent_continent.currentText()
        country = self.cb_addevent_country.currentText()
        region = self.cb_addevent_region.currentText()
        break_name = self.cb_addevent_break.currentText()

        print(f"Tour: {tour_type}")
        print(f"Stop: {stop_num}  {event_name}")
        print(f"From: {open_date}  to  {close_date}")
        print(f"Location: {continent}, {country}, {region}, {break_name}")

        # Add the Events to wsl.events
        try:
            # Need to grab region id tied to event that needs to be added
            table = 'wsl.tour_type'
            column = 'id'
            col_filter = f"where tour_type = '{tour_type}' "
            inst = Places.SqlCommands()
            tour_id = inst.select_a_column(table=table,
                                             column=column,
                                             col_filter=col_filter
                                             )[0]

            print(tour_id)

            # Need to grab break_id tied to event that needs to be added
            table = 'wsl.breaks'
            column = 'id'
            col_filter = f"where break = '{break_name}'"
            break_id = inst.select_a_column(table=table,
                                            column=column,
                                            col_filter = col_filter
                                            )[0]
            print(break_id)

            # Insert into Break Table
            table = 'wsl.events'
            columns = f"tour_id, 'event_name', stop_num, 'open_date', 'close_date', break_id"
            fields = f"{tour_id}, '{event_name}', {stop_num}, '{open_date}', '{close_date}', {break_id}"
            inst.insert_to_table(table=table,
                                 columns=columns,
                                 fields=fields
                                 )
        except:
            print('I went to the fucking except')

        # Clear Form on Submit
        self.slot_pb_addbreak_clear_clicked()


    ########################################################################################################################

    # Event Handler Functions for The Add Break Tab

    # Change Country List when a Continent is selected
    def slot_cb_addbreak_continent_on_index_change(self):

        # Set all the instance variables in the instance of the Region class to None, by calling a function in the
        # add_break_region_instance instance.
        self.add_break_region_instance.set_everything_to_none()

        # Clear the country combo boxs.
        self.cb_addbreak_country.clear()

        # Set the current value of the selected_continent variable in add_break_region_instance to the current text in the continent
        # combo box.
        self.add_break_region_instance.selected_continent = self.cb_addbreak_continent.currentText()

        # Add the countries to the country combo box.
        self.cb_addbreak_country.addItems(['']+self.add_break_region_instance.return_countries())

    # Change Region List when a Country is selected
    def slot_cb_addbreak_country_on_index_change(self):
        # Clear the add_break_region_instance combo boxs.
        self.cb_addbreak_region.clear()

        # Set the current value of the selected_country variable in add_break_region_instance to the current text
        # in the country combo box.
        self.add_break_region_instance.selected_country = self.cb_addbreak_country.currentText()

        # Add the regions to the add_break_region_instance combo box.
        self.cb_addbreak_region.addItems(['']+self.add_break_region_instance.return_regions())

    # Open a PopUp to enter new places when The Add Location Button is selected
    def slot_pb_addbreak_newloc_clicked(self):
        dialog = AddLocation(title="Add a location to the database.")

        if dialog.exec() == QDialog.Accepted:

            # Assign continent based on continent combobox
            continent = dialog.cb_continent.currentText()

            # Check to See if Country is Blank for Label and LineEdit
            if not dialog.line_country.text() == '':
                country = dialog.line_country.text()
            elif not dialog.cb_country.currentText() == '':
                country = dialog.cb_country.currentText()

            # Check to See if Region is Blank for Label and LineEdit
            if not dialog.line_region.text() == '':
                region = dialog.line_region.text()
            elif not dialog.cb_region.currentText() == '':
                region = dialog.cb_region.currentText()

            # Check to see if City is Blank for Label and LineEdit
            if not dialog.line_city.text() == '':
                city = dialog.line_city.text()
            else:
                print('Cities need names too.')
                # raise ValueError()

            print(f"You have found {city}, {region}, {country}, {continent}.")

            #Insert new country into country table
            try:
                # If New country is entered continue
                if not dialog.line_country.text() == '':
                    country = dialog.line_country.text()
                    # Need to grab continent id tied to country that needs to be added
                    table = 'wsl.continents'
                    column = 'id'
                    col_filter = f"where continent = '{continent}' "
                    inst = Places.SqlCommands()
                    continent_id = inst.select_a_column(table=table,
                                                        column=column,
                                                        col_filter=col_filter
                                                        )[0]
                    # Insert into Country Table
                    table = 'wsl.countries'
                    columns = 'country, continent_id'
                    fields = f"'{country}', {continent_id}"
                    inst.insert_to_table(table=table,
                                         columns=columns,
                                         fields=fields
                                         )
            except:
                print('I went to the fucking except')
                raise ValueError

            # Insert new region into region table
            try:
                # If New region is entered continue
                if not dialog.line_region.text() == '':
                    region = dialog.line_region.text()
                    # Need to grab country id tied to region that needs to be added
                    table = 'wsl.countries'
                    column = 'id'
                    col_filter = f"where country = '{country}' "
                    inst = Places.SqlCommands()
                    country_id = inst.select_a_column(table=table,
                                                        column=column,
                                                        col_filter=col_filter
                                                        )[0]
                    # Insert into Region Table
                    table = 'wsl.regions'
                    columns = 'region, country_id'
                    fields = f"'{region}', {country_id}"
                    inst.insert_to_table(table=table,
                                         columns=columns,
                                         fields=fields
                                         )
            except:
                print('I went to the fucking except')
                pass

            # Insert new city into city table
            try:
                # If New city is entered continue
                if not dialog.line_city.text() == '':
                    city = dialog.line_city.text()
                    # Need to grab region id tied to city that needs to be added
                    table = 'wsl.regions'
                    column = 'id'
                    col_filter = f"where region = '{region}' "
                    inst = Places.SqlCommands()
                    region_id = inst.select_a_column(table=table,
                                                      column=column,
                                                      col_filter=col_filter
                                                      )[0]
                    # Insert into City Table
                    table = 'wsl.cities'
                    columns = 'city, region_id'
                    fields = f"'{city}', {region_id}"
                    inst.insert_to_table(table=table,
                                         columns=columns,
                                         fields=fields
                                         )
            except:
                print('I went to the fucking except')
                pass

    # Clear the form when the Clear button is checked
    def slot_pb_addbreak_clear_clicked(self):
        self.cb_addbreak_continent.clear()
        self.cb_addbreak_continent.addItems([''] + self.add_break_region_instance.return_continents())
        self.cb_addbreak_country.clear()
        self.cb_addbreak_region.clear()
        self.line_addbreak_break.clear()
        self.check_addbreak_ability_green.setChecked(0)
        self.check_addbreak_ability_yellow.setChecked(0)
        self.check_addbreak_ability_red.setChecked(0)
        self.check_addbreak_burn_green.setChecked(0)
        self.check_addbreak_burn_yellow.setChecked(0)
        self.check_addbreak_burn_red.setChecked(0)
        self.check_addbreak_beach.setChecked(0)
        self.check_addbreak_point.setChecked(0)
        self.check_addbreak_reef.setChecked(0)
        self.check_addbreak_river.setChecked(0)
        self.check_addbreak_sandbar.setChecked(0)
        self.check_addbreak_jetty.setChecked(0)
        self.check_addbreak_eng.setChecked(0)
        self.line_addbreak_clean.clear()
        self.line_addbreak_blown.clear()
        self.line_addbreak_small.clear()

    # When the Submit button is clicked all data should be assigned a variable, prepared, and inserted into mysal db
    def slot_pb_addbreak_submit_clicked(self):
        if not self.line_addbreak_break.text() == '':
            # Grab Locations from Location Group
            continent = self.cb_addbreak_continent.currentText()
            country = self.cb_addbreak_country.currentText()
            region = self.cb_addbreak_region.currentText()
            break_name = self.line_addbreak_break.text()

            # Grab Reliability from Combobox
            reliability = self.cb_addbreak_reliability.currentText()

            # Grab Ability based on which color is checked
            ability = []
            if self.check_addbreak_ability_green.isChecked():
                ability.append('Beginner')
            if self.check_addbreak_ability_yellow.isChecked():
                ability.append('Intermediate')
            if self.check_addbreak_ability_red.isChecked():
                ability.append('Advanced')

            # Turn List of abilities into a string for mysql table
            ability_str = ""
            for ind, item in enumerate(ability):
                if not ind == (len(ability) - 1):
                    ability_str = ability_str + item + ', '
                else:
                    ability_str = ability_str + item

            # Grab Shoulder Burn based on which color is checked
            shoulder_burn = []
            if self.check_addbreak_burn_green.isChecked():
                shoulder_burn.append('Light')
            if self.check_addbreak_burn_yellow.isChecked():
                shoulder_burn.append('Medium')
            if self.check_addbreak_burn_red.isChecked():
                shoulder_burn.append('Exhausting')

            # Turn List of shoulder burn into a string for mysql table
            shoulder_burn_str = ""
            for ind, item in enumerate(shoulder_burn):
                if not ind == (len(shoulder_burn) - 1):
                    shoulder_burn_str = shoulder_burn_str + item + ', '
                else:
                    shoulder_burn_str = shoulder_burn_str + item

            # Grab Break Type based on which types are checked
            break_type = []
            if self.check_addbreak_beach.isChecked():
                break_type.append('Beach')
            if self.check_addbreak_point.isChecked():
                break_type.append('Point')
            if self.check_addbreak_reef.isChecked():
                break_type.append('Reef')
            if self.check_addbreak_river.isChecked():
                break_type.apped('River')
            if self.check_addbreak_sandbar.isChecked():
                break_type.append('Sandbar')
            if self.check_addbreak_jetty.isChecked():
                break_type.append('Jetty')
            if self.check_addbreak_eng.isChecked():
                break_type.append('Engineered')

            # Turn List of breaks into a string for mysql table
            break_type_str = ""
            for ind, item in enumerate(break_type):
                if not ind == (len(break_type) - 1):
                    break_type_str = break_type_str + item + ', '
                else:
                    break_type_str = break_type_str + item

            # Grab Surfability
            clean = self.line_addbreak_clean.text()
            blown = self.line_addbreak_blown.text()
            small = self.line_addbreak_small.text()

            # Make sure numbers were entered for surfability
            inst = Validations.NumCheck
            inst.int_check(self, input_num=clean)
            inst.int_check(self, input_num=blown)
            inst.int_check(self, input_num=small)

            print(f'Continent: {continent}, '
                  f'Country: {country}, '
                  f'Region: {region}, '
                  f'Break: {break_name}')
            print(reliability)
            print(ability)
            print(shoulder_burn)
            print(break_type)
            print(f"Clean: {clean}%  Blown: {blown}%  Small: {small}%")

        else:
            print('You should probably enter a break name.')

        # Add the Break to wsl.breaks
        try:
            # Need to grab region id tied to break that needs to be added
            table = 'wsl.regions'
            column = 'id'
            col_filter = f"where region = '{region}' "
            inst = Places.SqlCommands()
            region_id = inst.select_a_column(table=table,
                                                column=column,
                                                col_filter=col_filter
                                                )[0]
            # Insert into Break Table
            table = 'wsl.breaks'
            columns = f"break, region_id, break_type, reliability, ability, shoulder_burn, clean_waves, blown_waves, small_waves"
            fields = f"'{break_name}', {region_id}, '{break_type_str}', '{reliability}', '{ability_str}', '{shoulder_burn_str}',{int(clean)}, {int(blown)}, {int(small)}"
            inst.insert_to_table(table=table,
                                 columns=columns,
                                 fields=fields
                                 )
        except:
            print('I went to the fucking except')

        # Clear Form on Submit
        self.slot_pb_addbreak_clear_clicked()

    ####################################################################################################################
    # Event Handler Functions for Add Surfer Tab

    # Change Country List when Continent is Selected
    def slot_cb_addsurfer_continent_on_index_change(self):
        # Set all the instance variables in the instance of the Region class to None, by calling a function in the
        # add_break_region_instance instance.
        self.add_break_region_instance.set_everything_to_none()

        # Clear the country combo boxs.
        self.cb_addsurfer_country.clear()

        # Set the current value of the selected_continent variable in add_break_region_instance to the current text in the continent
        # combo box.
        self.add_break_region_instance.selected_continent = self.cb_addsurfer_continent.currentText()

        # Add the countries to the country combo box.
        self.cb_addsurfer_country.addItems(['']+self.add_break_region_instance.return_countries())

    # Change Home Country List when Home Continent is Selected
    def slot_cb_addsurfer_hcontinent_on_index_change(self):
        # Set all the instance variables in the instance of the Region class to None, by calling a function in the
        # add_break_region_instance instance.
        self.add_break_region_instance.set_everything_to_none()

        # Clear the country combo boxs.
        self.cb_addsurfer_hcountry.clear()

        # Set the current value of the selected_continent variable in add_break_region_instance to the current text in the continent
        # combo box.
        self.add_break_region_instance.selected_continent = self.cb_addsurfer_hcontinent.currentText()

        # Add the countries to the country combo box.
        self.cb_addsurfer_hcountry.addItems(['']+self.add_break_region_instance.return_countries())

    # Change Home Region List when Home Country is Selected
    def slot_cb_addsurfer_hcountry_on_index_change(self):
        # Clear the add_break_region_instance combo boxs.
        self.cb_addsurfer_hregion.clear()

        # Set the current value of the selected_country variable in add_break_region_instance to the current text
        # in the country combo box.
        self.add_break_region_instance.selected_country = self.cb_addsurfer_hcountry.currentText()

        # Add the regions to the add_break_region_instance combo box.
        self.cb_addsurfer_hregion.addItems(['']+self.add_break_region_instance.return_regions())

    # Change Home City List when Home Region is Selected
    def slot_cb_addsurfer_hregion_on_index_change(self):
        # Clear the add_break_region_instance combo boxs.
        self.cb_addsurfer_hcity.clear()

        # Set the current value of the selected_country variable in add_break_region_instance to the current text
        # in the country combo box.
        self.add_break_region_instance.selected_region = self.cb_addsurfer_hregion.currentText()

        # Add the regions to the add_break_region_instance combo box.
        self.cb_addsurfer_hcity.addItems(['']+self.add_break_region_instance.return_cities())

    # Event Handler for Clear Button Clicked
    def slot_pb_addsurfer_clear_clicked(self):
        self.line_addsurfer_firstname.clear()
        self.line_addsurfer_lastname.clear()
        self.check_addsurfer_goofy.setChecked(0)
        self.check_addsurfer_regular.setChecked(0)
        self.cb_addsurfer_continent.clear()
        self.cb_addsurfer_continent.addItems([''] + self.add_break_region_instance.return_continents())
        self.cb_addsurfer_country.clear()
        self.line_addsurfer_bday.clear()
        self.line_addsurfer_ht.clear()
        self.line_addsurfer_wt.clear()
        self.line_addsurfer_firstseason.clear()
        self.line_addsurfer_firsttour.clear()
        self.cb_addsurfer_hcontinent.clear()
        self.cb_addsurfer_hcontinent.addItems([''] + self.add_break_region_instance.return_continents())
        self.cb_addsurfer_hcountry.clear()
        self.cb_addsurfer_hregion.clear()
        self.cb_addsurfer_hcity.clear()
        self.check_addsurfer_male.setChecked(0)
        self.check_addsurfer_female.setChecked(0)

    # Event Handler for Add Location Button Clicked
    def slot_pb_addsurfer_newloc_clicked(self):
        self.slot_pb_addbreak_newloc_clicked()

    # Event Handler for Submit Button Clicked
    def slot_pb_addsurfer_submit_clicked(self):
        # Check to Make Sure a First and Last Name are entered
        condition_1 = self.line_addsurfer_firstname.text() == ''
        condition_2 = self.line_addsurfer_lastname.text() == ''
        if not condition_1 and not condition_2:
            print(f"You're not a complete fuck up. You entered a first and last name!")
        else:
            print(f"Enter a first and last name. Don't be a piece of shit.")

        # Grab First and Last Name
        first_name = self.line_addsurfer_firstname.text()
        last_name = self.line_addsurfer_lastname.text()

        # Determine Stance
        if self.check_addsurfer_regular.isChecked():
            stance = 'Regular'
        elif self.check_addsurfer_goofy.isChecked():
            stance = 'Goofy'
        else:
            stance = ''

        # Find Country they represent
        country = self.cb_addsurfer_country.currentText()

        # Grab birthday and turn into correct format for sql
        birthday = self.line_addsurfer_bday.text()
        inst = Validations.DateCheck
        birthday = inst.date_check(self, input_dt=birthday)

        # Grab Height and Weight and check to see if they are numbers
        height = self.line_addsurfer_ht.text()
        weight = self.line_addsurfer_wt.text()

        # Check to Make sure height and weight were entered as numbers
        inst = Validations.NumCheck
        inst.int_check(self, input_num=height)
        inst.int_check(self, input_num=weight)

        # Grab first season and tour
        first_season = self.line_addsurfer_firstseason.text()
        first_tour = self.line_addsurfer_firsttour.text()

        # Make sure first season has a length of 4 and is an integer
        if not first_season =='':
            if len(first_season) == 4:
                pass
            else:
                "First Season must be a year in form YYYY"
        inst = Validations.NumCheck
        inst.int_check(self, input_num=first_season)

        # Grab Home City
        home_city = self.cb_addsurfer_hcity.currentText()

        # Grab Male or Female
        if self.check_addsurfer_male.isChecked():
            if self.check_addsurfer_female.isChecked():
                print('Dude, we have to separate by gender because of stuff like muscle density to keep it fair.')
                raise ValueError
            gender = 'Men'
        elif self.check_addsurfer_female.isChecked():
            gender = 'Women'
        else:
            print("Bruh, you have to choose a gender for this to work.")
            raise ValueError

        print(f"Name: {first_name} {last_name}")
        print(f"Stance: {stance}")
        print(f"Representing: {country}")
        print(f"Date of Birth: {birthday}")
        print(f"Height(cm): {height}    Weight(kg): {weight}")
        print(f"First Season: {first_season} {first_tour}")
        print(f"Hometown: {home_city}")
        print(f"Competing in the {gender}'s tour.")

        # Add the Break to wsl.surfers
        try:
            # Need to grab country id tied to rep country
            table = 'wsl.countries'
            column = 'id'
            col_filter = f"where country = '{country}'"
            inst = Places.SqlCommands()
            country_id = inst.select_a_column(table=table,
                                              column=column,
                                              col_filter=col_filter
                                              )[0]

            # Need to grab city id tied to home city
            table = 'wsl.cities'
            column = 'id'
            col_filter = f"where city = '{home_city}' "
            inst = Places.SqlCommands()
            home_city_id = inst.select_a_column(table=table,
                                             column=column,
                                             col_filter=col_filter
                                             )[0]
            # Insert into Surfers Table
            table = 'wsl.surfers'
            columns = f"gender, first_name, last_name, stance, country_id, birthday, height, weight, first_season, first_tour, home_city_id"
            fields = f"'{gender}', '{first_name}', '{last_name}', '{stance}', {country_id}, '{birthday}', {height}, {weight}, '{first_season}', '{first_tour}', {home_city_id}"
            inst.insert_to_table(table=table,
                                 columns=columns,
                                 fields=fields
                                 )
        except:
            print('I went to the fucking except')

        # Clear Everything on Submit
        self.slot_pb_addsurfer_clear_clicked()

    ####################################################################################################################


########################################################################################################################

if __name__ == '__main__':
    app = QApplication([])
    win = MainWidget()
    win.show()

    sys.exit(app.exec())