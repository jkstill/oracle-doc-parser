---
id: 19c__DBMS_UTILITY.GET_TZ_TRANSITIONS
name: DBMS_UTILITY.GET_TZ_TRANSITIONS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_UTILITY
tags: [dbms_utility]
source_file: DBMS_UTILITY.html
---

# DBMS_UTILITY.GET_TZ_TRANSITIONS

This procedure returns time zone transitions by regionid from the timezone.dat file.

## Syntax

```sql
DBMS_UTILITY.GET_TZ_TRANSITIONS 
   regionid      IN     NUMBER,
   transitions   OUT    MAXRAW);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| regionid | NUMBER | IN | Number corresponding to the region |
| transitions | MAXRAW) | OUT | Raw bytes from the timezone.dat file |

## Usage Notes

Syntax DBMS_UTILITY.GET_TZ_TRANSITIONS regionid IN NUMBER, transitions OUT MAXRAW); Parameters Table 187-24 GET_TZ_TRANSITIONS Procedure Parameters Parameter Description regionid Number corresponding to the region transitions Raw bytes from the timezone.dat file Exceptions Table 187-25 GET_TZ_TRANSITIONS Procedure Exceptions Exception Description ORA-6502: PL/SQL: NUMERIC OR VALUE ERROR For an invalid regionid