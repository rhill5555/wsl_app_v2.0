import sys
from typing import Optional

import PyQt5.QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QApplication, QDialogButtonBox

from src import hierarchy
from src.hierarchy import Region, Event


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
        self.hlayout_continent = QHBoxLayout()
        self.hlayout_country = QHBoxLayout()
        self.hlayout_region = QHBoxLayout()
        self.hlayout_city = QHBoxLayout()

        # Continent Label and Combobox
        self.hlayout_continent.addWidget(QLabel("Continent:"))
        self.cb_continent = PyQt5.QtWidgets.QComboBox()
        self.hlayout_continent.addWidget(self.cb_continent)
        # self.cb_continent.clear()
        # self.cb_continent.addItems(
        #     [item for item in Places.continent(mysql_connection=mysql_conn)]
        # )
        self.cb_continent.setFixedWidth(200)
        self.hlayout_continent.addWidget(QLabel(''))
        self.layout.addLayout(self.hlayout_continent)

        # Country Label and Line Edit
        self.hlayout_country.addWidget(QLabel("Country:"))
        self.cb_country = PyQt5.QtWidgets.QComboBox()
        self.hlayout_country.addWidget(self.cb_country)
        # self.cb_country.clear()
        # self.cb_country.addItems(
        #     [item[0] for item in Places.countries(mysql_connection=mysql_conn,
        #                                           continent=self.cb_continent.currentText())])
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

        Q_Btn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.ButtonBox = QDialogButtonBox(Q_Btn)
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
        # Add Continents to the combobox.
        self.cb_continent.addItems(self.return_continents())

    # Change Country when Continent is selected
    def slot_cb_continent_on_index_change(self):
        # Set all the instance variables in the instance of the Region class to None, by calling a function in the
        # add_region_instance instance.
        self.set_everything_to_none()

        # Clear the country combo boxs.
        self.cb_country.clear()

        # Set the current value of the selected_continent variable in add_region_instance to the current text in the continent
        # combo box.
        self.selected_continent = self.cb_continent.currentText()

        # Add the countries to the country combo box.
        self.cb_country.addItems(self.return_countries())

    # Change Region when Country is selected
    def slot_cb_country_on_index_change(self):
        # Set all the instance variables in the instance of the Region class to None, by calling a function in the
        # add_region_instance instance.
        self.set_everything_to_none()

        # Clear the country combo boxs.
        self.cb_region.clear()

        # Set the current value of the selected_continent variable in add_region_instance to the current text in the continent
        # combo box.
        self.selected_country = self.cb_country.currentText()

        # Add the countries to the country combo box.
        self.cb_region.addItems(self.return_regions())

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

        Q_Btn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.ButtonBox = QDialogButtonBox(Q_Btn)
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
        self.vlayout_round.addWidget(QLabel("Event Type:"))
        self.line_round = PyQt5.QtWidgets.QLineEdit()
        self.vlayout_round.addWidget(self.line_round)
        self.line_round.setFixedWidth(200)
        self.vlayout_round.addWidget(QLabel(''))
        self.layout.addLayout(self.vlayout_round)

        Q_Btn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.ButtonBox = QDialogButtonBox(Q_Btn)
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
                 parent=None):
        # Calls constructor for QDialog
        QDialog.__init__(self, parent=parent)

        # Calls the constructor for the Region Class
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
        self.hlayout_event.addWidget(QLabel("TourName:"))
        self.cb_event = PyQt5.QtWidgets.QComboBox()
        self.hlayout_event.addWidget(self.cb_event)
        self.cb_event.setFixedWidth(200)
        self.hlayout_event.addWidget(QLabel(''))
        self.layout.addLayout(self.hlayout_event)

        # Create Horizontal Layouts.
        self.hlayout_round = QHBoxLayout()

        # Tour Year Label and Combobox
        self.hlayout_round.addWidget(QLabel("Event:"))
        self.cb_round = PyQt5.QtWidgets.QComboBox()
        self.hlayout_round.addWidget(self.cb_round)
        self.cb_round.setFixedWidth(200)
        self.hlayout_round.addWidget(QLabel(''))
        self.layout.addLayout(self.hlayout_round)

        # Create Horizontal Layouts.
        self.hlayout_heat = QHBoxLayout()

        # Tour Year Label and Combobox
        self.hlayout_heat.addWidget(QLabel("Round:"))
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

        Q_Btn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.ButtonBox = QDialogButtonBox(Q_Btn)
        self.ButtonBox.accepted.connect(self.accept)
        self.ButtonBox.rejected.connect(self.reject)
        self.layout.addWidget(self.ButtonBox)

        self.setLayout(self.layout)

        self.connect_slots()

        # Sql Connection Variables
        self.__sql_user: str = "Heather"
        self.__sql_password: str = "#LAwaItly19"
        self.__sql_host: str = "localhost"

        # Instance of TourYear Class.
        self.add_heat_round_instance: Event = Event(
            sql_host_name=self.__sql_host,
            sql_password=self.__sql_password,
            sql_user_name=self.__sql_user
        )

        self.on_startup()

    ####################################################################################################################
    def connect_slots(self):

        self.cb_year.currentIndexChanged.connect(self.slot_cb_year_on_index_change)
        self.cb_tour.currentIndexChanged.connect(self.slot_cb_tour_name_on_index_change)
        self.cb_event.currentIndexChanged.connect(self.slot_cb_event_round_name_on_index_change)
        self.cb_round.currentIndexChanged.connect(self.slot_cb_event_heat_name_on_index_change)

        self.add_surfer.clicked.connect(self.slot_add_surfer_clicked)

    ####################################################################################################################
    def on_startup(self):

        # Add Tour Years
        inst = Places.Event()
        self.cb_year.addItems([''] + inst.return_tour_years())

        # Add Surfers to Drop Down
        inst = Places.SqlCommands
        self.cb_surfer.addItems([''] + inst.select_a_column(self,
            table='wsl.surfers',
            column=f"concat(first_name, ' ', last_name) as name",
            col_filter=''
        ))

        # put blank stings in all combo boxes besides year
        self.cb_tour.addItems([''])
        self.cb_event.addItems([''])
        self.cb_round.addItems([''])
        self.cb_heat.addItems([''])
        self.cb_surfer.addItems([''])

    ####################################################################################################################

    def slot_cb_year_on_index_change(self):
        inst = Places.Event()
        inst.set_everything_to_none()

        self.cb_tour.clear()

        self.cb_tour.addItems([''] + self.return_tour_names_by_year(year=self.cb_year.currentText()))

    def slot_cb_tour_name_on_index_change(self):
        self.cb_event.clear()

        self.add_heat_round_instance.selected_tourname = self.cb_tour.currentText()

        self.cb_event.addItems([''] + self.add_heat_round_instance.return_events())

    def slot_cb_event_round_name_on_index_change(self):
        self.cb_round.clear()

        self.cb_round.addItems(([''] + self.add_heat_round_instance.return_rounds()))

    def slot_cb_event_heat_name_on_index_change(self):
        self.cb_heat.clear()

        self.add_heat_round_instance.selected_event = self.cb_event.currentText()
        self.add_heat_round_instance.selected_round = self.cb_round.currentText()

        self.cb_heat.addItems([''] + self.add_heat_round_instance.return_heats())

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
        heat_nbr = self.cb_heat.currentText()
        surfer = self.cb_surfer.currentText()

        try:
            # Need to grab event_id tied to event that needs to be added
            inst = hierarchy.SqlCommands()
            table = 'wsl.heats'
            column = 'event_id'
            col_filter = f"where heat_nbr = {heat_nbr} "
            heat_id = inst.select_a_column(table=table,
                                            column=column,
                                            col_filter=col_filter
                                            )[0]

            print(f"Round ID: {heat_id}")

            # Insert into Events Table
            table = 'wsl.heat_surfers'
            columns = f"heat_id, surfer"
            fields = f"{heat_id}, '{surfer}'"
            inst.insert_to_table(table=table,
                                 columns=columns,
                                 fields=fields
                                 )
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