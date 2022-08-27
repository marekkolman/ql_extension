import pandas as pd

def combine_legs(*legs):
    '''
        Function combines multiple leg objects into a single leg
    '''
    if len(legs) == 1:
        return legs[0]
    else:
        joined_leg = ql.Leg()
        for leg in legs:
            for cf in leg:
                joined_leg.push_back(cf)
        return joined_leg
        
def explore_leg(leg) -> pd.DataFrame:
    '''
        Function shows a cash flow overview of a leg
    '''
    flds = ['date', 'amount', 'accrualDays', 'accrualEndDate', 'accrualPeriod', 'accrualStartDate', 'dayCounter',
            'exCouponDate', 'nominal', 'rate', 'referencePeriodEnd','referencePeriodStart']

    res = []
    for idx, cf in enumerate(list(map(ql.as_coupon, leg))):
        cf   = leg[idx] if not cf else cf # if as coupon was successful, take the coupon cf; if as coupon was not successful, use leg's cf
        vals = [getattr(cf, fld)() if hasattr(cf, fld) else None for fld in flds] # check if the cf has the function above and call it
        res.append(vals)

    return pd.DataFrame(res, columns = flds).dropna(axis = 1, how = 'all')