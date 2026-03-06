---
id: 19c__DBMS_FLASHBACK.ENABLE_AT_TIME
name: DBMS_FLASHBACK.ENABLE_AT_TIME
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_FLASHBACK
tags: [dbms_flashback]
source_file: DBMS_FLASHBACK.html
---

# DBMS_FLASHBACK.ENABLE_AT_TIME

This procedure enables Flashback for the entire session.

## Syntax

```sql
DBMS_FLASHBACK.ENABLE_AT_TIME (
   query_time   IN TIMESTAMP);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| query_time | TIMESTAMP) | IN | This is an input parameter of type TIMESTAMP . A time stamp can be specified in the following ways: Using the TIMESTAMP constructor EXECUTE DBMS_FLASHBACK.ENABLE_AT_TIME(TIMESTAMP '2001-01-09 12:31:00'). Use the Globalization Support (NLS) format and supply a string. The format depends on the Globalization Support settings. Using the TO_TIMESTAMP function: EXECUTE DBMS_FLASHBACK.ENABLE_AT_TIME(TO_TIMESTAMP('12-02-2001 14:35:00', 'DD-MM-YYYY HH24:MI:SS')) You provide the format you want to use. This example shows the TO_TIMESTAMP function for February 12, 2001, 2:35 PM. If the time is omitted from query time, it defaults to the beginning of the day, that is, 12:00 A.M. Note that if the query time contains a time zone, the time zone information is truncated. |

## Usage Notes

The snapshot time is set to the SCN that most closely matches the time specified in query_time. It enables Flashback for the entire session. Syntax DBMS_FLASHBACK.ENABLE_AT_TIME ( query_time IN TIMESTAMP); Parameters Table 72-5 ENABLE_AT_TIME Procedure Parameters Parameter Description query_time This is an input parameter of type TIMESTAMP . A time stamp can be specified in the following ways: Using the TIMESTAMP constructor EXECUTE DBMS_FLASHBACK.ENABLE_AT_TIME(TIMESTAMP '2001-01-09 12:31:00'). Use the Globalization Support (NLS) format and supply a string. The format depends on the Globalization Support settings. Using the TO_TIMESTAMP function: EXECUTE DBMS_FLASHBACK.ENABLE_AT_TIME(TO_TIMESTAMP('12-02-2001 14:35:00', 'DD-MM-YYYY HH24:MI:SS')) You provide the format you want to use. This example shows the TO_TIMESTAMP function for February 12, 2001, 2:35 PM. If the time is omitted from query time, it defaults to the beginning of the day, that is, 12:00 A.M. Note that if the query time contains a time zone, the time zone information is truncated.