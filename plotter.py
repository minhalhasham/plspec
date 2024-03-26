import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = ['Arial']


def plot (waves,y, color='black', lw=4,label='data', title='plot', xlabel='Wavelength (nm)', ylabel='PL Intensity (arb.)',label_font=26, save=False, name='plot.png'):
    """
    Plotting convenience, these are Minhal's preferred parameters. Feel free to change for yourself, but if you're sending Minhal a figure, don't change.
    """
    plt.figure(figsize=(8,8))
    plt.plot(waves,y, color=color, label=label, lw=lw)
    plt.xlabel(xlabel,fontsize=label_font)
    plt.ylabel(ylabel,fontsize=label_font)
    plt.tick_params(axis='both', labelsize=22)
    plt.legend(fontsize=22)
    plt.tight_layout()
    if save==True:
        plt.savefig(name)
    plt.show()


def plot_ev(E,PL_ev, color='black', lw=4,label='data', title='plot', xlabel='Energy (eV)', ylabel='PL Intensity (arb.)',label_font=26, save=False, name='plot.png'):
    """
    Plotting convenience in energy units, these are Minhal's preferred parameters. Feel free to change for yourself, but if you're sending Minhal a figure, don't change.
    """
    plt.figure(figsize=(8,8))
    plt.plot(E,PL_ev, color=color, label=label, lw=lw)
    plt.xlabel(xlabel,fontsize=label_font)
    plt.ylabel(ylabel,fontsize=label_font)
    plt.tick_params(axis='both', labelsize=22)
    plt.legend(fontsize=22)
    plt.tight_layout()
    if save==True:
        plt.savefig(name)
    plt.show()

def tf(x):
    """
    Convert the x-axis from wavelength to energy. 
    You'll need this if you're converting/plotting in units of energy.
    """
    V=1240./x
    return ["%2.0f" %i for i in V]