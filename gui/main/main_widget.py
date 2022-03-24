########################################################################################################################
# Project: wsl_app_v2.0
# FileName: main_widget.py
# Main Python Code for GUI
########################################################################################################################
from typing import Optional

import mysql
from mysql.connector import MySQLConnection

from PyQt5.QtWidgets import QMainWindow

from gui.main.ui_to_py.wsl_analytics_ui_v2 import Ui_Form

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
        # Slots for Break Data Entry Tab
        self.BreakContCb.currentIndexChanged.connect(self.slot_break_cont_cb_on_index_change)