#-*- coding:utf-8 –*-
import gi
import os,os.path
import zipfile
from zipfile import ZIP_DEFLATED
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk,GObject

class ButtonWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="网站整站下载器v1.0-njcx")
        self.set_border_width(100)

        hbox = Gtk.Box(spacing=6)
        self.add(hbox)
        
        self.entry = Gtk.Entry()
        self.entry.set_text("在这输入网站地址")
        hbox.pack_start(self.entry, True, True, 0)

        button = Gtk.Button.new_with_label("下载不打包")
        button.connect("clicked", self.on_click_me_clicked)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_mnemonic("下载并打包")
        button.connect("clicked", self.on_open_clicked)
        hbox.pack_start(button, True, True, 0)
    def on_click_me_clicked(self, button):
        add= self.entry.get_text()
        add1="wget -r -p -np -k "+add
        cmd1 = os.system(add1)

    def on_open_clicked(self, button):
        """add= self.entry.get_text()
        cwd1=os.getcwd()
        add1="wget -r -p -np -k "+add
        add2=cwd1+"//"+add+".zip"
        add3="rm -rf "+add
        add4=cwd1+"//"+add
        cmd1 = os.system(add1)
        self.zip_dir(str(add4),str(add2))
        cmd3 = os.system(add3)"""
    def zip_dir(dirname,zipfilename):
        filelist = []
        if os.path.isfile(dirname):
            filelist.append(dirname)
        else :
            for root, dirs, files in os.walk(dirname):
                for name in files:
                    filelist.append(os.path.join(root, name))
        zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)
        for tar in filelist:
            arcname = tar[len(dirname):]
            zf.write(tar,arcname)
            zf.close()
        
win = ButtonWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
