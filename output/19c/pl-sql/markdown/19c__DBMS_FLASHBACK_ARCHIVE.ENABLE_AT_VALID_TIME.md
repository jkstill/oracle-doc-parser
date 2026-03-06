---
id: 19c__DBMS_FLASHBACK_ARCHIVE.ENABLE_AT_VALID_TIME
name: DBMS_FLASHBACK_ARCHIVE.ENABLE_AT_VALID_TIME
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_FLASHBACK_ARCHIVE
tags: [dbms_flashback_archive]
source_file: DBMS_FLASHBACK_ARCHIVE.html
---

# DBMS_FLASHBACK_ARCHIVE.ENABLE_AT_VALID_TIME

This procedure enables session level valid time flashback.

## Syntax

```sql
DBMS_FLASHBACK_ARCHIVE.ENABLE_AT_VALID_TIME (
   level          IN    VARCHAR2, 
   query_time     IN    TIMESTAMP DEFAULT SYSTIMESTAMP);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| level | VARCHAR2 | IN | Options: All - Sets the visibility of temporal data to the full table, which is the default temporal table visibility CURRENT - Sets the visibility of temporal data to currently valid data within the valid time period at the session level ASOF - Sets the visibility of temporal data to data valid as of the given time as defined by the timestamp |
| query_time | TIMESTAMP | IN | Used only if level is ASOF . Data which is valid at this query_time will only be shown. |

## Usage Notes

Syntax DBMS_FLASHBACK_ARCHIVE.ENABLE_AT_VALID_TIME ( level IN VARCHAR2, query_time IN TIMESTAMP DEFAULT SYSTIMESTAMP); Parameters Table 73-10 ENABLE_AT_VALID_TIME Procedure Parameters Parameter Description level Options: All - Sets the visibility of temporal data to the full table, which is the default temporal table visibility CURRENT - Sets the visibility of temporal data to currently valid data within the valid time period at the session level ASOF - Sets the visibility of temporal data to data valid as of the given time as defined by the timestamp query_time Used only if level is ASOF . Data which is valid at this query_time will only be shown.