---
id: 19c__DBMS_STATS.COPY_TABLE_STATS
name: DBMS_STATS.COPY_TABLE_STATS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.COPY_TABLE_STATS

This procedure copies statistics of all dependent object such as columns and local indexes. If the statistics for source are not available then nothing is copied. It can optionally scale the statistics (such as the number of blks , or number of rows) based on the given scale_factor .

## Syntax

```sql
DBMS_STATS.COPY_TABLE_STATS (
   ownname          VARCHAR2, 
   tabname          VARCHAR2, 
   srcpartname      VARCHAR2,
   dstpartname      VARCHAR2, 
   scale_factor     VARCHAR2 DEFAULT 1,
   flags            NUMBER DEFAULT NULL,
   force            BOOLEAN DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ownname | VARCHAR2 | IN | Schema of the table of source and destination [sub] partitions |
| tabname | VARCHAR2 | IN | Table name of source and destination [sub] partitions |
| srcpartname | VARCHAR2 | IN | Source [sub] partition |
| dtspartname |  |  | Destination [sub] partition |
| scale_factor | VARCHAR2 | IN | Scale factor to scale nblks , nrows etc. in dstpartname |
| flags | NUMBER | IN | For internal Oracle use (should be left as NULL ) |
| force | BOOLEAN | IN | When value of this argument is TRUE copy statistics even if the destination [sub]partition is locked |

## Usage Notes

Syntax DBMS_STATS.COPY_TABLE_STATS ( ownname VARCHAR2, tabname VARCHAR2, srcpartname VARCHAR2, dstpartname VARCHAR2, scale_factor VARCHAR2 DEFAULT 1, flags NUMBER DEFAULT NULL, force BOOLEAN DEFAULT FALSE); Parameters Table 171-13 COPY_TABLE_STATS Procedure Parameters Parameter Description ownname Schema of the table of source and destination [sub] partitions tabname Table name of source and destination [sub] partitions srcpartname Source [sub] partition dtspartname Destination [sub] partition scale_factor Scale factor to scale nblks , nrows etc. in dstpartname flags For internal Oracle use (should be left as NULL ) force When value of this argument is TRUE copy statistics even if the destination [sub]partition is locked Security Model To invoke this procedure you must be owner of the table, or you need the ANALYZE ANY privilege. For objects owned by SYS , you need to be either the owner of the table, or you need the ANALYZE ANY DICTIONARY privilege or the SYSDBA privilege. Exceptions ORA-20000 : Invalid [sub]partition name ORA-20001 : Bad input value Usage Notes This procedure updates the minimum and maximum values of destination partition for the first partitioning column as follows: If the partitioning type is HASH , then the minimum and maximum values of the destination partition are same as that of the source partition. If the partitioning type is LIST , then the behavior depends on the setting of the destination partition: If the destination partition is a NOT DEFAULT partition, then the following statements are true: The minimum value of the destination partition is set to the minimum value of the value list that describes the destination partition. The maximum value of the destination partition is set to the maximum value of the value list that describes the destination partition. Alternatively, if the destination partition is a DEFAULT partition, then the following statements are true: The minimum value of the destination partition is set to the minimum value of the source partition. The maximum value of the destination partition is set to the maximum value of the source partition. If the partitioning type is RANGE , then the following statements are true: The minimum value of the destination partition is set to the high bound of previous partition unless the destination partition is the first partition. For the first partition, the minimum value is set to the high bound of the destination partition. The maximum value of the destination partition is set to the high bound of the destination partition unless the high bound of the destination partition is MAXVALUE , in which case the maximum value of the destination partition is set to the high bound of the previous partition. If the source partition column's minimum value is equal to its maximum value, and if both are equal to the source partition's lower bound, and if it has a single distinct value, then the destination partition column's minimum and maximum values are both set to the destination partition's lower bound. This is done for all partitioning columns. If the above condition does not apply, second and subsequent partitioning columns are updated as follows. The destination partition column's maximum value is set to the greater of the destination partition upper bound and the source partition column's maximum value, with one exception. If the destination partition is D and its preceding partition is D-1 and the key column to be adjusted is Cn , the maximum value for Cn is set to the upper bound of D (ignoring the maximum value of the source partition column) provided that the upper bounds of the previous key column Cn-1 are the same in partitions D and D-1 . If the minimum and maximum values are different for a column after modifications, and if the number of distinct values is less than 1, then the number of distinct values is updated as 2. If the source or destination is a partition of a composite partitioned table, then this procedure does not copy statistics of the underlying subpartitions.