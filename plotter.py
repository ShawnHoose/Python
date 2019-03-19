#!/usr/bin/python
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_gtkagg import FigureCanvasGTKAgg as FigureCanvas
import sys
import pygtk
pygtk.require('2.0')
import gtk
import time

args = sys.argv[1:]

if len(args)>1:
    filelist = args
    print ('\nYou have chosen %s files. You do not need to select them again in the interface..\n'%(len(filelist)))

else:
    print ('\nNo files selected. Please select files to plot using the interface..\n')
    filelist = []


class PlotWindow:
    fig = plt.figure()
    ax = fig.add_subplot(111)
    canvas = FigureCanvas(fig)

    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_position(gtk.WIN_POS_CENTER_ALWAYS)
        self.window.set_border_width(10)
        self.window.set_title("Autoplot")
        self.window.show()


        topframe = gtk.VBox()
        highframe = gtk.Frame()
        lowframe = gtk.Frame()

        table = gtk.Table(4,3,True)

        self.window.add(topframe)
        topframe.add(highframe)
        topframe.add(lowframe)
        highframe.add(table)

        filebutton = gtk.Button("Choose files")
        table.attach(filebutton,1,2,0,1)
        filebutton.show()

        def get_files(self):
            global filelist
            dialog = gtk.FileChooserDialog("Open..",None,gtk.FILE_CHOOSER_ACTION_OPEN,(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,gtk.STOCK_OPEN, gtk.RESPONSE_OK))
            dialog.set_default_response(gtk.RESPONSE_OK)
            dialog.set_select_multiple(True)
            response = dialog.run()
            if response == gtk.RESPONSE_OK:
                    filelist = dialog.get_filenames()
                    print ('\n%s files have been selected\n%s'%(len(filelist),filelist))
                    dialog.destroy()
            elif response == gtk.RESPONSE_CANCEL:
                    print ('Closed, no files selected')
                    dialog.destroy()

        filebutton.connect('clicked',get_files)

        title= gtk.Label("Graph Title:")
        title_entry = gtk.Entry()
        title_entry.set_activates_default(True)
        table.attach(title,0,1,1,2)
        table.attach(title_entry,1,2,1,2)

        saveas=gtk.Label("Save as(no extention):")
        saveas_entry = gtk.Entry()
        saveas_entry.set_activates_default(True)
        table.attach(saveas,0,1,2,3)
        table.attach(saveas_entry,1,2,2,3)

        kbs = gtk.RadioButton(None,'KB/s')
        table.attach(kbs,2,3,1,2)
        kbs.set_active(True)

        mbs = gtk.RadioButton(kbs,'MB/s')
        table.attach(mbs,2,3,2,3)

        kbs.show()
        mbs.show()
        table.show()
        saveas_entry.show()
        title_entry.show()
        title.show()
        saveas.show()

        plot = gtk.Button("Plot")
        table.attach(plot,0,1,3,4)
        plot.show()

        clear = gtk.Button("Clear plot")
        table.attach(clear,2,3,3,4)
        clear.show()


        def clearPlot(self):
            self.window.resize(1000,1000)
            lowframe.remove(PlotWindow.canvas)
            topframe.remove(lowframe)
            PlotWindow.ax.clear()
            self.window.resize(20,20)
        clear.connect("clicked",clearPlot)

        def plotPress(self):
            totalout = [ [None for i in range(3)]for j in range(len(filelist))]
            readvals = [ None for _ in range(len(filelist))]
            writevals = [None for _ in range (len(filelist))]
            i=0
            k=0


            for name in filelist:
                datafile=open(name,'r')
                totalfile=datafile.read().splitlines()
                totalout[i][0]=totalfile[0]
                j=0
                if (len(totalfile) <= 5):
                    while(j<len(totalfile)):
                        if totalfile[j].find('Block_') != -1:
                            split=totalfile[j].split()
                            if split[0].find("_Write") != -1:
                                totalout[i][1]=float(split[1])
                            elif split[0].find("_Read") !=-1:
                                totalout[i][2]=float(split[1])
                        j+=1
                else:
                    data=totalfile[-1].split(',')
                    totalout[i][1]=float(data[10])
                    totalout[i][2]=float(data[4])
                readvals[k] = totalout[i][2]
                writevals[k] = totalout[i][1]
                k+=1
                i+=1
                datafile.close()


            ind = 0.25 + np.arange(len(filelist))
            wid = 0.40

            ax = PlotWindow.ax

            if mbs.get_active():
                ax.set_ylabel('MB/s')
                for i in range(len(readvals)):
                    readvals[i] = readvals[i] * 10**-3
                    writevals[i] = writevals[i] * 10**-3
            else:
                ax.set_ylabel('KB/s')

            amax = max(readvals)
            bmax = max(writevals)
            totmax = 0
            if amax > bmax:
                totmax = amax
            else:
                totmax = bmax

            rects1 = ax.bar(ind,readvals, wid, color='r', alpha=0.7)
            rects2 = ax.bar(ind+wid, writevals, wid, color='b', alpha=0.7)
            ax.set_xticks(ind+wid)
            ax.set_title(title_entry.get_text())
            ax.set_ylim([0,totmax*1.1])
            ax.set_xlim([0,len(filelist) + 0.40])
            xtickMarks = [totalout[i][0] for i in range(0,len(filelist))]
            xtickNames = ax.set_xticklabels(xtickMarks)
            plt.setp(xtickNames, rotation = 30)

            if (len(totalfile) == 10):
                ax.legend( (rects1[0], rects2[0]), ('with connections', 'without connections'))
            else:
                ax.legend( (rects1[0], rects2[0]),('Block Read', 'Block Write'))

            def autolabel(rects):
                for rect in rects:
                    height = rect.get_height()
                    ax.text(rect.get_x() + rect.get_width()/2. , 1.03*height, '%d'%float(height), ha='center', va='bottom')

            autolabel(rects1)
            autolabel(rects2)
            topframe.add(lowframe)
            ax.plot()
            PlotWindow.canvas.draw()

            PlotWindow.canvas.set_size_request(640,640)
            lowframe.add(PlotWindow.canvas)
            PlotWindow.canvas.show()
            lowframe.show()

            print ('\nsaving plot as %s.png'%(saveas_entry.get_text()))
            plt.savefig('%s.png'%(saveas_entry.get_text()), bbox_inches ='tight')



        plot.connect("clicked",plotPress)
        title_entry.connect("activate",plotPress)
        saveas_entry.connect("activate",plotPress)

        topframe.show()
        highframe.show()
        lowframe.show()

        self.window.connect("delete-event",gtk.main_quit)
        self.window.show()


def main():
    gtk.main()
    return 0

if __name__=="__main__":
    window = PlotWindow()
    main()
