# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\alex\Documents\Dr Peters\qt\mainwindow.ui'
#
# Created: Sun Apr 29 10:38:22 2012
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(910, 800)
        MainWindow.setMinimumSize(QtCore.QSize(800, 800))
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.views_box = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.views_box.sizePolicy().hasHeightForWidth())
        self.views_box.setSizePolicy(sizePolicy)
        self.views_box.setMinimumSize(QtCore.QSize(145, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.views_box.setFont(font)
        self.views_box.setTitle(_fromUtf8(""))
        self.views_box.setObjectName(_fromUtf8("views_box"))
        self.protein_input_button = QtGui.QCommandLinkButton(self.views_box)
        self.protein_input_button.setEnabled(True)
        self.protein_input_button.setGeometry(QtCore.QRect(10, 44, 131, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(10)
        self.protein_input_button.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/blank.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/right-32.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.protein_input_button.setIcon(icon)
        self.protein_input_button.setCheckable(True)
        self.protein_input_button.setChecked(True)
        self.protein_input_button.setObjectName(_fromUtf8("protein_input_button"))
        self.analysis_button = QtGui.QCommandLinkButton(self.views_box)
        self.analysis_button.setGeometry(QtCore.QRect(10, 90, 131, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(10)
        self.analysis_button.setFont(font)
        self.analysis_button.setAcceptDrops(False)
        self.analysis_button.setAutoFillBackground(False)
        self.analysis_button.setIcon(icon)
        self.analysis_button.setCheckable(True)
        self.analysis_button.setObjectName(_fromUtf8("analysis_button"))
        self.view_label = QtGui.QLabel(self.views_box)
        self.view_label.setGeometry(QtCore.QRect(10, 10, 111, 21))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.view_label.setFont(font)
        self.view_label.setObjectName(_fromUtf8("view_label"))
        self.quick_help_label = QtGui.QLabel(self.views_box)
        self.quick_help_label.setGeometry(QtCore.QRect(10, 170, 71, 16))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.quick_help_label.setFont(font)
        self.quick_help_label.setObjectName(_fromUtf8("quick_help_label"))
        self.quick_help = QtGui.QLabel(self.views_box)
        self.quick_help.setGeometry(QtCore.QRect(10, 199, 131, 301))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.quick_help.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStrikeOut(False)
        self.quick_help.setFont(font)
        self.quick_help.setFrameShape(QtGui.QFrame.NoFrame)
        self.quick_help.setTextFormat(QtCore.Qt.RichText)
        self.quick_help.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.quick_help.setWordWrap(True)
        self.quick_help.setObjectName(_fromUtf8("quick_help"))
        self.gridLayout_2.addWidget(self.views_box, 0, 0, 1, 1)
        self.view_frame = QtGui.QStackedWidget(self.centralwidget)
        self.view_frame.setMinimumSize(QtCore.QSize(0, 0))
        self.view_frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.view_frame.setObjectName(_fromUtf8("view_frame"))
        self.batch_page = QtGui.QWidget()
        self.batch_page.setObjectName(_fromUtf8("batch_page"))
        self.gridLayout_6 = QtGui.QGridLayout(self.batch_page)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.DD_2 = QtGui.QWidget(self.batch_page)
        self.DD_2.setMinimumSize(QtCore.QSize(700, 500))
        self.DD_2.setObjectName(_fromUtf8("DD_2"))
        self.gridLayout_7 = QtGui.QGridLayout(self.DD_2)
        self.gridLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout_7.setHorizontalSpacing(5)
        self.gridLayout_7.setVerticalSpacing(0)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.batch_input = QtGui.QGroupBox(self.DD_2)
        self.batch_input.setMinimumSize(QtCore.QSize(0, 285))
        self.batch_input.setMaximumSize(QtCore.QSize(16777215, 300))
        self.batch_input.setObjectName(_fromUtf8("batch_input"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.batch_input)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.widget_2 = QtGui.QWidget(self.batch_input)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.batch_protein_B_label = QtGui.QLabel(self.widget_2)
        self.batch_protein_B_label.setGeometry(QtCore.QRect(20, 110, 43, 16))
        self.batch_protein_B_label.setObjectName(_fromUtf8("batch_protein_B_label"))
        self.batch_add_button = QtGui.QPushButton(self.widget_2)
        self.batch_add_button.setEnabled(False)
        self.batch_add_button.setGeometry(QtCore.QRect(170, 180, 100, 23))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.batch_add_button.sizePolicy().hasHeightForWidth())
        self.batch_add_button.setSizePolicy(sizePolicy)
        self.batch_add_button.setMinimumSize(QtCore.QSize(100, 0))
        self.batch_add_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.batch_add_button.setObjectName(_fromUtf8("batch_add_button"))
        self.batch_protein_A_button = QtGui.QPushButton(self.widget_2)
        self.batch_protein_A_button.setGeometry(QtCore.QRect(234, 70, 31, 23))
        self.batch_protein_A_button.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/fileopen.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.batch_protein_A_button.setIcon(icon1)
        self.batch_protein_A_button.setObjectName(_fromUtf8("batch_protein_A_button"))
        self.batch_protein_A = QtGui.QLineEdit(self.widget_2)
        self.batch_protein_A.setGeometry(QtCore.QRect(20, 70, 211, 20))
        self.batch_protein_A.setObjectName(_fromUtf8("batch_protein_A"))
        self.batch_protein_B = QtGui.QLineEdit(self.widget_2)
        self.batch_protein_B.setGeometry(QtCore.QRect(20, 130, 211, 20))
        self.batch_protein_B.setObjectName(_fromUtf8("batch_protein_B"))
        self.batch_protein_A_Label = QtGui.QLabel(self.widget_2)
        self.batch_protein_A_Label.setGeometry(QtCore.QRect(20, 50, 44, 16))
        self.batch_protein_A_Label.setObjectName(_fromUtf8("batch_protein_A_Label"))
        self.batch_protein_B_button = QtGui.QPushButton(self.widget_2)
        self.batch_protein_B_button.setGeometry(QtCore.QRect(234, 130, 31, 23))
        self.batch_protein_B_button.setText(_fromUtf8(""))
        self.batch_protein_B_button.setIcon(icon1)
        self.batch_protein_B_button.setObjectName(_fromUtf8("batch_protein_B_button"))
        self.batch_remove_button = QtGui.QPushButton(self.widget_2)
        self.batch_remove_button.setEnabled(False)
        self.batch_remove_button.setGeometry(QtCore.QRect(170, 230, 100, 23))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.batch_remove_button.sizePolicy().hasHeightForWidth())
        self.batch_remove_button.setSizePolicy(sizePolicy)
        self.batch_remove_button.setMinimumSize(QtCore.QSize(100, 0))
        self.batch_remove_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.batch_remove_button.setObjectName(_fromUtf8("batch_remove_button"))
        self.horizontalLayout.addWidget(self.widget_2)
        self.widget = QtGui.QWidget(self.batch_input)
        self.widget.setMinimumSize(QtCore.QSize(400, 0))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.batch_list = QtGui.QListWidget(self.widget)
        self.batch_list.setGeometry(QtCore.QRect(0, 20, 391, 241))
        self.batch_list.setObjectName(_fromUtf8("batch_list"))
        self.batch_list_label = QtGui.QLabel(self.widget)
        self.batch_list_label.setGeometry(QtCore.QRect(0, 0, 321, 21))
        self.batch_list_label.setObjectName(_fromUtf8("batch_list_label"))
        self.horizontalLayout.addWidget(self.widget)
        self.gridLayout_7.addWidget(self.batch_input, 0, 0, 1, 1)
        self.batch_options = QtGui.QGroupBox(self.DD_2)
        self.batch_options.setMinimumSize(QtCore.QSize(0, 0))
        self.batch_options.setMaximumSize(QtCore.QSize(16777215, 161))
        self.batch_options.setObjectName(_fromUtf8("batch_options"))
        self.batch_output_folder_button = QtGui.QPushButton(self.batch_options)
        self.batch_output_folder_button.setGeometry(QtCore.QRect(265, 50, 41, 23))
        self.batch_output_folder_button.setText(_fromUtf8(""))
        self.batch_output_folder_button.setIcon(icon1)
        self.batch_output_folder_button.setObjectName(_fromUtf8("batch_output_folder_button"))
        self.batch_output_folder_label = QtGui.QLabel(self.batch_options)
        self.batch_output_folder_label.setGeometry(QtCore.QRect(25, 30, 91, 16))
        self.batch_output_folder_label.setObjectName(_fromUtf8("batch_output_folder_label"))
        self.batch_output_folder = QtGui.QLineEdit(self.batch_options)
        self.batch_output_folder.setGeometry(QtCore.QRect(25, 50, 231, 20))
        self.batch_output_folder.setObjectName(_fromUtf8("batch_output_folder"))
        self.batch_saving_convention_label = QtGui.QLabel(self.batch_options)
        self.batch_saving_convention_label.setGeometry(QtCore.QRect(25, 90, 111, 16))
        self.batch_saving_convention_label.setObjectName(_fromUtf8("batch_saving_convention_label"))
        self.batch_saving_convention = QtGui.QLineEdit(self.batch_options)
        self.batch_saving_convention.setGeometry(QtCore.QRect(25, 110, 231, 20))
        self.batch_saving_convention.setObjectName(_fromUtf8("batch_saving_convention"))
        self.batch_saving_convention_help_label = QtGui.QLabel(self.batch_options)
        self.batch_saving_convention_help_label.setGeometry(QtCore.QRect(270, 99, 321, 31))
        self.batch_saving_convention_help_label.setObjectName(_fromUtf8("batch_saving_convention_help_label"))
        self.batch_create_folder = QtGui.QCheckBox(self.batch_options)
        self.batch_create_folder.setGeometry(QtCore.QRect(25, 140, 191, 17))
        self.batch_create_folder.setObjectName(_fromUtf8("batch_create_folder"))
        self.batch_open_analysis = QtGui.QCheckBox(self.batch_options)
        self.batch_open_analysis.setGeometry(QtCore.QRect(360, 50, 241, 17))
        self.batch_open_analysis.setObjectName(_fromUtf8("batch_open_analysis"))
        self.gridLayout_7.addWidget(self.batch_options, 1, 0, 1, 1)
        self.input_button_frame_2 = QtGui.QWidget(self.DD_2)
        self.input_button_frame_2.setMinimumSize(QtCore.QSize(0, 37))
        self.input_button_frame_2.setMaximumSize(QtCore.QSize(700, 43))
        self.input_button_frame_2.setObjectName(_fromUtf8("input_button_frame_2"))
        self.batch_map_button = QtGui.QPushButton(self.input_button_frame_2)
        self.batch_map_button.setEnabled(False)
        self.batch_map_button.setGeometry(QtCore.QRect(110, 20, 100, 23))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.batch_map_button.sizePolicy().hasHeightForWidth())
        self.batch_map_button.setSizePolicy(sizePolicy)
        self.batch_map_button.setMinimumSize(QtCore.QSize(100, 0))
        self.batch_map_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.batch_map_button.setObjectName(_fromUtf8("batch_map_button"))
        self.batch_progress_bar = QtGui.QProgressBar(self.input_button_frame_2)
        self.batch_progress_bar.setEnabled(True)
        self.batch_progress_bar.setGeometry(QtCore.QRect(290, 20, 411, 23))
        self.batch_progress_bar.setProperty(_fromUtf8("value"), 0)
        self.batch_progress_bar.setTextVisible(True)
        self.batch_progress_bar.setInvertedAppearance(False)
        self.batch_progress_bar.setObjectName(_fromUtf8("batch_progress_bar"))
        self.gridLayout_7.addWidget(self.input_button_frame_2, 3, 0, 1, 1)
        self.gridLayout_6.addWidget(self.DD_2, 0, 0, 1, 1)
        self.view_frame.addWidget(self.batch_page)
        self.analysis_page = QtGui.QWidget()
        self.analysis_page.setObjectName(_fromUtf8("analysis_page"))
        self.gridLayout_4 = QtGui.QGridLayout(self.analysis_page)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.tabWidget = QtGui.QTabWidget(self.analysis_page)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.new_analysis = QtGui.QWidget()
        self.new_analysis.setEnabled(False)
        self.new_analysis.setObjectName(_fromUtf8("new_analysis"))
        self.gridLayout_5 = QtGui.QGridLayout(self.new_analysis)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.DD = QtGui.QWidget(self.new_analysis)
        self.DD.setMinimumSize(QtCore.QSize(700, 0))
        self.DD.setObjectName(_fromUtf8("DD"))
        self.gridLayout_3 = QtGui.QGridLayout(self.DD)
        self.gridLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.mapping_information = QtGui.QTextEdit(self.DD)
        self.mapping_information.setEnabled(False)
        self.mapping_information.setReadOnly(True)
        self.mapping_information.setObjectName(_fromUtf8("mapping_information"))
        self.gridLayout_3.addWidget(self.mapping_information, 0, 0, 1, 1)
        self.export_box = QtGui.QGroupBox(self.DD)
        self.export_box.setMinimumSize(QtCore.QSize(0, 56))
        self.export_box.setObjectName(_fromUtf8("export_box"))
        self.xls_export_button = QtGui.QPushButton(self.export_box)
        self.xls_export_button.setGeometry(QtCore.QRect(190, 20, 131, 31))
        self.xls_export_button.setObjectName(_fromUtf8("xls_export_button"))
        self.pdb_export_button = QtGui.QPushButton(self.export_box)
        self.pdb_export_button.setGeometry(QtCore.QRect(330, 20, 131, 31))
        self.pdb_export_button.setObjectName(_fromUtf8("pdb_export_button"))
        self.gridLayout_3.addWidget(self.export_box, 2, 0, 1, 1)
        self.graphing_box = QtGui.QGroupBox(self.DD)
        self.graphing_box.setMinimumSize(QtCore.QSize(0, 138))
        self.graphing_box.setObjectName(_fromUtf8("graphing_box"))
        self.graph_button = QtGui.QPushButton(self.graphing_box)
        self.graph_button.setGeometry(QtCore.QRect(470, 60, 75, 23))
        self.graph_button.setObjectName(_fromUtf8("graph_button"))
        self.graph_type_label = QtGui.QLabel(self.graphing_box)
        self.graph_type_label.setGeometry(QtCore.QRect(110, 40, 71, 16))
        self.graph_type_label.setObjectName(_fromUtf8("graph_type_label"))
        self.graph_type = QtGui.QComboBox(self.graphing_box)
        self.graph_type.setGeometry(QtCore.QRect(110, 60, 121, 22))
        self.graph_type.setObjectName(_fromUtf8("graph_type"))
        self.graph_type.addItem(_fromUtf8(""))
        self.graph_data = QtGui.QComboBox(self.graphing_box)
        self.graph_data.setGeometry(QtCore.QRect(240, 60, 221, 22))
        self.graph_data.setObjectName(_fromUtf8("graph_data"))
        self.graph_data.addItem(_fromUtf8(""))
        self.graph_data.addItem(_fromUtf8(""))
        self.graph_data.addItem(_fromUtf8(""))
        self.graph_data_label = QtGui.QLabel(self.graphing_box)
        self.graph_data_label.setGeometry(QtCore.QRect(240, 40, 71, 16))
        self.graph_data_label.setObjectName(_fromUtf8("graph_data_label"))
        self.graph_filter_hi = QtGui.QCheckBox(self.graphing_box)
        self.graph_filter_hi.setGeometry(QtCore.QRect(310, 100, 91, 20))
        self.graph_filter_hi.setObjectName(_fromUtf8("graph_filter_hi"))
        self.graph_filter_amount_hi = QtGui.QSpinBox(self.graphing_box)
        self.graph_filter_amount_hi.setGeometry(QtCore.QRect(410, 100, 42, 22))
        self.graph_filter_amount_hi.setMinimum(-20)
        self.graph_filter_amount_hi.setMaximum(20)
        self.graph_filter_amount_hi.setProperty(_fromUtf8("value"), 0)
        self.graph_filter_amount_hi.setObjectName(_fromUtf8("graph_filter_amount_hi"))
        self.graph_filter_amount_low = QtGui.QSpinBox(self.graphing_box)
        self.graph_filter_amount_low.setGeometry(QtCore.QRect(230, 100, 42, 22))
        self.graph_filter_amount_low.setMinimum(-20)
        self.graph_filter_amount_low.setMaximum(20)
        self.graph_filter_amount_low.setProperty(_fromUtf8("value"), 0)
        self.graph_filter_amount_low.setObjectName(_fromUtf8("graph_filter_amount_low"))
        self.graph_filter_low = QtGui.QCheckBox(self.graphing_box)
        self.graph_filter_low.setGeometry(QtCore.QRect(130, 100, 91, 20))
        self.graph_filter_low.setObjectName(_fromUtf8("graph_filter_low"))
        self.gridLayout_3.addWidget(self.graphing_box, 1, 0, 1, 1)
        self.gridLayout_5.addWidget(self.DD, 0, 0, 1, 1)
        self.tabWidget.addTab(self.new_analysis, _fromUtf8(""))
        self.gridLayout_4.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.view_frame.addWidget(self.analysis_page)
        self.gridLayout_2.addWidget(self.view_frame, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 910, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QtGui.QDockWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget.sizePolicy().hasHeightForWidth())
        self.dockWidget.setSizePolicy(sizePolicy)
        self.dockWidget.setMinimumSize(QtCore.QSize(274, 232))
        self.dockWidget.setFeatures(QtGui.QDockWidget.DockWidgetFloatable)
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.gridLayout = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.console = QtGui.QLabel(self.dockWidgetContents)
        self.console.setAutoFillBackground(False)
        self.console.setFrameShape(QtGui.QFrame.Panel)
        self.console.setFrameShadow(QtGui.QFrame.Sunken)
        self.console.setText(_fromUtf8(""))
        self.console.setTextFormat(QtCore.Qt.LogText)
        self.console.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.console.setWordWrap(True)
        self.console.setObjectName(_fromUtf8("console"))
        self.gridLayout.addWidget(self.console, 0, 0, 1, 1)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidget)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionProtein_Input = QtGui.QAction(MainWindow)
        self.actionProtein_Input.setCheckable(True)
        self.actionProtein_Input.setChecked(True)
        self.actionProtein_Input.setObjectName(_fromUtf8("actionProtein_Input"))
        self.actionAnalysis = QtGui.QAction(MainWindow)
        self.actionAnalysis.setCheckable(True)
        self.actionAnalysis.setObjectName(_fromUtf8("actionAnalysis"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionOpen_Results = QtGui.QAction(MainWindow)
        self.actionOpen_Results.setObjectName(_fromUtf8("actionOpen_Results"))
        self.menuFile.addAction(self.actionOpen_Results)
        self.menuFile.addAction(self.actionQuit)
        self.menuView.addAction(self.actionProtein_Input)
        self.menuView.addAction(self.actionAnalysis)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.view_frame.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Protein Contact Mapping", None, QtGui.QApplication.UnicodeUTF8))
        self.protein_input_button.setText(QtGui.QApplication.translate("MainWindow", "Protein Input", None, QtGui.QApplication.UnicodeUTF8))
        self.analysis_button.setText(QtGui.QApplication.translate("MainWindow", "Analysis", None, QtGui.QApplication.UnicodeUTF8))
        self.view_label.setText(QtGui.QApplication.translate("MainWindow", "Views", None, QtGui.QApplication.UnicodeUTF8))
        self.quick_help_label.setText(QtGui.QApplication.translate("MainWindow", "Quick Help", None, QtGui.QApplication.UnicodeUTF8))
        self.quick_help.setText(QtGui.QApplication.translate("MainWindow", "In the \"Protein Input\" view, you can select different protein (.pdb) files to map to each other. Multiple mappings can be set up to run as a batch.", None, QtGui.QApplication.UnicodeUTF8))
        self.batch_input.setTitle(QtGui.QApplication.translate("MainWindow", "Protein Input", None, QtGui.QApplication.UnicodeUTF8))
        self.batch_protein_B_label.setText(QtGui.QApplication.translate("MainWindow", "Protein B", None, QtGui.QApplication.UnicodeUTF8))
        self.batch_add_button.setText(QtGui.QApplication.translate("MainWindow", "Add ->", None, QtGui.QApplication.UnicodeUTF8))
        self.batch_protein_A_Label.setText(QtGui.QApplication.translate("MainWindow", "Protein A", None, QtGui.QApplication.UnicodeUTF8))
        self.batch_remove_button.setText(QtGui.QApplication.translate("MainWindow", "Remove <-", None, QtGui.QApplication.UnicodeUTF8))
        self.batch_list_label.setText(QtGui.QApplication.translate("MainWindow", "Mappings to process:", None, QtGui.QApplication.UnicodeUTF8))
        self.batch_options.setTitle(QtGui.QApplication.translate("MainWindow", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.batch_output_folder_label.setText(QtGui.QApplication.translate("MainWindow", "Output Destination", None, QtGui.QApplication.UnicodeUTF8))
        self.batch_saving_convention_label.setText(QtGui.QApplication.translate("MainWindow", "Filename Convention", None, QtGui.QApplication.UnicodeUTF8))
        self.batch_saving_convention_help_label.setText(QtGui.QApplication.translate("MainWindow", "%d - date, %n - protein names, %t - time, %q - batch id", None, QtGui.QApplication.UnicodeUTF8))
        self.batch_create_folder.setText(QtGui.QApplication.translate("MainWindow", "Create new folder for each mapping", None, QtGui.QApplication.UnicodeUTF8))
        self.batch_open_analysis.setText(QtGui.QApplication.translate("MainWindow", "Load result(s) into analysis when completed", None, QtGui.QApplication.UnicodeUTF8))
        self.batch_map_button.setText(QtGui.QApplication.translate("MainWindow", "Run", None, QtGui.QApplication.UnicodeUTF8))
        self.export_box.setTitle(QtGui.QApplication.translate("MainWindow", "Export", None, QtGui.QApplication.UnicodeUTF8))
        self.xls_export_button.setText(QtGui.QApplication.translate("MainWindow", "Export to .xls (Excel)", None, QtGui.QApplication.UnicodeUTF8))
        self.pdb_export_button.setText(QtGui.QApplication.translate("MainWindow", "Export combined .pdb", None, QtGui.QApplication.UnicodeUTF8))
        self.graphing_box.setTitle(QtGui.QApplication.translate("MainWindow", "Graphing", None, QtGui.QApplication.UnicodeUTF8))
        self.graph_button.setText(QtGui.QApplication.translate("MainWindow", "Graph", None, QtGui.QApplication.UnicodeUTF8))
        self.graph_type_label.setText(QtGui.QApplication.translate("MainWindow", "Graph Type", None, QtGui.QApplication.UnicodeUTF8))
        self.graph_type.setItemText(0, QtGui.QApplication.translate("MainWindow", "2D Map", None, QtGui.QApplication.UnicodeUTF8))
        self.graph_data.setItemText(0, QtGui.QApplication.translate("MainWindow", "Residue-Residue Separation", None, QtGui.QApplication.UnicodeUTF8))
        self.graph_data.setItemText(1, QtGui.QApplication.translate("MainWindow", "Lennard-Jones", None, QtGui.QApplication.UnicodeUTF8))
        self.graph_data.setItemText(2, QtGui.QApplication.translate("MainWindow", "Coulombic Potential", None, QtGui.QApplication.UnicodeUTF8))
        self.graph_data_label.setText(QtGui.QApplication.translate("MainWindow", "Graph Data", None, QtGui.QApplication.UnicodeUTF8))
        self.graph_filter_hi.setText(QtGui.QApplication.translate("MainWindow", "Graph Ceiling", None, QtGui.QApplication.UnicodeUTF8))
        self.graph_filter_low.setText(QtGui.QApplication.translate("MainWindow", "Graph Floor", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.new_analysis), QtGui.QApplication.translate("MainWindow", "(New Analysis)", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuView.setTitle(QtGui.QApplication.translate("MainWindow", "View", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Console", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionProtein_Input.setText(QtGui.QApplication.translate("MainWindow", "Protein Input", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAnalysis.setText(QtGui.QApplication.translate("MainWindow", "Analysis", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_Results.setText(QtGui.QApplication.translate("MainWindow", "Open Results for Analysis", None, QtGui.QApplication.UnicodeUTF8))

import mainwindow_rc
