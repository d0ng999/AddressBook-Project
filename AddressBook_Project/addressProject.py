import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import pymysql

class qtApp(QMainWindow):
    conn = None
    curIdx = 0


    def __init__(self):
        super().__init__()
        uic.loadUi('./AddressBook_Project/addressBook.ui', self)
        self.setWindowIcon(QIcon('./AddressBook_Project/address-book.png'))
        self.setWindowTitle('AddressBook v0.5')

        self.initDB()

        self.btnNew.clicked.connect(self.btnNewClicked)
        self.btnSave.clicked.connect(self.btnSaveClicked)
        self.tblAddress.doubleClicked.connect(self.tblAddressDoubleClicked)
        self.btnDel.clicked.connect(self.btnDelClicked)

    def btnDelClicked(self):
        if self.curIdx == 0:
            QMessageBox.warning(self, 'Warning', 'Please select the data to delete.')
            return # 함수를 빠져나감
        else:
            reply = QMessageBox.question(self, 'Ok', 'Are you sure you wanna delete?', QMessageBox.Yes | QMessageBox.No, 
                                         QMessageBox.Yes)
            if reply == QMessageBox.No:
                return

            self.conn = pymysql.connect(host='localhost', user='root', password='12345',
                                        db='miniproject', charset='utf8')
            query = 'DELETE FROM addressbook WHERE Idx = %s'
            cur = self.conn.cursor()
            cur.execute(query, (self.curIdx))

            self.conn.commit()
            self.conn.close()

            QMessageBox.about(self, 'Success', 'You have successfully deleted your data.')

            self.initDB()
            self.btnNewClicked()

    def btnNewClicked(self):
        self.txtName.setText('')
        self.txtPhone.setText('')
        self.txtEmail.setText('')
        self.txtAddress.setText('')
        self.txtName.setFocus()
        self.curIdx = 0
        print(self.curIdx)

    def tblAddressDoubleClicked(self): #
        rowIndex = self.tblAddress.currentRow()
        self.txtName.setText(self.tblAddress.item(rowIndex, 1).text())
        self.txtPhone.setText(self.tblAddress.item(rowIndex, 2).text())
        self.txtEmail.setText(self.tblAddress.item(rowIndex, 3).text())
        self.txtAddress.setText(self.tblAddress.item(rowIndex, 4).text())
        self.curIdx = int(self.tblAddress.item(rowIndex, 0).text()) 
        print(self.curIdx)

    def btnSaveClicked(self):
        fullName = self.txtName.text()
        phoneNum = self.txtPhone.text()
        email = self.txtEmail.text()
        address = self.txtAddress.text()

        if fullName == '' or phoneNum == '':
            QMessageBox.warning(self, 'Caution', 'Enter your name and Mobile number')
            return
        else:
            self.conn = pymysql.connect(host='localhost', user='root', password='12345',
                                        db='miniproject', charset='utf8')
            if self.curIdx == 0:
                query = '''INSERT INTO addressbook (FullName, PhoneNum, Email, Address)
                                VALUES (%s, %s, %s, %s)'''
            else:
                query = '''UPDATE addressbook
                              SET FullName = %s
                                , PhoneNum = %s
                                , Email = %s
                                , Address = %s
                            WHERE Idx = %s'''

            cur = self.conn.cursor()
            if self.curIdx == 0:
                cur.execute(query, (fullName, phoneNum, email, address))
            else:
                cur.execute(query, (fullName, phoneNum, email, address, self.curIdx))

            self.conn.commit() 
            self.conn.close()
            
            if self.curIdx == 0:   # 저장성공 메시지
                QMessageBox.about(self, 'Success', 'You have successfully saved your data!')
            else:
                QMessageBox.about(self, 'Success', 'You have successfully changed your data!')

            self.initDB()
            self.btnNewClicked()

    def initDB(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='12345',
                                    db='miniproject', charset='utf8')
        cur = self.conn.cursor()
        query = '''SELECT Idx
                        , FullName
                        , PhoneNum
                        , Email
                        , Address
                     FROM addressbook'''
        cur.execute(query)
        rows = cur.fetchall()

        # print(rows)
        self.makeTable(rows)
        self.conn.close()
    
    def makeTable(self, rows):
        self.tblAddress.setColumnCount(5)
        self.tblAddress.setRowCount(len(rows))
        self.tblAddress.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tblAddress.setHorizontalHeaderLabels(['Number','Name','Mobile Number','Email','Address'])
        self.tblAddress.setColumnWidth(0, 0)
        self.tblAddress.setColumnWidth(1, 70)
        self.tblAddress.setColumnWidth(2, 105)
        self.tblAddress.setColumnWidth(3, 175)
        self.tblAddress.setColumnWidth(4, 200)
        self.tblAddress.setEditTriggers(QAbstractItemView.NoEditTriggers)

        for i, row in enumerate(rows):
            # row[0] ~ row[4]
            idx = row[0]
            fullName = row[1]
            phoneNum = row[2]
            email = row[3]
            address = row[4]

            self.tblAddress.setItem(i, 0, QTableWidgetItem(str(idx)))
            self.tblAddress.setItem(i, 1, QTableWidgetItem(fullName))
            self.tblAddress.setItem(i, 2, QTableWidgetItem(phoneNum))
            self.tblAddress.setItem(i, 3, QTableWidgetItem(email))
            self.tblAddress.setItem(i, 4, QTableWidgetItem(address))

        self.stbCurrent.showMessage(f'Total Address :{len(rows)}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())
