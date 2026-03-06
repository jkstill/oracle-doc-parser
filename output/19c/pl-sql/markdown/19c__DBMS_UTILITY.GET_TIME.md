---
id: 19c__DBMS_UTILITY.GET_TIME
name: DBMS_UTILITY.GET_TIME
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_UTILITY
tags: [dbms_utility]
source_file: DBMS_UTILITY.html
---

# DBMS_UTILITY.GET_TIME

This function determines the current time in hundredths of a second. This subprogram is primarily used for determining elapsed time. The subprogram is called twice – at the beginning and end of some process – and then the first (earlier) number is subtracted from the second (later) number to determine the time elapsed.

## Syntax

```sql
DBMS_UTILITY.GET_TIME 
  RETURN NUMBER;
```

**Returns:** `NUMBER`

## Usage Notes

Syntax DBMS_UTILITY.GET_TIME RETURN NUMBER; Return Values Time is the number of hundredths of a second from the point in time at which the subprogram is invoked. Usage Notes Numbers are returned in the range -2147483648 to 2147483647 depending on platform and machine, and your application must take the sign of the number into account in determining the interval. For instance, in the case of two negative numbers, application logic must allow that the first (earlier) number will be larger than the second (later) number which is closer to zero. By the same token, your application should also allow that the first (earlier) number be negative and the second (later) number be positive.