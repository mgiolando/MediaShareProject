# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src_ui/ui_main.ui'
#
# Created: Mon May 23 21:42:32 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from watchvideo.qt import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(750, 637)
        MainWindow.setMinimumSize(QtCore.QSize(700, 600))
        MainWindow.setMouseTracking(False)
        MainWindow.setWindowTitle("WatchVideo")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/media/watchvideo-32x32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tab_widget = QtGui.QTabWidget(self.centralwidget)
        self.tab_widget.setObjectName("tab_widget")
        self.tab_player = QtGui.QWidget()
        self.tab_player.setObjectName("tab_player")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab_player)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.nameLabel = QtGui.QLabel(self.tab_player)
        self.nameLabel.setStyleSheet("None")
        self.nameLabel.setText("")
        self.nameLabel.setObjectName("nameLabel")
        self.verticalLayout_4.addWidget(self.nameLabel)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.videoWidget = QtGui.QWidget(self.tab_player)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.videoWidget.sizePolicy().hasHeightForWidth())
        self.videoWidget.setSizePolicy(sizePolicy)
        self.videoWidget.setMinimumSize(QtCore.QSize(0, 300))
        self.videoWidget.setMouseTracking(True)
        self.videoWidget.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.videoWidget.setObjectName("videoWidget")
        self.horizontalLayout_3.addWidget(self.videoWidget)
        self.playlistWidget = QtGui.QTreeWidget(self.tab_player)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playlistWidget.sizePolicy().hasHeightForWidth())
        self.playlistWidget.setSizePolicy(sizePolicy)
        self.playlistWidget.setMouseTracking(True)
        self.playlistWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.playlistWidget.setRootIsDecorated(False)
        self.playlistWidget.setObjectName("playlistWidget")
        self.playlistWidget.headerItem().setText(0, "-")
        self.playlistWidget.headerItem().setText(1, "-")
        self.playlistWidget.header().setVisible(False)
        self.playlistWidget.header().setDefaultSectionSize(30)
        self.horizontalLayout_3.addWidget(self.playlistWidget)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stackedWidget = QtGui.QStackedWidget(self.tab_player)
        self.stackedWidget.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QtCore.QSize(47, 36))
        self.stackedWidget.setMaximumSize(QtCore.QSize(47, 34))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtGui.QWidget()
        self.page.setObjectName("page")
        self.btn_play = QtGui.QPushButton(self.page)
        self.btn_play.setEnabled(True)
        self.btn_play.setGeometry(QtCore.QRect(0, 0, 46, 34))
        self.btn_play.setMinimumSize(QtCore.QSize(46, 34))
        self.btn_play.setMaximumSize(QtCore.QSize(46, 34))
        self.btn_play.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/media/start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_play.setIcon(icon1)
        self.btn_play.setObjectName("btn_play")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setEnabled(True)
        self.page_2.setObjectName("page_2")
        self.btn_pause = QtGui.QPushButton(self.page_2)
        self.btn_pause.setEnabled(True)
        self.btn_pause.setGeometry(QtCore.QRect(0, 0, 46, 34))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_pause.sizePolicy().hasHeightForWidth())
        self.btn_pause.setSizePolicy(sizePolicy)
        self.btn_pause.setMinimumSize(QtCore.QSize(46, 34))
        self.btn_pause.setMaximumSize(QtCore.QSize(46, 34))
        self.btn_pause.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/media/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_pause.setIcon(icon2)
        self.btn_pause.setObjectName("btn_pause")
        self.stackedWidget.addWidget(self.page_2)
        self.horizontalLayout.addWidget(self.stackedWidget)
        self.btn_stop = QtGui.QPushButton(self.tab_player)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(46)
        sizePolicy.setVerticalStretch(34)
        sizePolicy.setHeightForWidth(self.btn_stop.sizePolicy().hasHeightForWidth())
        self.btn_stop.setSizePolicy(sizePolicy)
        self.btn_stop.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/media/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_stop.setIcon(icon3)
        self.btn_stop.setObjectName("btn_stop")
        self.horizontalLayout.addWidget(self.btn_stop)
        self.btn_replay = QtGui.QPushButton(self.tab_player)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(46)
        sizePolicy.setVerticalStretch(34)
        sizePolicy.setHeightForWidth(self.btn_replay.sizePolicy().hasHeightForWidth())
        self.btn_replay.setSizePolicy(sizePolicy)
        self.btn_replay.setMinimumSize(QtCore.QSize(46, 34))
        self.btn_replay.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/media/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_replay.setIcon(icon4)
        self.btn_replay.setFlat(True)
        self.btn_replay.setObjectName("btn_replay")
        self.horizontalLayout.addWidget(self.btn_replay)
        self.progressBar = Slider(self.tab_player)
        self.progressBar.setMaximum(1000)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout.addWidget(self.progressBar)
        self.timeLabel = QtGui.QLabel(self.tab_player)
        self.timeLabel.setStatusTip("None")
        self.timeLabel.setText("00:00/00:00")
        self.timeLabel.setObjectName("timeLabel")
        self.horizontalLayout.addWidget(self.timeLabel)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.tab_widget.addTab(self.tab_player, "")
        self.tab_downloads = QtGui.QWidget()
        self.tab_downloads.setObjectName("tab_downloads")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_downloads)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tree_downloads = QtGui.QTreeWidget(self.tab_downloads)
        self.tree_downloads.setAlternatingRowColors(True)
        self.tree_downloads.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.tree_downloads.setItemsExpandable(True)
        self.tree_downloads.setAllColumnsShowFocus(True)
        self.tree_downloads.setColumnCount(5)
        self.tree_downloads.setObjectName("tree_downloads")
        self.tree_downloads.header().setDefaultSectionSize(140)
        self.tree_downloads.header().setMinimumSectionSize(60)
        self.tree_downloads.header().setStretchLastSection(True)
        self.verticalLayout_2.addWidget(self.tree_downloads)
        self.tab_widget.addTab(self.tab_downloads, "")
        self.verticalLayout.addWidget(self.tab_widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 750, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setEnabled(True)
        self.toolBar.setWindowTitle("toolBar")
        self.toolBar.setIconSize(QtCore.QSize(32, 32))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea(QtCore.Qt.TopToolBarArea), self.toolBar)
        self.dockWidget = SearchWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget.sizePolicy().hasHeightForWidth())
        self.dockWidget.setSizePolicy(sizePolicy)
        self.dockWidget.setMinimumSize(QtCore.QSize(101, 131))
        self.dockWidget.setWindowTitle("")
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.searchLine = SearchField(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchLine.sizePolicy().hasHeightForWidth())
        self.searchLine.setSizePolicy(sizePolicy)
        self.searchLine.setStyleSheet("None")
        self.searchLine.setObjectName("searchLine")
        self.horizontalLayout_2.addWidget(self.searchLine)
        self.b_search = QtGui.QPushButton(self.dockWidgetContents)
        self.b_search.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/media/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.b_search.setIcon(icon5)
        self.b_search.setObjectName("b_search")
        self.horizontalLayout_2.addWidget(self.b_search)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.resultsWidget = QtGui.QTreeWidget(self.dockWidgetContents)
        self.resultsWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.resultsWidget.setRootIsDecorated(False)
        self.resultsWidget.setWordWrap(True)
        self.resultsWidget.setHeaderHidden(True)
        self.resultsWidget.setObjectName("resultsWidget")
        self.resultsWidget.headerItem().setText(0, "1")
        self.resultsWidget.header().setMinimumSectionSize(50)
        self.verticalLayout_3.addWidget(self.resultsWidget)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        self.a_addVideos = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/media/harddisk-add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.a_addVideos.setIcon(icon6)
        self.a_addVideos.setObjectName("a_addVideos")
        self.a_searchBrowser = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/media/Web-browser.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.a_searchBrowser.setIcon(icon7)
        self.a_searchBrowser.setObjectName("a_searchBrowser")
        self.a_clearCompleted = QtGui.QAction(MainWindow)
        self.a_clearCompleted.setEnabled(False)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/media/edit-clear-list.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.a_clearCompleted.setIcon(icon8)
        self.a_clearCompleted.setObjectName("a_clearCompleted")
        self.a_about = QtGui.QAction(MainWindow)
        self.a_about.setIcon(icon)
        self.a_about.setObjectName("a_about")
        self.a_preferences = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/media/preferences.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.a_preferences.setIcon(icon9)
        self.a_preferences.setObjectName("a_preferences")
        self.a_quit = QtGui.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/media/quit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.a_quit.setIcon(icon10)
        self.a_quit.setObjectName("a_quit")
        self.a_clipboard = QtGui.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/media/klipper.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.a_clipboard.setIcon(icon11)
        self.a_clipboard.setObjectName("a_clipboard")
        self.a_play = QtGui.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/media/internet-play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.a_play.setIcon(icon12)
        self.a_play.setObjectName("a_play")
        self.a_download = QtGui.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/media/internet-download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.a_download.setIcon(icon13)
        self.a_download.setObjectName("a_download")
        self.a_viewSearch = QtGui.QAction(MainWindow)
        self.a_viewSearch.setCheckable(True)
        self.a_viewSearch.setChecked(True)
        self.a_viewSearch.setObjectName("a_viewSearch")
        self.menuFile.addAction(self.a_quit)
        self.menuEdit.addAction(self.a_preferences)
        self.menuHelp.addAction(self.a_about)
        self.menuView.addAction(self.a_viewSearch)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.a_addVideos)
        self.toolBar.addAction(self.a_searchBrowser)
        self.toolBar.addAction(self.a_clipboard)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.a_play)
        self.toolBar.addAction(self.a_download)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.a_clearCompleted)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        self.tab_widget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_player), QtGui.QApplication.translate("MainWindow", "Player", None, QtGui.QApplication.UnicodeUTF8))
        self.tree_downloads.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Title", None, QtGui.QApplication.UnicodeUTF8))
        self.tree_downloads.headerItem().setText(1, QtGui.QApplication.translate("MainWindow", "Size", None, QtGui.QApplication.UnicodeUTF8))
        self.tree_downloads.headerItem().setText(2, QtGui.QApplication.translate("MainWindow", "Progress", None, QtGui.QApplication.UnicodeUTF8))
        self.tree_downloads.headerItem().setText(3, QtGui.QApplication.translate("MainWindow", "Speed", None, QtGui.QApplication.UnicodeUTF8))
        self.tree_downloads.headerItem().setText(4, QtGui.QApplication.translate("MainWindow", "Time Left", None, QtGui.QApplication.UnicodeUTF8))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_downloads), QtGui.QApplication.translate("MainWindow", "Downloads", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuView.setTitle(QtGui.QApplication.translate("MainWindow", "View", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setToolTip(QtGui.QApplication.translate("MainWindow", "Shortcut to get the links from the clipboard", None, QtGui.QApplication.UnicodeUTF8))
        self.a_addVideos.setText(QtGui.QApplication.translate("MainWindow", "Add Videos", None, QtGui.QApplication.UnicodeUTF8))
        self.a_addVideos.setToolTip(QtGui.QApplication.translate("MainWindow", "Add one or more links to download or play directly in your favorite mediaplayer.", None, QtGui.QApplication.UnicodeUTF8))
        self.a_searchBrowser.setText(QtGui.QApplication.translate("MainWindow", "Search Browser", None, QtGui.QApplication.UnicodeUTF8))
        self.a_searchBrowser.setToolTip(QtGui.QApplication.translate("MainWindow", "Searches open windows and tabs in your browser for flash videos (only Firefox and derivatives are suported)", None, QtGui.QApplication.UnicodeUTF8))
        self.a_clearCompleted.setText(QtGui.QApplication.translate("MainWindow", "Clear Completed", None, QtGui.QApplication.UnicodeUTF8))
        self.a_about.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.a_preferences.setText(QtGui.QApplication.translate("MainWindow", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.a_quit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.a_clipboard.setText(QtGui.QApplication.translate("MainWindow", "Clipboard", None, QtGui.QApplication.UnicodeUTF8))
        self.a_clipboard.setToolTip(QtGui.QApplication.translate("MainWindow", "Fetch link from the clipboard", None, QtGui.QApplication.UnicodeUTF8))
        self.a_play.setText(QtGui.QApplication.translate("MainWindow", "Play", None, QtGui.QApplication.UnicodeUTF8))
        self.a_play.setToolTip(QtGui.QApplication.translate("MainWindow", "Shortcut to play the video(s) from the url(s) on the clipboard", None, QtGui.QApplication.UnicodeUTF8))
        self.a_download.setText(QtGui.QApplication.translate("MainWindow", "Download", None, QtGui.QApplication.UnicodeUTF8))
        self.a_download.setToolTip(QtGui.QApplication.translate("MainWindow", "Shortcut to download the video(s) from the url(s) on the clipboard", None, QtGui.QApplication.UnicodeUTF8))
        self.a_viewSearch.setText(QtGui.QApplication.translate("MainWindow", "Search", None, QtGui.QApplication.UnicodeUTF8))

from slider import Slider
from searchfield import SearchField
from search_widget import SearchWidget
from watchvideo import icons_rc
assert icons_rc