
def hidrociclon_balance(feed_tms,feed_rcc,feed_sg,uf_density,of_density):
    """
    Genera tres listas de 6 elemntos que representan el balance de masa en 
    el hidrociclon en over, under y feed 
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