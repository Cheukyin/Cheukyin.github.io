#!/usr/bin/python2.7
#coding=utf-8
from bs4 import BeautifulSoup
import sys
import re

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

class Pygments_Html:
    def __init__(self,file):
        self.filename = file
        self.language_dict = {'sh':'sh','matlab':'matlab','C':'c','C++':'c++','css':'css',
                              'python':'python','scheme':'scheme','latex':'latex',
                              'ruby':'ruby','css':'css','html':'html','others':'text'}

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

        # soup is prettified by BeautifulSoup,
        # so there're always something different from the original file, "re.S" is for any charater including \n
        src_html_list = re.findall(r'<div class="org-src-container">.*?</div>',file_read,re.S)

        if src_html_list == []:
            return

        for src_html in src_html_list:
            soup=BeautifulSoup(src_html)
            # code_segment exported by org-mode inside <div class="org-src-container">
            src_soup = soup.find("div",class_="org-src-container")

            # code_segment exported by org-mode has a tag <pre class="src src-lang">,
            # lang identifies the code language
            language = (src_soup.pre['class'][1]).split('-')[1]
            # map language to language_dict
            if language in self.language_dict:
                language = self.language_dict[language]
            else:
                language = self.language_dict['others']
            print "Colorizing " + language

            lexer = get_lexer_by_name(language, stripall=True)
            formatter = HtmlFormatter(linespans='line', cssclass="highlight")

            # Colorize the code with pygmentize
            src_colorized = highlight(src_soup.text, lexer, formatter)

            # replace src_html with src_colorized in file_read
            file_read = file_read.replace(src_html,src_colorized)

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
