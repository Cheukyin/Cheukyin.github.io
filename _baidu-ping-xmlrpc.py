#!/usr/bin/python2

import xmlrpclib

class ping_xmlrpclib:
    def __init__(self,Server):
        self.server = xmlrpclib.ServerProxy(Server)
        self.respond = "Failed"

    def ping_baidu(self,blog_name,index_addr,new_post_addr,rss_addr):
        result = self.server.weblogUpdates.extendedPing(blog_name,index_addr,new_post_addr,rss_addr)
        if result == 0:
            self.respond = "Success"

    def response(self):
        print self.respond

ping_baidu = ping_xmlrpclib("http://ping.baidu.com/ping/RPC2")

blog_name = "Cheukyin.blog"
index_addr = "http://cheukyin.github.io/"
print "Input your page url:",
page_url = raw_input(index_addr)
new_post_addr = index_addr + page_url
rss_addr = "http://cheukyin.github.io/rss.xml"

ping_baidu.ping_baidu(blog_name,index_addr,new_post_addr,rss_addr)
ping_baidu.response()