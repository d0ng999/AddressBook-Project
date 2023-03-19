import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from NaverApi import *
from PyQt5.QtGui import *
import webbrowser
from urllib.request import urlopen

class qtApp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('./Naver_OpneAPI_Movie_Version/naverApiMovie.ui', self)
        self.setWindowIcon(QIcon('./Naver_OpneAPI_Movie_Version/movie.png'))

        self.btnSearch.clicked.connect(self.btnSearchClicked)
        self.txtSearch.returnPressed.connect(self.txtSearchReturned)
        self.tblResult.doubleClicked.connect(self.tblResultDoubleClicked)

    def tblResultDoubleClicked(self):
        selected = self.tblResult.currentRow()
        url = self.tblResult.item(selected, 5).text()
        webbrowser.open(url)


    def txtSearchReturned(self):
        self.btnSearchClicked()

    def btnSearchClicked(self):
        search = self.txtSearch.text()

        if search == '':
            QMessageBox.warning(self, 'Warning', 'Please, Enter a movie title')
            return 
        else:
            api = NaverApi()
            node = 'movie'
            display = 100

            result = api.get_naver_search(node, search, 1, display)
            print(result)
            items = result['items']
            self.makeTable(items)
    
    def makeTable(self, items) -> None:
        self.tblResult.setSelectionMode(QAbstractItemView.SingleSelection) 
        self.tblResult.setColumnCount(7)
        self.tblResult.setRowCount(len(items))
        self.tblResult.setHorizontalHeaderLabels(['Movie Title', 'Realease Year', 'Director', 'Actor',
                                                   'Rating', 'Link', 'Poster'])
        self.tblResult.setColumnWidth(0, 150)
        self.tblResult.setColumnWidth(1, 60)
        self.tblResult.setColumnWidth(4, 40)
        self.tblResult.setEditTriggers(QAbstractItemView.NoEditTriggers)

        for i, post in enumerate(items):
            title = self.replaceHtmlTag(post['title'])
            subtitle = post['subtitle']
            title = f'{title}\n({subtitle})'
            pubDate = post['pubDate']
            director = post['director'].replace('|', ',')[:-1]
            actor = post['actor'].replace('|',',')[:-1]
            userRating = post['userRating']
            link = post['link']
            img_url = post['image']
            

            if img_url != '':
                data = urlopen(img_url).read()
                image = QImage()
                image.loadFromData(data)

                imgLabel = QLabel()
                imgLabel.setPixmap(QPixmap(image))

            self.tblResult.setItem(i, 0, QTableWidgetItem(title))
            self.tblResult.setItem(i, 1, QTableWidgetItem(pubDate))
            self.tblResult.setItem(i, 2, QTableWidgetItem(director))
            self.tblResult.setItem(i, 3, QTableWidgetItem(actor))
            self.tblResult.setItem(i, 4, QTableWidgetItem(userRating))
            self.tblResult.setItem(i, 5, QTableWidgetItem(link))
            
            if img_url != '':
                self.tblResult.setCellWidget(i, 6, imgLabel)
                self.tblResult.setRowHeight(i, 110)
            else:
                self.tblResult.setItem(i, 6, QTableWidgetItem('No Poster'))
                
    def replaceHtmlTag(self, sentence) -> str:
        result = sentence.replace('&lt;', '<')
        result = result.replace('&gt;', '>')
        result = result.replace('<b>', '')
        result = result.replace('</b>', '')
        result = result.replace('&apos', "'")
        result = result.replace('&quot', '"') 
        return result
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())