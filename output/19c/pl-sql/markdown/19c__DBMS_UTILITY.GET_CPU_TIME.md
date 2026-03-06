---
id: 19c__DBMS_UTILITY.GET_CPU_TIME
name: DBMS_UTILITY.GET_CPU_TIME
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_UTILITY
tags: [dbms_utility]
source_file: DBMS_UTILITY.html
---

# DBMS_UTILITY.GET_CPU_TIME

This function returns a measure of current CPU processing time in hundredths of a second. The difference between the times returned from two calls measures the CPU processing time (not the total elapsed time) between those two points.

## Syntax

```sql
DBMS_UTILITY.GET_CPU_TIME
   RETURN NUMBER;
```

**Returns:** `NUMBER`

## Usage Notes

Syntax DBMS_UTILITY.GET_CPU_TIME RETURN NUMBER; Return Values Time is the number of 100th's of a second from some arbitrary epoch. Usage Notes The amount of work performed is calculated by measuring the difference between a start point and end point for a particular operation.