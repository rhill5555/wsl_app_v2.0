########################################################################################################################
# Project: wsl_app_v2.0
# FileName: main_widget.py
# Main Python Code for GUI
########################################################################################################################
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog

from gui.common_widget.dialog_widget.add_location_popup import AddLocation
from gui.main.ui_to_py.wsl_analytics_ui_v2 import Ui_Form
from src.Places import Region
from src import Places
from src.Places import CommonSQL


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

        # Call to setup everything on the gui.
        self.on_startup()

    # This defines the event handlers for everything on the Main Widget
    def connect_slots(self):
        pass
        # Slots for Add Break Tab
        # Change Country when Continent is selected
        self.cb_addbreak_continent.currentIndexChanged.connect(self.slot_cb_addbreak_continent_on_index_change)
        self.cb_addbreak_country.currentIndexChanged.connect(self.slot_cb_addbreak_country_on_index_change)
    #     self.cb_addbreak_region.currentIndexChanged.connect(self.slot_cb_addbreak_region_on_index_change)
    #     self.pb_addbreak_clear.clicked.connect(self.slot_pb_addbreak_clear_clicked)
        self.pb_addbreak_newloc.clicked.connect(self.slot_pb_addbreak_newloc_clicked)
    #     self.pb_addbreak_submit.clicked.connect(self.slot_pb_addbreak_submit_clicked)

    def on_startup(self):
        self.cb_addbreak_continent.addItems(self.add_break_region_instance.return_continents())

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
        self.cb_addbreak_country.addItems(self.add_break_region_instance.return_countries())

    def slot_cb_addbreak_country_on_index_change(self):
        # Clear the add_break_region_instance combo boxs.
        self.cb_addbreak_region.clear()

        # Set the current value of the selected_country variable in add_break_region_instance to the current text
        # in the country combo box.
        self.add_break_region_instance.selected_country = self.cb_addbreak_country.currentText()

        # Add the regions to the add_break_region_instance combo box.
        self.cb_addbreak_region.addItems(self.add_break_region_instance.return_regions())

    def slot_pb_addbreak_newloc_clicked(self):
        dialog = AddLocation(title="Add a location to the database.")

        if dialog.exec() == QDialog.Accepted:
            pass


########################################################################################################################

if __name__ == '__main__':
    app = QApplication([])
    win = MainWidget()
    win.show()

    sys.exit(app.exec())