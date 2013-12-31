# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/yeison/Documentos/Pinguino/pinguino-ide/qtgui/frames/board_config.ui'
#
# Created: Tue Dec 31 12:23:58 2013
#      by: pyside-uic 0.2.14 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(342, 272)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/art/windowIcon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.groupBox_arch = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_arch.setAutoFillBackground(False)
        self.groupBox_arch.setObjectName("groupBox_arch")
        self.gridLayout = QtGui.QGridLayout(self.groupBox_arch)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.radioButton_arch_8 = QtGui.QRadioButton(self.groupBox_arch)
        self.radioButton_arch_8.setObjectName("radioButton_arch_8")
        self.gridLayout.addWidget(self.radioButton_arch_8, 0, 0, 1, 1)
        self.radioButton_arch_32 = QtGui.QRadioButton(self.groupBox_arch)
        self.radioButton_arch_32.setObjectName("radioButton_arch_32")
        self.gridLayout.addWidget(self.radioButton_arch_32, 0, 1, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_arch, 0, 0, 1, 2)
        self.groupBox_bootloader = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_bootloader.setObjectName("groupBox_bootloader")
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_bootloader)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.radioButton_bootloader_v1_v2 = QtGui.QRadioButton(self.groupBox_bootloader)
        self.radioButton_bootloader_v1_v2.setObjectName("radioButton_bootloader_v1_v2")
        self.gridLayout_3.addWidget(self.radioButton_bootloader_v1_v2, 0, 0, 1, 1)
        self.radioButton_bootloader_v4 = QtGui.QRadioButton(self.groupBox_bootloader)
        self.radioButton_bootloader_v4.setObjectName("radioButton_bootloader_v4")
        self.gridLayout_3.addWidget(self.radioButton_bootloader_v4, 0, 1, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_bootloader, 2, 0, 1, 2)
        self.groupBox_devices_8 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_devices_8.setObjectName("groupBox_devices_8")
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_devices_8)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setContentsMargins(0, -1, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_device_8 = QtGui.QGridLayout()
        self.gridLayout_device_8.setObjectName("gridLayout_device_8")
        self.gridLayout_4.addLayout(self.gridLayout_device_8, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_devices_8, 3, 0, 1, 2)
        self.label_warning = QtGui.QLabel(self.centralwidget)
        self.label_warning.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_warning.setObjectName("label_warning")
        self.gridLayout_5.addWidget(self.label_warning, 7, 0, 1, 2)
        self.groupBox_devices_32 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_devices_32.setObjectName("groupBox_devices_32")
        self.gridLayout_7 = QtGui.QGridLayout(self.groupBox_devices_32)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setContentsMargins(0, -1, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_device_32 = QtGui.QGridLayout()
        self.gridLayout_device_32.setObjectName("gridLayout_device_32")
        self.gridLayout_7.addLayout(self.gridLayout_device_32, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_devices_32, 4, 0, 1, 2)
        self.buttonBox = QtGui.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_5.addWidget(self.buttonBox, 8, 0, 1, 2)
        self.groupBox_mode = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_mode.setObjectName("groupBox_mode")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_mode)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.radioButton_mode_icsp = QtGui.QRadioButton(self.groupBox_mode)
        self.radioButton_mode_icsp.setObjectName("radioButton_mode_icsp")
        self.gridLayout_2.addWidget(self.radioButton_mode_icsp, 0, 0, 1, 1)
        self.radioButton_mode_bootloader = QtGui.QRadioButton(self.groupBox_mode)
        self.radioButton_mode_bootloader.setObjectName("radioButton_mode_bootloader")
        self.gridLayout_2.addWidget(self.radioButton_mode_bootloader, 0, 1, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_mode, 1, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(318, 2, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem, 6, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Board config", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_arch.setTitle(QtGui.QApplication.translate("MainWindow", "Architecture", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_arch_8.setText(QtGui.QApplication.translate("MainWindow", "8-bit", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_arch_32.setText(QtGui.QApplication.translate("MainWindow", "32-bit", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_bootloader.setTitle(QtGui.QApplication.translate("MainWindow", "Bootloader", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_bootloader_v1_v2.setText(QtGui.QApplication.translate("MainWindow", "v1.x or v2.x", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_bootloader_v4.setText(QtGui.QApplication.translate("MainWindow", "v4.x", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_devices_8.setTitle(QtGui.QApplication.translate("MainWindow", "Devices", None, QtGui.QApplication.UnicodeUTF8))
        self.label_warning.setText(QtGui.QApplication.translate("MainWindow", "warning!", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_devices_32.setTitle(QtGui.QApplication.translate("MainWindow", "Devices", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_mode.setTitle(QtGui.QApplication.translate("MainWindow", "Progamming Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_mode_icsp.setText(QtGui.QApplication.translate("MainWindow", "ICSP", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_mode_bootloader.setText(QtGui.QApplication.translate("MainWindow", "USB Bootloader", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
