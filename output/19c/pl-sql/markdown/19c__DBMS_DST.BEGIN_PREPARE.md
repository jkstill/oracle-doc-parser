---
id: 19c__DBMS_DST.BEGIN_PREPARE
name: DBMS_DST.BEGIN_PREPARE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DST
tags: [dbms_dst]
source_file: DBMS_DST.html
---

# DBMS_DST.BEGIN_PREPARE

This procedure starts a prepare window. Once a prepare window is started successfully, the database property ' DST_UPGRADE_STATE ' is set to ' PREPARE ', and the database property ' SECONDARY_TT_VERSION ' is set to a new timezone version.

## Syntax

```sql
DBMS_DST.BEGIN_PREPARE (
   new_version                IN  BINARY_INTEGER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| new_version | BINARY_INTEGER) | IN | New timezone version to which the database is to be prepared to upgrade |

## Usage Notes

The prepare window lets a DBA investigate data affected by the upgrade, and so judge when it is optimal to perform the upgrade. The prepare window can overlap normal database operation. Syntax DBMS_DST.BEGIN_PREPARE ( new_version IN BINARY_INTEGER); Parameters Table 65-3 BEGIN_PREPARE Procedure Parameters Parameter Description new_version New timezone version to which the database is to be prepared to upgrade