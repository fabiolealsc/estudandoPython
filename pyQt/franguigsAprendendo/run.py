import sys
from PyQt5.QtWidgets import QDialog, QApplication
from templates.login import UI_login

app = QApplication(sys.argv)
if (QDialog.Accepted == True):
    window = UI_login
    
sys.exit(app.exec_())
sys.show()