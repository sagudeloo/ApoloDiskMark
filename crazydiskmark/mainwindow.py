import sys
import os
import subprocess
import json
import humanfriendly
from pathlib import Path
from PyQt5 import QtWidgets, uic, QtCore, QtGui
import logging

resource_path = os.path.dirname(__file__)


class ThreadBenchmark(QtCore.QThread):
    logger = logging.getLogger(__name__)
    bw_bytes = ''
    target = ''
    loops = '--loops=1'
    size = '--size=1024m'
    tmpFile = 'fiomark.tmp'
    stoneWall = '--stonewall'
    ioEngine = '--ioengine=libaio'
    direct = '--direct=1'
    zeroBuffers = '--zero_buffers=0'
    outputFormat = '--output-format=json'
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

    def __init__(self, parent=None):
        super(ThreadBenchmark, self).__init__(parent)
        self.finished.connect(self.threadFinished)

    def threadFinished(self):
        pass
        self.logger.info('Thread Finished, garbage collecting now...')
        targetFilename = f'{self.target}/{self.tmpFile}'
        self.logger.info(f'Verifying if temp file exists {targetFilename}')
        if os.path.isfile(targetFilename):
            self.logger.info(f'Yes, removing the file: [{targetFilename}]')
            os.remove(targetFilename)

    def run(self):
        # executing Benchmarks
        self.logger.info('Executing Benchmarks....')
        for index, operation in enumerate(self.operations):
            self.logger.info(f'Running index: [{index}]\tprefix:\t[{operation["prefix"]}] rw:[{operation["rw"]}]')
            filename = f'--filename="{self.target}/{self.tmpFile}"'
            name = f'--name={operation["prefix"]}{operation["rw"]}'
            currentCmd = f'{self.fioWhich} {self.loops} {self.size} {filename} {self.stoneWall} {self.ioEngine} {self.direct} {self.zeroBuffers} {name} --bs={operation["bs"]} --iodepth={operation["ioDepth"]} --numjobs={operation["numJobs"]} --rw={operation["rw"]} {self.outputFormat}'
            self.logger.info(f'Executing Command: {currentCmd}')
            output = json.loads(subprocess.getoutput(currentCmd).encode('utf-8'))
            if 'read' in operation['rw']:
                self.bw_bytes = '{}/s'.format(humanfriendly.format_size(output['jobs'][0]['read']['bw_bytes']))
            else:
                self.logger.info('Type Write')
                self.bw_bytes = '{}/s'.format(humanfriendly.format_size(output['jobs'][0]['write']['bw_bytes']))

            # self.bw_bytes = f'{operation["prefix"]}{operation["rw"]}'
            self.sleep(1)
            self.signal.emit(self.bw_bytes)


class MainWindow(QtWidgets.QMainWindow):
    logger = logging.getLogger(__name__)
    thread = ThreadBenchmark()
    target = ''
    labelWidgets = []
    operationIndex = 0

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
        # self.thread.setPriority(QtCore.QThread.HighestPriority)
        # self.thread.setTerminationEnabled()
        self.thread.signal.connect(self.receiveThreadBenchmark)
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

    def receiveThreadBenchmark(self, val):
        self.logger.info(f'Receiving ===> {val}')
        self.labelWidgets[self.operationIndex].setText(val)
        self.progressBar.setProperty('value', (self.operationIndex + 1) * 12.5)
        self.operationIndex += 1
        if self.operationIndex == len(self.thread.operations):
            self.startPushButton.setText('Start')
            self.operationIndex = 0

    def startBenchMark(self):
        if self.thread.isRunning():
            self.startPushButton.setText('Start')
            self.statusbar.showMessage('IDLE')
            self.logger.info('Stopping Thread....')
            self.thread.terminate()
            self.operationIndex = 0
        else:
            self.clearResults()
            # Verify if directory is writable
            if self.isWritable():
                self.startPushButton.setText('Stop')
                self.logger.info('Starting benchmark...')
                self.statusbar.showMessage('Running. Please wait, this may take several minutes...')
                self.logger.info('Directory writable. OK [Starting Thread]')
                self.thread.start()
            else:
                self.logger.info('Directory not writable. [ERROR]')

    def clearResults(self):
        self.statusbar.showMessage('IDLE')
        self.thread.operationsIndex = 0
        self.progressBar.setProperty('value', 0)
        for label in self.labelWidgets:
            label.setText('')

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
        self.thread.target = self.directoryLineEdit.text()
        self.logger.info(f'Verify if dir {self.thread.target} is writable...')
        if os.access(self.thread.target, os.W_OK):
            self.logger.info(f'{self.thread.target} is writable.')
            return True
        else:
            self.logger.info(f'{self.thread.target} NOT writable.')
            errorDialog = QtWidgets.QMessageBox()
            errorDialog.setIcon(QtWidgets.QMessageBox.Warning)
            errorDialog.setText(f'Cannot write to directory {self.thread.target}')
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
