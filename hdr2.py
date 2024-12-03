def MOD (n, m):
    return n % m

def hrd2(counter: int, entity: int, varId: int, seed3: int, seed4: int) -> float:
    """
    Computes the HDR2 random number for the given parameters.
    Based on the Excel formula referenced in the paper.
    We use the MOD function (defined above) to compute the modulo operation and keep the structure of original formula intact.
    """
    return ( MOD(( MOD( MOD( 999999999999989, MOD( counter*2499997 + (varId)*1800451 + (entity)*2000371 + (seed3)*1796777 + (seed4)*2299603, 7450589 ) * 4658 + 7450581 ) * 383, 99991 ) * 7440893 + MOD( MOD( 999999999999989, MOD( counter*2246527 + (varId)*2399993 + (entity)*2100869 + (seed3)*1918303 + (seed4)*1624729, 7450987 ) * 7580 + 7560584 ) * 17669, 7440893 )) * 1343, 4294967296 ) + 0.5 ) / 4294967296

if __name__ == "__main__":
    for i in range(1,11):
        print("%d,%s" %(i, str(hrd2(i, 10, 7, 37,1))))

