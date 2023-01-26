
#This function is for plotting a line graph with a single dataset, and customizable with the label, color, marker, marksrsize, xlabel, ylabel, and title.

def makeplot(data, label, color, marker, size, linewidth, xlabel, ylabel, title):
'''
    data:   the dataset that we want to plot (ie. data1)
    label:  what we want to label the line (ie. 'line for the legend')
    color:  what color we want the line
    marker: what kind of marker we want
    size:   markersize
    linewidth:  the thickness of the line
    xlabel: The measure and units of the xlabel
    ylabel: The measure and units of the ylabel
    title: the title of the plot
'''

    import matplotlib.pyplot as plt
    plt.plot(data, color, marker, size, linewidth, label)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    return plt.show()
    
