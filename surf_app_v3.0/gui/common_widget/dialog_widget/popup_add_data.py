import sys
from typing import Optional

import PyQt5.QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QApplication, QDialogButtonBox

from src import hierarchy
from src.hierarchy import Region, Event, Heat


########################################################################################################################

class AddLocation(QDialog, Region):
    def __init__(self,
                 title,
                 left=10,
                 top=10,
                 width=520,
                 height=400,
                 sql_host_name: Optional[str] = None,
                 sql_user_name: Optional[str] = None,
                 sql_password: Optional[str] = None,
                 prev_selected_continent: Optional[str] = None,
                 prev_selected_country: Optional[str] = None,
                 prev_selected_region: Optional[str] = None,
                 parent=None):
        # Calls constructor for QDialog
        QDialog.__init__(self, parent=parent)

        # Calls the constructor for the Region Class
        Region.__init__(self,
                        sql_host_name=sql_host_name,
                        sql_user_name=sql_user_name,
                        sql_password=sql_password
                        )

        self.prev_selected_continent: Optional[str] = prev_selected_continent
        self.prev_selected_country: Optional[str] = prev_selected_country
        self.prev_selected_region: Optional[str] = prev_selected_region

        # Set Title of the QDialog.
        self.setWindowTitle(title)

        # Set Geometry of the QDialog.
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.setGeometry(left, top, width, height)

        # Disable x button to force "yes" or "no" click
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        # Disable help button
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)

        # Set this custom widget's parent, if it was passed to the constructor function (not None).
        if not(parent is None):
            self.setParent(parent)

        # Create Vertical Layout Box.
        self.layout = QVBoxLayout()

        # Create Horizontal Layouts.
        self.hlayout_continent = QHBoxLayout()
        self.hlayout_country = QHBoxLayout()
        self.hlayout_region = QHBoxLayout()
        self.hlayout_city = QHBoxLayout()

        # Continent Label and Combobox
        self.hlayout_continent.addWidget(QLabel("Continent:"))
        self.cb_continent = PyQt5.QtWidgets.QComboBox()
        self.hlayout_continent.addWidget(self.cb_continent)
        self.cb_continent.setFixedWidth(200)
        self.hlayout_continent.addWidget(QLabel(''))
        self.layout.addLayout(self.hlayout_continent)

        # Country Label and Line Edit
        self.hlayout_country.addWidget(QLabel("Country:"))
        self.cb_country = PyQt5.QtWidgets.QComboBox()
        self.hlayout_country.addWidget(self.cb_country)
        self.cb_country.setFixedWidth(200)
        self.line_country = PyQt5.QtWidgets.QLineEdit()
        self.hlayout_country.addWidget(self.line_country)
        self.line_country.setFixedWidth(200)

        self.layout.addLayout(self.hlayout_country)

        # Region Label and Line Edit
        self.hlayout_region.addWidget(QLabel("Region:"))

        self.cb_region = PyQt5.QtWidgets.QComboBox()
        self.hlayout_region.addWidget(self.cb_region)
        self.cb_region.clear()
        # self.cb_region.addItems()
        self.cb_region.setFixedWidth(200)

        self.line_region = PyQt5.QtWidgets.QLineEdit()
        self.hlayout_region.addWidget(self.line_region)
        self.line_region.setFixedWidth(200)

        self.layout.addLayout(self.hlayout_region)

        # City Label and Line Edit
        self.hlayout_city.addWidget(QLabel("City:"))
        self.line_city = PyQt5.QtWidgets.QLineEdit()
        self.hlayout_city.addWidget(self.line_city)
        self.line_city.setFixedWidth(200)
        self.hlayout_city.addWidget(QLabel(''))
        self.layout.addLayout(self.hlayout_city)

        q_btn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.ButtonBox = QDialogButtonBox(q_btn)
        self.ButtonBox.accepted.connect(self.accept)
        self.ButtonBox.rejected.connect(self.reject)
        self.layout.addWidget(self.ButtonBox)

        self.setLayout(self.layout)

        self.on_startup()

        self.connect_slots()

    # This defines the event handlers for everything.
    def connect_slots(self):
        self.cb_continent.currentIndexChanged.connect(self.slot_cb_continent_on_index_change)
        self.cb_country.currentIndexChanged.connect(self.slot_cb_country_on_index_change)

    # This setups up everything at the first startup.
    def on_startup(self):

        # If a Continent been selected from the previous tab add it on startup.
        if self.prev_selected_continent is None or self.prev_selected_continent == "":
            self.cb_continent.addItems([''] + self.return_continents())
        else:
            self.cb_continent.addItem(self.prev_selected_continent)

        # If a Country has been selected from the previous tab add it on startup
        if self.prev_selected_country is not None and self.prev_selected_country != "":
            self.cb_country.addItem(self.prev_selected_country)
        else:
            self.slot_cb_continent_on_index_change()

        # If a Country has been selected from the previous tab add it on startup
        if self.prev_selected_region is not None and self.prev_selected_region != "":
            self.cb_region.addItem(self.prev_selected_region)
        else:
            self.slot_cb_country_on_index_change()

    # Change Country when Continent is selected
    def slot_cb_continent_on_index_change(self):
        self.set_everything_to_none()
        self.cb_country.clear()

        # Set value of the selected_continent variable in add_region_instnace to text in continent combobox
        self.selected_continent = self.cb_continent.currentText()

        # Add the countries to the country combo box.
        self.cb_country.addItems([''] + self.return_countries())

    # Change Region when Country is selected
    def slot_cb_country_on_index_change(self):
        # Set all the instance variables in the instance of the Region class to None, by calling a function in the
        # add_region_instance instance.
        self.set_everything_to_none()

        # Clear the country combo boxs.
        self.cb_region.clear()
        self.selected_country = self.cb_country.currentText()
        self.cb_region.addItems([''] + self.return_regions())

########################################################################################################################


class AddTourType(QDialog, Region):
    def __init__(self,
                 title,
                 left=10,
                 top=10,
                 width=520,
                 height=400,
                 sql_host_name: Optional[str] = None,
                 sql_user_name: Optional[str] = None,
                 sql_password: Optional[str] = None,
                 parent=None):
        # Calls constructor for QDialog
        QDialog.__init__(self, parent=parent)

        # Calls the constructor for the Region Class
        Region.__init__(self,
                        sql_host_name=sql_host_name,
                        sql_user_name=sql_user_name,
                        sql_password=sql_password)

        # Set Title of the QDialog.
        self.setWindowTitle(title)

        # Set Geometry of the QDialog.
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.setGeometry(left, top, width, height)

        # Disable x button to force "yes" or "no" click
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        # Disable help button
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)

        # Set this custom widget's parent, if it was passed to the constructor function (not None).
        if not(parent is None):
            self.setParent(parent)

        # Create Vertical Layout Box.
        self.layout = QVBoxLayout()

        # Create Horizontal Layouts.
        self.vlayout_tour = QVBoxLayout()

        # Tour Gender CheckBox
        self.chkbox_men = PyQt5.QtWidgets.QCheckBox()
        self.chkbox_men.setText("Men")
        self.chkbox_women = PyQt5.QtWidgets.QCheckBox()
        self.chkbox_women.setText("Women")
        self.vlayout_tour.addWidget(self.chkbox_men)
        self.vlayout_tour.addWidget(self.chkbox_women)

        # Tour Year Label and Combobox
        self.vlayout_tour.addWidget(QLabel("Tour Year:"))
        self.line_year = PyQt5.QtWidgets.QLineEdit()
        self.vlayout_tour.addWidget(self.line_year)
        self.line_year.setFixedWidth(200)
        self.vlayout_tour.addWidget(QLabel(''))

        # Continent Label and Combobox
        self.vlayout_tour.addWidget(QLabel("Tour Type:"))
        self.line_tourtype = PyQt5.QtWidgets.QLineEdit()
        self.vlayout_tour.addWidget(self.line_tourtype)
        self.line_tourtype.setFixedWidth(200)
        self.vlayout_tour.addWidget(QLabel(''))
        self.layout.addLayout(self.vlayout_tour)

        q_btn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.ButtonBox = QDialogButtonBox(q_btn)
        self.ButtonBox.accepted.connect(self.accept)
        self.ButtonBox.rejected.connect(self.reject)
        self.layout.addWidget(self.ButtonBox)

        self.setLayout(self.layout)


class AddEventType(QDialog, Event):
    def __init__(self,
                 title,
                 left=10,
                 top=10,
                 width=520,
                 height=400,
                 sql_host_name: Optional[str] = None,
                 sql_user_name: Optional[str] = None,
                 sql_password: Optional[str] = None,
                 parent=None):
        # Calls constructor for QDialog
        QDialog.__init__(self, parent=parent)

        # Calls the constructor for the Event Class
        Event.__init__(self,
                       sql_host_name=sql_host_name,
                       sql_user_name=sql_user_name,
                       sql_password=sql_password)

        # Set Title of the QDialog.
        self.setWindowTitle(title)

        # Set Geometry of the QDialog.
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.setGeometry(left, top, width, height)

        # Disable x button to force "yes" or "no" click
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        # Disable help button
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)

        # Set this custom widget's parent, if it was passed to the constructor function (not None).
        if not(parent is None):
            self.setParent(parent)

        # Create Vertical Layout Box.
        self.layout = QVBoxLayout()

        # Create Horizontal Layouts.
        self.vlayout_round = QVBoxLayout()

        # Event Label and Combobox
        self.vlayout_round.addWidget(QLabel("Round Type:"))
        self.line_round = PyQt5.QtWidgets.QLineEdit()
        self.vlayout_round.addWidget(self.line_round)
        self.line_round.setFixedWidth(200)
        self.vlayout_round.addWidget(QLabel(''))
        self.layout.addLayout(self.vlayout_round)

        q_btn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.ButtonBox = QDialogButtonBox(q_btn)
        self.ButtonBox.accepted.connect(self.accept)
        self.ButtonBox.rejected.connect(self.reject)
        self.layout.addWidget(self.ButtonBox)

        self.setLayout(self.layout)

        ################################################################################################################


class SurferToHeat(QDialog, Event):
    def __init__(self,
                 title,
                 left=10,
                 top=10,
                 width=520,
                 height=400,
                 sql_host_name: Optional[str] = None,
                 sql_user_name: Optional[str] = None,
                 sql_password: Optional[str] = None,
                 prev_selected_year: Optional[str] = None,
                 prev_selected_tour: Optional[str] = None,
                 prev_selected_event: Optional[str] = None,
                 prev_selected_round: Optional[str] = None,
                 prev_selected_heat: Optional[str] = None,
                 parent=None):
        # Calls constructor for QDialog
        QDialog.__init__(self, parent=parent)

        # Calls the constructor for the Region Class
        Event.__init__(self,
                       sql_host_name=sql_host_name,
                       sql_user_name=sql_user_name,
                       sql_password=sql_password)

        self.prev_selected_year: Optional[str] = prev_selected_year
        self.prev_selected_tour: Optional[str] = prev_selected_tour
        self.prev_selected_event: Optional[str] = prev_selected_event
        self.prev_selected_round: Optional[str] = prev_selected_round
        self.prev_selected_heat: Optional[str] = prev_selected_heat

        # Set Title of the QDialog.
        self.setWindowTitle(title)

        # Set Geometry of the QDialog.
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.setGeometry(left, top, width, height)

        # Disable x button to force "yes" or "no" click
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        # Disable help button
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)

        # Set this custom widget's parent, if it was passed to the constructor function (not None).
        if not (parent is None):
            self.setParent(parent)

        # Create Vertical Layout Box.
        self.layout = QVBoxLayout()

        # Create Horizontal Layouts.
        self.hlayout_year = QHBoxLayout()

        # Tour Year Label and Combobox
        self.hlayout_year.addWidget(QLabel("Tour Year:"))
        self.cb_year = PyQt5.QtWidgets.QComboBox()
        self.hlayout_year.addWidget(self.cb_year)
        self.cb_year.setFixedWidth(200)
        self.hlayout_year.addWidget(QLabel(''))
        self.layout.addLayout(self.hlayout_year)

        # Create Horizontal Layouts.
        self.hlayout_tour = QHBoxLayout()

        # Tour Year Label and Combobox
        self.hlayout_tour.addWidget(QLabel("Tour Name:"))
        self.cb_tour = PyQt5.QtWidgets.QComboBox()
        self.hlayout_tour.addWidget(self.cb_tour)
        self.cb_tour.setFixedWidth(200)
        self.hlayout_tour.addWidget(QLabel(''))
        self.layout.addLayout(self.hlayout_tour)

        # Create Horizontal Layouts.
        self.hlayout_event = QHBoxLayout()

        # Tour Year Label and Combobox
        self.hlayout_event.addWidget(QLabel("Event:"))
        self.cb_event = PyQt5.QtWidgets.QComboBox()
        self.hlayout_event.addWidget(self.cb_event)
        self.cb_event.setFixedWidth(200)
        self.hlayout_event.addWidget(QLabel(''))
        self.layout.addLayout(self.hlayout_event)

        # Create Horizontal Layouts.
        self.hlayout_round = QHBoxLayout()

        # Tour Year Label and Combobox
        self.hlayout_round.addWidget(QLabel("Round:"))
        self.cb_round = PyQt5.QtWidgets.QComboBox()
        self.hlayout_round.addWidget(self.cb_round)
        self.cb_round.setFixedWidth(200)
        self.hlayout_round.addWidget(QLabel(''))
        self.layout.addLayout(self.hlayout_round)

        # Create Horizontal Layouts.
        self.hlayout_heat = QHBoxLayout()

        # Tour Year Label and Combobox
        self.hlayout_heat.addWidget(QLabel("Heat:"))
        self.cb_heat = PyQt5.QtWidgets.QComboBox()
        self.hlayout_heat.addWidget(self.cb_heat)
        self.cb_heat.setFixedWidth(200)
        self.hlayout_heat.addWidget(QLabel(''))
        self.layout.addLayout(self.hlayout_heat)

        # Create Horizontal Layouts.
        self.hlayout_surfer = QHBoxLayout()

        # Tour Year Label and Combobox
        self.hlayout_surfer.addWidget(QLabel("Surfer:"))
        self.cb_surfer = PyQt5.QtWidgets.QComboBox()
        self.hlayout_surfer.addWidget(self.cb_surfer)
        self.cb_surfer.setFixedWidth(200)
        self.hlayout_surfer.addWidget(QLabel(''))
        self.layout.addLayout(self.hlayout_surfer)

        # Add Button To Submit Data to Table
        self.add_surfer = PyQt5.QtWidgets.QPushButton("Add to Round")
        self.add_surfer.setFixedWidth(200)
        self.add_surfer.setFixedHeight(50)
        self.add_surfer.setDefault(True)
        # self.add_surfer.clicked.connect(lambda: self.whichbtn(self.b4))
        self.layout.addWidget(self.add_surfer)

        q_btn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.ButtonBox = QDialogButtonBox(q_btn)
        self.ButtonBox.accepted.connect(self.accept)
        self.ButtonBox.rejected.connect(self.reject)
        self.layout.addWidget(self.ButtonBox)

        self.setLayout(self.layout)

        self.connect_slots()

        # Sql Connection Variables
        self.__sql_user: str = "Heather"
        self.__sql_password: str = "#LAwaItly19"
        self.__sql_host: str = "localhost"

        # Instance of Heat Class.
        self.add_heat_instance: Heat = Heat(
            sql_host_name=self.__sql_host,
            sql_password=self.__sql_password,
            sql_user_name=self.__sql_user
        )

        # Instance of SQLCommands Class.
        self.add_sql_command_instance: hierarchy.SqlCommands = hierarchy.SqlCommands(
            sql_host_name=self.__sql_host,
            sql_password=self.__sql_password,
            sql_user_name=self.__sql_user
        )

        self.on_startup()

    ####################################################################################################################
    def connect_slots(self):
        pass
        self.cb_year.currentIndexChanged.connect(self.slot_cb_year_on_index_change)
        self.cb_tour.currentIndexChanged.connect(self.slot_cb_tour_name_on_index_change)
        self.cb_event.currentIndexChanged.connect(self.slot_cb_event_round_name_on_index_change)
        self.cb_round.currentIndexChanged.connect(self.slot_cb_event_heat_name_on_index_change)

        self.add_surfer.clicked.connect(self.slot_add_surfer_clicked)

    ####################################################################################################################
    def on_startup(self):

        # If a Year been selected from the previous tab add it on startup.
        if self.prev_selected_year is None or self.prev_selected_year == "":
            self.cb_year.addItems([''] + self.return_tour_years())
        else:
            self.cb_year.addItem(self.prev_selected_year)

        # If a Tour has been selected from the previous tab add it on startup
        if self.prev_selected_tour is not None and self.prev_selected_tour != "":
            self.cb_tour.clear()
            self.cb_tour.addItem(self.prev_selected_tour)
        else:
            self.slot_cb_year_on_index_change()

        # If an Event has been selected from the previous tab add it on startup
        if self.prev_selected_event is not None and self.prev_selected_event != "":
            self.cb_event.clear()
            self.cb_event.addItem(self.prev_selected_event)
        else:
            self.slot_cb_tour_name_on_index_change()

        # If a Round has been selected from the previous tab add it on startup
        if self.prev_selected_round is not None and self.prev_selected_round != "":
            self.cb_round.clear()
            self.cb_round.addItem(self.prev_selected_round)
        else:
            self.slot_cb_event_round_name_on_index_change()

        # If a Heat has been selected from the previous tab add it on startup
        if self.prev_selected_heat is not None and self.prev_selected_heat != "":
            self.cb_heat.clear()
            self.cb_heat.addItem(self.prev_selected_heat)
        else:
            self.slot_cb_event_heat_name_on_index_change()

        # Add Surfers to Drop Down
        inst = hierarchy.SqlCommands()
        surfers = inst.select_a_column(
            table='wsl.surfers',
            column=f"concat(first_name, ' ', last_name) as name",
            col_filter=''
        )
        surfers.sort()
        self.cb_surfer.addItems([''] + surfers)

        # put blank stings in all combo boxes besides year
        self.cb_tour.addItems([''])
        self.cb_event.addItems([''])
        self.cb_round.addItems([''])
        self.cb_heat.addItems([''])
        self.cb_surfer.addItems([''])

    ####################################################################################################################

    def slot_cb_year_on_index_change(self):
        self.cb_tour.clear()
        self.add_heat_instance.selected_tour_year = self.cb_year.currentText()
        self.cb_tour.addItems(self.add_heat_instance.return_tours())

    def slot_cb_tour_name_on_index_change(self):
        self.cb_event.clear()
        self.add_heat_instance.selected_tour_name = self.cb_tour.currentText()
        self.cb_event.addItems([''] + self.add_heat_instance.return_events())

    def slot_cb_event_round_name_on_index_change(self):
        self.cb_round.clear()
        self.add_heat_instance.selected_event = self.cb_event.currentText()
        self.cb_round.addItems(([''] + self.add_heat_instance.return_all_rounds()))

    def slot_cb_event_heat_name_on_index_change(self):
        self.cb_heat.clear()
        self.add_heat_instance.selected_tour_name = self.cb_tour.currentText()
        self.add_heat_instance.selected_event = self.cb_event.currentText()
        self.add_heat_instance.selected_round = self.cb_round.currentText()
        self.cb_heat.addItems([''] + self.add_heat_instance.return_heats())

    def slot_add_surfer_clicked(self):

        # Check that tour name, event, round, heat, and surfer are entered
        if self.cb_tour.currentText() == '':
            print("How the fuck do I know which tour to add the surfer to?")
        if self.cb_event.currentText() == '':
            print(f"Which event in {self.cb_tour} should I add the surfer to?")
        if self.cb_round.currentText() == '':
            print(f"Which round in {self.cb_event} should I add the surfer to?")
        if self.cb_heat.currentText() == '':
            print(f"Which heat in {self.cb_event} in the {self.cb_round} should the surfer be added to?")
        if self.cb_surfer.currentText() == '':
            print(f"What's the surfer's name, dude?")

        # Assign Value to Round and Surfer
        tour_name = self.cb_tour.currentText()
        event_name = self.cb_event.currentText()
        round_name = self.cb_round.currentText()
        heat_nbr = self.cb_heat.currentText()
        surfer = self.cb_surfer.currentText()

        try:
            # Need to grab tour id
            inst = hierarchy.SqlCommands()
            table = 'wsl.tour'
            column = 'tour_id'
            col_filter = f"where tour_name = '{tour_name}' "
            tour_id = inst.select_a_column(table=table,
                                           column=column,
                                           col_filter=col_filter
                                           )[0]

            # Need to grab event id
            inst = hierarchy.SqlCommands()
            table = 'wsl.event'
            column = 'event_id'
            col_filter = f"where tour_id = {tour_id} " \
                         f"and event_name = '{event_name}' "
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

            # Need to grab heat_id tied to event that needs to be added
            inst = hierarchy.SqlCommands()
            table = 'wsl.heat_details'
            column = 'heat_id'
            col_filter = f"where heat_nbr = {heat_nbr} " \
                         f"and event_id = {event_id} " \
                         f"and round_id = {round_id} "
            heat_id = inst.select_a_column(table=table,
                                           column=column,
                                           col_filter=col_filter
                                           )[0]

            # Need to Grab surfer_id
            inst = hierarchy.SqlCommands()
            table = 'wsl.surfers'
            column = 'surfer_id'
            col_filter = f"where concat(first_name, ' ', last_name) = '{surfer}' "
            surfer_id = inst.select_a_column(table=table,
                                             column=column,
                                             col_filter=col_filter
                                             )[0]

            # Check to see if surfer has already been added to the heat
            table = 'wsl.heat_surfers'
            column = 'heat_id, surfer_id'
            col_filter = f"where heat_id = {heat_id} " \
                         f"and surfer_id = {surfer_id}"
            inst = hierarchy.SqlCommands()
            dupe = inst.check_for_dupe_add(table=table,
                                           column=column,
                                           col_filter=col_filter
                                           )

            # Insert into Heat Surfers Table if not a duplicate
            if not dupe:
                table = 'wsl.heat_surfers'
                columns = f"heat_id, surfer_id"
                fields = f"{heat_id}, '{surfer_id}'"
                inst.insert_to_table(table=table,
                                     columns=columns,
                                     fields=fields
                                     )

            else:
                print(f"{surfer} has already been added to heat number {heat_nbr}.")

        except:
            print('I went to the goddamn except')

        self.cb_surfer.clear()

########################################################################################################################


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = AddLocation(title='Add a New Location',
                      sql_user_name="Heather",
                      sql_password="#LAwaItly19",
                      sql_host_name="localhost"
                      )
    win.show()

    sys.exit(app.exec())
