from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

# from ReSimplexAlg import setup_algorithm
from ReSimplexAlg_v1 import setup_algorithm


class Ui_MainWindow_resimplex(object):

    def setupUi(self, MainWindow_resimplex):

        MainWindow_resimplex.setObjectName("MainWindow_resimplex")
        MainWindow_resimplex.setWindowModality(QtCore.Qt.NonModal)
        MainWindow_resimplex.setEnabled(True)
        MainWindow_resimplex.resize(800, 555)
        MainWindow_resimplex.setAccessibleName("")
        MainWindow_resimplex.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow_resimplex.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("re_simplex_icon.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow_resimplex.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow_resimplex)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_mainmenu = QtWidgets.QFrame(self.centralwidget)
        self.frame_mainmenu.setEnabled(True)
        self.frame_mainmenu.setGeometry(QtCore.QRect(10, 0, 790, 550))
        self.frame_mainmenu.setAutoFillBackground(True)
        self.frame_mainmenu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_mainmenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_mainmenu.setObjectName("frame_mainmenu")
        self.label_title = QtWidgets.QLabel(self.frame_mainmenu)
        self.label_title.setGeometry(QtCore.QRect(10, 10, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setLineWidth(1)
        self.label_title.setObjectName("label_title")
        
        self.lineEdit_var = QtWidgets.QLineEdit(self.frame_mainmenu)
        self.lineEdit_var.setGeometry(QtCore.QRect(400, 170, 113, 22))
        self.lineEdit_var.setObjectName("lineEdit_var")
        self.lineEdit_cons = QtWidgets.QLineEdit(self.frame_mainmenu)
        self.lineEdit_cons.setGeometry(QtCore.QRect(400, 200, 113, 22))
        self.lineEdit_cons.setObjectName("lineEdit_cons")
        self.comboBox_prob_type = QtWidgets.QComboBox(self.frame_mainmenu)
        self.comboBox_prob_type.setGeometry(QtCore.QRect(400, 230, 113, 22))
        self.comboBox_prob_type.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.comboBox_prob_type.setEditable(False)
        self.comboBox_prob_type.setFrame(True)
        self.comboBox_prob_type.setObjectName("comboBox_prob_type")
        self.comboBox_prob_type.addItem("")
        self.comboBox_prob_type.addItem("")
        self.btn_next_1 = QtWidgets.QPushButton(self.frame_mainmenu)
        self.btn_next_1.setGeometry(QtCore.QRect(680, 510, 93, 28))
        self.btn_next_1.setObjectName("btn_next_1")
        self.label_var = QtWidgets.QLabel(self.frame_mainmenu)
        self.label_var.setGeometry(QtCore.QRect(250, 170, 141, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_var.setFont(font)
        self.label_var.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_var.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_var.setObjectName("label_var")
        
        self.label_cons = QtWidgets.QLabel(self.frame_mainmenu)
        self.label_cons.setGeometry(QtCore.QRect(220, 200, 171, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_cons.setFont(font)
        self.label_cons.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_cons.setObjectName("label_cons")
        self.label_prob_type = QtWidgets.QLabel(self.frame_mainmenu)
        self.label_prob_type.setGeometry(QtCore.QRect(250, 230, 141, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_prob_type.setFont(font)
        self.label_prob_type.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_prob_type.setObjectName("label_prob_type")
        self.label_legacy = QtWidgets.QLabel(self.centralwidget)
        self.label_legacy.setGeometry(QtCore.QRect(10, 523, 301, 16))
        self.label_legacy.setObjectName("label_legacy")
        self.frame_data_input = QtWidgets.QFrame(self.centralwidget)
        self.frame_data_input.setEnabled(True)
        self.frame_data_input.setGeometry(QtCore.QRect(10, 0, 790, 550))
        self.frame_data_input.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.frame_data_input.setStatusTip("")
        self.frame_data_input.setAutoFillBackground(True)
        self.frame_data_input.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_data_input.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_data_input.setObjectName("frame_data_input")
        self.btn_next_2 = QtWidgets.QPushButton(self.frame_data_input)
        self.btn_next_2.setGeometry(QtCore.QRect(680, 510, 93, 28))
        self.btn_next_2.setObjectName("btn_next_2")
        self.btn_back_2 = QtWidgets.QPushButton(self.frame_data_input)
        self.btn_back_2.setGeometry(QtCore.QRect(580, 510, 93, 28))
        self.btn_back_2.setObjectName("btn_back_2")
        self.label_title_2 = QtWidgets.QLabel(self.frame_data_input)
        self.label_title_2.setGeometry(QtCore.QRect(10, 0, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_title_2.setFont(font)
        self.label_title_2.setLineWidth(1)
        self.label_title_2.setObjectName("label_title_2")
        #self.label_prob_type_2 = QtWidgets.QLabel(self.frame_data_input)
        #self.label_prob_type_2.setGeometry(QtCore.QRect(400, 40, 141, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        #self.label_prob_type_2.setFont(font)
        #self.label_prob_type_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        #self.label_prob_type_2.setObjectName("label_prob_type_2")
        self.line_3 = QtWidgets.QFrame(self.frame_data_input)
        self.line_3.setGeometry(QtCore.QRect(20, 50, 381, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.tableWidget_model = QtWidgets.QTableWidget(self.frame_data_input)
        self.tableWidget_model.setGeometry(QtCore.QRect(20, 70, 700, 420))
        self.tableWidget_model.setObjectName("tableWidget_model")
        self.label_title_2.raise_()
        self.btn_next_2.raise_()
        self.btn_back_2.raise_()
        #self.label_prob_type_2.raise_()
        self.line_3.raise_()
        self.tableWidget_model.raise_()
        self.frame_result = QtWidgets.QFrame(self.centralwidget)
        self.frame_result.setEnabled(True)
        self.frame_result.setGeometry(QtCore.QRect(10, 0, 790, 550))
        self.frame_result.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.frame_result.setStatusTip("")
        self.frame_result.setAutoFillBackground(True)
        self.frame_result.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_result.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_result.setObjectName("frame_result")
        self.btn_try_3 = QtWidgets.QPushButton(self.frame_result)
        self.btn_try_3.setGeometry(QtCore.QRect(680, 510, 93, 28))
        self.btn_try_3.setObjectName("btn_try_3")
        self.btn_back_3 = QtWidgets.QPushButton(self.frame_result)
        self.btn_back_3.setGeometry(QtCore.QRect(580, 510, 93, 28))
        self.btn_back_3.setObjectName("btn_back_3")
        self.label_title_3 = QtWidgets.QLabel(self.frame_result)
        self.label_title_3.setGeometry(QtCore.QRect(10, 0, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_title_3.setFont(font)
        self.label_title_3.setLineWidth(1)
        self.label_title_3.setObjectName("label_title_3")
        #self.label_prob_type_3 = QtWidgets.QLabel(self.frame_result)
        #self.label_prob_type_3.setGeometry(QtCore.QRect(400, 40, 141, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        #self.label_prob_type_3.setFont(font)
        #self.label_prob_type_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        #self.label_prob_type_3.setObjectName("label_prob_type_3")
        self.line_4 = QtWidgets.QFrame(self.frame_result)
        self.line_4.setGeometry(QtCore.QRect(20, 50, 600, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.tableWidget_result_vars = QtWidgets.QTableWidget(self.frame_result)
        self.tableWidget_result_vars.setGeometry(QtCore.QRect(20, 90, 600, 300))
        self.tableWidget_result_vars.setObjectName("tableWidget_result_vars")
        self.tableWidget_result_vars.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_result_vars.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_result_vars.setHorizontalHeaderItem(1, item)
        self.label_subtitle_3_1 = QtWidgets.QLabel(self.frame_result)
        self.label_subtitle_3_1.setGeometry(QtCore.QRect(20, 65, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_subtitle_3_1.setFont(font)
        self.label_subtitle_3_1.setLineWidth(1)
        self.label_subtitle_3_1.setObjectName("label_subtitle_3_1")
        self.label_subtitle_3_2 = QtWidgets.QLabel(self.frame_result)
        self.label_subtitle_3_2.setGeometry(QtCore.QRect(20, 400, 600, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_subtitle_3_2.setFont(font)
        self.label_subtitle_3_2.setLineWidth(1)
        self.label_subtitle_3_2.setObjectName("label_subtitle_3_2")
        self.lineEdit_result_obj = QtWidgets.QLineEdit(self.frame_result)
        self.lineEdit_result_obj.setGeometry(QtCore.QRect(20, 430, 381, 22))
        self.lineEdit_result_obj.setObjectName("lineEdit_result_obj")
        self.frame_result.raise_()
        self.frame_data_input.raise_()
        self.frame_mainmenu.raise_()
        self.label_legacy.raise_()
        MainWindow_resimplex.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_resimplex)
        self.btn_next_1.clicked.connect(self.frame_mainmenu.hide)
        self.btn_next_1.clicked.connect(self.frame_data_input.show)
        
        self.btn_next_1.clicked.connect(self.data_input_setup)
        
        self.btn_back_2.clicked.connect(self.frame_mainmenu.show)
        
        
        self.btn_back_2.clicked.connect(self.frame_data_input.hide)
        self.btn_next_2.clicked.connect(self.run_re_simp)
        self.btn_back_3.clicked.connect(self.frame_data_input.show)
        self.btn_back_3.clicked.connect(self.frame_result.hide)
        self.btn_try_3.clicked.connect(self.frame_result.hide)
        self.btn_try_3.clicked.connect(self.frame_mainmenu.show)
        self.btn_try_3.clicked.connect(self.tableWidget_model.clear)
        self.btn_try_3.clicked.connect(self.tableWidget_model.clearContents)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_resimplex)
    
    def filter_data(self):
        global data_ml_
        self.data_ml_filtered = data_ml_.df[[i.text() for i in self.listWidget.selectedItems()]]
        self.tableView.setRowCount(30)
        self.tableView.setColumnCount(len(self.data_ml_filtered.columns))
        for j,item_ in enumerate(self.data_ml_filtered.columns):
            self.tableView.setHorizontalHeaderItem(j,QTableWidgetItem(item_))
        for i in range(30):
            for j in range(len(self.data_ml_filtered.columns)):
                self.tableView.setItem(i,j,QTableWidgetItem(str(self.data_ml_filtered.iloc[i,j])))
    
    def data_input_setup(self):#(self,column,row):
        var = int(self.lineEdit_var.text())
        cons = int(self.lineEdit_cons.text())
        self.tableWidget_model.setColumnCount(var+2)
        self.tableWidget_model.setRowCount(cons+1)
        #_translate = QtCore.QCoreApplication.translate
        
        for i in range(var):
            self.tableWidget_model.setHorizontalHeaderItem(i,QTableWidgetItem('X{}'.format(i+1)))
            
        self.tableWidget_model.setHorizontalHeaderItem(var,QTableWidgetItem('Equality'))
        self.tableWidget_model.setHorizontalHeaderItem(var+1,QTableWidgetItem('RHS'))
        for j in range(cons+1):
            self.tableWidget_model.setVerticalHeaderItem(j,QTableWidgetItem('Row{}'.format(j)))
        
        
        item_locked = QTableWidgetItem("")
        item_locked.setFlags(QtCore.Qt.ItemIsEnabled)
        item_locked.setBackground(QtGui.QColor(164, 164, 164))
        item_locked1 = QTableWidgetItem("")
        item_locked1.setFlags(QtCore.Qt.ItemIsEnabled)
        item_locked1.setBackground(QtGui.QColor(164, 164, 164))
        self.tableWidget_model.setItem(0, var, item_locked)
        self.tableWidget_model.setItem(0, var+1, item_locked1)
        
        header = self.tableWidget_model.horizontalHeader()       
        for i in range(var+2):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)
        
        for con_ in range(1,cons+1):
            item = QtWidgets.QComboBox()
            item.addItems(['==',
                           '>=',
                           '<='])
            self.tableWidget_model.setCellWidget(con_,var,item)
            
        
            
            
    def run_re_simp(self):
        
        
        self.frame_data_input.hide()

        import numpy as np
        
        try:
            A = [[ np.float32(self.tableWidget_model.item(j, i).text().replace(',','.')) 
                      if ',' in self.tableWidget_model.item(j, i).text() else np.float32(self.tableWidget_model.item(j, i).text()) 
                          for i in range(self.tableWidget_model.columnCount()-2) ] 
                             for j in range(1,self.tableWidget_model.rowCount()) ]
            A = np.array(A)
            print(A)
        except:
            print('yanlis yazim var!!!')
        
        
        var = self.tableWidget_model.columnCount()-2
        b = [[ np.float32(self.tableWidget_model.item(j, var+1).text().replace(',','.')) 
                      if ',' in self.tableWidget_model.item(j, var+1).text() else np.float32(self.tableWidget_model.item(j, var+1).text()) ] 
                             for j in range(1,self.tableWidget_model.rowCount()) ]
        b = np.array(b)
        print(b)
        c = [ np.float32(self.tableWidget_model.item(0, i).text().replace(',','.')) 
                      if ',' in self.tableWidget_model.item(0, i).text() else np.float32(self.tableWidget_model.item(0, i).text()) 
                          for i in range(self.tableWidget_model.columnCount()-2)]
        c = np.array(c)
        print(c)
        
        convertion = {'==':0,'<=':1,'>=':2}
        e =  [[ convertion[self.tableWidget_model.cellWidget(j, var).currentText()] ] 
                             for j in range(1,self.tableWidget_model.rowCount()) ]
        e = np.array(e)
        print(e)
        
        type_prob = 0 if self.comboBox_prob_type.currentText()=='Minimization'  else 1 
        
        basis_name, NB_name, x_b, z, feasibility, unb = setup_algorithm(type_prob, c, e, A, b)
        
        if feasibility and not unb:
            total_var = len(basis_name)+len(NB_name)
            
            self.tableWidget_result_vars.setRowCount(total_var)
            
            for i in range(total_var):
                if i < len(basis_name):
                    item = QTableWidgetItem(basis_name[i])
                    if 'x' in basis_name[i]:
                        item.setBackground(QtGui.QColor(198, 243, 193))
                    self.tableWidget_result_vars.setItem(i,0,item)
                    item = QTableWidgetItem(str(x_b[i,0]))
                    if 'x' in basis_name[i]:
                        item.setBackground(QtGui.QColor(198, 243, 193))
                    self.tableWidget_result_vars.setItem(i,1,item)
                else:
                    item = QTableWidgetItem(NB_name[i-len(basis_name)])
                    if 'x' in NB_name[i-len(basis_name)]:
                        item.setBackground(QtGui.QColor(255, 119, 119))
                    self.tableWidget_result_vars.setItem(i,0,item)
                    item = QTableWidgetItem(str(0.0))
                    if 'x' in NB_name[i-len(basis_name)]:
                        item.setBackground(QtGui.QColor(255, 119, 119))
                    self.tableWidget_result_vars.setItem(i,1,item)
                    
            self.lineEdit_result_obj.setText(str(z[0]))
        else:
            self.lineEdit_result_obj.setText('Infeasible' if not unb else 'Unbounded' )
        
        
        
        
        self.frame_result.show()
            
            
            
    def retranslateUi(self, MainWindow_resimplex):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_resimplex.setWindowTitle(_translate("MainWindow_resimplex", "ReSimplex Algorithm"))
        self.label_title.setText(_translate("MainWindow_resimplex", "Setup Stage"))
        self.btn_next_1.setText(_translate("MainWindow_resimplex", "Next >>"))
        self.comboBox_prob_type.setItemText(0, _translate("MainWindow_resimplex", "Maximization"))
        self.comboBox_prob_type.setItemText(1, _translate("MainWindow_resimplex", "Minimization"))
        self.label_var.setText(_translate("MainWindow_resimplex", "Number of Variables :"))
        self.label_cons.setText(_translate("MainWindow_resimplex", "Number of Constraints :"))
        self.label_prob_type.setText(_translate("MainWindow_resimplex", "Problem Type :"))
        self.label_legacy.setText(_translate("MainWindow_resimplex", "This program has been created by Mert Parcaoglu."))
        self.btn_next_2.setText(_translate("MainWindow_resimplex", "Next >>"))
        self.btn_back_2.setText(_translate("MainWindow_resimplex", "<< Back"))
        self.label_title_2.setText(_translate("MainWindow_resimplex", "Problem Definiton"))
        #self.label_prob_type_2.setText(_translate("MainWindow_resimplex", "Problem Type :"))
        #item = self.tableWidget_model.verticalHeaderItem(0)
        #item.setText(_translate("MainWindow_resimplex", "1"))
        #item = self.tableWidget_model.horizontalHeaderItem(0)
        #item.setText(_translate("MainWindow_resimplex", "x1"))
        #__sortingEnabled = self.tableWidget_model.isSortingEnabled()
        #self.tableWidget_model.setSortingEnabled(False)
        #item = self.tableWidget_model.item(0, 0)
        #item.setText(_translate("MainWindow_resimplex", "12"))
        #self.tableWidget_model.setSortingEnabled(__sortingEnabled)
        self.btn_try_3.setText(_translate("MainWindow_resimplex", "Try Again!"))
        self.btn_back_3.setText(_translate("MainWindow_resimplex", "<< Back"))
        self.label_title_3.setText(_translate("MainWindow_resimplex", "Results"))
        #8self.label_prob_type_3.setText(_translate("MainWindow_resimplex", "Problem Type :"))
        item = self.tableWidget_result_vars.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow_resimplex", "Variables"))
        item = self.tableWidget_result_vars.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow_resimplex", "Values"))
        __sortingEnabled = self.tableWidget_result_vars.isSortingEnabled()
        self.tableWidget_result_vars.setSortingEnabled(False)
        self.tableWidget_result_vars.setSortingEnabled(__sortingEnabled)
        self.label_subtitle_3_1.setText(_translate("MainWindow_resimplex", "Variables"))
        self.label_subtitle_3_2.setText(_translate("MainWindow_resimplex", "Objective Function Value"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_resimplex = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_resimplex()
    ui.setupUi(MainWindow_resimplex)
    MainWindow_resimplex.show()
    sys.exit(app.exec_())

