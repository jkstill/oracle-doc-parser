---
id: 19c__DBMS_SYNC_REFRESH.REGISTER_PARTITION_OPERATION
name: DBMS_SYNC_REFRESH.REGISTER_PARTITION_OPERATION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SYNC_REFRESH
tags: [dbms_sync_refresh]
source_file: DBMS_SYNC_REFRESH.html
---

# DBMS_SYNC_REFRESH.REGISTER_PARTITION_OPERATION

This procedure registers a partition-maintenance operation (PMOP) on a partition of a base table.

## Syntax

```sql
DBMS_SYNC_REFRESH.REGISTER_PARTITION_OPERATION (
   partition_op                IN VARCHAR2,
   schema_name                 IN VARCHAR2,
   base_table_name             IN VARCHAR2,
   partition_name              IN VARCHAR2,
   outside_partn_table_schema  IN VARCHAR2,
   outside_partn_table_name    IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| partition_op | VARCHAR2 | IN | The name of the partition operation ( DROP , EXCHANGE , or TRUNCATE ). |
| schema_name | VARCHAR2 | IN | The name of the schema of the base table. |
| base_table_name | VARCHAR2 | IN | The name of the base table. |
| partition_name | VARCHAR2 | IN | The name of the partition to be changed; either exchanged with the outside partition table or dropped or truncated. |
| outside_partn_table_schema | VARCHAR2 | IN | The name of the schema of the outside partition table (required for EXCHANGE only). |
| outside_partn_table_name | VARCHAR2) | IN | The name of the outside partition table (required for EXCHANGE only). |

## Usage Notes

Syntax DBMS_SYNC_REFRESH.REGISTER_PARTITION_OPERATION ( partition_op IN VARCHAR2, schema_name IN VARCHAR2, base_table_name IN VARCHAR2, partition_name IN VARCHAR2, outside_partn_table_schema IN VARCHAR2, outside_partn_table_name IN VARCHAR2); Parameters Table 173-13 REGISTER_PARTITION_OPERATION Procedure Parameters Parameter Description partition_op The name of the partition operation ( DROP , EXCHANGE , or TRUNCATE ). schema_name The name of the schema of the base table. base_table_name The name of the base table. partition_name The name of the partition to be changed; either exchanged with the outside partition table or dropped or truncated. outside_partn_table_schema The name of the schema of the outside partition table (required for EXCHANGE only). outside_partn_table_name The name of the outside partition table (required for EXCHANGE only). Usage Notes The three kinds of change operations that may be specified on partitions are DROP , TRUNCATE , and EXCHANGE . If DROP is specified, then the partition will be dropped from the base table at the time of EXECUTE_REFRESH . If TRUNCATE is specified, then the data from the partition will be deleted but the partition itself will not be dropped. These operations provide a more efficient way of specifying the deletes of all the rows in a partition than specifying them individually in the staging log. If EXCHANGE is specified, then the contents of the outside table is exchanged with contents of the specified partition of EXECUTE_REFRESH . This provides an alternative method to the user of providing the changes to the base tables instead of populating the staging log.