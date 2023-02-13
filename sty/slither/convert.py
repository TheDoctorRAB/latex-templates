def Temperature(T, from_unit, to_unit):
    if from_unit == 'C':
        if to_unit == 'K':
            return T+273.15

    elif from_unit == 'K':
        if to_unit == 'C':
            return T-273.15

def Metric(value,from_prefix,to_prefix):
    exponent = {'k': 3,
                'M': 6}

    return value*10**(exponent[from_prefix]-exponent[to_prefix])
