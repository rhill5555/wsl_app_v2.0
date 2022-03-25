import sys
from typing import Optional

import PyQt5.QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QApplication, QDialogButtonBox
from src.Places import Region


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
        # add_break_region_instance instance.
        self.set_everything_to_none()

        # Clear the country combo boxs.
        self.cb_country.clear()

        # Set the current value of the selected_continent variable in add_break_region_instance to the current text in the continent
        # combo box.
        self.selected_continent = self.cb_continent.currentText()

        # Add the countries to the country combo box.
        self.cb_country.addItems(self.return_countries())

    # Change Region when Country is selected
    def slot_cb_country_on_index_change(self):
        # Set all the instance variables in the instance of the Region class to None, by calling a function in the
        # add_break_region_instance instance.
        self.set_everything_to_none()

        # Clear the country combo boxs.
        self.cb_region.clear()

        # Set the current value of the selected_continent variable in add_break_region_instance to the current text in the continent
        # combo box.
        self.selected_country = self.cb_country.currentText()

        # Add the countries to the country combo box.
        self.cb_region.addItems(self.return_regions())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = AddLocation(title='Add a New Location',
                      sql_user_name="Heather",
                      sql_password="#LAwaItly19",
                      sql_host_name="localhost"
    )
    win.show()

    sys.exit(app.exec())