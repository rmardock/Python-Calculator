# Entry point for the application
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from main_window import MainWindow

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	# Define style parameters
	app.setStyle('Fusion')
	palette = QtGui.QPalette()
	palette.setColor(QtGui.QPalette.Window, QtGui.QColor(53,53,53))
	palette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)
	palette.setColor(QtGui.QPalette.Base, QtGui.QColor(15,15,15))
	palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53,53,53))
	palette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.white)
	palette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.white)
	palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
	palette.setColor(QtGui.QPalette.Button, QtGui.QColor(53,53,53))
	palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.white)
	palette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)  
	palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(142,45,197).lighter())
	palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)
	# Set palette
	app.setPalette(palette)
	# Instantiate MainWindow Class
	ui = MainWindow()
	# Get QMainWindow from ui variable ((is Mainwindow object))
	mw = ui.get_mw()
	mw.setWindowFlags(QtCore.Qt.FramelessWindowHint)
	# Show window
	mw.show()
	sys.exit(app.exec_())