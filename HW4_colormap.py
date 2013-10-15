# ==============================================================================     
#  HW4: function to call the RGB colomap data from http://geography.uoregon.edu, 
#       and return the number of color (leng) & a colormap dictionary (cdict) 
# ==============================================================================     
#  by InOk Jun
#  OCNG 658, Fall 2013
# ==============================================================================  

# import statement
import urllib
import numpy as np
import matplotlib
import matplotlib.pylab as plt


def colormap(filename):
    '''
    This function is designed to 
    1) call the RGB colomap data from http://geography.uoregon.edu
    2) return the number of color (leng) & a colormap dictionary (cdict) 

    Input : filename = name of colormap in website
    Output: cdic     = dictionay for the colormap
            leng     = number of color in the colormap
    
    '''
    
    # open URL to call the colormap information
    address = 'http://geography.uoregon.edu/datagraphics/color/'+filename+'.txt'
    URL = urllib.urlopen(address)
    
    # make an empty list
    R = []
    G = []
    B = []
    
    # read RGB data from the website
    for line in URL.readlines()[2:]:
        colors = line.split()  
        R.append(float(colors[0]))
        G.append(float(colors[1]))
        B.append(float(colors[2]))

    # close URL for memory
    URL.close()

    # make a colormap dictionary (cdict) 
    leng   = len(R)
    Reds   = [(float(i)/(leng-1), R[i-1], R[i]) for i in range(leng)]
    Greens = [(float(i)/(leng-1), G[i-1], G[i]) for i in range(leng)]
    Blues  = [(float(i)/(leng-1), B[i-1], B[i]) for i in range(leng)]
    cdict  = {'red': Reds, 'green':Greens, 'blue': Blues}

    # return the result
    return cdict, leng



# define the colormap to use
cfile = 'BuDOr_18'

# get the colormap using the function 'colormap'
mydict, n = colormap(cfile)

# plot the result using the random number
my_cmap = matplotlib.colors.LinearSegmentedColormap('my_colormap',mydict,n)
plt.pcolor(np.random.rand(10,10),cmap=my_cmap)
plt.colorbar()
plt.show()

# save the figure
plt.savefig('HW4_by_Jun.png', dpi = 600)