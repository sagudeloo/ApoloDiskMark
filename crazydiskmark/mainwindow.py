import sys
import os
import subprocess
import json
import humanfriendly
import shutil
from pathlib import Path
from PyQt5 import QtWidgets, uic, QtCore, QtGui
import logging

resource_path = os.path.dirname(__file__)


class ThreadClass(QtCore.QThread):
    logger = logging.getLogger(__name__)
    bw_bytes = ''
    operationIndex = 0
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

    signal = QtCore.pyqtSignal(str, name='ThreadFinish')
    directory = os.getcwd()

    def __init__(self, parent=None):
        super(ThreadClass, self).__init__(parent)
        self.finished.connect(self.threadFinished)

    def threadFinished(self):
        self.signal.emit(self.bw_bytes)
        self.logger.info('Finished QThread operationIndex = {}'.format(self.operationIndex))
        self.operationIndex += 1
        if self.operationIndex == len(self.operations):
            self.logger.info('all the jobs done.')
        else:
            self.start()

    @staticmethod
    def isEven(number):
        if number % 2 == 0:
            return True
        else:
            return False

    def run(self):
        # executing command
        self.logger.info(f'Running Thread [{self.operationIndex}] Even? {self.isEven(self.operationIndex)}')
        cmd: str = '{}/scripts/{}{}.sh {}'.format(resource_path, self.operations[self.operationIndex]['prefix'],
                                                  self.operations[self.operationIndex]['suffix'], self.directory)
        self.logger.info(f'Running [{cmd}]')
        bw_bytes = ''
        output = json.loads(subprocess.getoutput(cmd).encode('utf-8'))

        if self.isEven(self.operationIndex):
            # This is read benchmark
            self.bw_bytes = '{}/s'.format(humanfriendly.format_size(output['jobs'][0]['read']['bw_bytes']))
        else:
            # This is write benchmark
            self.bw_bytes = '{}/s'.format(humanfriendly.format_size(output['jobs'][0]['write']['bw_bytes']))


class MainWindow(QtWidgets.QMainWindow):
    logger = logging.getLogger(__name__)
    thread = ThreadClass()
    labelWidgets = []

    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi(f'{resource_path}/crazydiskmark.ui', self)
        # Init default values
        self.labelDefaultStyle = """
        border: 1px solid black;
        border-radius: 5px;
        """
        self.directoryLineEdit = self.findChild(QtWidgets.QLineEdit, 'directoryLineEdit')
        self.directoryLineEdit.setText(str(Path.home()))
        self.selectPushButton = self.findChild(QtWidgets.QPushButton, 'selectPushButton')
        self.selectPushButton.setIcon(QtGui.QIcon(f'{resource_path}/images/directoryicon.png'))
        self.selectPushButton.clicked.connect(self.showDirectoryDialog)
        self.actionQuit = self.findChild(QtWidgets.QAction, 'actionQuit')
        self.actionQuit.triggered.connect(self.appQuit)
        self.actionAbout = self.findChild(QtWidgets.QAction, 'actionAbout')
        self.actionAbout.triggered.connect(self.showAboutDialog)
        self.progressBar = self.findChild(QtWidgets.QProgressBar, 'progressBar')

        self.labelWidgets.append(self.findChild(QtWidgets.QLabel, 'seq1mq8t1ReadLabel'))
        self.labelWidgets.append(self.findChild(QtWidgets.QLabel, 'seq1mq8t1WriteLabel'))
        self.labelWidgets.append(self.findChild(QtWidgets.QLabel, 'seq1mq1t1ReadLabel'))
        self.labelWidgets.append(self.findChild(QtWidgets.QLabel, 'seq1mq1t1WriteLabel'))
        self.labelWidgets.append(self.findChild(QtWidgets.QLabel, 'rnd4kq32t16ReadLabel'))
        self.labelWidgets.append(self.findChild(QtWidgets.QLabel, 'rnd4kq32t16WriteLabel'))
        self.labelWidgets.append(self.findChild(QtWidgets.QLabel, 'rnd4kq1t1ReadLabel'))
        self.labelWidgets.append(self.findChild(QtWidgets.QLabel, 'rnd4kq1t1WriteLabel'))
        for label in self.labelWidgets:
            label.setStyleSheet(self.labelDefaultStyle)

        self.statusbar = self.findChild(QtWidgets.QStatusBar, 'statusbar')
        self.startPushButton = self.findChild(QtWidgets.QPushButton, 'startPushButton')
        self.startPushButton.setIcon(QtGui.QIcon(f'{resource_path}/images/starticon.png'))
        self.startPushButton.clicked.connect(self.startBenchMark)
        # Configura e conecta a thread
        #  self.thread.setPriority(QtCore.QThread.HighestPriority)
        self.thread.signal.connect(self.receiveThreadfinish)

        self.aboutDialog = QtWidgets.QDialog()
        uic.loadUi(f'{resource_path}/aboutdialog.ui', self.aboutDialog)
        self.okPushButton = self.aboutDialog.findChild(QtWidgets.QPushButton, 'okPushButton')
        self.okPushButton.clicked.connect(self.quitAboutDialog)

        self.version = self.aboutDialog.findChild(QtWidgets.QLabel, 'versionLabel').text()

        self.setWindowTitle(f'Crazy DiskMark - {self.version}')
        # Test if fio (Flexible I/O Tester) is in path
        if shutil.which('fio') is None:
            errorDialog = QtWidgets.QMessageBox()
            errorDialog.setIcon(QtWidgets.QMessageBox.Warning)
            errorDialog.setText('Flexible I/O Tester not present in your system.')
            errorDialog.exec()
            sys.exit()
        # Init results label and others widgets
        self.clearResults()
        # show window
        self.show()

    def receiveThreadfinish(self, val):
        self.logger.info('Receiving signal ok ')
        self.labelWidgets[self.thread.operationIndex].setText(val)
        self.progressBar.setProperty('value', (self.thread.operationIndex + 1) * 12.5)
        if self.thread.operationIndex == 7:
            self.startPushButton.setText('Start')
            self.statusbar.showMessage('IDLE')

    def startBenchMark(self):
        if self.thread.isRunning():
            tempFile = f'{self.directoryLineEdit.text()}/fiomark.tmp'
            if os.path.isfile(tempFile):
                os.remove(tempFile)

            self.startPushButton.setText('Start')
            self.statusbar.showMessage('IDLE')
            self.thread.terminate()
        else:
            self.clearResults()
            # Verify if directory is writable
            if self.isWritable():
                self.logger.info('Starting benchmark...')
                self.startPushButton.setText('Stop')
                self.statusbar.showMessage('Running. Please wait, this may take several minutes...')
                self.logger.info('Directory writable. OK [Starting Thread]')
                self.thread.operationsIndex = 0
                self.thread.start()
            else:
                self.logger.info('Directory not writable. [ERROR]')

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
        self.startPushButton.setText('Start')

    # show directory dialog
    def showDirectoryDialog(self):
        self.logger.info('Show Directory Dialog!')
        dialog = QtWidgets.QFileDialog()
        dialog.setFileMode(QtWidgets.QFileDialog.DirectoryOnly)
        if dialog.exec():
            self.thread.directory = dialog.selectedFiles()[0]
            self.logger.info(f'Directory ===> {self.thread.directory}')
            self.directoryLineEdit.setText(self.thread.directory)

    def isWritable(self):
        self.thread.directory = self.directoryLineEdit.text()
        self.logger.info(f'Verify if dir {self.thread.directory} is writable...')
        if os.access(self.thread.directory, os.W_OK):
            self.logger.info(f'{self.thread.directory} is writable.')
            return True
        else:
            self.logger.info(f'{self.thread.directory} NOT writable.')
            errorDialog = QtWidgets.QMessageBox()
            errorDialog.setIcon(QtWidgets.QMessageBox.Warning)
            errorDialog.setText(f'Cannot write to directory {self.thread.directory}')
            errorDialog.exec()
            return False

    def showAboutDialog(self):
        self.aboutDialog.exec_()

    def quitAboutDialog(self):
        self.aboutDialog.hide()

    @staticmethod
    def appQuit():
        sys.exit()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    app.exec_()
