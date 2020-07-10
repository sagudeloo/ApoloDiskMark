import sys
import os
from PyQt5 import QtWidgets, uic


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('mainwindow.ui', self)
        # Init default values
        self.directoryLineEdit = self.findChild(QtWidgets.QLineEdit, 'directoryLineEdit')
        self.directoryLineEdit.setText(os.getcwd())
        self.selectPushButton = self.findChild(QtWidgets.QPushButton, 'selectPushButton')
        self.selectPushButton.clicked.connect(self.showDirectoryDialog)
        self.actionQuit = self.findChild(QtWidgets.QAction, 'actionQuit')
        self.actionQuit.triggered.connect(self.appQuit)
        self.progressBar = self.findChild(QtWidgets.QProgressBar, 'progressBar')
        self.seq1mq8t1ReadLabel = self.findChild(QtWidgets.QLabel, 'seq1mq8t1ReadLabel')
        self.seq1mq8t1WriteLabel = self.findChild(QtWidgets.QLabel, 'seq1mq8t1WriteLabel')
        self.seq1mq1t1ReadLabel = self.findChild(QtWidgets.QLabel, 'seq1mq1t1ReadLabel')
        self.seq1mq1t1WriteLabel = self.findChild(QtWidgets.QLabel, 'seq1mq1t1WriteLabel')
        self.rnd4kq32t16ReadLabel = self.findChild(QtWidgets.QLabel, 'rnd4kq32t16ReadLabel')
        self.rnd4kq32t16WriteLabel = self.findChild(QtWidgets.QLabel, 'rnd4kq32t16WriteLabel')
        self.rnd4kq1t1ReadLabel = self.findChild(QtWidgets.QLabel, 'rnd4kq1t1ReadLabel')
        self.rnd4kq1t1WriteLabel = self.findChild(QtWidgets.QLabel, 'rnd4kq1t1WriteLabel')
        self.statusbar = self.findChild(QtWidgets.QStatusBar, 'statusbar')
        self.clearResults()
        # show window
        self.show()

    def clearResults(self):
        self.progressBar.setProperty("value", 0)
        self.seq1mq8t1ReadLabel.setText("")
        self.seq1mq8t1WriteLabel.setText("")
        self.seq1mq1t1ReadLabel.setText("")
        self.seq1mq1t1WriteLabel.setText("")
        self.rnd4kq32t16ReadLabel.setText("")
        self.rnd4kq32t16WriteLabel.setText("")
        self.rnd4kq1t1ReadLabel.setText("")
        self.rnd4kq1t1WriteLabel.setText("")
        self.statusbar.showMessage("IDLE")

    # show directory dialog
    def showDirectoryDialog(self):
        print("Show Directory Dialog!")
        dialog = QtWidgets.QFileDialog()
        dialog.setFileMode(QtWidgets.QFileDialog.DirectoryOnly)
        if dialog.exec():
            file = dialog.selectedFiles()[0]
            print(f"file ===> {file}")
            self.directoryLineEdit.setText(file)

    def isWritable(self):
        directory = self.directoryLineEdit.text()
        print(f"Verify if dir {directory} is writable...")
        if os.access(directory, os.W_OK):
            print(f"{directory} is writable.")
        else:
            print(f"{directory} NOT writable.")
            errorDialog = QtWidgets.QMessageBox()
            errorDialog.setIcon(QtWidgets.QMessageBox.Warning)
            errorDialog.setText(f"Cannot write to {directory}")
            errorDialog.exec()

    def appQuit(self):
        app.quit()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    app.exec_()
