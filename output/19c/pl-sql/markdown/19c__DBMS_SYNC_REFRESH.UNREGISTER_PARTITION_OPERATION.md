---
id: 19c__DBMS_SYNC_REFRESH.UNREGISTER_PARTITION_OPERATION
name: DBMS_SYNC_REFRESH.UNREGISTER_PARTITION_OPERATION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SYNC_REFRESH
tags: [dbms_sync_refresh]
source_file: DBMS_SYNC_REFRESH.html
---

# DBMS_SYNC_REFRESH.UNREGISTER_PARTITION_OPERATION

This procedure unregisters a partition-maintenance operation (PMOP) that had been previously registered with REGISTER_PARTITION_OPERATION on a base table. The three kinds of change operations that can be specified on partitions are DROP , TRUNCATE , and EXCHANGE .

## Syntax

```sql
DBMS_SYNC_REFRESH.UNREGISTER_PARTITION_OPERATION (
   partition_op     IN VARCHAR2,
   schema_name      IN VARCHAR2,
   base_table_name  IN VARCHAR2,
   partition_name   IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| partition_op | VARCHAR2 | IN | The name of the partition operation ( DROP , EXCHANGE , or TRUNCATE ). |
| schema_name | VARCHAR2 | IN | The name of the schema of the base table. |
| base_table_name | VARCHAR2 | IN | The name of the base table. |
| partition_name | VARCHAR2) | IN | The name of the partition to be changed; either exchanged with the outside partition table or dropped or truncated. |

## Usage Notes

Syntax DBMS_SYNC_REFRESH.UNREGISTER_PARTITION_OPERATION ( partition_op IN VARCHAR2, schema_name IN VARCHAR2, base_table_name IN VARCHAR2, partition_name IN VARCHAR2); Parameters Table 173-15 UNREGISTER_PARTITION_OPERATION Procedure Parameters Parameter Description partition_op The name of the partition operation ( DROP , EXCHANGE , or TRUNCATE ). schema_name The name of the schema of the base table. base_table_name The name of the base table. partition_name The name of the partition to be changed; either exchanged with the outside partition table or dropped or truncated.