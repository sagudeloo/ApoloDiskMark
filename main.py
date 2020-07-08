import os
import sys
import subprocess
import getpass
import json
import humanfriendly
import re
import time
import threading
import gi
from string import digits

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

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


class Handler:
    benchmarkRunning = False

    def thread_function(self, i, directory):
        print(f"Thread {i}: starting")
        print(f"Index: [{i}] {benchmarks[i]}.sh {directory}")
        output = json.loads(
            self.executeCmd(f"./scripts/{benchmarks[i]}.sh {directory}")
        )
        if i == 0:
            bw_bytes = output["jobs"][0]["read"]["bw_bytes"]
            print(f"{humanfriendly.format_size(bw_bytes)}/s")

        print(f"Thread {i}: finishing")

    def __init__(self):
        print("Init...")
        self.directoryChoose = builder.get_object("directoryChoose")
        self.directoryChoose.set_filename(os.getcwd())
        self.devicesLabel = builder.get_object("devicesLabel")
        self.statusDynamicLabel = builder.get_object("statusDynamicLabel")
        self.progressBar = builder.get_object("progressBar")
        self.runButton = builder.get_object("runButton")
        self.seq1mq8t1R = builder.get_object("seq1mq8t1R")
        self.seq1mq8t1W = builder.get_object("seq1mq8t1W")
        self.seq1mq1t1R = builder.get_object("seq1mq1t1R")
        self.seq1mq1t1W = builder.get_object("seq1mq1t1W")
        self.rnd4kq32t16R = builder.get_object("rnd4kq32t16R")
        self.rnd4kq32t16W = builder.get_object("rnd4kq32t16W")
        self.rnd4kq1t1R = builder.get_object("rnd4kq1t1R")
        self.rnd4kq1t1W = builder.get_object("rnd4kq1t1W")
        self.updateSysInfo()

    def updateSysInfo(self):
        print("Refresh SystemInfo()")
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
        window.refresh()

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
        x = threading.Thread(
            target=self.thread_function, args=(0, self.directoryChoose.get_filename())
        )
        print("Main    : before running thread")
        x.start()
        print("Main    : wait for the thread to finish")


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

