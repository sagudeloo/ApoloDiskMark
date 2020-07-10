import sys
import os
import time
from PyQt5 import QtWidgets, uic, QtCore


class ThreadClass(QtCore.QThread):
    signal = QtCore.pyqtSignal(int, name='ThreadFinish')

    def __init__(self, parent=None):
        super(ThreadClass, self).__init__(parent)

    def run(self):
        print('Thread Starting...')
        time.sleep(5)
        print('Thread finish!')
        self.signal.emit(34)


class MainWindow(QtWidgets.QMainWindow):
    thread = ThreadClass()

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
        self.startPushButton = self.findChild(QtWidgets.QPushButton, 'startPushButton')
        self.startPushButton.clicked.connect(self.startBenchMark)
        #Conecta a thread
        self.thread.signal.connect(self.receiveThreadfinish)
        # Init results label and others widgets
        self.clearResults()
        # show window
        self.show()

    def receiveThreadfinish(self, val):
        print('Recebi o sinal', val)

    def startBenchMark(self):
        print('Starting benchmark...')
        # Verify if directory is writable
        if self.isWritable():
            print('Directory writable. OK [NEXT]')
            print('Before run thread')
            self.thread.start()
            print('After run thread')
        else:
            print('Directory not writable. [ERROR]')

    def clearResults(self):
        self.progressBar.setProperty('value', 0)
        self.seq1mq8t1ReadLabel.setText('')
        self.seq1mq8t1WriteLabel.setText('')
        self.seq1mq1t1ReadLabel.setText('')
        self.seq1mq1t1WriteLabel.setText('')
        self.rnd4kq32t16ReadLabel.setText('')
        self.rnd4kq32t16WriteLabel.setText('')
        self.rnd4kq1t1ReadLabel.setText('')
        self.rnd4kq1t1WriteLabel.setText('')
        self.statusbar.showMessage('IDLE')

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
            return True
        else:
            print(f"{directory} NOT writable.")
            errorDialog = QtWidgets.QMessageBox()
            errorDialog.setIcon(QtWidgets.QMessageBox.Warning)
            errorDialog.setText(f'Cannot write to directory {directory}')
            errorDialog.exec()
            return False

    def appQuit(self):
        app.quit()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    app.exec_()
