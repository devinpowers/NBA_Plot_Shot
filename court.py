
import matplotlib.pylab as plt
import matplotlib as mpl
from matplotlib.patches import Circle, Rectangle, Arc

from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox

#start plotting

#lw = line width = standard for court

def create_ncaa_half_court(ax=None, court_color='white', lw=3, lines_color='black', lines_alpha=0.5, paint_fill='Green', paint_alpha=0.4, inner_arc= True):
    
    # combining two independent plots with matplotlib
    # ax = axes
    if ax is None:
        ax = plt.gca()
    
        
    # Center Circle
    # Circle(xy, radius, color, fill)
    center_circle = Circle((50/2, 94/2), 6, inewidth=lw, color=lines_color, lw=lw, fill=False, alpha=lines_alpha)
    
    #Basketball Hoop
    hoop = Circle((50/2, 5.25), 1.5 / 2, linewidth=lw, color=lines_color, lw=lw, fill=False, alpha=lines_alpha)
    
    
    # Paint - 18 Feet 10 inches which converts to 18.83333 feet 
    # Rectangle(xy, width, height, linewidth, edgecolor, facecolor)
    paint = Rectangle(((50/2)-6, 0), 12, 18.833333,fill=paint_fill, alpha=paint_alpha, lw=lw, edgecolor='Green')
    
    paint_boarder = Rectangle(((50/2)-6, 0), 12, 18.833333, fill=False, alpha=lines_alpha, lw=lw, edgecolor=lines_color)
    
    arc = Arc((50/2, 18.833333), 12, 12, theta1=-0, theta2=180, color=lines_color, lw=lw, alpha=lines_alpha)
    
    block1 = Rectangle(((50/2)-6-0.666, 7), 0.666, 1, fill=True, alpha=lines_alpha,lw=0, edgecolor=lines_color,facecolor=lines_color)
    
    block2 = Rectangle(((50/2)+6, 7), 0.666, 1, fill=True, alpha=lines_alpha,lw=0, edgecolor=lines_color, facecolor=lines_color)
    
    # add a patch 
    ax.add_patch(block1)
    ax.add_patch(block2)
    
    #lines on freethrow line
    
    l1 = Rectangle(((50/2)-6-0.666, 11), 0.666, 0.166,fill=True, alpha=lines_alpha,lw=0, edgecolor=lines_color, facecolor=lines_color)
   
    l2 = Rectangle(((50/2)-6-0.666, 14), 0.666, 0.166,fill=True, alpha=lines_alpha,lw=0, edgecolor=lines_color,facecolor=lines_color)
   
    l3 = Rectangle(((50/2)-6-0.666, 17), 0.666, 0.166,fill=True, alpha=lines_alpha,lw=0, edgecolor=lines_color,facecolor=lines_color)
    
    l4 = Rectangle(((50/2)+6, 11), 0.666, 0.166,fill=True, alpha=lines_alpha,lw=0, edgecolor=lines_color,facecolor=lines_color)
    
    l5 = Rectangle(((50/2)+6, 14), 0.666, 0.166,fill=True, alpha=lines_alpha,lw=0, edgecolor=lines_color,facecolor=lines_color)
    
    l6 = Rectangle(((50/2)+6, 17), 0.666, 0.166, fill=True, alpha=lines_alpha,lw=0, edgecolor=lines_color,facecolor=lines_color)
    
    ax.add_patch(l1)
    ax.add_patch(l2)
    ax.add_patch(l3)
    ax.add_patch(l4)
    ax.add_patch(l5)
    ax.add_patch(l6)
    
    
    # 3 Point Line !!!
    
    
