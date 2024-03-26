import plsc
import plotter as pltr
import sys


file=r"C:\users\minha\desktop\plspec\test.dat"
peaks=1
to_ev=1

x,y=plsc.load(file,peaks,to_ev)

if to_ev==1:
    fig=pltr.plot_ev(x,y,label=file[-8:-4])
else:
    fig=pltr.plot(x,y,label=file[-8:-4])



