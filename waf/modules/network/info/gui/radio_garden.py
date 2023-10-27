import time,sys
from waf.libs.color  import *
from waf.libs import variable as var
try :
    from PyQt5.QtWidgets import *
    from PyQt5.QtWebEngineWidgets import *
    from PyQt5.QtCore import *
except Exception as e:
    error =e

info = {
        "name"        : "radio_garden",
        "title"       : "View any world radio",
        "module"      : "network/info/gui/radio_garden",
        "description" : """
  It is an interface to the {RADIO GARDEN}
  website that allows you to connect to all
  the radio stations in the world."""
}

options = {}

def running():
    try:
            print ('')
            print (blue+"[*]"+default+"starting the radio")
            time.sleep(0.01)
            try:
                #main window class (to create a window)-sub class of QMainWindow class
                class Window(QMainWindow):

                    #defining constructor function
                    def __init__(self):
                        #creating connnection with parent class constructor
                        super(Window,self).__init__()

                        #---------------------adding browser-------------------
                        self.browser = QWebEngineView()

                        #setting url for browser, you can use any other url also
                        self.browser.setUrl(QUrl('http://radio.garden'))

                        #to display google search engine on our browser
                        self.setCentralWidget(self.browser)

                        #-------------------full screen mode------------------
                        #to display browser in full screen mode, you may comment below line if you don't want to open your browser in full screen mode
                        self.showMaximized()

                        #----------------------navbar-------------------------
                        #creating a navigation bar for the browser
                        navbar = QToolBar()
                        #adding created navbar
                        self.addToolBar(navbar)

                        #-----------------prev Button-----------------
                        #creating prev button
                        prevBtn = QAction('Prev',self)
                        #when triggered set connection
                        prevBtn.triggered.connect(self.browser.back)
                        # adding prev button to the navbar
                        navbar.addAction(prevBtn)

                        #-----------------next Button---------------
                        nextBtn = QAction('Next',self)
                        nextBtn.triggered.connect(self.browser.forward)
                        navbar.addAction(nextBtn)

                        #-----------refresh Button--------------------
                        refreshBtn = QAction('Refresh',self)
                        refreshBtn.triggered.connect(self.browser.reload)
                        navbar.addAction(refreshBtn)

                        #-----------home button----------------------
                        homeBtn = QAction('Home',self)
                        #when triggered call home method
                        homeBtn.triggered.connect(self.home)
                        navbar.addAction(homeBtn)


                    #method to navigate back to home page
                    def home(self):
                        self.browser.setUrl(QUrl('http://radio.garden'))

                    #method to load the required url
                    def loadUrl(self):
                        #fetching entered url from searchBar
                        url = self.searchBar.text()
                        #loading url
                        self.browser.setUrl(QUrl(url))

                    #method to update the url
                    def updateUrl(self, url):
                        #changing the content(text) of searchBar
                        self.searchBar.setText(url.toString())


                MyApp = QApplication(sys.argv)

                #setting application name
                QApplication.setApplicationName('Radio')

                #creating window
                window = Window()

                #executing created app
                MyApp.exec_()

                print (basic_yellow + '[*] Done ')
                print ('')
            except Exception as e:
                print(red+"\n[-]"+default+"Error : "+str(e))


    except Exception as e:
        print(red+"\n[-]"+default+"Error : "+str(e))

