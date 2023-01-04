import sys
sys.path.append(r'./')
import threading

from GUI.gui import ScraperGUI
from PySide6 import QtWidgets


def run_gui():
    app = QtWidgets.QApplication(sys.argv)
    window = ScraperGUI()
    window.show()
    app.exec_()

thread_gui = threading.Thread(target=run_gui)
thread_gui.start()