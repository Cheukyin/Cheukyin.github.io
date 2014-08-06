#!/usr/bin/python2.7
#coding=utf-8
import os
from bs4 import BeautifulSoup
import sys

class Pygments_Html:
    def __init__(self,file):
        self.filename = file
        self.language_dict = {'sh':'sh','matlab':'matlab','C':'c','C++':'c++',
                              'python':'python','scheme':'scheme','latex':'latex',
                              'ruby':'ruby','css':'css','others':'text'}

    def colorize(self):
        try:
            # open the html file
            file = open( self.filename,'r' )
        except IOError:
            print self.filename,'not exists'
            return

        file_read = file.read()
        print "Opening",self.filename
        file.close()

        soup=BeautifulSoup(file_read)

        # code_segment exported by org-mode inside <div class="org-src-container">
        src_soup_list = soup.find_all("div",class_="org-src-container")

        if src_soup_list == []:
            return

        for src_soup in src_soup_list:
            # write src_segment to file "temp"
            src_segment = src_soup.text
            temp=open('temp','w')
            temp.write(src_segment)
            temp.close()

            # code_segment exported by org-mode has a tag <pre class="src src-lang">,
            # lang identifies the code language
            language = (src_soup.pre['class'][1]).split('-')[1]
            # map language to language_dict
            if language in self.language_dict:
                language = self.language_dict[language]
            else:
                language = self.language_dict['others']
            print "Colorizing " + language

            # Colorize the code with pygmentize
            src_colorized = os.popen('pygmentize -f html -l ' + language + ' temp').read()

            # src_html is prettified by BeautifulSoup,
            # so there's a "\n" missing after <div class="org-src-container">
            src_html = str(src_soup)
            src_html = src_html.replace('<div class="org-src-container">\n','<div class="org-src-container">\n\n')

            # replace src_html with src_colorized in file_read
            file_read = file_read.replace(src_html,src_colorized)

        #remove file "temp"
        os.remove('temp')

        file = open( self.filename,'w' )
        file.write(file_read)
        file.close()


if __name__=='__main__':

    # Change the encodeing of the interpreter from "ascii" to "utf8"
    reload(sys)
    sys.setdefaultencoding('utf8')

    if len(sys.argv)==1:
        print 'No Arguments!'

    else:
        for file in sys.argv[1:]:
            if '.html' in file:
                hightlight_instance = Pygments_Html(file)
                hightlight_instance.colorize()