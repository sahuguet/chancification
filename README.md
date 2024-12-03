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

Here is a test set from Excel
* entity	10
* varId	7
* seed3	37
* seed4	1
```
1	0.54558909137267600
2	0.47917687788140000
3	0.81382024695631100
4	0.16771954821888400
5	0.88200610980857200
6	0.52571581501979400
7	0.07926920370664450
8	0.87031667365226900
9	0.01457489083986730
10	0.52163563633803300
```


### Python implementation
Here is a list of Python-based implementations:
* https://github.com/chrphb/hdr-random

We provide our own implementation in `hdr2.py`.

We test against 10 random values with count = 1..10, entity=12, varId=7, seed3=37 and seed4=1.
```
for i in range(1,11):
    print("%d,%s" %(i, str(hrd2(i, 10, 7, 37,1))))

1,0.5455890913726762
2,0.4791768778814003
3,0.8138202469563112
4,0.16771954821888357
5,0.8820061098085716
6,0.5257158150197938
7,0.07926920370664448
8,0.870316673652269
9,0.014574890839867294
10,0.5216356363380328
```

Python provides full precision numbers. Excel is limited to 15 digits.

### SQL implementation

We implement HRD2 using SQL (we are using DuckDB).
We preserve the original Excel formula by creation a `MOD` macro we can use.
We need to typecast integer value to `::BIGINT` to avoid buffer overflows. 

```
CREATE MACRO MOD(a,b) AS ( a % b);
CREATE MACRO hdr2(counter, varId:=0, entity:=0, seed3:=0, seed4:=0) AS
( MOD(( MOD( MOD( 999999999999989::BIGINT, MOD( counter*2499997::BIGINT + (varId)*1800451::BIGINT + (entity)*2000371::BIGINT + (seed3)*1796777::BIGINT + (seed4)*2299603::BIGINT, 7450589::BIGINT ) * 4658::BIGINT + 7450581::BIGINT ) * 383::BIGINT, 99991::BIGINT ) * 7440893::BIGINT + MOD( MOD( 999999999999989::BIGINT, MOD( counter*2246527::BIGINT + (varId)*2399993::BIGINT + (entity)*2100869::BIGINT + (seed3)*1918303::BIGINT + (seed4)*1624729::BIGINT, 7450987::BIGINT ) * 7580::BIGINT + 7560584::BIGINT ) * 17669::BIGINT, 7440893::BIGINT )) * 1343::BIGINT, 4294967296::BIGINT ) + 0.5 ) / 4294967296::BIGINT
```

And we can test the functiona as follows:
```
D SELECT counter, hdr2(counter, entity:=10, varId:=7, seed3:=37, seed4:=1) AS v
FROM (SELECT generate_series AS counter from generate_series(1,10));
┌─────────┬──────────────────────┐
│ counter │          v           │
│  int64  │        double        │
├─────────┼──────────────────────┤
│       1 │   0.5455890913726762 │
│       2 │   0.4791768778814003 │
│       3 │   0.8138202469563112 │
│       4 │  0.16771954821888357 │
│       5 │   0.8820061098085716 │
│       6 │   0.5257158150197938 │
│       7 │  0.07926920370664448 │
│       8 │    0.870316673652269 │
│       9 │ 0.014574890839867294 │
│      10 │   0.5216356363380328 │
├─────────┴──────────────────────┤
│ 10 rows              2 columns │
└────────────────────────────────┘
```

## Metalog generator (TODO)

We provide some code to generate Metalog random variables.