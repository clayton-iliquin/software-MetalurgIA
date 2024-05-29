import pandas as pd
import numpy as np


class HydroyclonMassBalance():
    """
    This Class contains different elements to execute hydrocyclon mass balances.
    """

    def __init__(self):
        pass

    def circulating_load_sol_method(self, sol_over, sol_under,sol_feed):
        """
        Return CC base on %sol hydrocyclon in feed, over and under streams.
        Transforms in to dilution rate each one and return a Circulating load
        in integers.
        """
        cc = (1/sol_over-1/sol_feed)/(1/sol_feed - 1/sol_under)

        return cc
    
    def hydrocyclon_balance_by_solid(self, feed_tms,feed_sg,solid_feed,solid_uf,solid_of):
        """
        This function calculate the mass balance in an hydrocyclon, generate three list of
        five elements heach one (TMS, % solids, TMA, density,TMP) for flows of OF, UF and Feed.
        """

        cc = self.circulating_load_sol_method(solid_of,solid_uf,solid_feed)
        # OF Balance
        of_TMS = feed_tms/(1+cc)
        of_solid = solid_of
        of_TMP = of_TMS/of_solid*100
        of_TMA = of_TMP - of_TMS
        of_VMP  = of_TMS/feed_sg + of_TMA
        of_density = of_TMP/of_VMP
        of_sol_vol = of_TMS/feed_sg/of_VMP*100


        of_balance = [of_TMS, of_TMA, of_TMP, of_VMP, of_density,of_sol_vol, of_solid]
        # UF Balance
        uf_TMS = of_TMS*cc
        uf_solid = solid_uf
        uf_TMP = uf_TMS/uf_solid*100
        uf_TMA = uf_TMP - uf_TMS
        uf_VMP = uf_TMS/feed_sg + uf_TMA
        uf_density = uf_TMP/uf_VMP
        uf_sol_vol = uf_TMS/feed_sg/uf_VMP*100

        uf_balance = [uf_TMS, uf_TMA, uf_TMP, uf_VMP, uf_density,uf_sol_vol, uf_solid]

        # Feed Balance 
        feed_TMS = feed_tms
        feed_sol = solid_feed
        feed_TMA = of_TMA + uf_TMA
        feed_TMP = of_TMP + uf_TMP
        feed_VMP = uf_VMP + of_VMP
        feed_sol_vol = feed_TMP/feed_VMP
        feed_density = feed_TMP/feed_VMP
        feed_sol_vol = feed_TMS/feed_sg/feed_VMP*100
        
        feed_balance = [feed_TMS, feed_TMA, feed_TMP, feed_VMP, feed_density,feed_sol_vol, feed_sol]

        return of_balance, uf_balance, feed_balance

    ## This code below could be an class to be more readable
    def hydrocyclon_mass_balance_simple_chart(self):
        """
        Create a matrix to display in 2_Hydrocyclon mass balance
        """
        tabular = pd.DataFrame({'Stream':['Ore (ton/hr)','Water (m3/hr)','Slurry (ton/hr)','Slurry (m3/hr)','Density (ton/m3)','%Solids (v/v)','%Solids (w/w)'],
                            'Feed':['','','','','','',''],
                            'OverFlow':['','','','','','',''],
                            'UnderFlow':['','','','','','','']})

        return tabular

    def hydrocyclon_mass_balance_simple(self, feed_tms,feed_rcc,feed_sg,uf_density,of_density,chart):
        """
        Take the chart from hydrocyclon_mass_balance and the calcs from hidrociclon_balance
        and returns a fill chart.
        """
        of_balance, uf_balance,feed_balance = self.hydrocyclon_balance_by_solid(feed_tms,feed_rcc,feed_sg,uf_density,of_density)

        chart.loc[:,'Feed'] = feed_balance
        chart.loc[:,'OverFlow'] =  of_balance
        chart.loc[:,'UnderFlow'] = uf_balance
        
def mass_balance_1_conc_1_elemet_chart(element,law):
    """
    Create a matrix to display in Metallurgical Balance App
    """
    tabular = pd.DataFrame({'Stream':['Feed','Concentrate','Tail'],
                        'Mass of Stream (Ton)':['','',''],
                        f'{element} Assay ({law})':['','',''],
                        f'Mass of {element}':['','',''],
                        '% Distribution':['','',''],
                        'Ratio':['','','']})

    return tabular 

def mass_balance_1_conc_1_element_calc(feed_ton, feed_humidity,feed_law,conc_law,tail_law,chart):
    """ 
    Responsible for generating the necessary calculations to execute the mass balance
    of 1 conc and load the values in mass_balance_1_conc_1_element_chart.
    """
    feed_tons_dry = feed_ton*((100-feed_humidity)/100)
    conc_ratio = (feed_law-tail_law)/(conc_law-tail_law)
    conc_tons_dry = feed_tons_dry*conc_ratio
    tail_tons_dry = feed_tons_dry - conc_ratio

    #entering data in a the chart. 
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


def mass_balance_2_conc_2_elemet_chart(element_1,element_2,law_1,law_2):
    """
    Create a matrix to display in Metallurgical Balance App
    """
    tabular = pd.DataFrame({'Stream':['Feed',f'Concentrate {element_1}',f'Concentrate {element_2}','Tail'],
                        'Mass of Stream (Ton)':['','','',''],
                        f'{element_1} Assay ({law_1})':['','','',''],
                        f'{element_2} Assay ({law_2})':['','','',''],
                        f'Mass of {element_1}':['','','',''],
                        f'Mass of {element_2}':['','','',''],
                        f'% Distribution {element_1}':['','','',''],
                        f'% Distribution {element_2}':['','','',''],
                        'Ratio':['','','','']})
    return tabular 

def solve_matrix(a,b):
    """
    Returns
    x -> array contain the solution of a^(-1)*b
    a -> matrix clean to use for mass_balance_n_conc_n_element_calc.

    """
    # calc x = a^(-1)*b use function
    if np.linalg.det(a) == 0:
        x = None
    else:
        x = np.linalg.solve(a,b)
    
    # matrix a transpose to use in chart 
    a = np.transpose(a)
    a = a[:,1:]

    # matrix x reshape to 1 row and x columns
    x = np.reshape(x,(1,-1))
    return a, x

def mass_balance_2_conc_2_elemet_calc(feed_ton, feed_humidity,feed_law_1, feed_law_2, conc_1_law_1, conc_1_law_2, conc_2_law_1, conc_2_law_2,tail_law_1,tail_law_2,chart):
    """ 
    Responsible for generating the necessary calculations for the mass balance 
    of 2 conc and load the values in mass_balance_2_conc_2_element_chart.

    Use the linear algorithm solve using matrix to solve.
    X = a^(-1)*b
    """
    feed_tons_dry = feed_ton*((100-feed_humidity)/100)
    a = np.array([[1,1,1],
    [conc_1_law_1,conc_2_law_1,tail_law_1],
    [conc_1_law_2,conc_2_law_2,tail_law_2]])
    b = np.array([1,feed_law_1,feed_law_2])
    
    a,x = solve_matrix(a,b)
    
    # entering data in a the chart. 
    chart.iloc[0,1] = feed_tons_dry
    chart.iloc[[1,2,3],1] = x*feed_tons_dry

    chart.iloc[0,2] = feed_law_1
    chart.iloc[0,3] = feed_law_2
    chart.iloc[[1,2,3],[2,3]] = a

    chart.iloc[:,4] =  chart.iloc[:,1]* chart.iloc[:,2]/100
    chart.iloc[:,5]=  chart.iloc[:,1]* chart.iloc[:,3]/100
    
    chart.iloc[0,6] = 100
    chart.iloc[0,7] = 100

    chart.iloc[[1,2,3],6] = chart.iloc[[1,2,3],4]/chart.iloc[0,4]*100
    chart.iloc[[1,2,3],7] = chart.iloc[[1,2,3],5]/chart.iloc[0,5]*100

    chart.iloc[1,8] = chart.iloc[0,1]/chart.iloc[1,1]
    chart.iloc[2,8] = chart.iloc[0,1]/chart.iloc[2,1]


def mass_balance_3_conc_3_elemet_chart(element_1,element_2,element_3,law_1,law_2,law_3):
    """
    Create a matrix to display in Metallurgycal Balance App for 3 concentrates.
    """
    tabular = pd.DataFrame({'Stream':['Feed',f'Concentrate {element_1}',f'Concentrate {element_2}',f'Concentrate {element_3}','Tail'],
                        'Mass of Stream (Ton)':['','','','',''],
                        f'{element_1} Assay ({law_1})':['','','','',''],
                        f'{element_2} Assay ({law_2})':['','','','',''],
                        f'{element_3} Assay ({law_3})':['','','','',''],
                        f'Mass of {element_1}':['','','','',''],
                        f'Mass of {element_2}':['','','','',''],
                        f'Mass of {element_3}':['','','','',''],
                        f'% Distribution {element_1}':['','','','',''],
                        f'% Distribution {element_2}':['','','','',''],
                        f'% Distribution {element_3}':['','','','',''],
                        'Ratio':['','','','','']})
    return tabular 




def mass_balance_3_conc_3_elemet_calc(feed_ton, feed_law_1, feed_law_2,feed_law_3, 
    conc_1_law_1, conc_1_law_2, conc_1_law_3, conc_2_law_1, conc_2_law_2, conc_2_law_3,
    conc_3_law_1, conc_3_law_2, conc_3_law_3,tail_law_1,tail_law_2, tail_law_3, chart):
    """ 
    Responsible for generating the necessary calculations to execute the mass balance
    of 3 conc and load the values in mass_balance_3_conc_3_element_chart.

    Use the linear algorithm solve using matrix to solve.
    X = a^(-1)*b
    """
    a = np.array([[1,1,1,1],
    [conc_1_law_1,conc_2_law_1,conc_3_law_1,tail_law_1],
    [conc_1_law_2,conc_2_law_2,conc_3_law_2,tail_law_2],
    [conc_1_law_3,conc_2_law_3,conc_3_law_3,tail_law_3]])

    b = np.array([1,feed_law_1,feed_law_2,feed_law_3])
    
    a,x = solve_matrix(a,b)
    
    #asing the data in a the chart. 
    chart.iloc[0,1] = feed_ton
    chart.iloc[[1,2,3,4],1] = x*feed_ton

    chart.iloc[0,2] = feed_law_1
    chart.iloc[0,3] = feed_law_2
    chart.iloc[0,4] = feed_law_3
    chart.iloc[[1,2,3,4],[2,3,4]] = a

    chart.iloc[:,5] =  chart.iloc[:,1]* chart.iloc[:,2]/100
    chart.iloc[:,6]=  chart.iloc[:,1]* chart.iloc[:,3]/100
    chart.iloc[:,7]=  chart.iloc[:,1]* chart.iloc[:,4]/100
    
    chart.iloc[0,[8,9,10]] = 100
  

    chart.iloc[[1,2,3,4],8] = chart.iloc[[1,2,3,4],5]/chart.iloc[0,5]*100
    chart.iloc[[1,2,3,4],9] = chart.iloc[[1,2,3,4],6]/chart.iloc[0,6]*100
    chart.iloc[[1,2,3,4],10] = chart.iloc[[1,2,3,4],7]/chart.iloc[0,7]*100

    chart.iloc[1,11] = chart.iloc[0,1]/chart.iloc[1,1]
    chart.iloc[2,11] = chart.iloc[0,1]/chart.iloc[2,1]
    chart.iloc[3,11] = chart.iloc[0,1]/chart.iloc[3,1]


class DirectGrinding():
    
    def __init__(self):
        pass

    def circulating_load_sol_method(self, sol_over, sol_under,sol_feed):
        """
        Return CC base on %sol hydrocyclon in feed, over and under streams.
        Transforms in to dilution rate each one and return a Circulating load
        in integers.
        """
        cc = (1/sol_over-1/sol_feed)/(1/sol_feed - 1/sol_under)

        return cc

    def chart_balance(self):
        """
        Chart use to show data of mass balance in grinding circuits.
        """

        tabular = pd.DataFrame({'Characteristic':['Ore (ton/hr)','Water (m3/hr)','Slurry (ton/hr)','Slurry (m3/hr)','Density (ton/m3)','%Solids (v/v)','%Solids (w/w)'],
        'Fresh Feed' : ['','','','','','',''],
        'Mill Feed': ['','','','','','',''],
        'Water to Mill' : ['','','','','','',''],
        'Mill Discharge' : ['','','','','','',''],
        'Water to Discharge' : ['','','','','','',''],
        'Cyclon Feed' : ['','','','','','',''],
        'Cyclon U\' flow' : ['','','','','','',''],
        'Cyclon O\' flow' : ['','','','','','','']
        })

        return tabular

    def mass_balance_direct_circuit(self, fresh_feed, moisture,specific_gravity,over_sol,under_sol,feed_sol,discharge_sol, chart):
        """
        This function recives:
        (fresh_feed = ton/hr, Moisture = %,Specific gravity, over_sol = %Sol in OverFlow of hidrocyclon
        under_sol = %Sol in UnderFlow of hidrocyclon, feed_sol = %Sol in Feed of hidrocyclon,
        discharge_sol = %Sol in discharge of Mill)

        And Returns the solution in the chart
        """
        # for Fresh Feed

        chart.iloc[0,1] = fresh_feed*(100-moisture)/100
        chart.iloc[2,1] = fresh_feed
        chart.iloc[1,1] = chart.iloc[2,1]-chart.iloc[0,1]
        chart.iloc[3,1] = chart.iloc[0,1]/specific_gravity + chart.iloc[1,1]
        chart.iloc[6,1] = chart.iloc[0,1]/chart.iloc[2,1]*100

        #for Overflow

        chart.iloc[0,8] = chart.iloc[0,1] # Ore ton/h
        chart.iloc[6,8] = over_sol # sol (w/w)
        chart.iloc[2,8] = chart.iloc[0,8]/chart.iloc[6,8] *100 #Slurty ton/h
        chart.iloc[1,8] = chart.iloc[2,8]-chart.iloc[0,8] # Wtaer m3/h
        chart.iloc[3,8] = chart.iloc[0,8]/specific_gravity + chart.iloc[1,8] #slurry m3/h
        
        # Circulating Charge
        cc = self.circulating_load_sol_method(over_sol, under_sol, feed_sol)
        
        # for UnderFlow

        chart.iloc[0,7] = chart.iloc[0,8]*cc # Oren Ton/h
        chart.iloc[6,7] = under_sol # %sol (w/w)
        chart.iloc[2,7] =  chart.iloc[0,7]/chart.iloc[6,7]*100 #Slurty ton/h
        chart.iloc[1,7] = chart.iloc[2,7]-chart.iloc[0,7] # Wtaer m3/h
        chart.iloc[3,7] = chart.iloc[0,7]/specific_gravity + chart.iloc[1,7] #slurry m3/h
       

        # mill feed (Underflow + Fress feed)

        chart.iloc[0:4,2] = chart.iloc[0:4,7] + chart.iloc[0:4,1] # Ore, slury ton/h and m3/h
        chart.iloc[6,2] = chart.iloc[0,2]/chart.iloc[2,2]*100

        # mill discharge 
        chart.iloc[0,4] = chart.iloc[0,2]# Oren Ton/h
        chart.iloc[6,4] = discharge_sol # %sol (w/w)
        chart.iloc[2,4] = chart.iloc[0,4]/discharge_sol*100 #Slurry ton/h
        chart.iloc[1,4] = chart.iloc[2,4] - chart.iloc[0,4] # Water Slurry m3/h
        chart.iloc[3,4] = chart.iloc[0,4]/specific_gravity + chart.iloc[1,4] #Slurry m3/h

        # cyclone feed 
        chart.iloc[0,6] = chart.iloc[0,2] # Oren Ton/h
        chart.iloc[1:4,6] = chart.iloc[1:4,7] + chart.iloc[1:4,8]
        chart.iloc[6,6] = feed_sol

        # water to Mill
        chart.iloc[0,3] = 0.0 # Ore Ton/h
        chart.iloc[6,3] = 0.0 # %Sol (w/w)
        chart.iloc[1,3] = chart.iloc[1,4]-chart.iloc[1,2]
        chart.iloc[2:4,3] = chart.iloc[1,3]

        # water to mill discharge
        chart.iloc[0,5] = 0.0 # Ore Ton/h
        chart.iloc[6,5] = 0.0 # %Sol (w/w)
        chart.iloc[1,5] = chart.iloc[1,8] - chart.iloc[1,1]-(chart.iloc[1,4]-chart.iloc[1,2])
        chart.iloc[2:4,5] = chart.iloc[1,5]
        # Density 
        chart.iloc[4,1:] = chart.iloc[2,1:]/chart.iloc[3,1:]
        # %Sol (v/v)
        chart.iloc[5,1:] = (chart.iloc[0,1:]/specific_gravity)/chart.iloc[3,1:]*100


class ReverseGrinding(DirectGrinding):
    def __init__(self):
        pass

    # I understood that this is not a good solution because only 3 cols 
    # change some calcs, but is the way that I know.
    def mass_balance_reverse_circuit(self, fresh_feed, moisture,specific_gravity,over_sol,under_sol,feed_sol,discharge_sol, chart):
        """
        This function recives:
        (fresh_feed = ton/hr, Moisture = %,Specific gravity, over_sol = %Sol in OverFlow of hidrocyclon
        under_sol = %Sol in UnderFlow of hidrocyclon, feed_sol = %Sol in Feed of hidrocyclon,
        discharge_sol = %Sol in discharge of Mill)

        And Returns the solution in the chart
        """
        # for Fresh Feed

        chart.iloc[0,1] = fresh_feed*(100-moisture)/100
        chart.iloc[2,1] = fresh_feed
        chart.iloc[1,1] = chart.iloc[2,1]-chart.iloc[0,1]
        chart.iloc[3,1] = chart.iloc[0,1]/specific_gravity + chart.iloc[1,1]
        chart.iloc[6,1] = chart.iloc[0,1]/chart.iloc[2,1]*100

        #for Overflow

        chart.iloc[0,8] = chart.iloc[0,1] # Ore ton/h
        chart.iloc[6,8] = over_sol # sol (w/w)
        chart.iloc[2,8] = chart.iloc[0,8]/chart.iloc[6,8] *100 #Slurty ton/h
        chart.iloc[1,8] = chart.iloc[2,8]-chart.iloc[0,8] # Wtaer m3/h
        chart.iloc[3,8] = chart.iloc[0,8]/specific_gravity + chart.iloc[1,8] #slurry m3/h
        
        # Circulating Charge
        cc = self.circulating_load_sol_method(over_sol, under_sol, feed_sol)
        
        # for UnderFlow

        chart.iloc[0,7] = chart.iloc[0,8]*cc # Oren Ton/h
        chart.iloc[6,7] = under_sol # %sol (w/w)
        chart.iloc[2,7] =  chart.iloc[0,7]/chart.iloc[6,7]*100 #Slurty ton/h
        chart.iloc[1,7] = chart.iloc[2,7]-chart.iloc[0,7] # Wtaer m3/h
        chart.iloc[3,7] = chart.iloc[0,7]/specific_gravity + chart.iloc[1,7] #slurry m3/h
       

        # mill feed (Underflow + Fress feed)

        chart.iloc[:,2] = chart.iloc[:,7] # Ore, slury ton/h and m3/h
        

        # mill discharge 
        chart.iloc[0,4] = chart.iloc[0,2]# Oren Ton/h
        chart.iloc[6,4] = discharge_sol # %sol (w/w)
        chart.iloc[2,4] = chart.iloc[0,4]/discharge_sol*100 #Slurry ton/h
        chart.iloc[1,4] = chart.iloc[2,4] - chart.iloc[0,4] # Water Slurry m3/h
        chart.iloc[3,4] = chart.iloc[0,4]/specific_gravity + chart.iloc[1,4] #Slurry m3/h

        # cyclone feed 
        chart.iloc[0,6] =  chart.iloc[0,7] + chart.iloc[0,8] # Oren Ton/h
        chart.iloc[1:4,6] = chart.iloc[1:4,7] + chart.iloc[1:4,8]
        chart.iloc[6,6] = feed_sol

        # water to Mill
        chart.iloc[0,3] = 0.0 # Ore Ton/h
        chart.iloc[6,3] = 0.0 # %Sol (w/w)
        chart.iloc[1,3] = chart.iloc[1,4]-chart.iloc[1,2]
        chart.iloc[2:4,3] = chart.iloc[1,3]

        # water to mill discharge
        chart.iloc[0,5] = 0.0 # Ore Ton/h
        chart.iloc[6,5] = 0.0 # %Sol (w/w)
        chart.iloc[1,5] = chart.iloc[1,8] - chart.iloc[1,1]-(chart.iloc[1,4]-chart.iloc[1,2])
        chart.iloc[2:4,5] = chart.iloc[1,5]
        # Density 
        chart.iloc[4,1:] = chart.iloc[2,1:]/chart.iloc[3,1:]
        # %Sol (v/v)
        chart.iloc[5,1:] = (chart.iloc[0,1:]/specific_gravity)/chart.iloc[3,1:]*100

        return chart

class DSagGrinding(ReverseGrinding):

    def __init__(self):
        pass

    def chart_d_sag_grinding(self):
        tabular = pd.DataFrame({'Characteristic':['Ore (ton/hr)','Water (m3/hr)','Slurry (ton/hr)','Slurry (m3/hr)','Density (ton/m3)','%Solids (v/v)','%Solids (w/w)'],
        'Fresh Feed' : ['','','','','','',''],
        'Water to SAG' : ['','','','','','',''],
        'SAG Disch.' : ['','','','','','',''],
        'Over Trommel' : ['','','','','','',''],
        'Under Trommel' : ['','','','','','',''],
        'Mill Feed': ['','','','','','',''],
        'Water to Mill' : ['','','','','','',''],
        'Mill Discharge' : ['','','','','','',''],
        'Water to Discharge' : ['','','','','','',''],
        'Cyclon Feed' : ['','','','','','',''],
        'Cyclon U\' flow' : ['','','','','','',''],
        'Cyclon O\' flow' : ['','','','','','','']
        })

        return tabular
    
    def mass_balance_d_sag(self, fresh_charge, moisture, spec_grav, sag_solid_discharge, cc_pebbles,moisture_pebbles,over_sol,under_sol,feed_sol,discharge_sol,chart):
        """
        For this balance I reuse some functions from Reverse grinding Class, 
        1. chart_balance: who returns a chart for calc the mass balance. (Heredatary by DirectGrinding)
        2. mass_balance_reverse_circuit to execute calcs to mass balance. 

        After that, I could merge the calcs in chart_d_sag_grinding() to display the final result. 

        """

        mall_bill_chart = self.chart_balance()

        ball_mill_balance = self.mass_balance_reverse_circuit(fresh_charge,moisture,spec_grav,over_sol,under_sol,feed_sol,discharge_sol, mall_bill_chart)

        # fill data 
        chart.iloc[:,6:13]  = ball_mill_balance.iloc[:,2:]
        chart.iloc[:,1] = ball_mill_balance.iloc[:,1]

        # Pebbles / Over Trommel
        chart.iloc[0,4] = chart.iloc[0,1]*cc_pebbles/100 # Ore Ton/h
        chart.iloc[1,4] = chart.iloc[0,4]*moisture_pebbles/(100-moisture_pebbles) # Water Slurry m3/h
        chart.iloc[2,4] = chart.iloc[0,4] + chart.iloc[1,4] # Slurry ton/h
        chart.iloc[6,4] = 100 - moisture_pebbles # %Sol w/w
        # chart.iloc[3,4] = chart.iloc[0,4]/spec_grav + chart.iloc[1,4] # Slurry m3/h

        # SAG Discharge
        chart.iloc[0,3] = chart.iloc[0,4] + chart.iloc[0,1] # Ore Ton/h
        chart.iloc[6,3] = sag_solid_discharge # %Sol w/w
        chart.iloc[2,3] = chart.iloc[0,3]/sag_solid_discharge*100 # Slurry ton/h
        chart.iloc[1,3] = chart.iloc[2,3] - chart.iloc[0,3] # Water Slurry m3/h
        # chart.iloc[3,3] = chart.iloc[0,3]/spec_grav + chart.iloc[1,3] # Slurry m3/h

        # Under Trommel
        chart.iloc[0,5] = chart.iloc[0,1]  # Ore Ton/h
        chart.iloc[1,5] = chart.iloc[1,3] - chart.iloc[1,4] # Water Slurry m3/h
        chart.iloc[2,5] = chart.iloc[1,5] + chart.iloc[0,5] # Slurry ton/h
        # chart.iloc[3,5] = chart.iloc[0,5]/spec_grav + chart.iloc[1,5] #Slurry m3/h
        chart.iloc[6,5] = chart.iloc[0,1]/chart.iloc[2,5]*100 # %Sol w/w

        # Slurry m3/h
        chart.iloc[3,3:6] = chart.iloc[0,3:6]/spec_grav + chart.iloc[1,3:6] # %Sol w/w

        # Water to SAG
        chart.iloc[1:4,2] = chart.iloc[3,3]-(chart.iloc[3,1]+chart.iloc[3,4])
        chart.iloc[0,2] = 0
        chart.iloc[6,2] = 0

        # Density 
        chart.iloc[4,2:6] = chart.iloc[2,2:6]/chart.iloc[3,2:6]
        # %Sol (v/v)
        chart.iloc[5,2:6] = (chart.iloc[0,2:6]/spec_grav)/chart.iloc[3,2:6]*100
        
        return chart