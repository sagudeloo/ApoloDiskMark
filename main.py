import sys
import os
import subprocess
import json
import humanfriendly
from PyQt5 import QtWidgets, uic, QtCore


class ThreadClass(QtCore.QThread):
    operations = [
        {
            "prefix": "seq1mq8t1",
            "suffix": "read"
        },
        {
            "prefix": "seq1mq8t1",
            "suffix": "write"
        },
        {
            "prefix": "seq1mq1t1",
            "suffix": "read"
        },
        {
            "prefix": "seq1mq1t1",
            "suffix": "write"
        },
        {
            "prefix": "rnd4kq32t16",
            "suffix": "read"
        },
        {
            "prefix": "rnd4kq32t16",
            "suffix": "write"
        },
        {
            "prefix": "rnd4kq1t1",
            "suffix": "read"
        },
        {
            "prefix": "rnd4kq1t1",
            "suffix": "write"
        }
    ]

    operationsIndex = 0
    signal = QtCore.pyqtSignal(str, name='ThreadFinish')
    directory = os.getcwd()

    def __init__(self, parent=None):
        super(ThreadClass, self).__init__(parent)

    def isEven(self, number):
        if number % 2 == 0:
            return True
        else:
            return False

    def run(self):
        # executing command
        print(f'Running Thread [{self.operationsIndex}] Even? {self.isEven(self.operationsIndex)}')
        cmd: str = './scripts/{}{}.sh {}'.format(self.operations[self.operationsIndex]['prefix'],
                                                 self.operations[self.operationsIndex]['suffix'], self.directory)
        print(f'Running [{cmd}]')
        bw_bytes = ''
        output = json.loads(subprocess.getoutput(cmd))
        if self.isEven(self.operationsIndex):
            # This is read benchmark
            bw_bytes = '{}/s'.format(humanfriendly.format_size(output['jobs'][0]['read']['bw_bytes']))
            print(bw_bytes)

        else:
            # This is write benchmark
            bw_bytes = '{}/s'.format(humanfriendly.format_size(output['jobs'][0]['write']['bw_bytes']))
            print(bw_bytes)

        self.signal.emit(bw_bytes)


class MainWindow(QtWidgets.QMainWindow):
    thread = ThreadClass()

    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('mainwindow.ui', self)
        # Init default values
        self.directoryLineEdit = self.findChild(QtWidgets.QLineEdit, 'directoryLineEdit')
        self.directoryLineEdit.setText(self.thread.directory)
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
        # Configura e conecta a thread
        #  self.thread.setPriority(QtCore.QThread.HighestPriority)
        self.thread.signal.connect(self.receiveThreadfinish)
        # Init results label and others widgets
        self.clearResults()
        # show window
        self.show()

    def receiveThreadfinish(self, val):
        print('Receiving signal ok ', val)
        if self.thread.operationsIndex == 0:
            self.seq1mq8t1ReadLabel.setText(val)
        elif self.thread.operationsIndex == 1:
            self.seq1mq8t1WriteLabel.setText(val)
        elif self.thread.operationsIndex == 2:
            self.seq1mq1t1ReadLabel.setText(val)
        elif self.thread.operationsIndex == 3:
            self.seq1mq1t1WriteLabel.setText(val)
        elif self.thread.operationsIndex == 4:
            self.rnd4kq32t16ReadLabel.setText(val)
        elif self.thread.operationsIndex == 5:
            self.rnd4kq32t16WriteLabel.setText(val)
        elif self.thread.operationsIndex == 6:
            self.rnd4kq1t1ReadLabel.setText(val)
        else:
            self.rnd4kq1t1WriteLabel.setText(val)

        self.thread.operationsIndex += 1
        if len(self.thread.operations) == self.thread.operationsIndex:
            print('Stoping all threads')
            self.thread.quit()
            self.thread.operationsIndex = 0
        else:
            self.thread.start()

    def startBenchMark(self):
        if self.thread.isRunning():
            self.startPushButton.setText('Start')
            self.thread.terminate()
            self.thread.operationsIndex = 0
        else:
            self.startPushButton.setText('Stop')
            print('Starting benchmark...')
            # Verify if directory is writable
            if self.isWritable():
                print('Directory writable. OK [Starting Thread]')
                self.thread.operationsIndex = 0
                self.thread.start()
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
        self.thread.operationsIndex = 0

    # show directory dialog
    def showDirectoryDialog(self):
        print('Show Directory Dialog!')
        dialog = QtWidgets.QFileDialog()
        dialog.setFileMode(QtWidgets.QFileDialog.DirectoryOnly)
        if dialog.exec():
            self.thread.directory = dialog.selectedFiles()[0]
            print(f'Directory ===> {self.thread.directory}')
            self.directoryLineEdit.setText(self.thread.directory)

    def isWritable(self):
        self.thread.directory = self.directoryLineEdit.text()
        print(f'Verify if dir {self.thread.directory} is writable...')
        if os.access(self.thread.directory, os.W_OK):
            print(f'{self.thread.directory} is writable.')
            return True
        else:
            print(f'{self.thread.directory} NOT writable.')
            errorDialog = QtWidgets.QMessageBox()
            errorDialog.setIcon(QtWidgets.QMessageBox.Warning)
            errorDialog.setText(f'Cannot write to directory {self.thread.directory}')
            errorDialog.exec()
            return False

    def appQuit(self):
        app.quit()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    app.exec_()
