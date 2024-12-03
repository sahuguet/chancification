# Chancification

This is code related to SIP, Metalog, HDR2, from https://www.probabilitymanagement.org/ .


## Random number generator
HDR2 is a random number generator that is counter-based.
Details about HDR2 can be found at https://www.probabilitymanagement.org/hdr ,


The official Excel formula (from [the official Excel sheet](https://www.probabilitymanagement.org/s/HDR_2_0-Seed-Standard.xlsx)) is:
```
=( MOD(( MOD( MOD( 999999999999989, MOD( counter*2499997 + (varId)*1800451 + (entity)*2000371 + (seed3)*1796777 + (seed4)*2299603, 7450589 ) * 4658 + 7450581 ) * 383, 99991 ) * 7440893 + MOD( MOD( 999999999999989, MOD( counter*2246527 + (varId)*2399993 + (entity)*2100869 + (seed3)*1918303 + (seed4)*1624729, 7450987 ) * 7580 + 7560584 ) * 17669, 7440893 )) * 1343, 4294967296 ) + 0.5 ) / 4294967296
```

A translated version into an Excel Lambda is
```
=LAMBDA(_counter,[_varId],[_entity],[_seed3],[_seed4],
LET(
    varIdDefault, IF(ISOMITTED(_varId), 0, _varId),
    entityDefault, IF(ISOMITTED(_entity), 0, _entity),
    seed3Default, IF(ISOMITTED(_seed3), 0, _seed3),
    seed4Default, IF(ISOMITTED(_seed4), 0, _seed4),
( MOD(( MOD( MOD( 999999999999989, MOD( _counter*2499997 + (varIdDefault)*1800451 + (entityDefault)*2000371 + (seed3Default)*1796777 + (seed4Default)*2299603, 7450589 ) * 4658 + 7450581 ) * 383, 99991 ) * 7440893 + MOD( MOD( 999999999999989, MOD( _counter*2246527 + (varIdDefault)*2399993 + (entityDefault)*2100869 + (seed3Default)*1918303 + (seed4Default)*1624729, 7450987 ) * 7580 + 7560584 ) * 17669, 7440893 )) * 1343, 4294967296 ) + 0.5 ) / 4294967296
)
)
```

Here is a list of Python-based implementations:
* https://github.com/chrphb/hdr-random
