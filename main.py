import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Handler:
    def on_runButton_clicked(self, widget):
        print("Clicou em Run!")

    def on_directoryChoose_file_set(self, widget):
        print("Escolheu um diretório....")

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
