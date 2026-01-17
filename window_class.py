from sys import path
from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon
import os
import sqlite3
from ui_window import Ui_MainWindow
def get_db_path():
    db_path = os.path.join(
        os.getenv("LOCALAPPDATA"),
        "ExpenseTracker",
        "expense.db"
    )
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    return db_path

class Window(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Expense Tracker")
        self.setupUi(self)
        
        self.pushButton.clicked.connect(self.switch_to_home)
        self.pushButton_7.clicked.connect(self.switch_to_home)
        self.pushButton_2.clicked.connect(self.switch_to_profile)
        self.pushButton_8.clicked.connect(self.switch_to_profile)
        self.pushButton_3.clicked.connect(self.switch_to_add)
        self.pushButton_9.clicked.connect(self.switch_to_add)
        self.pushButton_5.clicked.connect(self.switch_to_remove)
        self.pushButton_10.clicked.connect(self.switch_to_remove)
        self.pushButton_4.clicked.connect(self.switch_to_edit)
        self.pushButton_11.clicked.connect(self.switch_to_edit)
        
        self.btn_home_showall.clicked.connect(self.home_show_all)
        self.btn_showall_remove.clicked.connect(self.home_show_all_2)
        self.pushButton_15.clicked.connect(self.home_show_all_1)
        
        self.btn_add_expense.clicked.connect(self.add_expense)

        self.btn_remove_remove.clicked.connect(self.remove_data)

        self.btn_extract_edit.clicked.connect(self.extract_data)
        self.btn_update_edit.clicked.connect(self.update_data)

        self.insert_data()#Must call function insert_data to insert data  

    #Fuctions for page switching(moving to different pages)     
    def switch_to_home(self):
        self.addpage.setCurrentIndex(0)
    def switch_to_profile(self):
        self.addpage.setCurrentIndex(1)
    def switch_to_add(self):
        self.addpage.setCurrentIndex(2)
    def switch_to_remove(self):
        self.addpage.setCurrentIndex(4)
    def switch_to_edit(self):
        self.addpage.setCurrentIndex(3)
        
    def create_connection(self):
        self.connection=sqlite3.connect(get_db_path())
        return self.connection
    #use this function to avoid duplication of insert demo data
    def insert_data(self):
        self.crsr=self.create_connection().cursor()
        # Create table if not exists
        self.crsr.execute("""CREATE TABLE IF NOT EXISTS expenses (
            Expense TEXT,
            Category TEXT,
            Date TEXT,
            Amount INTEGER,
            Total INTEGER,
            Remaining INTEGER,
            Review TEXT
        )
    """)

        # 🔍 CHECK IF DATA ALREADY EXISTS
        self.crsr.execute("SELECT COUNT(*) FROM expenses")
        count = self.crsr.fetchone()[0]

        if count == 0:
            demo_data = [
            ('Peanut', 'food', '12/12/25', 100, 30000, 29900, 'Good'),
            ('Rice', 'food', '13/12/25', 200, 30000, 29800, 'Nice'),
            ('Milk', 'food', '14/12/25', 150, 30000, 29650, 'Fresh'),
        ]

            self.crsr.executemany(
            "INSERT INTO expenses VALUES (?,?,?,?,?,?,?)",
            demo_data
            )
            self.connection.commit()
            #print("Demo data inserted (FIRST RUN ONLY)")
        #else:
            #print("Demo data already exists — skipping insert")
        self.connection.close()

    def home_show_all(self):
        self.crsr=self.create_connection().cursor()
        rowcount_sqlquery="SELECT COUNT(*) FROM expenses"#Chose only selected rows
        employees_sqlquery="SELECT * FROM expenses"
        #Find the number of rows in the table
        self.crsr.execute(rowcount_sqlquery)
        result=self.crsr.fetchone()
        #print("Number of rows",result[0])
        self.tableWidget_home.setRowCount(result[0])
        self.tableWidget_home.setColumnCount(7)
        self.tableWidget_home.setHorizontalHeaderLabels(["Expense", "Category", "Date", "Amount","Total","Remaining","Review"])
        #Adding employes from table to QTable 
        table_row=0
        for i in self.crsr.execute(employees_sqlquery):
            self.tableWidget_home.setItem(table_row,0,QTableWidgetItem(str(i[0])))
            self.tableWidget_home.setItem(table_row,1,QTableWidgetItem(str(i[1])))
            self.tableWidget_home.setItem(table_row,2,QTableWidgetItem(str(i[2])))
            self.tableWidget_home.setItem(table_row,3,QTableWidgetItem(str(i[3])))
            self.tableWidget_home.setItem(table_row,4,QTableWidgetItem(str(i[4])))
            self.tableWidget_home.setItem(table_row,5,QTableWidgetItem(str(i[5])))
            self.tableWidget_home.setItem(table_row,6,QTableWidgetItem(str(i[6])))
            table_row+=1
        self.connection.commit()
        self.connection.close()
        
    def home_show_all_1(self):
        self.crsr=self.create_connection().cursor()
        rowcount_sqlquery="SELECT COUNT(*) FROM expenses"#Chose only selected rows
        employees_sqlquery="SELECT * FROM expenses"
        #Find the number of rows in the table
        self.crsr.execute(rowcount_sqlquery)
        result=self.crsr.fetchone()
        #print("Number of rows",result[0])
        self.tableWidget.setRowCount(result[0])
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(["Expense", "Category", "Date", "Amount","Total","Remaining","Review"])
        #Adding employes from table to QTable 
        table_row=0
        for i in self.crsr.execute(employees_sqlquery):
            self.tableWidget.setItem(table_row,0,QTableWidgetItem(str(i[0])))
            self.tableWidget.setItem(table_row,1,QTableWidgetItem(str(i[1])))
            self.tableWidget.setItem(table_row,2,QTableWidgetItem(str(i[2])))
            self.tableWidget.setItem(table_row,3,QTableWidgetItem(str(i[3])))
            self.tableWidget.setItem(table_row,4,QTableWidgetItem(str(i[4])))
            self.tableWidget.setItem(table_row,5,QTableWidgetItem(str(i[5])))
            self.tableWidget.setItem(table_row,6,QTableWidgetItem(str(i[6])))
            table_row+=1
        self.connection.commit()
        self.connection.close()

    def home_show_all_2(self):
        self.crsr=self.create_connection().cursor()
        rowcount_sqlquery="SELECT COUNT(*) FROM expenses"#Chose only selected rows
        employees_sqlquery="SELECT * FROM expenses"
        #Find the number of rows in the table
        self.crsr.execute(rowcount_sqlquery)
        result=self.crsr.fetchone()
        #print("Number of rows",result[0])
        self.tableWidget_2.setRowCount(result[0])
        self.tableWidget_2.setColumnCount(7)
        self.tableWidget_2.setHorizontalHeaderLabels(["Expense", "Category", "Date", "Amount","Total","Remaining","Review"])
        #Adding employes from table to QTable 
        table_row=0
        for i in self.crsr.execute(employees_sqlquery):
            self.tableWidget_2.setItem(table_row,0,QTableWidgetItem(str(i[0])))
            self.tableWidget_2.setItem(table_row,1,QTableWidgetItem(str(i[1])))
            self.tableWidget_2.setItem(table_row,2,QTableWidgetItem(str(i[2])))
            self.tableWidget_2.setItem(table_row,3,QTableWidgetItem(str(i[3])))
            self.tableWidget_2.setItem(table_row,4,QTableWidgetItem(str(i[4])))
            self.tableWidget_2.setItem(table_row,5,QTableWidgetItem(str(i[5])))
            self.tableWidget_2.setItem(table_row,6,QTableWidgetItem(str(i[6])))
            table_row+=1
        self.connection.commit()
        self.connection.close()
    def add_expense(self):
        self.crsr=self.create_connection().cursor()
        #First Initialize expense information from QLine edits as a list
        self.new_expense=[self.lineEdit.text(),
                           self.lineEdit_2.text(),
                           self.lineEdit_3.text(),
                           self.lineEdit_4.text(),
                           self.lineEdit_5.text(),
                           self.lineEdit_7.text(),
                           self.lineEdit_6.text()]
        #To add new expenses to SQlite table
        self.crsr.execute("Insert into expenses values(?,?,?,?,?,?,?)",self.new_expense)
        #Showing the addition on terminal
        #print("New Expense added:",self.lineEdit.text())
        #Clearing the line edit after  adding the information
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.lineEdit_7.clear()
        self.connection.commit()
        self.connection.close() 

    def remove_data(self):
        self.crsr=self.create_connection().cursor()
        current_row=self.tableWidget_2.currentRow()
        #Call name in row and assign to avriable
        name_item=str(self.tableWidget_2.item(current_row,0).text())
        if current_row<0:
            warning=QMessageBox.warning(self,'warning',"Please select a record to delete.")
        else:
            question=QMessageBox.question(self,'Conformation','Are you sure you want to delete the selected row?',QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if question==QMessageBox.StandardButton.Yes:
            sqlquery="DELETE FROM expenses WHERE Expense=?"
            self.crsr.execute(sqlquery,(name_item,))
            #print("You deleted ",name_item)
        self.connection.commit()
        self.connection.close() 
    def extract_data(self):
        current_row=self.tableWidget.currentRow()
        #Calling variables details and assigning them to variables
        self.expense_edit=str(self.tableWidget.item(current_row,0).text())
        self.category_edit=str(self.tableWidget.item(current_row,1).text())
        self.date_edit=str(self.tableWidget.item(current_row,2).text())
        self.amount_edit=str(self.tableWidget.item(current_row,3).text())
        self.total_edit=str(self.tableWidget.item(current_row,4).text())
        self.remaining_edit=str(self.tableWidget.item(current_row,5).text())
        self.review_edit=str(self.tableWidget.item(current_row,3).text())

        #Change the QLine edits to above variables
        self.lineEdit_8.setText(self.expense_edit)
        self.lineEdit_9.setText(self.category_edit)
        self.lineEdit_10.setText(self.date_edit)
        self.lineEdit_11.setText(self.amount_edit)
        self.lineEdit_12.setText(self.total_edit)
        self.lineEdit_13.setText(self.remaining_edit)
        self.lineEdit_14.setText(self.review_edit)
    def update_data(self):
        self.crsr=self.create_connection().cursor()
        #Getting current text from Qline edits
        current=(
            self.lineEdit_8.text(),
            self.lineEdit_9.text(),
            self.lineEdit_10.text(),
            self.lineEdit_11.text(),
            self.lineEdit_12.text(),
            self.lineEdit_13.text(),
            self.lineEdit_14.text(),
            self.expense_edit
        )
        self.crsr.execute("UPDATE expenses SET Expense=?,Category=?,Date=?,Amount=?,Total=?,Remaining=?,Review=? WHERE Expense=?",current)
        #print("Old expense was:",self.expense_edit)
        #print("New expense is:",self.lineEdit_8.text())

        #Clearing the line edit after  adding the information
        self.lineEdit_8.clear()
        self.lineEdit_9.clear()
        self.lineEdit_10.clear()
        self.lineEdit_11.clear()
        self.lineEdit_12.clear()
        self.lineEdit_13.clear()
        self.lineEdit_14.clear()

        self.connection.commit()
        self.connection.close()