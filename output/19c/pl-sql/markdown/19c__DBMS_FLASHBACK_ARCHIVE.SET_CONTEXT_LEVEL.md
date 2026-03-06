---
id: 19c__DBMS_FLASHBACK_ARCHIVE.SET_CONTEXT_LEVEL
name: DBMS_FLASHBACK_ARCHIVE.SET_CONTEXT_LEVEL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_FLASHBACK_ARCHIVE
tags: [dbms_flashback_archive]
source_file: DBMS_FLASHBACK_ARCHIVE.html
---

# DBMS_FLASHBACK_ARCHIVE.SET_CONTEXT_LEVEL

This procedure defines how much of the user context is to be saved.

## Syntax

```sql
DBMS_FLASHBACK_ARCHIVE.SET_CONTEXT_LEVEL (
   level          VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| level | VARCHAR2) | IN | Depending on how much of the user context needs to be saved: ALL - the entire SYS_CONTEXT TYPICAL - the user ID, global user ID and the hostname NONE - nothing |

## Usage Notes

Syntax DBMS_FLASHBACK_ARCHIVE.SET_CONTEXT_LEVEL ( level VARCHAR2); Parameters Table 73-18 SET_CONTEXT_LEVEL Procedure Parameters Parameter Description level Depending on how much of the user context needs to be saved: ALL - the entire SYS_CONTEXT TYPICAL - the user ID, global user ID and the hostname NONE - nothing