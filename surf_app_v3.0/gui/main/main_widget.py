########################################################################################################################
# Project: wsl_app_v2.0
# FileName: main_widget.py
# Main Python Code for GUI
########################################################################################################################
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog

from gui.common_widget.dialog_widget.popup_add_data import AddLocation, AddTourType, AddEventType, SurferToHeat
from gui.main.ui_to_py.wsl_analytics_ui_v2 import Ui_Form

from src.hierarchy import Region, Heat
from src import hierarchy, Validations

########################################################################################################################


class MainWidget(QMainWindow, Ui_Form):
    def __init__(self):

        # Call the constructor for the inherited QWidget class.
        QMainWindow.__init__(self)

        # This function is inherited from the Ui_Form class.
        self.setupUi(self)

        # Call the connect_slots function to connect all the event-handlers to functions in this class.
        self.connect_slots()

        # Sql Connection Variables
        self.__sql_user: str = "Heather"
        self.__sql_password: str = "#LAwaItly19"
        self.__sql_host: str = "localhost"

        # Instance of the Region Class.
        self.add_region_instance: Region = Region(
            sql_host_name=self.__sql_host,
            sql_password=self.__sql_password,
            sql_user_name=self.__sql_user
        )

        # Instance of Heat Class.
        self.add_heat_instance: Heat = Heat(
            sql_host_name=self.__sql_host,
            sql_password=self.__sql_password,
            sql_user_name=self.__sql_user
        )

        # Call to setup everything on the gui.
        self.on_startup()

    # This defines the event handlers for everything on the Main Widget
    def connect_slots(self):

        # Slots for Add Event Tab
        self.cb_addevent_year.currentIndexChanged.connect(self.slot_cb_addevent_year_on_index_change)
        self.cb_addevent_continent.currentIndexChanged.connect(self.slot_cb_addevent_continent_on_index_change)
        self.cb_addevent_country.currentIndexChanged.connect(self.slot_cb_addevent_country_on_index_change)
        self.cb_addevent_region.currentIndexChanged.connect(self.slot_cb_addevent_region_on_index_change)

        self.pb_addevent_newtour.clicked.connect(self.slot_pb_addevent_newtour_clicked)
        self.pb_addevent_clear.clicked.connect(self.slot_pb_addevent_clear_clicked)
        self.pb_addevent_submit.clicked.connect(self.slot_pb_addevent_submit_clicked)

        # Slots for Add Heat Tab
        self.cb_addheat_year.currentIndexChanged.connect(self.slot_cb_addheat_year_on_index_change)
        self.cb_addheat_tour.currentIndexChanged.connect(self.slot_cb_addheat_tour_on_index_change)

        self.pb_addheat_newround.clicked.connect(self.slot_pb_addheat_newround_clicked)
        self.pb_addheat_clear.clicked.connect(self.slot_pb_addheat_clear_clicked)
        self.pb_addheat_submit.clicked.connect(self.slot_pb_addheat_submit_clicked)
        self.pb_addheat_surfers.clicked.connect(self.slot_pb_addheat_surfers_clicked)

        # Slots for Add Round Results Tab
        self.cb_addresults_year.currentIndexChanged.connect(self.slot_cb_addresults_year_on_index_change)
        self.cb_addresults_tour.currentIndexChanged.connect(self.slot_cb_addresults_tour_on_index_change)
        self.cb_addresults_event.currentIndexChanged.connect(self.slot_cb_addresults_round_on_index_change)
        self.cb_addresults_round.currentIndexChanged.connect(self.slot_cb_addresults_heat_on_index_change)
        self.cb_addresults_heat.currentIndexChanged.connect(self.slot_cb_addresults_surfer_on_index_change)

        self.pb_addresults_clear.clicked.connect(self.slot_pb_addresults_clear_clicked)
        self.pb_addresults_submit.clicked.connect(self.slot_pb_addresults_submit_clicked)

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
        self.cb_addevent_continent.addItems([''] + self.add_region_instance.return_continents())
        self.cb_addevent_year.addItems([''] + self.add_heat_instance.return_tour_years())

        # Add Heat Tab
        self.cb_addheat_year.addItems([''] + self.add_heat_instance.return_tour_years())
        self.cb_addheat_round.addItems([''] + self.add_heat_instance.return_all_rounds())

        # Add Round Results Tab
        # Add Tour Years
        inst = hierarchy.TourYear()
        self.cb_addresults_year.addItems([''] + inst.return_tour_years())

        # Add Break Tab
        self.cb_addbreak_continent.addItems([''] + self.add_region_instance.return_continents())

        # Add Surfer Tab
        self.cb_addsurfer_continent.addItems([''] + self.add_region_instance.return_continents())
        self.cb_addsurfer_hcontinent.addItems([''] + self.add_region_instance.return_continents())

    ####################################################################################################################
    # Add Event Tab

    # Add Countries when a Continent is selected
    def slot_cb_addevent_continent_on_index_change(self):
        self.add_region_instance.set_everything_to_none()
        self.cb_addevent_country.clear()
        self.add_region_instance.selected_continent = self.cb_addevent_continent.currentText()
        self.cb_addevent_country.addItems([''] + self.add_region_instance.return_countries())

    # Add Regions when a Country is selected
    def slot_cb_addevent_country_on_index_change(self):
        self.cb_addevent_region.clear()
        self.add_region_instance.selected_country = self.cb_addevent_country.currentText()
        self.cb_addevent_region.addItems([''] + self.add_region_instance.return_regions())

    # Add Breaks when a Region is selected
    def slot_cb_addevent_region_on_index_change(self):
        self.cb_addevent_break.clear()
        self.add_region_instance.selected_region = self.cb_addevent_region.currentText()
        self.cb_addevent_break.addItems([''] + self.add_region_instance.return_breaks())

    # Add Tour Names when a Year is selected
    def slot_cb_addevent_year_on_index_change(self):
        self.cb_addevent_tourtype.clear()
        self.add_heat_instance.selected_tour_year = self.cb_addevent_year.currentText()
        self.cb_addevent_tourtype.addItems(self.add_heat_instance.return_tours())

    # Button for Adding a New Tour Type
    # noinspection PyMethodMayBeStatic
    def slot_pb_addevent_newtour_clicked(self):
        dialog = AddTourType(title="Add a Tour Type to database.")

        if dialog.exec() == QDialog.Accepted:

            # Check to see if Tour Name is Blank for Label and LineEdit
            if dialog.line_tourtype.text() == '':
                print(f"You can't add a blank tour type. Just make something up.")
                raise ValueError

            # Check to see if Year is Blank for the Label and LineEdit
            if dialog.line_year.text() == '':
                print(f"You have to tell us the year...")
                raise ValueError

            # Insert new tour type into  tour type table
            try:
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

                # noinspection PyUnboundLocalVariable
                tour_name = f"{year} {gender}s {tour_type}"
                print(tour_name)

                # Check to see if it's already in wsl.tour
                table = 'wsl.tour'
                column = 'year, gender, tour_type'
                col_filter = f"where year = {year} " \
                             f"and gender = '{gender}' " \
                             f"and tour_type = '{tour_type}' "
                inst = hierarchy.SqlCommands()
                dupe = inst.check_for_dupe_add(table=table,
                                               column=column,
                                               col_filter=col_filter
                                               )

                if not dupe:
                    # Insert into Country Table
                    table = 'wsl.tour'
                    columns = f"year, gender, tour_type, tour_name"
                    fields = f"{year}, '{gender}', '{tour_type}', '{tour_name}'"
                    inst = hierarchy.SqlCommands()
                    inst.insert_to_table(table=table,
                                         columns=columns,
                                         fields=fields
                                         )
                else:
                    print(f"You are entering a duplicate Tour.")
                    print(f"you entered {dupe}")
            except:
                print('I went to the fucking except when you were trying to enter a new tour.')
                raise ValueError

    # Clear Form
    def slot_pb_addevent_clear_clicked(self):
        self.cb_addevent_tourtype.clear()
        self.line_addevent_name.clear()
        self.line_addevent_stop.clear()
        self.line_addevent_open.clear()
        self.line_addevent_close.clear()
        self.cb_addevent_continent.clear()
        self.cb_addevent_continent.addItems([''] + self.add_region_instance.return_continents())
        self.cb_addevent_country.clear()
        self.cb_addevent_region.clear()
        self.cb_addevent_break.clear()

    # Logic for when Submit Button is clicked
    def slot_pb_addevent_submit_clicked(self):
        # Check to make sure Tour Type has data
        condition_1 = self.cb_addevent_tourtype.currentText() == ''
        if not condition_1:
            print(f"Tour is {self.cb_addevent_tourtype.currentText()}")
        else:
            print("You need to enter a Tour.")
            raise ValueError

        # Grab Tour Type and Name
        tour_name = self.cb_addevent_tourtype.currentText()
        event_name = self.line_addevent_name.text()

        # Grab Stop nbr and check to make sure it's and integer
        stop_nbr = self.line_addevent_stop.text()
        inst = Validations.NumCheck()
        stop_nbr = inst.int_check(input_num=stop_nbr)

        # Grab Date Open and Date close and check that they are in the correct format
        open_date = self.line_addevent_open.text()
        close_date = self.line_addevent_close.text()
        # print(open_date)
        # print(close_date)
        inst = Validations.DateCheck()
        open_date = inst.date_check(input_dt=open_date)
        inst = Validations.DateCheck()
        close_date = inst.date_check(input_dt=close_date)

        print("Dates successful")

        # Grab Location Data
        continent = self.cb_addevent_continent.currentText()
        country = self.cb_addevent_country.currentText()
        region = self.cb_addevent_region.currentText()
        break_name = self.cb_addevent_break.currentText()

        print(f"Tour: {tour_name}")
        print(f"Stop: {stop_nbr}  {event_name}")
        print(f"From: {open_date}  to  {close_date}")
        print(f"Location: {continent}, {country}, {region}, {break_name}")

        # Add the Events to wsl.events
        try:
            # Need to grab region id tied to event that needs to be added
            table = 'wsl.tour'
            column = 'tour_id'
            col_filter = f"where tour_name = '{tour_name}' "
            inst = hierarchy.SqlCommands()
            tour_id = inst.select_a_column(table=table,
                                           column=column,
                                           col_filter=col_filter
                                           )[0]

            print(tour_id)

            # Need to grab break_id tied to event that needs to be added
            table = 'wsl.break'
            column = 'break_id'
            col_filter = f"where break = '{break_name}' "
            break_id = inst.select_a_column(table=table,
                                            column=column,
                                            col_filter=col_filter
                                            )[0]
            print(break_id)

            # Insert into Events Table
            table = 'wsl.event'
            columns = f"event_name, tour_id, stop_nbr, break_id, " \
                      f"open_date, close_date"
            fields = f"'{event_name}', {tour_id}, {stop_nbr}, " \
                     f"{break_id}, '{open_date}', '{close_date}' "
            inst.insert_to_table(table=table,
                                 columns=columns,
                                 fields=fields
                                 )
        except:
            print('I went to the fucking except')

        # Clear Form on Submit
        self.slot_pb_addevent_clear_clicked()

    ####################################################################################################################
    # Add Heat Tab

    # Add Tour Names when Year is selected
    def slot_cb_addheat_year_on_index_change(self):
        self.cb_addheat_tour.clear()
        self.add_heat_instance.selected_tour_year = self.cb_addheat_year.currentText()
        self.cb_addheat_tour.addItems([''] + self.add_heat_instance.return_tours())

    # Add Events when a Tour Name is selected
    def slot_cb_addheat_tour_on_index_change(self):
        self.cb_addheat_event.clear()
        self.add_heat_instance.selected_tour_name = self.cb_addheat_tour.currentText()
        self.cb_addheat_event.addItems([''] + self.add_heat_instance.return_events())

    # Button for Adding New Round Types
    # noinspection PyMethodMayBeStatic
    def slot_pb_addheat_newround_clicked(self):
        dialog = AddEventType(title="Add a Tour Type to database.")

        if dialog.exec() == QDialog.Accepted:
            round_name = dialog.line_round.text()

            # Check to see if Event Name is Blank for Label and LineEdit
            if dialog.line_round.text() == '':
                print(f"You can't add a blank round type. WSL even tells you wtf it should be!")
                raise ValueError

                # Insert new tour type into  tour type table
            try:
                # Insert into Event Table
                table = 'wsl.round'
                columns = f"round"
                fields = f"'{round_name}' "
                inst = hierarchy.SqlCommands()
                inst.insert_to_table(table=table,
                                     columns=columns,
                                     fields=fields
                                     )
            except:
                print('I went to the fucking except')
                raise ValueError

    # Clear the Form
    def slot_pb_addheat_clear_clicked(self):
        self.cb_addheat_tour.clear()
        self.cb_addheat_tour.addItems([''] + self.add_heat_instance.return_tours())
        self.cb_addheat_event.clear()
        self.cb_addheat_round.clear()
        self.cb_addheat_round.addItems([''] + self.add_heat_instance.return_all_rounds())
        self.line_addheat_heat.clear()
        self.line_addheat_date.clear()
        self.line_addheat_duration.clear()
        self.line_addheat_wavemin.clear()
        self.line_addheat_wavemax.clear()
        self.check_addheat_calm.setChecked(0)
        self.check_addheat_light.setChecked(0)
        self.check_addheat_onshore.setChecked(0)
        self.check_addheat_offshore.setChecked(0)
        self.check_addheat_cross.setChecked(0)
        self.check_addheat_storm.setChecked(0)

    # Logic for when Submit Button is clicked
    def slot_pb_addheat_submit_clicked(self):

        # Check to Make sure a Tour is Entered
        if self.cb_addheat_tour.currentText() == '':
            print("What tour was this?")
            raise ValueError
        # Check to Make sure an TourName is Entered
        if self.cb_addheat_event.currentText() == '':
            print("What Event? If the tour doesn't have an event just repeat the tour name without the date.")
            raise ValueError
        # Check to see if Event is Entered
        if self.cb_addheat_round.currentText() == '':
            print('What round? If there is only one round then type 1')
            raise ValueError
        # Check to see if Round is Entered
        if self.line_addheat_heat.text() == '':
            print('What heat? If there is only one then type 1')

        # Grab Tour, TourName, Event, and Round from Add Round Tab
        tour_name = self.cb_addheat_tour.currentText()
        event_name = self.cb_addheat_event.currentText()
        round_name = self.cb_addheat_round.currentText()
        heat_nbr = self.line_addheat_heat.text()

        # Check that heat_num is an integer
        inst = Validations.NumCheck()
        heat_nbr = inst.int_check(input_num=heat_nbr)

        # Grab date from the form
        heat_date = self.line_addheat_date.text()
        # Check that date is in the correct format
        inst = Validations.DateCheck()
        heat_date = inst.date_check(input_dt=heat_date)

        # Grab duration from the form
        duration = self.line_addheat_duration.text()
        # Check that duration is an int
        inst = Validations.NumCheck(input_num=duration)
        duration = inst.int_check(input_num=duration)

        # Find Wave Range
        wave_min = self.line_addheat_wavemin.text()
        inst = Validations.NumCheck()
        wave_min = inst.int_check(input_num=wave_min)
        wave_max = self.line_addheat_wavemax.text()
        inst = Validations.NumCheck()
        inst.int_check(input_num=wave_max)

        # Assign Wind Type
        wind_type_list = []
        if self.check_addheat_calm.isChecked():
            wind_type_list.append('Calm')
        if self.check_addheat_light.isChecked():
            wind_type_list.append('Light')
        if self.check_addheat_onshore.isChecked():
            wind_type_list.append('Onshore')
        if self.check_addheat_offshore.isChecked():
            wind_type_list.append('Offshore')
        if self.check_addheat_cross.isChecked():
            wind_type_list.append('Cross')
        if self.check_addheat_storm.isChecked():
            wind_type_list.append('Storm')

        # Turn wind_type into a string
        wind = ""
        for ind, item in enumerate(wind_type_list):
            if not ind == (len(wind_type_list) - 1):
                wind = wind + item + ', '
            else:
                wind = wind + item

        print(f"Tour: {tour_name}")
        print(f"TourName: {event_name}")
        print(f"Round & Heat: {round_name} - Heat {heat_nbr}")
        print(f"{duration} minutes")
        print(f"Waves ranged from {wave_min} to {wave_max}")
        print(f"Wind: {wind_type_list}")

        # Add the Round to wsl.heats
        try:
            # Need to grab event_id
            table = 'wsl.event'
            column = 'event_id'
            col_filter = f"where event_name = '{event_name}' "
            inst = hierarchy.SqlCommands()
            event_id = inst.select_a_column(table=table,
                                            column=column,
                                            col_filter=col_filter
                                            )[0]
            # Need to grab round_id
            table = 'wsl.round'
            column = 'round_id'
            col_filter = f"where round = '{round_name}' "
            inst = hierarchy.SqlCommands()
            round_id = inst.select_a_column(table=table,
                                            column=column,
                                            col_filter=col_filter
                                            )[0]

            # Insert into Round Table
            table = 'wsl.heat_details'
            columns = f"heat_nbr, event_id, round_id, " \
                      f"wind, heat_date, duration, wave_min, wave_max"
            fields = f"{heat_nbr}, {event_id}, {round_id}, " \
                     f"'{wind}', '{heat_date}', {duration}, {wave_min}, {wave_max}"
            inst.insert_to_table(table=table,
                                 columns=columns,
                                 fields=fields
                                 )
        except:
            print('I went to the fucking except')

        # Clear Form on Submit
        self.slot_pb_addheat_clear_clicked()

    # Button for adding surfers to a heat
    # noinspection PyMethodMayBeStatic
    def slot_pb_addheat_surfers_clicked(self):
        dialog = SurferToHeat(title="Add a location to the database.")

        if dialog.exec() == QDialog.Accepted:
            pass

    ####################################################################################################################
    # Add Results Tab

    # Add Tour Names when a Year is selected
    def slot_cb_addresults_year_on_index_change(self):
        self.cb_addresults_tour.clear()
        self.add_heat_instance.selected_tour_year = self.cb_addresults_year.currentText()
        self.cb_addresults_tour.addItems([''] + self.add_heat_instance.return_tours())

    # Add Events when a Tour Name is selected
    def slot_cb_addresults_tour_on_index_change(self):
        self.cb_addresults_event.clear()
        self.add_heat_instance.selected_tour_name = self.cb_addresults_tour.currentText()
        self.cb_addresults_event.addItems([''] + self.add_heat_instance.return_events())

    # Add Round Types
    def slot_cb_addresults_round_on_index_change(self):
        self.cb_addresults_round.clear()
        self.cb_addresults_round.addItems([''] + self.add_heat_instance.return_all_rounds())

    # Add Heat Numbers when a Round is selected
    def slot_cb_addresults_heat_on_index_change(self):
        self.cb_addresults_heat.clear()
        self.add_heat_instance.selected_tour_name = self.cb_addresults_tour.currentText()
        self.add_heat_instance.selected_event = self.cb_addresults_event.currentText()
        self.add_heat_instance.selected_round = self.cb_addresults_round.currentText()
        self.cb_addresults_heat.addItems([''] + self.add_heat_instance.return_heats())

    # Add Surfers when a Heat is selected
    def slot_cb_addresults_surfer_on_index_change(self):
        self.cb_addresults_surfer.clear()
        self.add_heat_instance.selected_tourname = self.cb_addresults_tour.currentText()
        self.add_heat_instance.selected_event = self.cb_addresults_event.currentText()
        self.add_heat_instance.selected_round = self.cb_addresults_round.currentText()
        self.add_heat_instance.selected_heat = self.cb_addresults_heat.currentText()
        self.cb_addresults_surfer.addItems([''] + self.add_heat_instance.return_surfers_in_heat())

    def slot_pb_addresults_clear_clicked(self):
        self.cb_addresults_year.clear()
        inst = hierarchy.Event()
        self.cb_addresults_year.addItems([''] + inst.return_tour_years())

        self.cb_addresults_tour.clear()
        self.cb_addresults_event.clear()
        self.cb_addresults_round.clear()
        self.cb_addresults_heat.clear()
        self.cb_addresults_surfer.clear()

        self.line_addresults_picks.clear()

        self.check_addresults_jersey_yellow.setChecked(0)
        self.check_addresults_jersey_red.setChecked(0)
        self.check_addresults_jersey_black.setChecked(0)
        self.check_addresults_jersey_white.setChecked(0)
        self.check_addresults_jersey_blue.setChecked(0)
        self.check_addresults_jersey_pink.setChecked(0)

        self.check_addresults_advanced.setChecked(0)
        self.check_addresults_eliminated.setChecked(0)

        self.line_addresults_1.clear()
        self.line_addresults_2.clear()
        self.line_addresults_3.clear()
        self.line_addresults_4.clear()
        self.line_addresults_5.clear()
        self.line_addresults_6.clear()
        self.line_addresults_7.clear()
        self.line_addresults_8.clear()
        self.line_addresults_9.clear()
        self.line_addresults_10.clear()
        self.line_addresults_11.clear()
        self.line_addresults_12.clear()
        self.line_addresults_13.clear()
        self.line_addresults_14.clear()
        self.line_addresults_15.clear()

    def slot_pb_addresults_submit_clicked(self):

        # Get Tour down through heat and surfer from Form
        year = self.cb_addresults_year.currentText()
        tour_name = self.cb_addresults_tour.currentText()
        event_name = self.cb_addresults_event.currentText()
        round_name = self.cb_addresults_round.currentText()
        heat_nbr = self.cb_addresults_heat.currentText()
        surfer = self.cb_addresults_surfer.currentText()
        self.add_heat_instance.selected_surfer = self.cb_addresults_surfer.currentText()

        # Get picked % from form and check that it's float
        picked_percent = self.line_addresults_picks.text()
        inst = Validations.NumCheck(input_num=picked_percent)
        inst.float_check()

        # Find the Jersey Color
        if self.check_addresults_jersey_yellow.isChecked():
            jersey_color = 'Yellow'
        if self.check_addresults_jersey_red.isChecked():
            jersey_color = 'Red'
        if self.check_addresults_jersey_black.isChecked():
            jersey_color = 'Black'
        if self.check_addresults_jersey_white.isChecked():
            jersey_color = 'White'
        if self.check_addresults_jersey_blue.isChecked():
            jersey_color = 'Blue'
        if self.check_addresults_jersey_pink.isChecked():
            jersey_color = 'Pink'

        # Check To Make sure Advanced or Eliminated are checked but not both
        cond_advanced = self.check_addresults_advanced.isChecked()
        cond_eliminated = self.check_addresults_eliminated.isChecked()
        if cond_advanced and cond_eliminated:
            print("This isn't Schrodinger's Tournament. Was the surfer observed Advancing or being Eliminated?")
            raise ValueError
        if not cond_advanced and not cond_eliminated:
            print("This isn't Schrodinger's Tournament. Was the surfer observed Advancing or being Eliminated?")
            raise ValueError

        # Set Advanced or Eliminated based on which is checked
        if cond_advanced:
            status = 'Advanced'
        if cond_eliminated:
            status = 'Eliminated'

        # Grab wave scores from form

        if self.line_addresults_1.text() == '':
            wave_1 = 0
        else:
            wave_1 = self.line_addresults_1.text()
            inst = Validations.NumCheck(input_num=wave_1)
            inst.float_check()

        if self.line_addresults_2.text() == '':
            wave_2 = 0
        else:
            wave_2 = self.line_addresults_2.text()
            inst = Validations.NumCheck(input_num=wave_2)
            inst.float_check()

        if self.line_addresults_3.text() == '':
            wave_3 = 0
        else:
            wave_3 = self.line_addresults_3.text()
            inst = Validations.NumCheck(input_num=wave_3)
            inst.float_check()

        if self.line_addresults_4.text() == '':
            wave_4 = 0
        else:
            wave_4 = self.line_addresults_4.text()
            inst = Validations.NumCheck(input_num=wave_4)
            inst.float_check()

        if self.line_addresults_5.text() == '':
            wave_5 = 0
        else:
            wave_5 = self.line_addresults_5.text()
            inst = Validations.NumCheck(input_num=wave_5)
            inst.float_check()

        if self.line_addresults_6.text() == '':
            wave_6 = 0
        else:
            wave_6 = self.line_addresults_6.text()
            inst = Validations.NumCheck(input_num=wave_6)
            inst.float_check()

        if self.line_addresults_7.text() == '':
            wave_7 = 0
        else:
            wave_7 = self.line_addresults_7.text()
            inst = Validations.NumCheck(input_num=wave_7)
            inst.float_check()

        if self.line_addresults_8.text() == '':
            wave_8 = 0
        else:
            wave_8 = self.line_addresults_8.text()
            inst = Validations.NumCheck(input_num=wave_8)
            inst.float_check()

        if self.line_addresults_9.text() == '':
            wave_9 = 0
        else:
            wave_9 = self.line_addresults_9.text()
            inst = Validations.NumCheck(input_num=wave_9)
            inst.float_check()

        if self.line_addresults_10.text() == '':
            wave_10 = 0
        else:
            wave_10 = self.line_addresults_10.text()
            inst = Validations.NumCheck(input_num=wave_10)
            inst.float_check()

        if self.line_addresults_11.text() == '':
            wave_11 = 0
        else:
            wave_11 = self.line_addresults_11.text()
            inst = Validations.NumCheck(input_num=wave_11)
            inst.float_check()

        if self.line_addresults_12.text() == '':
            wave_12 = 0
        else:
            wave_12 = self.line_addresults_12.text()
            inst = Validations.NumCheck(input_num=wave_12)
            inst.float_check()

        if self.line_addresults_13.text() == '':
            wave_13 = 0
        else:
            wave_13 = self.line_addresults_13.text()
            inst = Validations.NumCheck(input_num=wave_13)
            inst.float_check()

        if self.line_addresults_14.text() == '':
            wave_14 = 0
        else:
            wave_14 = self.line_addresults_14.text()
            inst = Validations.NumCheck(input_num=wave_14)
            inst.float_check()

        if self.line_addresults_15.text() == '':
            wave_15 = 0
        else:
            wave_15 = self.line_addresults_15.text()
            inst = Validations.NumCheck(input_num=wave_15)
            inst.float_check()

        # Add To Table
        try:
            # # Need to grab tour id
            # inst = hierarchy.SqlCommands
            # table = 'wsl.tour'
            # column = 'tour_id'
            # col_filter = f"'where tour_name = '{tour_name}' "
            # tour_id = inst.select_a_column(table=table,
            #                                column=column,
            #                                col_filter=col_filter
            #                                )

            # Need to grab event id
            inst = hierarchy.SqlCommands()
            table = 'wsl.event'
            column = 'event_id'
            col_filter = f"where event_name = '{event_name}' "
            event_id = inst.select_a_column(table=table,
                                            column=column,
                                            col_filter=col_filter
                                            )[0]

            # Need to grab round id
            inst = hierarchy.SqlCommands()
            table = 'wsl.round'
            column = 'round_id'
            col_filter = f"where round = '{round_name}' "
            round_id = inst.select_a_column(table=table,
                                            column=column,
                                            col_filter=col_filter
                                            )[0]

            # Need to grab heat id
            inst = hierarchy.SqlCommands()
            table = 'wsl.heat_details'
            column = 'heat_id'
            col_filter = f"where event_id = {event_id} " \
                         f"and round_id = {round_id} " \
                         f"and heat_nbr = {heat_nbr}"
            heat_id = inst.select_a_column(table=table,
                                           column=column,
                                           col_filter=col_filter
                                           )[0]

            # Need to grab surfer id
            inst = hierarchy.SqlCommands()
            table = 'wsl.surfers'
            column = 'surfer_id'
            col_filter = f"where concat(first_name, ' ', last_name) = '{surfer}' "
            surfer_id = inst.select_a_column(table=table,
                                             column=column,
                                             col_filter=col_filter
                                             )[0]

            # Insert into Break Table
            inst = hierarchy.SqlCommands()
            table = 'wsl.heat_results'
            columns = f"heat_id, surfer_in_heat_id, " \
                      f"pick_to_win_percent, jersey_color, status, " \
                      f"wave_1, wave_2, wave_3, wave_4, wave_5, " \
                      f"wave_6, wave_7, wave_8, wave_9, wave_10, " \
                      f"wave_11, wave_12, wave_13, wave_14, wave_15 "
            # noinspection PyBroadException,PyUnboundLocalVariable
            fields = f"{heat_id}, {surfer_id}, " \
                     f"{picked_percent}, '{jersey_color}', '{status}', " \
                     f"{wave_1}, {wave_2}, {wave_3}, {wave_4}, {wave_5}, " \
                     f"{wave_6}, {wave_7}, {wave_8}, {wave_9}, {wave_10}, " \
                     f"{wave_11}, {wave_12}, {wave_13}, {wave_14}, {wave_15}"
            inst.insert_to_table(table=table,
                                 columns=columns,
                                 fields=fields
                                 )
        except:
            print('I went to the fucking except')

        # Clear Everything except tour info
        self.cb_addresults_surfer.clear()

        self.line_addresults_picks.clear()

        self.check_addresults_jersey_yellow.setChecked(0)
        self.check_addresults_jersey_red.setChecked(0)
        self.check_addresults_jersey_black.setChecked(0)
        self.check_addresults_jersey_white.setChecked(0)
        self.check_addresults_jersey_blue.setChecked(0)
        self.check_addresults_jersey_pink.setChecked(0)

        self.check_addresults_advanced.setChecked(0)
        self.check_addresults_eliminated.setChecked(0)

        self.line_addresults_1.clear()
        self.line_addresults_2.clear()
        self.line_addresults_3.clear()
        self.line_addresults_4.clear()
        self.line_addresults_5.clear()
        self.line_addresults_6.clear()
        self.line_addresults_7.clear()
        self.line_addresults_8.clear()
        self.line_addresults_9.clear()
        self.line_addresults_10.clear()
        self.line_addresults_11.clear()
        self.line_addresults_12.clear()
        self.line_addresults_13.clear()
        self.line_addresults_14.clear()
        self.line_addresults_15.clear()

    ####################################################################################################################
    #  Add Break Tab

    # Change Country List when a Continent is selected
    def slot_cb_addbreak_continent_on_index_change(self):
        self.add_region_instance.set_everything_to_none()
        self.cb_addbreak_country.clear()
        self.add_region_instance.selected_continent = self.cb_addbreak_continent.currentText()

        # Add the countries to the country combo box.
        self.cb_addbreak_country.addItems([''] + self.add_region_instance.return_countries())

    # Change Region List when a Country is selected
    def slot_cb_addbreak_country_on_index_change(self):
        self.cb_addbreak_region.clear()
        self.add_region_instance.selected_country = self.cb_addbreak_country.currentText()

        # Add the regions to the add_region_instance combo box.
        self.cb_addbreak_region.addItems([''] + self.add_region_instance.return_regions())

    # Open a PopUp to enter new places when The Add Location Button is selected
    # noinspection PyMethodMayBeStatic
    def slot_pb_addbreak_newloc_clicked(self):
        dialog = AddLocation(title="Add a location to the database.")

        if dialog.exec() == QDialog.Accepted:
            continent = dialog.cb_continent.currentText()

            # Create an instance of SQLCommands to use when entering data to mysql tables
            sql_command_instance = hierarchy.SqlCommands()

            # Check to see if text has been entered in the country line edit, combobox, or neither
            condition_country_line = dialog.line_country.text() != ''
            condition_country_cb = dialog.cb_country.currentText() != ''
            if condition_country_line:
                # Assign the text from the line_edit for country to the variable country
                country = dialog.line_country.text()

                # Pull the continent_id to use when adding the new country to the database
                # Future State: Put a check in here to make sure one continent_id is returned
                continent_id = sql_command_instance.select_a_column(table='wsl.continent',
                                                                    column='continent_id',
                                                                    col_filter=f"where continent = '{continent}' "
                                                                    )[0]

                # Check to see if it's already in wsl.country
                table = 'wsl.country'
                column = 'country, continent_id'
                col_filter = f"where country = '{country}' " \
                             f"and continent_id = {continent_id}"
                inst = hierarchy.SqlCommands()
                dupe = inst.check_for_dupe_add(table=table,
                                               column=column,
                                               col_filter=col_filter
                                               )

                # Add the new country to the table if not a duplicate
                if not dupe:
                    sql_command_instance.insert_to_table(table='wsl.country',
                                                         columns='country, continent_id',
                                                         fields=f"'{country}', {continent_id}"
                                                         )
                    print(f"You have discovered the country of {country} on {continent}")
                else:
                    print(f"You have already discovered the country of {country}")

            elif condition_country_cb:
                country = dialog.cb_country.currentText()
                print(f"Welcome back to {country}")
            else:
                print('Either choose a known Country or discover a new one.')
                raise ValueError

            # If a Region is typed in add it to the region table
            condition_region_line = dialog.line_region.text() != ''
            condition_region_cb = dialog.cb_region.currentText() != ''
            if condition_region_line:
                region = dialog.line_region.text()

                # Pull the continent_id to use when adding the new country to the database
                # Future State: Put a check in here to make sure one continent_id is returned
                country_id = sql_command_instance.select_a_column(table='wsl.country',
                                                                  column='country_id',
                                                                  col_filter=f"where country = '{country}' "
                                                                  )[0]

                # Add the new region to the table
                sql_command_instance.insert_to_table(table='wsl.region',
                                                     columns='region, country_id',
                                                     fields=f"'{region}', {country_id}"
                                                     )
                print(f"You have discovered the region of {region} in {country}")
                # Insert into table
            elif condition_region_cb:
                region = dialog.cb_region.currentText()
                print(f"Welcome back to {region} in {country}")
            else:
                print(f"Either choose a known region in {country} of discover a new one.")
                raise ValueError

            # Check to see if a City was entered
            condition_city_line = dialog.line_city.text() != ''
            if condition_city_line:
                city = dialog.line_city.text()

                # Pull the region_id to use when adding the new country to the database
                # Future State: Put a check in here to make sure one continent_id is returned
                region_id = sql_command_instance.select_a_column(table='wsl.region',
                                                                 column='region_id',
                                                                 col_filter=f"where region = '{region}' "
                                                                 )[0]

                # Add the new city to the table
                sql_command_instance.insert_to_table(table='wsl.city',
                                                     columns='city, region_id',
                                                     fields=f"'{city}', {region_id}"
                                                     )
                print(f"You have discovered the {city}, {region} in {country}")
            else:
                print(f"Discover a new city.")

    # Clear the form when the Clear button is checked
    def slot_pb_addbreak_clear_clicked(self):
        self.cb_addbreak_continent.clear()
        self.cb_addbreak_continent.addItems([''] + self.add_region_instance.return_continents())
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
            ability_list = []
            if self.check_addbreak_ability_green.isChecked():
                ability_list.append('Beginner')
            if self.check_addbreak_ability_yellow.isChecked():
                ability_list.append('Intermediate')
            if self.check_addbreak_ability_red.isChecked():
                ability_list.append('Advanced')

            # Turn List of abilities into a string for mysql table
            ability = ""
            for ind, item in enumerate(ability_list):
                if not ind == (len(ability_list) - 1):
                    ability = ability + item + ', '
                else:
                    ability = ability + item

            # Grab Shoulder Burn based on which color is checked
            shoulder_burn_list = []
            if self.check_addbreak_burn_green.isChecked():
                shoulder_burn_list.append('Light')
            if self.check_addbreak_burn_yellow.isChecked():
                shoulder_burn_list.append('Medium')
            if self.check_addbreak_burn_red.isChecked():
                shoulder_burn_list.append('Exhausting')

            # Turn List of shoulder burn into a string for mysql table
            shoulder_burn = ""
            for ind, item in enumerate(shoulder_burn_list):
                if not ind == (len(shoulder_burn_list) - 1):
                    shoulder_burn = shoulder_burn + item + ', '
                else:
                    shoulder_burn = shoulder_burn + item

            # Grab Break Type based on which types are checked
            break_type_list = []
            if self.check_addbreak_beach.isChecked():
                break_type_list.append('Beach')
            if self.check_addbreak_point.isChecked():
                break_type_list.append('Point')
            if self.check_addbreak_reef.isChecked():
                break_type_list.append('Reef')
            if self.check_addbreak_river.isChecked():
                break_type_list.append('River')
            if self.check_addbreak_sandbar.isChecked():
                break_type_list.append('Sandbar')
            if self.check_addbreak_jetty.isChecked():
                break_type_list.append('Jetty')
            if self.check_addbreak_eng.isChecked():
                break_type_list.append('Engineered')

            # Turn List of breaks into a string for mysql table
            break_type = ""
            for ind, item in enumerate(break_type_list):
                if not ind == (len(break_type_list) - 1):
                    break_type = break_type + item + ', '
                else:
                    break_type = break_type + item

            # Grab Surfability
            clean = self.line_addbreak_clean.text()
            blown_out = self.line_addbreak_blown.text()
            too_small = self.line_addbreak_small.text()

            # Make sure numbers were entered for surfability
            inst = Validations.NumCheck(input_num=clean)
            inst.int_check()
            inst = Validations.NumCheck(input_num=blown_out)
            inst.int_check()
            inst = Validations.NumCheck(input_num=too_small)
            inst.int_check()

            print(f'Continent: {continent}, '
                  f'Country: {country}, '
                  f'Region: {region}, '
                  f'Break: {break_name}')
            print(reliability)
            print(ability_list)
            print(shoulder_burn_list)
            print(break_type_list)
            print(f"Clean: {clean}%  Blown: {blown_out}%  Small: {too_small}%")

        else:
            print('You should probably enter a break name.')

        # Add the Break to wsl.breaks
        # noinspection PyBroadException
        try:
            table = 'wsl.region'
            column = 'region_id'
            # noinspection PyBroadException,PyUnboundLocalVariable
            col_filter = f"where region = '{region}' "
            inst = hierarchy.SqlCommands()
            region_id = inst.select_a_column(table=table,
                                             column=column,
                                             col_filter=col_filter
                                             )[0]
            # Insert into Break Table
            table = 'wsl.break'
            columns = f"break, region_id, break_type, " \
                      f"reliability, ability, shoulder_burn, " \
                      f"clean, blown_out, too_small"
            # noinspection PyBroadException,PyUnboundLocalVariable
            fields = f"'{break_name}', {region_id}, '{break_type}', " \
                     f"'{reliability}', '{ability}', '{shoulder_burn}', " \
                     f"{clean}, {blown_out}, {too_small}"
            inst.insert_to_table(table=table,
                                 columns=columns,
                                 fields=fields
                                 )
        except:
            print('I went to the fucking except')

        # Clear Form on Submit
        self.slot_pb_addbreak_clear_clicked()

    ####################################################################################################################
    # Add Surfer Tab

    # Change Country List when Continent is Selected
    def slot_cb_addsurfer_continent_on_index_change(self):

        # Set up and instance of the Region Class
        self.add_region_instance.set_everything_to_none()
        self.cb_addsurfer_country.clear()
        self.add_region_instance.selected_continent = self.cb_addsurfer_continent.currentText()

        # Add the countries to the country combo box.
        self.cb_addsurfer_country.addItems([''] + self.add_region_instance.return_countries())

    # Change Home Country List when Home Continent is Selected
    def slot_cb_addsurfer_hcontinent_on_index_change(self):

        # Set up and instnace of the Region Class
        self.add_region_instance.set_everything_to_none()
        self.cb_addsurfer_hcountry.clear()
        self.add_region_instance.selected_continent = self.cb_addsurfer_hcontinent.currentText()

        # Add the countries to the country combo box.
        self.cb_addsurfer_hcountry.addItems([''] + self.add_region_instance.return_countries())

    # Change Home Region List when Home Country is Selected
    def slot_cb_addsurfer_hcountry_on_index_change(self):
        self.cb_addsurfer_hregion.clear()
        self.add_region_instance.selected_country = self.cb_addsurfer_hcountry.currentText()

        # Add the regions to the add_region_instance combo box.
        self.cb_addsurfer_hregion.addItems([''] + self.add_region_instance.return_regions())

    # Change Home City List when Home Region is Selected
    def slot_cb_addsurfer_hregion_on_index_change(self):
        self.cb_addsurfer_hcity.clear()
        self.add_region_instance.selected_region = self.cb_addsurfer_hregion.currentText()

        # Add the regions to the add_region_instance combo box.
        self.cb_addsurfer_hcity.addItems([''] + self.add_region_instance.return_cities())

    # TourName Handler for Clear Button Clicked
    def slot_pb_addsurfer_clear_clicked(self):
        self.line_addsurfer_firstname.clear()
        self.line_addsurfer_lastname.clear()
        self.check_addsurfer_goofy.setChecked(0)
        self.check_addsurfer_regular.setChecked(0)
        self.cb_addsurfer_continent.clear()
        self.cb_addsurfer_continent.addItems([''] + self.add_region_instance.return_continents())
        self.cb_addsurfer_country.clear()
        self.line_addsurfer_bday.clear()
        self.line_addsurfer_ht.clear()
        self.line_addsurfer_wt.clear()
        self.line_addsurfer_firstseason.clear()
        self.line_addsurfer_firsttour.clear()
        self.cb_addsurfer_hcontinent.clear()
        self.cb_addsurfer_hcontinent.addItems([''] + self.add_region_instance.return_continents())
        self.cb_addsurfer_hcountry.clear()
        self.cb_addsurfer_hregion.clear()
        self.cb_addsurfer_hcity.clear()
        self.check_addsurfer_male.setChecked(0)
        self.check_addsurfer_female.setChecked(0)

    # TourName Handler for Add Location Button Clicked
    def slot_pb_addsurfer_newloc_clicked(self):
        self.slot_pb_addbreak_newloc_clicked()

    # TourName Handler for Submit Button Clicked
    def slot_pb_addsurfer_submit_clicked(self):

        # Check to Make Sure a First and Last Name are entered
        condition_1 = self.line_addsurfer_firstname.text() == ''
        condition_2 = self.line_addsurfer_lastname.text() == ''
        if not condition_1 and not condition_2:
            print(f"You're not a complete fuck up. You entered a first and last name!")
        else:
            print(f"Enter a first and last name. Don't be a piece of shit.")
            return None

        # Grab First and Last Name
        first_name = self.line_addsurfer_firstname.text()
        last_name = self.line_addsurfer_lastname.text()

        # Determine Stance
        if self.check_addsurfer_regular.isChecked():
            stance = 'Regular'
        elif self.check_addsurfer_goofy.isChecked():
            stance = 'Goofy'
        else:
            stance = ' '

        # Find Country they represent
        rep_country = self.cb_addsurfer_country.currentText()

        # Grab birthday and turn into correct format for sql
        birthday = Validations.DateCheck.date_check(
            input_dt=self.line_addsurfer_bday.text()
        )

        # Grab Height and Weight and check to see if they are numbers
        if self.line_addsurfer_ht.text() == '':
            height = '0'
        else:
            height = self.line_addsurfer_ht.text()
            inst = Validations.NumCheck(input_num=height)
            inst.int_check()
        if self.line_addsurfer_wt.text() == '':
            weight = '0'
        else:
            weight = self.line_addsurfer_wt.text()
            inst = Validations.NumCheck(input_num=weight)
            inst.int_check()

        # Grab first season and tour
        if self.line_addsurfer_firstseason.text() == '':
            first_season = '1900'
        else:
            first_season = self.line_addsurfer_firstseason.text()
        if self.line_addsurfer_firsttour.text() == '':
            first_tour = ' '
        else:
            first_tour = self.line_addsurfer_firsttour.text()

        # Make sure first season has a length of 4 and is an integer
        if not first_season == '':
            if len(first_season) == 4:
                pass
            else:
                "First Season must be a year in form YYYY"
        inst = Validations.NumCheck(input_num=first_season)
        inst.int_check()

        # Grab Home City
        if self.cb_addsurfer_hcity.currentText() == '':
            home_city = ' '
        else:
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

        # Add the Break to wsl.surfers
        try:
            # Need to grab country id tied to rep country
            table = 'wsl.country'
            column = 'country_id'
            col_filter = f"where country = '{rep_country}'"
            inst = hierarchy.SqlCommands()
            country_id = inst.select_a_column(table=table,
                                              column=column,
                                              col_filter=col_filter
                                              )[0]

            # Need to grab city id tied to home city
            table = 'wsl.city'
            column = 'city_id'
            if home_city == '':
                col_filter = f"where city = 'Unknown' "
            else:
                col_filter = f"where city = '{home_city}' "
            inst = hierarchy.SqlCommands()
            home_city_id = inst.select_a_column(table=table,
                                                column=column,
                                                col_filter=col_filter
                                                )[0]
            # Insert into Surfers Table
            table = 'wsl.surfers'
            columns = f"gender, first_name, last_name, stance, rep_country_id, " \
                      f"birthday, height, weight, " \
                      f"first_season, first_tour, home_city_id"
            fields = f"'{gender}', '{first_name}', '{last_name}', '{stance}', {country_id}, " \
                     f"'{birthday}', {height}, {weight}, " \
                     f"{first_season}, '{first_tour}', {home_city_id}"
            inst.insert_to_table(table=table,
                                 columns=columns,
                                 fields=fields
                                 )
        except:
            print('I went to the fucking except when trying to add a new surfer.')

        # Clear Everything on Submit
        self.slot_pb_addsurfer_clear_clicked()

    ####################################################################################################################


########################################################################################################################

if __name__ == '__main__':
    app = QApplication([])
    win = MainWidget()
    win.show()

    sys.exit(app.exec())
