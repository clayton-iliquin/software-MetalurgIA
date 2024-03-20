import pandas as pd

def hidrociclon_balance(feed_tms,feed_rcc,feed_sg,uf_density,of_density):
    """
    This function calculate the mass balance in an hidrociclon, generate three list of
    five elements heach one (TMS, % soldis, TMA, density,TMP) for flows of OF, UF and Feed.
    """

    # OF Balance
    of_TMS = round(feed_tms,2)
    of_density = round(of_density,2)
    of_solid = round((100*(of_density-1))/(of_density*(1-(1/feed_sg))),2)
    of_TMA = round((of_TMS/of_solid)*(100-of_solid),2)
    of_TMP = of_TMS + of_TMA
    
    of_balance = [of_TMS, of_solid, of_TMA, of_density,of_TMP]

    # UF Balance
    uf_TMS = round(feed_tms*(feed_rcc/100),2)
    uf_density = round(uf_density,2)
    uf_solid = round((100*(uf_density-1))/(uf_density*(1-(1/feed_sg))),2)
    uf_TMA = round((uf_TMS/uf_solid)*(100-uf_solid),2)
    uf_TMP = round(uf_TMS +  uf_TMA,2)
    
    uf_balance = [uf_TMS, uf_solid, uf_TMA, uf_density, uf_TMP]

    # Feed Balance 
    feed_TMS = round(feed_tms*((feed_rcc/100)+1),2)
    feed_TMA = uf_TMA + of_TMA
    feed_sol = round(feed_TMS/(feed_TMA+feed_TMS)*100,2)
    feed_TMP = feed_TMS + feed_TMA
    feed_density = round(1/(((feed_sol/100)/feed_sg)+1-(feed_sol/100)),2)

    feed_balance = [feed_TMS, feed_sol, feed_TMA, feed_density, feed_TMP]

    return of_balance, uf_balance, feed_balance

## This code below could be an class to be more readable

        
def mass_balance_1_conc_1_elemet_chart(element,law):
    """
    Create a matrix to display in Metallurgycal Balance App
    """
    tabular = pd.DataFrame({'Stream':['Feed','Concentrate','Tail'],
                        'Mass of Stream (Ton)':['','',''],
                        f'{element} Assay ({law})':['','',''],
                        f'Mass of {element}':['','',''],
                        'Distribution':['','',''],
                        'Ratio':['','','']})

    return tabular 

def mass_balance_1_conc_1_element_calc(feed_ton, feed_humidity,feed_law,conc_law,tail_law,chart):
    """ 
    
    """
    feed_tons_dry = feed_ton*((100-feed_humidity)/100)
    conc_ratio = (feed_law-tail_law)/(conc_law-tail_law)
    conc_tons_dry = feed_tons_dry*conc_ratio
    tail_tons_dry = feed_tons_dry - conc_ratio

    #asing the data in a the chart. 
    chart.iloc[0,1] = float(feed_tons_dry)
    chart.iloc[1,1] = float(conc_tons_dry)
    chart.iloc[2,1] = float(tail_tons_dry)
    
    chart.iloc[0,2] = float(feed_law)
    chart.iloc[1,2] = float(conc_law)
    chart.iloc[2,2] = float(tail_law)

    chart.iloc[:,3] = chart.iloc[:,1]*chart.iloc[:,2]

    chart.iloc[0,4] = 100
    chart.iloc[1,4] = 100*(chart.iloc[1,3]/chart.iloc[0,3])
    chart.iloc[2,4] = 100 - chart.iloc[1,4]

    chart.iloc[1,5] = round(conc_ratio,4)