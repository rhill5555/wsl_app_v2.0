import sys
from typing import Optional

import PyQt5.QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QApplication, QDialogButtonBox
from PyQt5.QtWidgets import QCheckBox

from src.Places import Region

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = AddTourType(title='Add a New Location',
                      sql_user_name="Heather",
                      sql_password="#LAwaItly19",
                      sql_host_name="localhost"
    )
    win.show()

    sys.exit(app.exec())