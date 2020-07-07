import os
import sys
import subprocess
import getpass
import gi
from string import digits

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

# check is user is root
if (getpass.getuser()) != "root":
    sys.exit("Yout need be root to run this program")


class Handler:
    def __init__(self):
        print("Init...")
        self.directoryChoose = builder.get_object("directoryChoose")
        self.directoryChoose.set_filename(os.getcwd())
        self.devicesLabel = builder.get_object('devicesLabel')
        self.statusDynamicLabel = builder.get_object("statusDynamicLabel")
        self.updateSysInfo()

    def updateSysInfo(self):
        print("Refresh SysteInfo()")
        # get device disk from directory
        partition = self.executeCmd(
            f"./scripts/getpartition.sh {self.directoryChoose.get_filename()}"
        )
        remove_digits = str.maketrans("", "", digits)
        device = partition.translate(remove_digits)
        model = self.executeCmd(f"./scripts/getdeviceinfo.sh {device}")
        cpuinfo = self.executeCmd('./scripts/getcpuinfo.sh')
        self.devicesLabel.set_text(f'{device} [{model}]\n{cpuinfo}')

    def showError(self, title, message):
        dialog = Gtk.MessageDialog(
            window, 0, Gtk.MessageType.ERROR, Gtk.ButtonsType.OK, title,
        )
        dialog.format_secondary_text(message)
        dialog.run()
        dialog.destroy()

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
