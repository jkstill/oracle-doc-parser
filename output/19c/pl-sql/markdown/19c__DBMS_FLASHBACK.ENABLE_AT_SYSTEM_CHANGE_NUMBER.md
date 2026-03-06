---
id: 19c__DBMS_FLASHBACK.ENABLE_AT_SYSTEM_CHANGE_NUMBER
name: DBMS_FLASHBACK.ENABLE_AT_SYSTEM_CHANGE_NUMBER
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_FLASHBACK
tags: [dbms_flashback]
source_file: DBMS_FLASHBACK.html
---

# DBMS_FLASHBACK.ENABLE_AT_SYSTEM_CHANGE_NUMBER

This procedure takes an SCN as an input parameter and sets the session snapshot to the specified number.

## Syntax

```sql
DBMS_FLASHBACK.ENABLE_AT_SYSTEM_CHANGE_NUMBER (
   query_scn IN NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| query_scn | NUMBER) | IN | The system change number (SCN), a version number for the database that is incremented on every transaction commit. |

## Usage Notes

In the Flashback mode, all queries return data consistent as of the specified wall-clock time or SCN. It enables Flashback for the entire session. Syntax DBMS_FLASHBACK.ENABLE_AT_SYSTEM_CHANGE_NUMBER ( query_scn IN NUMBER); Parameters Table 72-4 ENABLE_AT_SYSTEM_CHANGE_NUMBER Procedure Parameters Parameter Description query_scn The system change number (SCN), a version number for the database that is incremented on every transaction commit.