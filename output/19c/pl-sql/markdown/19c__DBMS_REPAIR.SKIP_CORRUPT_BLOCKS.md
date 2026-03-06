---
id: 19c__DBMS_REPAIR.SKIP_CORRUPT_BLOCKS
name: DBMS_REPAIR.SKIP_CORRUPT_BLOCKS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_REPAIR
tags: [dbms_repair]
source_file: DBMS_REPAIR.html
---

# DBMS_REPAIR.SKIP_CORRUPT_BLOCKS

This procedure enables or disables the skipping of corrupt blocks during index and table scans of the specified object.

## Syntax

```sql
DBMS_REPAIR.SKIP_CORRUPT_BLOCKS (
   schema_name  IN VARCHAR2,
   object_name  IN VARCHAR2,
   object_type  IN BINARY_INTEGER DEFAULT TABLE_OBJECT,
   flags        IN BINARY_INTEGER DEFAULT SKIP_FLAG);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schema_name | VARCHAR2 | IN | Schema name of the object to be processed. |
| object_name | VARCHAR2 | IN | Name of the object. |
| object_type | BINARY_INTEGER | IN | Type of the object to be processed. This must be either TABLE_OBJECT (default) or CLUSTER_OBJECT . See " Constants " . |
| flags | BINARY_INTEGER | IN | If SKIP_FLAG is specified, then it turns on the skip of software corrupt blocks for the object during index and table scans. If NOSKIP_FLAG is specified, then scans that encounter software corrupt blocks return an ORA - 1578 . See " Constants " . |

## Usage Notes

When the object is a table, skip applies to the table and its indexes. When the object is a cluster, it applies to all of the tables in the cluster, and their respective indexes. Note: When Oracle performs an index range scan on a corrupt index after DBMS_REPAIR.SKIP_CORRUPT_BLOCKS has been set for the base table, corrupt branch blocks and root blocks are not skipped. Only corrupt non-root leaf blocks are skipped. Note: When Oracle performs an index range scan on a corrupt index after DBMS_REPAIR.SKIP_CORRUPT_BLOCKS has been set for the base table, corrupt branch blocks and root blocks are not skipped. Only corrupt non-root leaf blocks are skipped. Syntax DBMS_REPAIR.SKIP_CORRUPT_BLOCKS ( schema_name IN VARCHAR2, object_name IN VARCHAR2, object_type IN BINARY_INTEGER DEFAULT TABLE_OBJECT, flags IN BINARY_INTEGER DEFAULT SKIP_FLAG); Parameters Table 140-11 SKIP_CORRUPT_BLOCKS Procedure Parameters Parameter Description schema_name Schema name of the object to be processed. object_name Name of the object. object_type Type of the object to be processed. This must be either TABLE_OBJECT (default) or CLUSTER_OBJECT . See " Constants " . flags If SKIP_FLAG is specified, then it turns on the skip of software corrupt blocks for the object during index and table scans. If NOSKIP_FLAG is specified, then scans that encounter software corrupt blocks return an ORA - 1578 . See " Constants " .