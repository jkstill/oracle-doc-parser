---
id: 19c__DBMS_PART.CLEANUP_ONLINE_OP
name: DBMS_PART.CLEANUP_ONLINE_OP
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PART
tags: [dbms_part]
source_file: DBMS_PART.html
---

# DBMS_PART.CLEANUP_ONLINE_OP

There are many possible points of failure when performing ALTER TABLE ... MOVE PARTITION ... ONLINE operations. This procedure pro-actively cleans up such failed online move operations instead of waiting for the background process ( SMON ) to do so.

## Syntax

```sql
DBMS_PART.CLEANUP_ONLINE_OP (
   schema_name       IN   VARCHAR2 DEFAULT NULL,
   table_name        IN   VARCHAR2 DEFAULT NULL, 
   partition_name    IN   VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schema_name | VARCHAR2 | IN | Name of schema |
| table_name | VARCHAR2 | IN | Name of schema |
| partition_name | VARCHAR2 | IN | Name of partition |

## Usage Notes

Syntax DBMS_PART.CLEANUP_ONLINE_OP ( schema_name IN VARCHAR2 DEFAULT NULL, table_name IN VARCHAR2 DEFAULT NULL, partition_name IN VARCHAR2 DEFAULT NULL); Parameters Table 122-4 CLEANUP_ONLINE_OP Function Parameters Parameter Description schema_name Name of schema table_name Name of schema partition_name Name of partition Usage Notes If schema_name , table_name and partition_name are specified, this cleans up the failed online move operation for the specified partition. If schema_name and table_name are specified, this cleans up all failed online move operations for all the partitions of the specified table. If only schema_name is specified, this cleans up all failed online move operations in the schema. If no arguments are provided, we cleans up all the failed online move operations in the system. All other cases raise ORA-20000 to inform the user of invalid inputs as arguments.