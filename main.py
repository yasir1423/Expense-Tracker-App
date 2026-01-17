from PySide6.QtWidgets import QApplication
from window_class import Window
import sys
app=QApplication(sys.argv)
window=Window()
window.show()
app.exec()