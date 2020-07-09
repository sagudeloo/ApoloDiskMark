from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(780, 480)
        MainWindow.setMinimumSize(QtCore.QSize(780, 480))
        MainWindow.setMaximumSize(QtCore.QSize(780, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftFrame = QtWidgets.QFrame(self.centralwidget)
        self.leftFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.leftFrame.setMaximumSize(QtCore.QSize(210, 16777215))
        self.leftFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.leftFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftFrame.setObjectName("leftFrame")
        self.logoLabel = QtWidgets.QLabel(self.leftFrame)
        self.logoLabel.setGeometry(QtCore.QRect(10, 0, 241, 311))
        self.logoLabel.setText("")
        self.logoLabel.setPixmap(QtGui.QPixmap("images/logo.png"))
        self.logoLabel.setObjectName("logoLabel")
        self.startPushButton = QtWidgets.QPushButton(self.leftFrame)
        self.startPushButton.setGeometry(QtCore.QRect(10, 350, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.startPushButton.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap("images/starticon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.startPushButton.setIcon(icon1)
        self.startPushButton.setObjectName("startPushButton")
        self.progressBar = QtWidgets.QProgressBar(self.leftFrame)
        self.progressBar.setGeometry(QtCore.QRect(10, 320, 191, 23))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout.addWidget(self.leftFrame)
        self.rightFrame = QtWidgets.QFrame(self.centralwidget)
        self.rightFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rightFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rightFrame.setObjectName("rightFrame")
        self.directoryLineEdit = QtWidgets.QLineEdit(self.rightFrame)
        self.directoryLineEdit.setGeometry(QtCore.QRect(0, 20, 421, 32))
        self.directoryLineEdit.setReadOnly(True)
        self.directoryLineEdit.setObjectName("directoryLineEdit")
        self.directoryLabel = QtWidgets.QLabel(self.rightFrame)
        self.directoryLabel.setGeometry(QtCore.QRect(0, 0, 141, 16))
        self.directoryLabel.setObjectName("directoryLabel")
        self.selectPushButton = QtWidgets.QPushButton(self.rightFrame)
        self.selectPushButton.setGeometry(QtCore.QRect(430, 20, 111, 32))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap("images/directoryicon.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.selectPushButton.setIcon(icon2)
        self.selectPushButton.setObjectName("selectPushButton")
        self.typeLabel = QtWidgets.QLabel(self.rightFrame)
        self.typeLabel.setGeometry(QtCore.QRect(0, 60, 81, 31))
        self.typeLabel.setAutoFillBackground(False)
        self.typeLabel.setStyleSheet("")
        self.typeLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.typeLabel.setObjectName("typeLabel")
        self.ReadLabel = QtWidgets.QLabel(self.rightFrame)
        self.ReadLabel.setGeometry(QtCore.QRect(90, 60, 221, 31))
        self.ReadLabel.setAutoFillBackground(False)
        self.ReadLabel.setStyleSheet("")
        self.ReadLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.ReadLabel.setObjectName("ReadLabel")
        self.writeLabel = QtWidgets.QLabel(self.rightFrame)
        self.writeLabel.setGeometry(QtCore.QRect(320, 60, 221, 31))
        self.writeLabel.setAutoFillBackground(False)
        self.writeLabel.setStyleSheet("")
        self.writeLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.writeLabel.setObjectName("writeLabel")
        self.seq1mq8t1Label = QtWidgets.QLabel(self.rightFrame)
        self.seq1mq8t1Label.setGeometry(QtCore.QRect(0, 100, 81, 71))
        self.seq1mq8t1Label.setAutoFillBackground(False)
        self.seq1mq8t1Label.setStyleSheet("")
        self.seq1mq8t1Label.setFrameShape(QtWidgets.QFrame.Box)
        self.seq1mq8t1Label.setObjectName("seq1mq8t1Label")
        self.seq1mq1t1Label = QtWidgets.QLabel(self.rightFrame)
        self.seq1mq1t1Label.setGeometry(QtCore.QRect(0, 180, 81, 71))
        self.seq1mq1t1Label.setAutoFillBackground(False)
        self.seq1mq1t1Label.setStyleSheet("")
        self.seq1mq1t1Label.setFrameShape(QtWidgets.QFrame.Box)
        self.seq1mq1t1Label.setObjectName("seq1mq1t1Label")
        self.rnd4kq32t16Label = QtWidgets.QLabel(self.rightFrame)
        self.rnd4kq32t16Label.setGeometry(QtCore.QRect(0, 260, 81, 71))
        self.rnd4kq32t16Label.setAutoFillBackground(False)
        self.rnd4kq32t16Label.setStyleSheet("")
        self.rnd4kq32t16Label.setFrameShape(QtWidgets.QFrame.Box)
        self.rnd4kq32t16Label.setObjectName("rnd4kq32t16Label")
        self.rnd4kq1t1Label = QtWidgets.QLabel(self.rightFrame)
        self.rnd4kq1t1Label.setGeometry(QtCore.QRect(0, 340, 81, 71))
        self.rnd4kq1t1Label.setAutoFillBackground(False)
        self.rnd4kq1t1Label.setStyleSheet("")
        self.rnd4kq1t1Label.setFrameShape(QtWidgets.QFrame.Box)
        self.rnd4kq1t1Label.setObjectName("rnd4kq1t1Label")
        self.seq1mq8t1ReadLabel = QtWidgets.QLabel(self.rightFrame)
        self.seq1mq8t1ReadLabel.setGeometry(QtCore.QRect(90, 100, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.seq1mq8t1ReadLabel.setFont(font)
        self.seq1mq8t1ReadLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.seq1mq8t1ReadLabel.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.seq1mq8t1ReadLabel.setObjectName("seq1mq8t1ReadLabel")
        self.seq1mq8t1WriteLabel = QtWidgets.QLabel(self.rightFrame)
        self.seq1mq8t1WriteLabel.setGeometry(QtCore.QRect(320, 100, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.seq1mq8t1WriteLabel.setFont(font)
        self.seq1mq8t1WriteLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.seq1mq8t1WriteLabel.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.seq1mq8t1WriteLabel.setObjectName("seq1mq8t1WriteLabel")
        self.seq1mq1t1ReadLabel = QtWidgets.QLabel(self.rightFrame)
        self.seq1mq1t1ReadLabel.setGeometry(QtCore.QRect(90, 180, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.seq1mq1t1ReadLabel.setFont(font)
        self.seq1mq1t1ReadLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.seq1mq1t1ReadLabel.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.seq1mq1t1ReadLabel.setObjectName("seq1mq1t1ReadLabel")
        self.seq1mq1t1WriteLabel = QtWidgets.QLabel(self.rightFrame)
        self.seq1mq1t1WriteLabel.setGeometry(QtCore.QRect(320, 180, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.seq1mq1t1WriteLabel.setFont(font)
        self.seq1mq1t1WriteLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.seq1mq1t1WriteLabel.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.seq1mq1t1WriteLabel.setObjectName("seq1mq1t1WriteLabel")
        self.rnd4kq32t16ReadLabel = QtWidgets.QLabel(self.rightFrame)
        self.rnd4kq32t16ReadLabel.setGeometry(QtCore.QRect(90, 260, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.rnd4kq32t16ReadLabel.setFont(font)
        self.rnd4kq32t16ReadLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.rnd4kq32t16ReadLabel.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.rnd4kq32t16ReadLabel.setObjectName("rnd4kq32t16ReadLabel")
        self.rnd4kq32t16WriteLabel = QtWidgets.QLabel(self.rightFrame)
        self.rnd4kq32t16WriteLabel.setGeometry(QtCore.QRect(320, 260, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.rnd4kq32t16WriteLabel.setFont(font)
        self.rnd4kq32t16WriteLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.rnd4kq32t16WriteLabel.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.rnd4kq32t16WriteLabel.setObjectName("rnd4kq32t16WriteLabel")
        self.rnd4kq1t1ReadLabel = QtWidgets.QLabel(self.rightFrame)
        self.rnd4kq1t1ReadLabel.setGeometry(QtCore.QRect(90, 340, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.rnd4kq1t1ReadLabel.setFont(font)
        self.rnd4kq1t1ReadLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.rnd4kq1t1ReadLabel.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.rnd4kq1t1ReadLabel.setObjectName("rnd4kq1t1ReadLabel")
        self.rnd4kq1t1WriteLabel = QtWidgets.QLabel(self.rightFrame)
        self.rnd4kq1t1WriteLabel.setGeometry(QtCore.QRect(320, 340, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.rnd4kq1t1WriteLabel.setFont(font)
        self.rnd4kq1t1WriteLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.rnd4kq1t1WriteLabel.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.rnd4kq1t1WriteLabel.setObjectName("rnd4kq1t1WriteLabel")
        self.horizontalLayout.addWidget(self.rightFrame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 780, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStyleSheet("")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Crazy DiskMark"))
        self.startPushButton.setText(_translate("MainWindow", "Start"))
        self.directoryLineEdit.setPlaceholderText(
            _translate("MainWindow", "Directory to Benchmark")
        )
        self.directoryLabel.setText(_translate("MainWindow", "Directory Select"))
        self.selectPushButton.setText(_translate("MainWindow", "Select"))
        self.typeLabel.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:14pt; font-weight:600;">Type</span></p></body></html>',
            )
        )
        self.ReadLabel.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:14pt; font-weight:600;">Read</span></p></body></html>',
            )
        )
        self.writeLabel.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:14pt; font-weight:600;">Write</span></p></body></html>',
            )
        )
        self.seq1mq8t1Label.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:14pt; font-weight:600;">SEQ1M</span></p><p align="center"><span style=" font-size:14pt; font-weight:600;">Q8T1</span></p></body></html>',
            )
        )
        self.seq1mq1t1Label.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:14pt; font-weight:600;">SEQ1M</span></p><p align="center"><span style=" font-size:14pt; font-weight:600;">Q1T1</span></p></body></html>',
            )
        )
        self.rnd4kq32t16Label.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:14pt; font-weight:600;">RND4K</span></p><p align="center"><span style=" font-size:14pt; font-weight:600;">Q32T16</span></p></body></html>',
            )
        )
        self.rnd4kq1t1Label.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:14pt; font-weight:600;">RND4K</span></p><p align="center"><span style=" font-size:14pt; font-weight:600;">Q1T1</span></p></body></html>',
            )
        )
        self.seq1mq8t1ReadLabel.setText(_translate("MainWindow", "2709.45 MB/s"))
        self.seq1mq8t1WriteLabel.setText(_translate("MainWindow", "2709.45 MB/s"))
        self.seq1mq1t1ReadLabel.setText(_translate("MainWindow", "2709.45 MB/s"))
        self.seq1mq1t1WriteLabel.setText(_translate("MainWindow", "2709.45 MB/s"))
        self.rnd4kq32t16ReadLabel.setText(_translate("MainWindow", "2709.45 MB/s"))
        self.rnd4kq32t16WriteLabel.setText(_translate("MainWindow", "2709.45 MB/s"))
        self.rnd4kq1t1ReadLabel.setText(_translate("MainWindow", "2709.45 MB/s"))
        self.rnd4kq1t1WriteLabel.setText(_translate("MainWindow", "2709.45 MB/s"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionQuit.triggered.connect(self.appQuit)

    def appQuit(self):
        app.quit()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
