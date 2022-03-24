import sys
import PyQt5.QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QApplication, QDialogButtonBox

from src.sql_commands import Places


class SimpleLineEdit(QDialog):
    def __init__(self, title, mysql_conn, left=10, top=10, width=520, height=400, parent=None):
        # Calls constructor for QDialog
        super().__init__(parent=parent)

        self.mysql = mysql_conn

        # Set Title
        self.setWindowTitle(title)

        # Set Geometry
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.setGeometry(left, top, width, height)

        # Set parent widget
        if not (parent is None):
            self.setParent(parent)

        # Create Vertical Layout Box
        self.layout = QVBoxLayout()

        # Create Horizontal Layouts
        self.HLayoutCont = QHBoxLayout()
        self.HLayoutCountry = QHBoxLayout()
        self.HLayoutReg = QHBoxLayout()
        self.HLayoutCity = QHBoxLayout()

        # Disable x button to force "yes" or "no" click
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        # Disable help button
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)

        # Continent Label and Combobox
        self.HLayoutCont.addWidget(QLabel("Continent:"))
        self.Cont_Cb = PyQt5.QtWidgets.QComboBox()
        self.HLayoutCont.addWidget(self.Cont_Cb)
        # self.Cont_Cb.clear()
        # self.Cont_Cb.addItems(
        #     [item for item in Places.continent(mysql_connection=mysql_conn)]
        # )
        self.Cont_Cb.setFixedWidth(200)
        self.HLayoutCont.addWidget(QLabel(''))
        self.layout.addLayout(self.HLayoutCont)

        # Country Label and Line Edit
        self.HLayoutCountry.addWidget(QLabel("Country:"))
        self.Country_Cb = PyQt5.QtWidgets.QComboBox()
        self.HLayoutCountry.addWidget(self.Country_Cb)
        # self.Country_Cb.clear()
        # self.Country_Cb.addItems(
        #     [item[0] for item in Places.countries(mysql_connection=mysql_conn,
        #                                           continent=self.Cont_Cb.currentText())])
        self.Country_Cb.setFixedWidth(200)
        self.Country_LineEdit = PyQt5.QtWidgets.QLineEdit()
        self.HLayoutCountry.addWidget(self.Country_LineEdit)
        self.Country_LineEdit.setFixedWidth(200)

        self.layout.addLayout(self.HLayoutCountry)

        # Region Label and Line Edit
        self.HLayoutReg.addWidget(QLabel("Region:"))

        self.Region_Cb = PyQt5.QtWidgets.QComboBox()
        self.HLayoutReg.addWidget(self.Region_Cb)
        self.Region_Cb.clear()
        # self.Region_Cb.addItems()
        self.Region_Cb.setFixedWidth(200)

        self.Region_LineEdit = PyQt5.QtWidgets.QLineEdit()
        self.HLayoutReg.addWidget(self.Region_LineEdit)
        self.Region_LineEdit.setFixedWidth(200)

        self.layout.addLayout(self.HLayoutReg)


        # City Label and Line Edit
        self.HLayoutCity.addWidget(QLabel("City:"))
        self.City_LineEdit = PyQt5.QtWidgets.QLineEdit()
        self.HLayoutCity.addWidget(self.City_LineEdit)
        self.City_LineEdit.setFixedWidth(200)
        self.HLayoutCity.addWidget(QLabel(''))
        self.layout.addLayout(self.HLayoutCity)

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
        self.Cont_Cb.currentIndexChanged.connect(self.slot_cont_cb_on_index_change)
        self.Country_Cb.currentIndexChanged.connect(self.slot_country_cb_on_index_change)

    # This setups up everything at the first startup.
    def on_startup(self):
        # Add Continents to the combobox.
        self.Cont_Cb.addItems(
            [item for item in Places.continent(mysql_connection=self.mysql)]
        )

    def slot_cont_cb_on_index_change(self):
        self.Country_Cb.clear()
        self.Country_Cb.addItems(
            [item for item in Places.countries(mysql_connection=self.mysql,
                                                  continent=self.Cont_Cb.currentText())])

    def slot_country_cb_on_index_change(self):
        self.Region_Cb.clear()
        self.Region_Cb.addItems(
            [item for item in Places.region(mysql_connection=self.mysql,
                                               country=self.Country_Cb.currentText())]
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = SimpleLineEdit(title="Title")
    win.show()
    if win.exec() == QDialog.Accepted:
        print('Hello Bitches!')