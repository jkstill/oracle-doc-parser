---
id: 19c__DBMS_AUDIT_MGMT.ALTER_PARTITION_INTERVAL
name: DBMS_AUDIT_MGMT.ALTER_PARTITION_INTERVAL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AUDIT_MGMT
tags: [dbms_audit_mgmt]
source_file: DBMS_AUDIT_MGMT.html
---

# DBMS_AUDIT_MGMT.ALTER_PARTITION_INTERVAL

This procedure changes the unified audit internal relational table's partition interval.

## Syntax

```sql
DBMS_AUDIT_MGMT.ALTER_PARTITION_INTERVAL(
   interval_number          IN BINARY_INTEGER,
   interval_frequency       IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| interval_number | BINARY_INTEGER | IN | Sets how often the database creates partitions for the unified audit internal relational table. For example, to specify that the partition is created every two days, you must enter 2 . |
| interval_frequency | VARCHAR2) | IN | Sets the frequency for the value that was set in the interval_number setting. For example, for a partition to be created every two days, with interval_number set to 2 , you must set interval_frequency to DAY . Supported values are YEAR , MONTH , and DAY . |

## Usage Notes

Syntax DBMS_AUDIT_MGMT.ALTER_PARTITION_INTERVAL( interval_number IN BINARY_INTEGER, interval_frequency IN VARCHAR2); Parameters Table 27-8 ALTER_PARTITION_INTERVAL Procedure Parameters Parameter Description interval_number Sets how often the database creates partitions for the unified audit internal relational table. For example, to specify that the partition is created every two days, you must enter 2 . interval_frequency Sets the frequency for the value that was set in the interval_number setting. For example, for a partition to be created every two days, with interval_number set to 2 , you must set interval_frequency to DAY . Supported values are YEAR , MONTH , and DAY . Usage Notes The interval frequency that you choose depends on the rate of audit records that are generated in your database. The default setting is for one month. If you have a high audit record rate and are using the default, then too many audit records may be generated in the same partition. In this case, you should change the interval frequency to a more frequent interval, such as one month or one day. If the audit record rate generation is not so high, then you may want to keep it at the default of one month. Example The following example sets the partition interval to occur every two months. BEGIN DBMS_AUDIT_MGMT.ALTER_PARTITION_INTERVAL( interval_number => 2, interval_frequency => 'MONTH'); END;