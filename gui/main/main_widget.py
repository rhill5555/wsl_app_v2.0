########################################################################################################################
# Project: wsl_app_v2.0
# FileName: main_widget.py
# Main Python Code for GUI
########################################################################################################################
import sys
from typing import Optional

import mysql
from mysql.connector import MySQLConnection

from PyQt5.QtWidgets import QMainWindow, QApplication

from gui.main.ui_to_py.wsl_analytics_ui_v2 import Ui_Form
from src.Places import Continent, Country, Region

########################################################################################################################


class MainWidget(QMainWindow, Ui_Form):
    def __init__(self, sql_host: str, sql_user: str, sql_password: str):
        # Call the constructor for the inherited QWidget class.
        QMainWindow.__init__(self)

        # Sql Connection Info and mysql connection
        self.__sql_host: str = sql_host
        self.__sql_user: str = sql_user
        self.__sql_password: str = sql_password
        self.__mysql_connection: Optional[MySQLConnection] = None

        # Call the setupUi function that adds all the pyqt stuff to this class, that was designed in the designer.
        # This function is inherited from the Ui_Form class.
        self.setupUi(self)

        # Call the connect_slots function to connect all the event-handlers to functions in this class.
        self.connect_slots()

        # Call to setup everything on the gui.
        self.on_startup()

    @property
    def mysql(self) -> MySQLConnection:
        # Connect to MySQL
        if self.__mysql_connection is None:
            self.__mysql_connection = mysql.connector.connect(
                host=self.__sql_host,
                user=self.__sql_user,
                password=self.__sql_password
            )
        return self.__mysql_connection

    # This defines the event handlers for everything on the Main Widget
    def connect_slots(self):
        # Slots for Add Break Tab
        # Change Country when Continent is selected
        self.cb_addbreak_continent.currentIndexChanged.connect(self.slot_cb_addbreak_continent_on_index_change)
        self.cb_addbreak_country.currentIndexChanged.connect(self.slot_cb_addbreak_country_on_index_change)
    #     self.cb_addbreak_region.currentIndexChanged.connect(self.slot_cb_addbreak_region_on_index_change)
    #     self.pb_addbreak_clear.clicked.connect(self.slot_pb_addbreak_clear_clicked)
    #     self.pb_addbreak_newloc.clicked.connect(self.slot_pb_addbreak_newloc_clicked)
    #     self.pb_addbreak_submit.clicked.connect(self.slot_pb_addbreak_submit_clicked)

    def on_startup(self):

        self.cb_addbreak_continent.addItems(
            [item for item in Continent.continent(mysql_connection=self.mysql)]
        )

    def slot_cb_addbreak_continent_on_index_change(self):

        country_list = Country.country(mysql_connection=self.mysql, continent=self.cb_addbreak_continent.currentText())
        self.cb_addbreak_country.clear()
        self.cb_addbreak_country.addItems(
            [item for item in country_list])

    def slot_cb_addbreak_country_on_index_change(self):
        region_list = Region.region(mysql_connection=self.mysql, country=self.cb_addbreak_country.currentText())
        self.cb_addbreak_region.clear()
        self.cb_addbreak_region.addItems(
            [item for item in region_list])

########################################################################################################################

if __name__ == '__main__':
    app = QApplication([])
    win = MainWidget(sql_host='localhost', sql_user='Heather', sql_password='#LAwaItly19')
    win.show()

    sys.exit(app.exec())