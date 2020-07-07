import os
import subprocess
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Handler:
    def __init__(self):
        print("Init...")
        self.directoryChoose = builder.get_object("directoryChoose")
        self.directoryChoose.set_filename(os.getcwd())
        self.statusDynamicLabel = builder.get_object("statusDynamicLabel")
        self.updateSysInfo()

    def updateSysInfo(self):
        print("Refresh SysteInfo()")
        # Verifica se pode escrever no diretório corrente
        if eval(
            self.executeCmd(
                f"./scripts/checkdir.sh {self.directoryChoose.get_filename()}"
            )
        ):
            print("Directory is writable...")
        else:
            print("Directory is not writable")

    def executeCmd(self, cmd):
        return subprocess.getoutput(cmd)

    def on_runButton_clicked(self, widget):
        print("Clicou em Run!")

    def on_directoryChoose_file_set(self, widget):
        print("Escolheu um diretório....")
        self.updateSysInfo()

    def on_mainWindow_destroy(self, *args):
        Gtk.main_quit()

    def on_quitMenuItem_activate(self, widget):
        Gtk.main_quit()

    def on_aboutMenuItem_activate(self, widget):
        print("Clicou em about...")


builder = Gtk.Builder()
builder.add_from_file("./glade/mainWindow.glade")
builder.connect_signals(Handler())

window = builder.get_object("mainWindow")
window.show_all()
Gtk.main()
