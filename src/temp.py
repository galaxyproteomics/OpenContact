#import QT modules
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from GUI import *

#import fortran modules
from contact import *
from inputUtil import *

#import util modules
import sys
import shutil
import os
import time
import subprocess
#from openpyxl import Workbook
import win32com.client as win32

#import plotting modules
#from mpl_toolkits.mplot3d import axes3d
import numpy as np
import matplotlib
matplotlib.use('Qt4Agg')
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.ticker import MaxNLocator, FixedFormatter, AutoLocator, FuncFormatter

#CUSTOM TAB BAR CLASS
class NTabBar(QTabBar):

    def __init__(self, *args):
        apply(QTabBar.__init__, (self,) + args)


#CONTACT MAPPER CLASS
class ContactMapper(QtGui.QMainWindow, Ui_MainWindow):

    filename = ""
    previousFilename = "."
    progressBarInterval = 0
    tabs = []
    placeholder = None
    atomLabelA = []
    atomLabelB = []
    atomNumberA = []
    atomNumberB = []
    sepDistance = []
    lennardJones = []
    coulombicPotential = []
    WAIT = 1
    RELEASE = 2
    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        #setup signals and slots

        self.connect(self.ui.protein_input_button, SIGNAL("clicked()"), lambda v=0 : self.selectView(v))
        self.connect(self.ui.analysis_button, SIGNAL("clicked()"), lambda v=1 : self.selectView(v))
        self.connect(self.ui.actionProtein_Input, SIGNAL("triggered()"), lambda v=0 : self.selectView(v))
        self.connect(self.ui.actionAnalysis, SIGNAL("triggered()"), lambda v=1 : self.selectView(v))

        self.connect(self.ui.actionOpen_Results, SIGNAL("triggered()"), lambda b="actionOpen_Results" : self.browseClick(b))
        self.connect(self.ui.batch_protein_A_button, SIGNAL("clicked()"), lambda b="batch_protein_A" : self.browseClick(b))
        self.connect(self.ui.batch_protein_B_button, SIGNAL("clicked()"), lambda b="batch_protein_B" : self.browseClick(b))
        self.connect(self.ui.batch_output_folder_button, SIGNAL("clicked()"), lambda b="batch_output_folder" : self.browseClick(b))

        self.ui.graph_button.clicked.connect(self.graphClick)
        self.ui.xls_export_button.clicked.connect(self.loadExcel)
        self.ui.pdb_export_button.clicked.connect(self.exportPDB)

        self.ui.batch_add_button.clicked.connect(self.addToBatch)
        self.ui.batch_remove_button.clicked.connect(self.removeFromBatch)
        self.ui.batch_output_folder.editingFinished.connect(self.checkEnabled)
        self.ui.batch_saving_convention.textEdited.connect(self.checkEnabled)
        self.ui.batch_map_button.clicked.connect(self.batchExecute)
#        self.ui.graph_button.clicked.connect(self.graph)
        self.ui.tabWidget.tabCloseRequested.connect(self.checkTabs)
        #self.connect(self.ui.new_analysis, SIGNAL("currentChanged(int)"),self.newAnalysis)

        #self.test()

        
    #SIGNAL AND SLOT HANDLING
    def exportPDB(self):
        self.output("Exporting combined PDB...",self.WAIT)
        time.sleep(1)
        self.output("Completed!",self.RELEASE)
        
    def loadExcel(self): 
        if os.path.isfile(self.filename):
            xl = win32.gencache.EnsureDispatch('Excel.Application')
            xl.Visible = True
            ss = xl.Workbooks.OpenText(self.filename,437,1,1,-4142,False,False,False,True)
            sb = xl.Workbooks(1)
            sh = sb.ActiveSheet
            sh.Rows(1).Insert(-4121)
            sh.Cells(1,1).Value = 'Residue A Name'
            sh.Cells(1,2).Value = 'Residue A Number'
            sh.Cells(1,3).Value = 'Atom A Name'
            sh.Cells(1,4).Value = 'Atom A Number'
            sh.Cells(1,5).Value = 'Residue B Name'
            sh.Cells(1,6).Value = 'Residue B Number'
            sh.Cells(1,7).Value = 'Atom B Name'
            sh.Cells(1,8).Value = 'Atom B Number'
            sh.Cells(1,9).Value = 'Separation Distance'
            sh.Cells(1,10).Value = 'Lennard-Jones'
            sh.Cells(1,11).Value = 'Coulombic Potential'
 
             
        
 
        
    def addToBatch(self):
        if self.ui.batch_protein_A.text() != "" and self.ui.batch_protein_B.text() !="":
            pathA = self.ui.batch_protein_A.text()
            pathB = self.ui.batch_protein_B.text()
            if os.sep == "\\":
                pathA = pathA.replace("/","\\")
                pathB = pathB.replace("/","\\")
            temp = "batch id: "+str(self.ui.batch_list.count()+1)+"\nprotA: "+pathA + "\nprotB: "+ pathB
            QListWidgetItem(temp, self.ui.batch_list)
            self.ui.batch_protein_A.setText("")
            self.ui.batch_protein_B.setText("")
            self.checkEnabled()
                
    def removeFromBatch(self):
        if self.ui.batch_list.currentItem()!= None:
            self.ui.batch_list.takeItem(self.ui.batch_list.currentRow())
            self.output("item removed")
            self.checkEnabled()
       
    def selectView(self,view):
        if view==0:
            self.ui.protein_input_button.setChecked(True)
            self.ui.analysis_button.setChecked(False)
            self.ui.actionProtein_Input.setChecked(True)
            self.ui.actionAnalysis.setChecked(False)
            self.ui.quick_help.setText("In the \"Protein Input\" view, you can select different protein (.pdb) files to map to each other. Multiple mappings can be set up to run as a batch.")
        if view==1:
            self.ui.protein_input_button.setChecked(False)
            self.ui.analysis_button.setChecked(True)
            self.ui.actionProtein_Input.setChecked(False)
            self.ui.actionAnalysis.setChecked(True)
            self.ui.quick_help.setText("In the \"Analysis\" view, you can view logged output from the protein mapping. In addition, you can graph different results from the mapping, as well as export the results.")
        self.ui.view_frame.setCurrentIndex(view)
        self.repaint()
        
    def browseClick(self, whichBrowse):
        if whichBrowse == "batch_protein_A":
            self.filename=QFileDialog.getOpenFileName(self, "Open Protein A", self.previousFilename, "*.pdb")
            self.ui.batch_protein_A.setText(self.filename)
        elif whichBrowse == "batch_protein_B":
            self.filename=QFileDialog.getOpenFileName(self, "Open Protein B", self.previousFilename, "*.pdb")
            self.ui.batch_protein_B.setText(self.filename)
        elif whichBrowse == "batch_output_folder":
            self.filename=QFileDialog.getExistingDirectory(self, "Open Protein B", self.previousFilename)
            self.ui.batch_output_folder.setText(self.filename)
        elif whichBrowse == "actionOpen_Results":
            self.filename=QFileDialog.getOpenFileName(self, "Open Protein Contact Results File", self.previousFilename, "*.pcr")
            if self.filename != "":
                self.loadResults(self.filename)
        self.checkEnabled()
        self.previousFilename = self.filename

    def loadResults(self, filename):
        self.selectView(1)
#        if self.ui.tabWidget.count()==1:
#        self.placeholder = self.ui.new_analysis
#            self.ui.tabWidget.removeTab(0)
#            self.ui.tabWidget.setTabsClosable(True)
#        self.tabs.append(self.generateAnalysisWidget())
#        self.tabs.append(copy.deepcopy(self.placeholder))
#        self.ui.tabWidget.insertTab(self.ui.tabWidget.count()-1,self.tabs[self.ui.tabWidget.count()],self.filename.split(os.sep)[-1].replace(".pcr",""))
#        analysisWidget = copy.deepcopy(self.ui.new_analysis)
        analysisWidget = self.ui.new_analysis
        aw = QWidget()
        self.ui.tabWidget.addTab(analysisWidget,filename.split(os.sep)[-1].replace(".pcr",""))
#        self.ui.tabWidget.addTab(analysisWidget,"test")
        if os.path.isfile(self.filename+".s"):
            tempString=""
            count_a = 0
            count_b = 0
            counter = 0
            with open(self.filename+".s","r") as fort18:
                for line in fort18:
                    counter+=1
                    if counter==7:
                        count_a = line[28:]
                    if counter==8:
                        count_b = line[28:]
                    tempString = tempString + line
                tempWidget = self.ui.tabWidget.widget(self.ui.tabWidget.count()-1).findChild(QTextEdit)
                tempWidget.setText(tempString)
                tempWidget.setEnabled(True)
            print count_a + " " + count_b
            self.generateArrays(self.filename,count_a,count_b)
            self.ui.tabWidget.currentWidget().setEnabled(True)
            self.ui.xls_export_button.setEnabled(True)

    def checkTabs(self,index):
        self.ui.tabWidget.removeTab(index)
        if self.ui.tabWidget.count()==0:
            self.ui.tabWidget.setTabsClosable(False)
            self.ui.tabWidget.addTab(self.placeholder,"(New Analysis)")
        
    def batchExecute(self):
        self.setEnabled(False)
        self.output("---------------------------", self.WAIT)
        self.output("| MAPPING STARTED |")
        self.output("---------------------------\n")
        if self.ui.batch_open_analysis.isChecked():
            progressBarInterval = 90 / self.ui.batch_list.count() / 4
        else:
            progressBarInterval = 90 / self.ui.batch_list.count() / 3
        self.ui.batch_progress_bar.setValue(5)
        tempString = ""
        for t in range(0,self.ui.batch_list.count()):
            self.output("Currently mapping Batch Id: "+str(t+1))
            tempString = self.ui.batch_list.item(t).text()
            tempList = tempString.split("\n")
            self.prepareProteins(tempList[1].replace("protA: ",""), tempList[2].replace("protB: ",""))
            self.generateContactMapping()
            tempString = self.ui.batch_saving_convention.text()
            tempString.replace("%d",time.strftime("%d-%b-%Y"))
            tempString.replace("%t",time.strftime("%H_%M_%S"))

            tempString.replace("%n", tempList[1].split(os.sep)[-1].replace(".pdb","") + " and "+ tempList[2].split(os.sep)[-1].replace(".pdb",""))
            tempString.replace("%q",str(t+1))
            self.saveResults(tempString)
            self.output("Cleaning up temp files...")
            cleanup()
            self.output("Done. Batch Id "+str(t+1)+" finished.\n", self.RELEASE)
        self.ui.batch_list.clear()
        self.ui.batch_progress_bar.setValue(100)
        if self.ui.batch_open_analysis.isChecked():
            self.filename=self.ui.batch_output_folder.text()+os.sep+tempString+".pcr"
            self.loadResults(self.filename)
        self.checkEnabled()
        self.setEnabled(True)

            
    def graphClick(self):
        self.output("Graphing started...",self.WAIT)
        start_time = time.time()
        filterWidget = self.ui.tabWidget.currentWidget().findChild(QWidget).findChild(QCheckBox)
        filterAmount = None
        if filterWidget.isChecked():
            filterAmount = self.ui.tabWidget.currentWidget().findChild(QWidget).findChild(QSpinBox).value()
        if self.ui.tabWidget.currentWidget().findChild(QWidget).findChild(QComboBox,"graph_data").currentIndex() == 0:
            self.showGraph(self.sepDistance,"Angstroms apart", filterAmount)
        elif self.ui.tabWidget.currentWidget().findChild(QWidget).findChild(QComboBox,"graph_data").currentIndex() == 1:
            self.showGraph(self.lennardJones,"P",filterAmount)
        elif self.ui.tabWidget.currentWidget().findChild(QWidget).findChild(QComboBox,"graph_data").currentIndex() == 2:
            self.showGraph(self.coulombicPotential,"P",filterAmount)
        end_time = time.time()
        elapsed = end_time - start_time
        self.output("Done. "+ str(elapsed)+ "s elapsed",self.RELEASE)
        

    #GRAPHING METHOD
    def showGraph(self, value, unitLabel, filterAmount):
        A = np.array(self.atomNumberA)
        B = np.array(self.atomNumberB)
        S = value
        if filterAmount != None:
            for i in range(0,len(S)):
                if unitLabel == "Angstroms apart":
                    if S[i] > filterAmount:
                        S[i] = filterAmount
                else:
                    if S[i] > -filterAmount:
                        S[i] = -filterAmount
        A = np.unique(A)
        B = np.unique(B)
        Z = np.zeros((A.size,B.size))
        i = 0
        for x in range(0,A.size):
            for y in range(0,B.size):
                Z[x,y] = S[i]
                i=i+1
        fig = plt.figure()
        majorYFormatter = FuncFormatter(self.yaxis)
        majorXFormatter = FuncFormatter(self.xaxis)
        majorXLocator = MaxNLocator(nbins=20,integer=True)
        majorYLocator = MaxNLocator(nbins=20,integer=True)
        #print np.size(A)
        #print np.size(B)
        #print len(self.atomLabelA)
        #print len(self.atomLabelB)
        plt.xticks( rotation=90 )
        ax = fig.add_subplot(111)
        CS = ax.contourf(B,A,Z,10,rstride=10,cstride=10,cmap=cm.hot_r)
        CB = plt.colorbar(CS, shrink=0.8, extend='both')
        CB.ax.set_ylabel(unitLabel)
        ax.set_xlabel('Protein B')
        ax.set_ylabel('Protein A')
        ax.xaxis.set_major_locator(majorXLocator)
        ax.yaxis.set_major_locator(majorYLocator)
        ax.xaxis.set_major_formatter(majorXFormatter)
        ax.yaxis.set_major_formatter(majorYFormatter)
        ax.grid(True)
        fig.set_size_inches(19.2,12)
        plt.show()
        
    def xaxis(self, x, pos):
        """Formatter for X axis, values are in megabytes"""
        #print x
        if x< len(self.atomLabelB):
            return '%s' % (self.atomLabelB[int(x)])

    def yaxis(self, x, pos):
        """Formatter for Y axis, values are in megabytes"""
        #print x
        if x< len(self.atomLabelA):
            return '%s' % (self.atomLabelA[int(x)])


    def graphSepDistance(self):
        A = np.array(self.atomNumberA)
        B = np.array(self.atomNumberB)
        S = np.array(self.sepDistance)
        #maximum = np.maximum(S)
        print S
        filterWidget = self.ui.tabWidget.currentWidget().findChild(QWidget).findChild(QCheckBox)
        filterAmount = self.ui.tabWidget.currentWidget().findChild(QWidget).findChild(QSpinBox).value()
        if filterWidget.isChecked():            
            for i in range(0,len(S)):
                if S[i] > filterAmount:
                    S[i] = 9
        A = np.unique(A)
        B = np.unique(B)
        Ylabel = np.array(self.atomResA)
        Xlabel = np.array(self.atomResB)
        Z = np.zeros((A.size,B.size))
        i = 0
        for x in range(0,A.size):
            for y in range(0,B.size):
                Z[x,y] = S[i]
                i=i+1
        fig = plt.figure()
        #ax = fig.add_subplot(111,projection='3d')
        #ax = fig.gca(projection='3d')
        print(np.size(Xlabel))
        ax = fig.add_subplot(111)# yticklabels=Ylabel)
        ax.set_yticklabels(Ylabel,size="xx-small")
        ax.set_xticklabels(Xlabel,size="xx-small",rotation="vertical")
        #ax.plot(A,B,Z)
        ax.contourf(B,A,Z,10,rstride=10,cstride=10)
        #ax.set_title("Title")
        ax.grid(True)
        #fig.set_size_inches(9.6,6)
        fig.set_size_inches(19.2,12)
        #plt.savefig("image/test.png", dpi=150)
        plt.show()
        

    #UTILITY METHODS
    def generateAnalysisWidget(self):
        new_analysis = QtGui.QWidget()
        new_analysis.setEnabled(False)
        new_analysis.setObjectName("new_analysis")
        gridLayout_5 = QtGui.QGridLayout(new_analysis)
        gridLayout_5.setObjectName("gridLayout_5")
        DD = QtGui.QWidget(new_analysis)
        DD.setMinimumSize(QtCore.QSize(700, 0))
        DD.setObjectName("DD")
        gridLayout_3 = QtGui.QGridLayout(DD)
        gridLayout_3.setContentsMargins(-1, 0, -1, -1)
        gridLayout_3.setObjectName("gridLayout_3")
        mapping_information = QtGui.QTextEdit(DD)
        mapping_information.setEnabled(False)
        mapping_information.setReadOnly(True)
        mapping_information.setObjectName("mapping_information")
        gridLayout_3.addWidget(mapping_information, 0, 0, 1, 1)
        graphing_box = QtGui.QGroupBox(DD)
        graphing_box.setMinimumSize(QtCore.QSize(0, 138))
        graphing_box.setObjectName("graphing_box")
        graph_button = QtGui.QPushButton(graphing_box)
        graph_button.setGeometry(QtCore.QRect(470, 60, 75, 23))
        graph_button.setObjectName("graph_button")
        graph_type_label = QtGui.QLabel(graphing_box)
        graph_type_label.setGeometry(QtCore.QRect(110, 40, 71, 16))
        graph_type_label.setObjectName("graph_type_label")
        graph_type = QtGui.QComboBox(graphing_box)
        graph_type.setGeometry(QtCore.QRect(110, 60, 121, 22))
        graph_type.setObjectName("graph_type")
        graph_type.addItem("")
        graph_type.addItem("")
        graph_data = QtGui.QComboBox(graphing_box)
        graph_data.setGeometry(QtCore.QRect(240, 60, 221, 22))
        graph_data.setObjectName("graph_data")
        graph_data.addItem("")
        graph_data.addItem("")
        graph_data.addItem("")
        graph_data_label = QtGui.QLabel(graphing_box)
        graph_data_label.setGeometry(QtCore.QRect(240, 40, 71, 16))
        graph_data_label.setObjectName("graph_data_label")
        graph_filter = QtGui.QCheckBox(graphing_box)
        graph_filter.setGeometry(QtCore.QRect(180, 100, 201, 20))
        graph_filter.setObjectName("graph_filter")
        graph_filter.setText("Distance threshold filter (angstroms)")
        graph_filter_amount = QtGui.QSpinBox(graphing_box)
        graph_filter_amount.setGeometry(QtCore.QRect(380, 100, 42, 22))
        graph_filter_amount.setMaximum(20)
        graph_filter_amount.setProperty("value", 10)
        graph_filter_amount.setObjectName("graph_filter_amount")
        gridLayout_3.addWidget(graphing_box, 1, 0, 1, 1)
        export_box = QtGui.QGroupBox(DD)
        export_box.setMinimumSize(QtCore.QSize(0, 56))
        export_box.setObjectName("export_box")
        xls_export_button = QtGui.QPushButton(export_box)
        xls_export_button.setGeometry(QtCore.QRect(190, 30, 131, 31))
        xls_export_button.setObjectName("xls_export_button")
        pdb_export_button = QtGui.QPushButton(export_box)
        pdb_export_button.setGeometry(QtCore.QRect(330, 30, 131, 31))
        pdb_export_button.setObjectName("pdb_export_button")
        gridLayout_3.addWidget(export_box, 2, 0, 1, 1)
        gridLayout_5.addWidget(DD, 0, 0, 1, 1)
        graph_type_label.setText(QtGui.QApplication.translate("MainWindow", "Graph Type", None, QtGui.QApplication.UnicodeUTF8))
        graphing_box.setTitle(QtGui.QApplication.translate("MainWindow", "Graphing", None, QtGui.QApplication.UnicodeUTF8))
        graph_button.setText(QtGui.QApplication.translate("MainWindow", "Graph", None, QtGui.QApplication.UnicodeUTF8))
        graph_type.setItemText(0, QtGui.QApplication.translate("MainWindow", "2D Map", None, QtGui.QApplication.UnicodeUTF8))
        graph_type.setItemText(1, QtGui.QApplication.translate("MainWindow", "3D Plot", None, QtGui.QApplication.UnicodeUTF8))
        graph_data.setItemText(0, QtGui.QApplication.translate("MainWindow", "Residue-Residue Separation", None, QtGui.QApplication.UnicodeUTF8))
        graph_data.setItemText(1, QtGui.QApplication.translate("MainWindow", "Lennard-Jones", None, QtGui.QApplication.UnicodeUTF8))
        graph_data.setItemText(2, QtGui.QApplication.translate("MainWindow", "Coulombic Potential", None, QtGui.QApplication.UnicodeUTF8))
        graph_data_label.setText(QtGui.QApplication.translate("MainWindow", "Graph Data", None, QtGui.QApplication.UnicodeUTF8))
        export_box.setTitle(QtGui.QApplication.translate("MainWindow", "Export", None, QtGui.QApplication.UnicodeUTF8))
        xls_export_button.setText(QtGui.QApplication.translate("MainWindow", "Export to .xls (Excel)", None, QtGui.QApplication.UnicodeUTF8))
        pdb_export_button.setText(QtGui.QApplication.translate("MainWindow", "Export combined .pdb", None, QtGui.QApplication.UnicodeUTF8))
        graph_button.clicked.connect(self.graphClick)
        return new_analysis

    def inputUtil(self):
        resfile = []
        ljfile = []
        cfile = []
        nfile = []
        prota = []
        protb = []
        with open("residc03.pdb", "r") as residue:
            for line in residue:
                tempdict = {"card":line[0:6],"nbar":line[6:11],"atomna":line[12:16],
                            "alt":line[16:17],"resna":line[17:20],
                            "chid":line[21:22], "resnr":line[22:26],"code":line[26:27],
                            "x":line[31:39], "y":line[39:47], "z":line[47:55],
                            "mass":line[55:63], "charge":line[63:70]
                            }
                resfile.append(tempdict)
        with open("ljresid", "r") as lj:
            for line in lj:
                tempdict = {"card":line[0:6],"nbar":line[6:11],"atomna":line[12:16],
                            "alt":line[16:17],"resna":line[17:20],
                            "chid":line[21:22], "resnr":line[22:26],"code":line[26:27],
                            "sig":line[28:37], "eps":line[37:46]
                            }
                ljfile.append(tempdict)
        with open("ctresc03.pdb", "r") as c:
            for line in c:
                tempdict = {"card":line[0:6],"nbar":line[6:11],"atomna":line[12:16],
                            "alt":line[16:17],"resna":line[17:20],
                            "chid":line[21:22], "resnr":line[22:26],"code":line[26:27],
                            "x":line[31:39], "y":line[39:47], "z":line[47:55],
                            "mass":line[55:63], "charge":line[63:70]
                            }
                cfile.append(tempdict)
        with open("ntresc03.pdb", "r") as n:
            for line in n:
                tempdict = {"card":line[0:6],"nbar":line[6:11],"atomna":line[12:16],
                            "alt":line[16:17],"resna":line[17:20],
                            "chid":line[21:22], "resnr":line[22:26],"code":line[26:27],
                            "x":line[31:39], "y":line[39:47], "z":line[47:55],
                            "mass":line[55:63], "charge":line[63:70]
                            }
                nfile.append(tempdict)
        with open("prota.pdb","r") as pa:
            for line in pa:
                tempdict = {"card":line[0:6],"nbar":line[6:11],"atomna":line[12:16],
                            "alt":line[16:17],"resna":line[17:20],
                            "chid":line[21:22], "resnr":line[22:26],"code":line[26:27],
                            "x":line[31:39], "y":line[39:47], "z":line[47:55]
                            }
                prota.append(tempdict)
        with open("protb.pdb","r") as pb:
            for line in pb:
                tempdict = {"card":line[0:6],"nbar":line[6:11],"atomna":line[12:16],
                            "alt":line[16:17],"resna":line[17:20],
                            "chid":line[21:22], "resnr":line[22:26],"code":line[26:27],
                            "x":line[31:39], "y":line[39:47], "z":line[47:55]
                            }
                protb.append(tempdict)
        protfilea = open("proteina", 'w')
        ljfilea = open("lja", 'w')
        atomfilea = open("atnma", 'w')
        number=0
        for prot in prota:
            for res in resfile:
                if prot["resna"]==res["resna"] and prot["atomna"]==res["atomna"]:
                    protfilea.write(prot["card"]+prot["nbar"]+" "+prot["atomna"]+prot["alt"]+
                                    prot["resna"]+" "+prot["chid"]+prot["resnr"]+prot["code"]+"    "+
                                    prot["x"]+prot["y"]+prot["z"]+res["mass"]+res["charge"]+"\n")
                    number=number+1
            if prot["atomna"] == " OXT":
                for c in cfile:
                    if prot["resna"]==c["resna"] and prot["atomna"]==c["atomna"]:
                        protfilea.write(prot["card"]+prot["nbar"]+" "+prot["atomna"]+prot["alt"]+
                                        prot["resna"]+" "+prot["chid"]+prot["resnr"]+prot["code"]+"    "+
                                        prot["x"]+prot["y"]+prot["z"]+c["mass"]+c["charge"]+"\n")
                        number=number+1
            elif prot["atomna"] == " HT1" or prot["atomna"] == " HT2":
                for n in nfile:
                    if prot["resna"]==n["resna"] and prot["atomna"]==n["atomna"]:
                        protfilea.write(prot["card"]+prot["nbar"]+" "+prot["atomna"]+prot["alt"]+
                                        prot["resna"]+" "+prot["chid"]+prot["resnr"]+prot["code"]+"     "+
                                        prot["x"]+prot["y"]+prot["z"]+n["mass"]+n["charge"]+"\n")
                        number=number+1
            for lj in ljfile:
                if prot["resna"]==lj["resna"] and prot["atomna"]==lj["atomna"]:
                    ljfilea.write(prot["card"]+prot["nbar"]+" "+prot["atomna"]+prot["alt"]+
                                    prot["resna"]+" "+prot["chid"]+prot["resnr"]+prot["code"]+" "+
                                    lj["sig"]+lj["eps"]+"\n")
        number_string = str(number)
        number_a=number
        while(len(number_string)<6):
            number_string = "0"+number_string
        atomfilea.write(number_string)
        atomfilea.close()
        ljfilea.close()
        protfilea.close()

        protfileb = open("proteinb", 'w')
        ljfileb = open("ljb", 'w')
        atomfileb = open("atnmb", 'w')
        number=0
        for prot in protb:
            for res in resfile:
                if prot["resna"]==res["resna"] and prot["atomna"]==res["atomna"]:
                    protfileb.write(prot["card"]+prot["nbar"]+" "+prot["atomna"]+prot["alt"]+
                                    prot["resna"]+" "+prot["chid"]+prot["resnr"]+prot["code"]+"    "+
                                    prot["x"]+prot["y"]+prot["z"]+res["mass"]+res["charge"]+"\n")
                    number=number+1
            if prot["atomna"] == " OXT":
                for c in cfile:
                    if prot["resna"]==c["resna"] and prot["atomna"]==c["atomna"]:
                        protfileb.write(prot["card"]+prot["nbar"]+" "+prot["atomna"]+prot["alt"]+
                                        prot["resna"]+" "+prot["chid"]+prot["resnr"]+prot["code"]+"    "+
                                        prot["x"]+prot["y"]+prot["z"]+c["mass"]+c["charge"]+"\n")
                        number=number+1
            elif prot["atomna"] == " HT1" or prot["atomna"] == " HT2":
                for n in nfile:
                    if prot["resna"]==n["resna"] and prot["atomna"]==n["atomna"]:
                        protfileb.write(prot["card"]+prot["nbar"]+" "+prot["atomna"]+prot["alt"]+
                                        prot["resna"]+" "+prot["chid"]+prot["resnr"]+prot["code"]+"     "+
                                        prot["x"]+prot["y"]+prot["z"]+n["mass"]+n["charge"]+"\n")
                        number=number+1
            for lj in ljfile:
                if prot["resna"]==lj["resna"] and prot["atomna"]==lj["atomna"]:
                    ljfileb.write(prot["card"]+prot["nbar"]+" "+prot["atomna"]+prot["alt"]+
                                    prot["resna"]+" "+prot["chid"]+prot["resnr"]+prot["code"]+" "+
                                    lj["sig"]+lj["eps"]+"\n")
        number_string = str(number)
        number_b=number
        while(len(number_string)<6):
            number_string = "0"+number_string
        atomfileb.write(number_string)
        atomfileb.close()
        ljfileb.close()
        protfileb.close()
        return number_a*number_b
        
    def prepareProteins(self, locationA, locationB):
        self.output("Generating temporary protein files...")
        start_time = time.time()
        
        shutil.copyfile(locationA,"."+os.sep+"prota.pdb")
        shutil.copyfile(locationB,"."+os.sep+"protb.pdb")
        #TODO - error handling for fortran file
        total = self.inputUtil()
        self.ui.batch_progress_bar.setValue(self.ui.batch_progress_bar.value()+self.progressBarInterval)
        self.repaint()
        end_time = time.time()
        elapsed = end_time - start_time
        self.output("Done. "+ str(elapsed)+ "s elapsed")
        if total > 90000:
            QMessageBox.information(self,"Large Mapping Detected","Large protein mapping detected. The mapping may take several minutes, during which time the program may appear to hang.",1)
 
    def saveResults(self, name):
        self.output("Writing to file...")
        start_time = time.time()
        
        shutil.copyfile("."+os.sep+"fort.8",self.ui.batch_output_folder.text()+os.sep+name+".pcr")
        shutil.copyfile("."+os.sep+"fort.18",self.ui.batch_output_folder.text()+os.sep+name+".pcr.s")
        shutil.copyfile("."+os.sep+"fort.19",self.ui.batch_output_folder.text()+os.sep+name+".pdb")
        end_time = time.time()
        self.ui.batch_progress_bar.setValue(self.ui.batch_progress_bar.value()+self.progressBarInterval)
        self.repaint()
        elapsed = end_time - start_time
        self.output("Done. "+ str(elapsed)+ "s elapsed")
        
    def generateContactMapping(self):
        self.output("Calculating protein mapping...")
        start_time = time.time()
        #TODO - error handling for fortran file
        contact()
        end_time = time.time()
        self.ui.batch_progress_bar.setValue(self.ui.batch_progress_bar.value()+self.progressBarInterval)
        self.repaint()
        elapsed = end_time - start_time
        self.output("Done. "+ str(elapsed)+ "s elapsed")
        
    def generateArrays(self, filename, count_a, count_b):
        self.output("Filling internal arrays...",self.WAIT)
        start_time = time.time()
        if os.path.isfile(filename):
            self.atomLabelA = count_a*[None]
            self.atomLabelB = count_b*[None]
            self.sepDistance = np.zeros(count_a*count_b)
            self.lennardJones = np.zeros(count_a*count_b)
            self.coulombicPotential = np.zeros(count_a*count_b)
            counter=0
            with open(filename,"r") as fort8:
                for line in fort8:
#                    temp = line.split(',')[0]
#                    self.atomNumberA.append(int(temp))
#                    temp = line.split(',')[1] + "-" + line.split(',')[2]
#                    mostRecentItem=""
#                    if len(self.atomLabelA) > 0:
#                        mostRecentItem = self.atomLabelA.pop()
#                        self.atomLabelA.append(mostRecentItem)
#                    if temp != mostRecentItem:
#                        self.atomLabelA.append(temp)

#                    temp = line.split(',')[1]
#                    self.atomNumberA.append(int(temp))
                    temp = line.split(',')[2].strip(' ') + ", " + line.split(',')[0].strip(' ') + "-" + line.split(',')[1].strip(' ')
                    mostRecentItem=""
                    if len(self.atomLabelA) > 0:
                        mostRecentItem = self.atomLabelA.pop()
                        self.atomLabelA.append(mostRecentItem)
                    if temp != mostRecentItem:
                        self.atomLabelA.append(temp)


#                    temp = line.split(',')[3]
#                    self.atomNumberB.append(int(temp))
#                    temp = line.split(',')[3]+","+line.split(',')[4]+"-" +line.split(',')[5]
#                    mostRecentItem=""
#                    if len(self.atomLabelB)>0:
#                        mostRecentItem = self.atomLabelB.pop()
#                        self.atomLabelB.append(mostRecentItem)
#                    if self.atomLabelB.count(temp) == 0:
#                        self.atomLabelB.append(temp)

#                    temp = line.split(',')[5]
#                    self.atomNumberB.append(int(temp))
                    temp = line.split(',')[6].strip(' ')+", "+line.split(',')[4].strip(' ')+"-" +line.split(',')[5].strip(' ')
                    mostRecentItem=""
                    if len(self.atomLabelB)>0:
                        mostRecentItem = self.atomLabelB.pop()
                        self.atomLabelB.append(mostRecentItem)
                    if self.atomLabelB.count(temp) == 0:
                        self.atomLabelB.append(temp)


#                    temp = line.split(',')[6]
#                    self.sepDistance.append(float(temp))
#                    temp = line.split(',')[7]
#                    self.lennardJones.append(float(temp))
#                    temp = line.split(',')[8]
#                    self.coulombicPotential.append(float(temp))

                    temp = line.split(',')[8]
                    self.sepDistance[counter] = float(temp)
                    temp = line.split(',')[9]
                    self.lennardJones[counter] = float(temp)
                    temp = line.split(',')[10]
                    self.coulombicPotential[counter] = float(temp)
                    counter++
            self.atomNumberA = range(0,len(self.atomLabelA))
            self.atomNumberB = range(0,len(self.atomLabelB))
        end_time = time.time()
        elapsed = end_time - start_time
        self.output(str(len(self.atomLabelA))+" "+str(len(self.atomLabelB)))
        self.output("Done. " +str(elapsed)+ "s elapsed",self.RELEASE)
        
    def checkEnabled(self):
        if self.ui.batch_protein_A.text() == "" and self.ui.batch_protein_B.text() =="":
            self.ui.batch_add_button.setEnabled(False)
        else:
            self.ui.batch_add_button.setEnabled(True)
        if self.ui.batch_list.count() != 0:
            self.ui.batch_remove_button.setEnabled(True)                
            if self.ui.batch_output_folder.text() != "" and self.ui.batch_saving_convention.text() != "":
                self.ui.batch_map_button.setEnabled(True)
        else:
            self.ui.batch_remove_button.setEnabled(False);
            self.ui.batch_map_button.setEnabled(False)
           
    def test(self):
        prota = Structure("./prota.pdb")
        protb = Structure("./prota.pdb")
        #residc = Structure("./residc03.pdb")
        ntresc = Structure("./ntresc03.pdb")
        ctresc = Structure("./ctresc03.pdb")
        ljresid = Structure("./ljresid")
        self.output(prota.objects)
        for residue in ntresc.residues:
            self.output(residue)
            for atom in residue:
                self.output(atom)
        
    def output(self,output,cursor=0):
        if cursor==self.WAIT:
            QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
        elif cursor==self.RELEASE:
            QApplication.restoreOverrideCursor()
        newText = time.strftime("[%a, %d %b %Y %H:%M:%S] - ")+ str(output)
        if self.ui.console.text() == "":
            self.ui.console.setText(newText)
        else:
            self.ui.console.setText(self.ui.console.text()+"\n"+newText)
#        if self.ui.console.verticalScollBar() != None:
#            self.ui.console.verticalScollBar().setValue(self.ui.console.verticalScollBar().maximum())
#        self.ui.console.setText
 #       self.ui.console.scrollToAnchor(newText)
#        self.ui.console.ensureCursorVisible()
        self.repaint()
        
#END CONTACT MAPPER CLASS
        
def init():
    cleanup()
    app = QtGui.QApplication(sys.argv)
    window = ContactMapper()
    window.show()
    app.exec_()
    cleanup()

def cleanup():
    if os.path.isfile("."+os.sep+"prota.pdb"):
        os.remove("."+os.sep+"prota.pdb")
    if os.path.isfile("."+os.sep+"protb.pdb"):
        os.remove("."+os.sep+"protb.pdb")
    if os.path.isfile("."+os.sep+"proteina"):
        os.remove("."+os.sep+"proteina")
    if os.path.isfile("."+os.sep+"proteinb"):
        os.remove("."+os.sep+"proteinb")
    if os.path.isfile("."+os.sep+"lja"):
        os.remove("."+os.sep+"lja")
    if os.path.isfile("."+os.sep+"ljb"):
        os.remove("."+os.sep+"ljb")
    if os.path.isfile("."+os.sep+"atnma"):
        os.remove("."+os.sep+"atnma")
    if os.path.isfile("."+os.sep+"atnmb"):
        os.remove("."+os.sep+"atnmb")
    if os.path.isfile("."+os.sep+"fort.8"):
        os.remove("."+os.sep+"fort.8")
    if os.path.isfile("."+os.sep+"fort.18"):
        os.remove("."+os.sep+"fort.18")
    if os.path.isfile("."+os.sep+"fort.19"):
        os.remove("."+os.sep+"fort.19")
        



init()
