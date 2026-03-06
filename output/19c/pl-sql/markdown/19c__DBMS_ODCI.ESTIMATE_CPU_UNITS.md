---
id: 19c__DBMS_ODCI.ESTIMATE_CPU_UNITS
name: DBMS_ODCI.ESTIMATE_CPU_UNITS
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ODCI
tags: [dbms_odci]
source_file: DBMS_ODCI.html
---

# DBMS_ODCI.ESTIMATE_CPU_UNITS

This function returns the approximate number of CPU instructions (in thousands) corresponding to a specified time interval (in seconds). This information can be used to associate the CPU cost with a user-defined function for the extensible optimizer.

## Syntax

```sql
DBMS_ODCI.ESTIMATE_CPU_UNITS(
   elapsed_time     NUMBER) 
  RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| elapsed_time | NUMBER) | IN | The elapsed time in seconds that it takes to execute a function. |

**Returns:** `NUMBER`

## Usage Notes

The function takes as input the elapsed time of the user function, measures CPU units by multiplying the elapsed time by the processor speed of the machine, and returns the approximate number of CPU instructions that should be associated with the user function. For a multiprocessor machine, ESTIMATE_CPU_UNITS considers the speed of a single processor. Syntax DBMS_ODCI.ESTIMATE_CPU_UNITS( elapsed_time NUMBER) RETURN NUMBER; Parameters Parameter Description elapsed_time The elapsed time in seconds that it takes to execute a function. Usage Notes When associating CPU cost with a user-defined function, use the full number of CPU units rather than the number of thousands of CPU units returned by ESTIMATE_CPU_UNITS ; multiply the number returned by ESTIMATE_CPU_UNITS by 1,000.