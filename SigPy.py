def add_significance_bars(ax, x1, x2, y, p_value, x_dodge=0, fontsize=12, 
                          linewidth=1, ns=True, asterisk=True, y_delta=True, significance_level=0.05):
    """Add significance bars to a plot.

    Args:
        ax (_type_):  Which axis to plot on.
        x1 (float): Start on x-axis.
        x2 (float): End on x-axis.
        y (float): Bar-height on y-axis.
        p_value (float): calculated p-value.
        x_dodge (int, optional): Dodge value of hue plots on x-axis. Defaults to 0.
        fontsize (int, optional): Fontsize of asterisk or p-value. Defaults to 14.
        linewidth (float, optional): Linewidth of bar.
        ns (bool, optional): If bar should be shown for non-significant values. Defaults to True.
        asterisk (bool, optional): If astersisk should be shown. If False, shows p-value instead. Defaults to True.
        y_delta (bool, optional): If bar should have downward brackets. Defaults to True.
        significance_level (float, optional): Level of significance. Defaults to 0.05.
    """   
    
    f = 6
    delta = (ax.get_yticks()[1] - ax.get_yticks()[0]) / f

    # Annotate with asterisks based on p-value
    if p_value < significance_level:
        if y_delta is True:
            y_f = 3
            y_delta = (ax.get_yticks()[1] - ax.get_yticks()[0]) / y_f
            ax.plot([x1 - (x_dodge/2), x1 - (x_dodge/2), x2 + (x_dodge/2), x2 + (x_dodge/2)], 
                [y - y_delta, y , y , y - y_delta], color='black', linewidth=linewidth)
        else:
            ax.plot([x1 - (x_dodge/2), x1 - (x_dodge/2), x2 + (x_dodge/2), x2 + (x_dodge/2)], 
                [y, y, y, y], color='black',linewidth=linewidth)
        if p_value <= 0.001:
            if asterisk is True:
                ax.text((x1 + x2) / 2, y + delta, '***', fontsize=fontsize, ha='center', fontname= "DejaVu Sans")
            else:
                ax.text((x1 + x2) / 2, y + delta, float('%.2g' % p_value), fontsize=fontsize, ha='center')
        elif p_value <= 0.01:
            if asterisk is True:                    
                ax.text((x1 + x2) / 2, y + delta, '**', fontsize=fontsize, ha='center', fontname= "DejaVu Sans")
            else:
                ax.text((x1 + x2) / 2, y + delta, float('%.2g' % p_value), fontsize=fontsize, ha='center')            
        elif p_value < significance_level:
            if asterisk is True:
                ax.text((x1 + x2) / 2, y + delta, '*', fontsize=fontsize, ha='center', fontname= "DejaVu Sans")
            else:
                ax.text((x1 + x2) / 2, y + delta, float('%.2g' % p_value), fontsize=fontsize, ha='center')
    elif p_value >= significance_level:
        if ns is True:
            if y_delta is True:
                y_f = 3
                y_delta = (ax.get_yticks()[1] - ax.get_yticks()[0]) / y_f
                ax.plot([x1 - (x_dodge/2), x1 - (x_dodge/2), x2 + (x_dodge/2), x2 + (x_dodge/2)], 
                        [y - y_delta, y , y , y - y_delta], color='black',linewidth=linewidth)
            else:
                ax.plot([x1 - (x_dodge/2), x1 - (x_dodge/2), x2 + (x_dodge/2), x2 + (x_dodge/2)], 
                        [y, y, y, y], color='black',linewidth=linewidth)            
            if asterisk is True:
                ax.text((x1 + x2) / 2, y + delta, 'ns', fontsize=fontsize, ha='center')
            else:
                ax.text((x1 + x2) / 2, y + delta, float('%.2g' % p_value), fontsize=fontsize, ha='center')  
        else:                
            print("Non-significant values not shown.")