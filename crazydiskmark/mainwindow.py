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


class ThreadBenchmark(QtCore.QThread):
    logger = logging.getLogger(__name__)
    bw_bytes = ''
    operationIndex = 0
    target = ''
    loops = '--loops=1'
    size = '--size=1024m'
    tmpFile = 'fiomark.tmp'
    filename = f'--filename="{target}/{tmpFile}"'
    stoneWall = '--stonewall'
    ioEngine = '--ioengine=libaio'
    direct = '--direct=1'
    zeroBuffers = '--zero_buffers=0'
    outputFormat = '--output - format = json'
    fioWhich = subprocess.getoutput('which fio')

    operations = [
        {
            "prefix": 'seq1mq8t1',
            "rw": 'read',
            'bs': '1m',
            'ioDepth': '8',
            'numJobs': '1',
        },
        {
            "prefix": 'seq1mq8t1',
            "rw": 'write',
            'bs': '1m',
            'ioDepth': '8',
            'numJobs': '1',
        },
        {
            "prefix": 'seq1mq1t1',
            "rw": 'read',
            'bs': '1m',
            'ioDepth': '1',
            'numJobs': '1',

        },
        {
            "prefix": 'seq1mq1t1',
            "rw": 'write',
            'bs': '1m',
            'ioDepth': '1',
            'numJobs': '1',
        },
        {
            "prefix": 'rnd4kq32t1',
            "rw": 'randread',
            'bs': '4k',
            'ioDepth': '32',
            'numJobs': '1',
        },
        {
            "prefix": 'rnd4kq32t1',
            "rw": 'randwrite',
            'bs': '4k',
            'ioDepth': '32',
            'numJobs': '1',
        },
        {
            "prefix": 'rnd4kq1t1',
            "rw": 'randread',
            'bs': '4k',
            'ioDepth': '1',
            'numJobs': '1',

        },
        {
            "prefix": 'rnd4kq1t1',
            "rw": 'randwrite',
            'bs': '4k',
            'ioDepth': '1',
            'numJobs': '1',
        }
    ]

    signal = QtCore.pyqtSignal(str, name='ThreadFinish')
    directory = os.getcwd()

    def __init__(self, parent=None):
        super(ThreadBenchmark, self).__init__(parent)
        self.finished.connect(self.threadFinished)

    def threadFinished(self):
        pass
        # self.signal.emit(self.bw_bytes)
        # self.logger.info('Finished QThread operationIndex = {}'.format(self.operationIndex))
        # self.operationIndex += 1
        # if self.operationIndex == len(self.operations):
        #     self.logger.info('all the jobs done.')
        # else:
        #     self.start()

    def run(self):
        # executing Benchmarks
        self.logger.info('Executing Benchmarks....')
        for index, operation in enumerate(self.operations):
            self.logger.info(f'Running index: [{index}] prefix: [{operation["prefix"]}] target: [{self.target}]')

        # output = json.loads(subprocess.getoutput(cmd).encode('utf-8'))

        # if self.isEven(self.operationIndex):
        #     # This is read benchmark
        #     self.bw_bytes = '{}/s'.format(humanfriendly.format_size(output['jobs'][0]['read']['bw_bytes']))
        # else:
        #     # This is write benchmark
        #     self.bw_bytes = '{}/s'.format(humanfriendly.format_size(output['jobs'][0]['write']['bw_bytes']))


class MainWindow(QtWidgets.QMainWindow):
    logger = logging.getLogger(__name__)
    thread = ThreadBenchmark()
    target = ''
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
        self.labelWidgets.append(self.findChild(QtWidgets.QLabel, 'rnd4kq32t1ReadLabel'))
        self.labelWidgets.append(self.findChild(QtWidgets.QLabel, 'rnd4kq32t1WriteLabel'))
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
        # self.thread.setTerminationEnabled()
        self.thread.signal.connect(self.receiveThreadfinish)
        self.thread.target = Path.home()

        self.aboutDialog = QtWidgets.QDialog()
        uic.loadUi(f'{resource_path}/aboutdialog.ui', self.aboutDialog)
        self.okPushButton = self.aboutDialog.findChild(QtWidgets.QPushButton, 'okPushButton')
        self.okPushButton.clicked.connect(self.quitAboutDialog)

        self.version = self.aboutDialog.findChild(QtWidgets.QLabel, 'versionLabel').text()

        self.setWindowTitle(f'Crazy DiskMark - {self.version}')
        # Init results label and others widgets
        self.clearResults()
        # show window
        self.show()

    def receiveThreadfinish(self, val):
        pass
        # self.logger.info('Receiving signal ok ')
        # self.labelWidgets[self.thread.operationIndex].setText(val)
        # self.progressBar.setProperty('value', (self.thread.operationIndex + 1) * 12.5)
        # if self.thread.operationIndex == 7:
        #     self.startPushButton.setText('Start')
        #     self.statusbar.showMessage('IDLE')

    def startBenchMark(self):
        self.thread.start()
        # if self.thread.isRunning():
        #     tempFile = f'{self.directoryLineEdit.text()}/fiomark.tmp'
        #     if os.path.isfile(tempFile):
        #         os.remove(tempFile)
        #
        #     self.startPushButton.setText('Start')
        #     self.statusbar.showMessage('IDLE')
        #     # self.thread.terminate()
        # else:
        #     self.clearResults()
        #     # Verify if directory is writable
        #     if self.isWritable():
        #         self.logger.info('Starting benchmark...')
        #         self.startPushButton.setText('Stop')
        #         self.statusbar.showMessage('Running. Please wait, this may take several minutes...')
        #         self.logger.info('Directory writable. OK [Starting Thread]')
        #         self.thread.operationsIndex = 0
        #         self.thread.start()
        #     else:
        #         self.logger.info('Directory not writable. [ERROR]')

    def clearResults(self):
        self.progressBar.setProperty('value', 0)
        self.seq1mq8t1ReadLabel.setText('')
        self.seq1mq8t1WriteLabel.setText('')
        self.seq1mq1t1ReadLabel.setText('')
        self.seq1mq1t1WriteLabel.setText('')
        self.rnd4kq32t1ReadLabel.setText('')
        self.rnd4kq32t1WriteLabel.setText('')
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
            self.thread.target = dialog.selectedFiles()[0]
            self.logger.info(f'Directory ===> {self.thread.target}')
            self.directoryLineEdit.setText(self.thread.target)

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
