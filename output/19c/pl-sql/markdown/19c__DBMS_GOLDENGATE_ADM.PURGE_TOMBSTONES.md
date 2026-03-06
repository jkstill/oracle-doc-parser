---
id: 19c__DBMS_GOLDENGATE_ADM.PURGE_TOMBSTONES
name: DBMS_GOLDENGATE_ADM.PURGE_TOMBSTONES
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_GOLDENGATE_ADM
tags: [dbms_goldengate_adm]
source_file: DBMS_GOLDENGATE_ADM.html
---

# DBMS_GOLDENGATE_ADM.PURGE_TOMBSTONES

This procedure purges rows that were deleted before the specified timestamp from the tombstone table.

## Syntax

```sql
DBMS_GOLDENGATE_ADM.PURGE_TOMBSTONES(
   purge_timestamp IN TIMESTAMP WITH TIME ZONE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| purge_timestamp | TIMESTAMP | IN | The timestamp before which records are purged. |

## Usage Notes

Syntax DBMS_GOLDENGATE_ADM.PURGE_TOMBSTONES( purge_timestamp IN TIMESTAMP WITH TIME ZONE); Parameters Table 76-9 PURGE_TOMBSTONES Procedure Parameters Parameter Description purge_timestamp The timestamp before which records are purged.