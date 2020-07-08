import os
import sys
import subprocess
import getpass
import json
import humanfriendly
import re
import gi
from string import digits

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Handler:
    benchmarkRunning = False

    def __init__(self):
        print("Init...")
        self.directoryChoose = builder.get_object("directoryChoose")
        self.directoryChoose.set_filename(os.getcwd())
        self.devicesLabel = builder.get_object("devicesLabel")
        self.statusDynamicLabel = builder.get_object("statusDynamicLabel")
        self.progressBar = builder.get_object("progressBar")
        self.runButton = builder.get_object("runButton")
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
        cpuinfo = self.executeCmd("./scripts/getcpuinfo.sh")
        self.devicesLabel.set_text(f"{device} [{model}]\n{cpuinfo}")

    def executeCmd(self, cmd):
        return subprocess.getoutput(cmd)

    def stopBechmark(self):
        self.benchmarkRunning = False
        self.runButton.set_label("Run")
        self.statusDynamicLabel.set_text("IDLE")

    def on_runButton_clicked(self, widget):
        self.progressBar.set_fraction(0)
        if self.benchmarkRunning:
            self.stopBechmark()
        else:
            self.runBenchmark()

    def on_directoryChoose_file_set(self, widget):
        print("Escolheu um diretório....")
        self.updateSysInfo()

    def on_mainWindow_destroy(self, *args):
        Gtk.main_quit()

    def on_quitMenuItem_activate(self, widget):
        Gtk.main_quit()

    def on_aboutMenuItem_activate(self, widget):
        print("Clicou em about...")

    def is_odd(self, a):
        return bool(a & 1)

    def runBenchmark(self):
        print("Running the Benchmark...")
        self.benchmarkRunning = True
        self.runButton.set_label("Stop")
        self.statusDynamicLabel.set_text("Running, please wait...")
        benchmarks = [
            "seq1mq8t1read",
            "seq1mq8t1write",
            "seq1mq1t1read",
            "seq1mq1t1write",
            "rnd4kq32t16read",
            "rnd4kq32t16write",
            "rnd4kq1t1read",
            "rnd4kq1t1write",
        ]
        for index, benchmark in enumerate(benchmarks):
            print(f"Index: [{index}] {benchmark}.sh {self.directoryChoose.get_filename()}")
            #output = json.loads(
            #    self.executeCmd(
            #        f"./scripts/{i}.sh {self.directoryChoose.get_filename()}"
            #    )
            #)


        self.stopBechmark()

    #  output = json.loads(
    #     self.executeCmd(
    #        f"./scripts/rnd4kq1t1read.sh {self.directoryChoose.get_filename()}"
    #    )
    # )
    # bw_bytes = output["jobs"][0]["read"]["bw_bytes"]
    # print(f"Bytes =====> {humanfriendly.format_size(bw_bytes)}/s")


builder = Gtk.Builder()
builder.add_from_file("./glade/mainWindow.glade")
builder.connect_signals(Handler())

window = builder.get_object("mainWindow")


def showError(title, message):
    dialog = Gtk.MessageDialog(
        window, 0, Gtk.MessageType.ERROR, Gtk.ButtonsType.OK, title,
    )
    dialog.format_secondary_text(message)
    dialog.run()
    dialog.destroy()


if (getpass.getuser()) != "root":
    showError("Superuser Rights", "You need root to run this application.")
    sys.exit(1)

window.show_all()
Gtk.main()

