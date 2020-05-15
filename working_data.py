# +
import numpy
import matplotlib.pyplot
import sys
import os

def visualize(filename='data/inflammation-01.csv'):
    '''
    Shows three plots with the average, max, and mean
    of a given csv data file
    
    '''
    
    data = numpy.loadtxt(fname=filename, delimiter=',')

    fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))

    axes1 = fig.add_subplot(1, 3, 1)
    axes2 = fig.add_subplot(1, 3, 2)
    axes3 = fig.add_subplot(1, 3, 3)

    axes1.set_ylabel('average')
    axes1.plot(numpy.mean(data, axis=0))

    axes2.set_ylabel('max')
    axes2.plot(numpy.max(data, axis=0))

    axes3.set_ylabel('min')
    axes3.plot(numpy.min(data, axis=0))

    fig.tight_layout()
    
    #name = filename.split('/')[-1]
    name = os.path.basename(filename)
    
    matplotlib.pyplot.savefig(name+'_fig.eps')
    
def detect_problems(filename):
    '''
    Prints a message if the csv data file has
    odd looking maxima or minima that are zero'''
    data = numpy.loadtxt(fname=filename, delimiter=',')

    max_inflammation_0 = numpy.max(data, axis=0)[0]
    max_inflammation_20 = numpy.max(data, axis=0)[20]

    if max_inflammation_0 == 0 and max_inflammation_20 == 20:
        print('Suspicious looking maxima!')
    elif numpy.sum(numpy.min(data, axis=0)) == 0:
        print('Minima add up to zero!')
    else:
        print('Seems OK!')
        
if __name__ == "__main__":
        
	filenames = sys.argv[1:]

	for file in filenames:
    		visualize(file)
    		detect_problems(file)
# -


