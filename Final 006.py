from graphics import *
import time
import operator

class Button:
    def __init__(self, win, center, width, height, label):
        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.active = True
    def clicked(self, p):
        return(self.active and
               self.xmin <= p.getX() <= self.xmax and
               self.ymin <= p.getY() <= self.ymax)
    def getLabel(self):
        return self.label.getText()
    def setLabel(self,val):
        self.label.setText(str(val))
    def deactivate(self):
        self.label.setFill('darkgray')
        self.rect.setWidth(1)
        self.active = False

class Song:
    def __init__(self, tit, art, lyr):
        self.tit = tit
        self.artist = art
        self.lyrics = lyr
        self.length = 0
    #calculates length of self.lyrics string
        for i in self.lyrics:
            self.length += 1
        self.freqs = []
        self.words = []
    #creates a list of tuples of words and frequencies from self.lyrics string
        freqlyr = self.lyrics.lower()
        temp = ""
        for i in freqlyr:
            if i not in ['"','.',',','?','!',"'",'(',')']:
                temp = temp + i
        freqlyr = temp
        freqlyr = freqlyr.split()
        for i in freqlyr:
            if i in self.words:
                a = self.words.index(i)
                self.freqs[a] = (i,int(self.freqs[a][1]) + 1)
            else:
                self.words = self.words + [i]
                self.freqs = self.freqs + [(i,1)]
        self.topWords = sorted(self.freqs, key=operator.itemgetter(1), reverse=True)
    def getTitle(self):
        return self.tit
    def setTitle(self, newtit):
        self.tit = newtit
    def artist(self, newartist = '000'):
        if newartist != '000':
            self.artist = artist
        return self.artist
    def getLength(self):
        return self.lengh
    def getFreqs(self):
        return self.freqs
    def getLyrics(self):
        return self.lyrics
    def setLyrics(self, newlyrics):
        self.lyrics = newlyrics
    def getSorted (self):
        return self.topWords
    def __str__(self):
        return self.tit, self.artist

def makeBarGraph(song, wn):
#clears the previous graph
    rect = Rectangle(Point(.25,.25), Point(6.1, 7.5))
    saver = Image(Point(2.75,3.25), 'Songs/BaseImage.png')
    rect.setOutline('lightblue')
    rect.setFill('lightblue')
    rect.draw(wn)
#graphs selected lyrics
    x = 1
    xaxis = Line(Point(.5, 1), Point(6, 1))
    yaxis = Line(Point(1, .5), Point(1, 7))
    xaxis.setWidth(2)
    yaxis.setWidth(2)
    for i in range(15):
        topWords = song.getSorted()
        maxh = topWords[0][1]
        bar = Rectangle(Point(x, (topWords[i][1]/maxh)*6+1), Point((x+.333),1))
        if i % 2 == 0:
            bar.setFill('lightgreen')
        else:
            bar.setFill('salmon')
        bar.draw(wn)
        
    #prints the key number under the bar
        num = Text(Point(x+.1665,.75), str(i +1))
        num.draw(wn)
    #prints the number of times each word was said above the bar
        count = Text(Point(x+.1665, topWords[i][1]/maxh*6+1.25), topWords[i][1])
        count.draw(wn)
        x += .333
    xaxis.draw(wn)
    yaxis.draw(wn)
    wn.update()
    return saver

def makeWordCloud(song, wn, num):
#clears the previous graph
    rect = Rectangle(Point(.25,.25), Point(6.1, 7.5))
    saver = Image(Point(2.75,3.25), 'Songs/BaseImage.png')
    rect.setOutline('lightblue')
    rect.setFill('lightblue')
    rect.draw(wn)
#sorts lyrics into frequency list and sets up variables
    topWords = song.getSorted()
    x = 3
    y = 5
    xvar = 0.8
    yvar = 0.4
#establishes spiral word cloud
    for i in range(num):
        word = Text(Point(x,y), str(topWords[i][0]))
    #defines word font size based on frequency
        if i == 0:
            word.setSize(36)
        else:
            word.setSize(36-(i*2))
    #defines transformations for each iteration
        if i == 0:
            x = x + xvar
        if i == 1:
            y = y + yvar
        if i == 2 or i == 3:
            x = x - xvar
        if i == 4 or i == 5:
            y = y - yvar
        if i == 6 or i == 7 or i == 8:
            x = x + xvar
        if i == 9 or i == 10 or i == 11:
            y = y + yvar
        if i == 12 or i == 13 or i == 14:
            x = x - xvar
        word.draw(wn)

#def makeSquareChart(song, wn):
#clears the previous graph
    #rect = Rectangle(Point(.25,.25), Point(6.1, 7.5))
    #saver = Image(Point(2.75,3.25), 'Songs/BaseImage.png')
    #rect.setOutline('lightblue')
    #rect.setFill('lightblue')
    #rect.draw(wn)
#draws basic word cloud

def openIntroWin():
#initializes and displays splash screen
    introwin = GraphWin('Lyric Stats', 450, 300)
    introwin.setCoords(0.0, 0.0, 4.5, 3.0)
    logo = Image(Point(2.25, 1.5), 'logo.png')
    logo.draw(introwin)
    time.sleep(2)
    introwin.close()

def openSongWin(num, lis):
#determines window width
    if 30 < num <= 60:
        width = 600
    elif 60 < num <= 90:
        width = 900
    elif 90 < num:
        width = 1200
    else:
        width = 300
#determines window heighth
    if num >= 30:
        height = 375
    else:
        height = num * 25
#creates window
    songWin = GraphWin('Songs', width, height)
    songWin.setCoords(0.0, 0.0, width, height)
    while songWin.isOpen:
    #creates song buttons
        if 30 < num <= 60:
            buttons2 = [Button(songWin, Point(300, i*25+10), 300, 25, lis[i].getTitle()) for i in range(30, mun)]
        elif 60 < num <= 90:
            buttons3 = [Button(songWin, Point(450, i*25+10), 300, 25, lis[i].getTitle()) for i in range(60, num)]
        elif 90 < num:
            buttons4 = [Button(songWin, Point(600, i*25+10), 300, 25, lis[i].getTitle()) for i in range(90, 100)]
        else:
            buttons1 = [Button(songWin, Point(150, i*25+10), 300, 25, lis[i].getTitle()) for i in range(0, num)]
    #waits for a song to be selected, returns song's number in songlist
        pt = songWin.getMouse()
        i = 1
    #returns number of clicked button
        while i == 1:
            for butt in buttons1:
                if butt.clicked(pt):
                    songWin.close()
                    pos = buttons1.index(butt)
                    return lis[pos]
            for butt in buttons2:
                if butt.clicked(pt):
                    songWin.close()
                    pos = buttons2.index(butt)
                    return lis[pos]
            for butt in buttons3:
                if butt.clicked(pt):
                    songWin.close()
                    pos = buttons3.index(butt)
                    return lis[pos]
            for butt in buttons4:
                if butt.clicked(pt):
                    songWin.close()
                    pos = buttons4.index(butt)
                    return lis[pos]

def openVisWin(num, lis):
#creates window
    height = 0
    while height != (num*25):
        height = height + 25
#creates visualization buttons
    visWin = GraphWin('Visualizations', 300, height)
    visWin.setCoords(0.0, 0.0, 300, height)
    buttons1 = Button(visWin, Point(150, height/num - 12.5), 300, 25, str(lis[0]))
    buttons2 = Button(visWin, Point(150, height/num + 12.5), 300, 25, str(lis[1]))
    buttons3 = Button(visWin, Point(150, height/num + 37.5), 300, 25, str(lis[2]))
#defines what happens when buttons are clicked
    while visWin.isOpen:
        pt = visWin.getMouse()
        i = 1
        while i == 1:
            if buttons1.clicked(pt):
                    visWin.close()
                    return lis[0]
            elif buttons2.clicked(pt):
                    visWin.close()
                    return lis[1]
            elif buttons3.clicked(pt):
                    visWin.close()
                    return lis[2]

def printLyrics(song, wn):
# draws lyrics of selected song
    title = Text(Point(7.875, 7.875), str(song.getTitle()))
    title.setSize(20)
    title.draw(wn)
    lyrics = Text(Point(7.875, 4.5), str(song.getLyrics()))
    lyrics.setSize(6)
    lyrics.draw(wn)

def openGUI(lis):
#initializes main GUI
    #openIntroWin()
    win = GraphWin('Lyric Stats', 1100, 850, autoflush=False)
    win.setCoords(0.0, 0.0, 11.0, 8.5)
    win.setBackground('lightblue')
#adds the "choose song" button
    choosefile = Button(win, Point(2, 8), 3, .25, 'Select Song')
#adds the "choose visualization" button
    choosevis = Button(win, Point(2, 7.75), 3, .25, 'Select Visualization')
#adds button to close the window
    exitbutton = Button(win, Point(3.75, 7.875), .5, .5, 'exit')
    win.update()
    pt = win.getMouse()
#closes window if the "exit" button is clicked
    while not exitbutton.clicked(pt):
    #opens the song choice window if the button is clicked
        if choosefile.clicked(pt):
                openedSongWin = openSongWin(len(lis), lis)
                choosefile.setLabel(str(openedSongWin.getTitle()))
                printLyrics(openedSongWin, win)
        if choosevis.clicked(pt):
                vislist = ['Bar Graph', 'Square Chart', 'Word Cloud']
                openedVisWin = openVisWin(len(vislist), vislist)
                choosevis.setLabel(str(openedVisWin))
                if openedVisWin == vislist[0]:
                    makeBarGraph(openedSongWin, win)
                ##elif openedVisWin == vislist[1]:
                    ##makeSquareChart(openedSongWin, win)
                elif openedVisWin == vislist[2]:
                    makeWordCloud(openedSongWin, win, 15)
    #looks for another click
        pt = win.getMouse()
    win.close()
    
def makeSongs():
#initializes the song lists
    titList = []
    artList = []
    lyricList = []
    namelist = []
    songInfo = open('Songs/TopSongs.txt', 'r')
    for aline in songInfo:
    #splits list of titles and artists into seperate lists
        a, b = aline.split('\t')
        titList = titList + [a]
        artList = artList + [b]
    for i in range(len(titList)):
    #creates list of filenames
        namelist = namelist + ['song' + str(i)]
        namebase = 'Songs/Lyrics'
        nameend = '.txt'
        name = namebase + str(i) + nameend
    #opens the lyric files and makes a string out of the lyrics
        file = open(name)
        text = file.read()
    #adds lyrics to the list of lyrics
        lyricList = lyricList + [text]
    songs = [Song(titList[i], artList[i], lyricList[i]) for i in range(20)]
    return songs

def main():
    songs = makeSongs()
    openGUI(songs)

main()