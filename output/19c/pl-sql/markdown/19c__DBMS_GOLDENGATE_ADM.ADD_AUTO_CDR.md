---
id: 19c__DBMS_GOLDENGATE_ADM.ADD_AUTO_CDR
name: DBMS_GOLDENGATE_ADM.ADD_AUTO_CDR
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_GOLDENGATE_ADM
tags: [dbms_goldengate_adm]
source_file: DBMS_GOLDENGATE_ADM.html
---

# DBMS_GOLDENGATE_ADM.ADD_AUTO_CDR

This procedure configures Oracle GoldenGate automatic conflict detection and resolution for a table.

## Syntax

```sql
DBMS_GOLDENGATE_ADM.ADD_AUTO_CDR(
   schema_name             IN VARCHAR2,
   table_name              IN VARCHAR2,
   resolution_granularity  IN VARCHAR2 DEFAULT 'ROW',
   existing_data_timestamp IN TIMESTAMP WITH TIME ZONE DEFAULT NULL,
   tombstone_deletes       IN BOOLEAN DEFAULT TRUE,
   fetchcols               IN BOOLEAN DEFAULT TRUE,
   record_conflicts        IN BOOLEAN DEFAULT FALSE,
   use_custom_handlers     IN BINARY_INTEGER DEFAULT 0);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schema_name | VARCHAR2 | IN | The name of the table’s schema. |
| table_name | VARCHAR2 | IN | The name of the table. |
| resolution_granularity | VARCHAR2 | IN | ROW , the default, adds one hidden TIMESTAMP column for the row and one hidden TIMESTAMP column for each LOB column. COLUMN adds one hidden TIMESTAMP column for each column in the table. |
| existing_data_timestamp | TIMESTAMP | IN | Timestamp to assign to existing rows. If NULL , then the current system timestamp is used. If a time is specified, and the operating system time zone is not a valid Oracle time zone, then Oracle uses UTC as the default value. |
| tombstone_deletes | BOOLEAN | IN | TRUE , the default, tracks deleted rows in a tombstone table. Tracking deleted rows might be required to detect and resolve some conflicts, but tracking deleted rows requires additional database resources. FALSE does not track deleted rows in a tombstone table. |
| fetchcols | BOOLEAN | IN | TRUE , the default, fetches the value of LOBs during conflict detection and resolution. Fetching LOBs can be an expensive operation. FALSE does not fetch the value of LOBs during conflict detection and resolution. |
| record_conflicts | BOOLEAN | IN | TRUE records the conflict in the DBA_APPLY_ERROR and DBA_APPLY_ERROR_MESSAGES views. FALSE , the default, does not record the conflict. |
| use_custom_handlers | BINARY_INTEGER | IN | 0 , the default, indicates that automatic conflict handlers are used. 1 indicates that automatic conflict handlers are not used and that a custom error handler must be specified using the SET_DML_HANDLER procedure in the DBMS_APPLY_ADM package. |

## Usage Notes

The conflict detection and resolution configured by this procedure is based on the timestamp of the changes. The procedure adds one or more hidden columns of TIMESTAMP type to the table, and each hidden column is counted against the limit of 1,000 columns for each table. The procedure automatically places the columns in the table into a default column group and into an unconditional supplemental log group, excluding nonscalar columns. To create column groups that include a subset of the columns in the table, use the ADD_AUTO_CDR_COLUMN_GROUP procedure in this package. Syntax DBMS_GOLDENGATE_ADM.ADD_AUTO_CDR( schema_name IN VARCHAR2, table_name IN VARCHAR2, resolution_granularity IN VARCHAR2 DEFAULT 'ROW', existing_data_timestamp IN TIMESTAMP WITH TIME ZONE DEFAULT NULL, tombstone_deletes IN BOOLEAN DEFAULT TRUE, fetchcols IN BOOLEAN DEFAULT TRUE, record_conflicts IN BOOLEAN DEFAULT FALSE, use_custom_handlers IN BINARY_INTEGER DEFAULT 0); Parameters Table 76-2 ADD_AUTO_CDR Procedure Parameters Parameter Description schema_name The name of the table’s schema. table_name The name of the table. resolution_granularity ROW , the default, adds one hidden TIMESTAMP column for the row and one hidden TIMESTAMP column for each LOB column. COLUMN adds one hidden TIMESTAMP column for each column in the table. existing_data_timestamp Timestamp to assign to existing rows. If NULL , then the current system timestamp is used. If a time is specified, and the operating system time zone is not a valid Oracle time zone, then Oracle uses UTC as the default value. tombstone_deletes TRUE , the default, tracks deleted rows in a tombstone table. Tracking deleted rows might be required to detect and resolve some conflicts, but tracking deleted rows requires additional database resources. FALSE does not track deleted rows in a tombstone table. fetchcols TRUE , the default, fetches the value of LOBs during conflict detection and resolution. Fetching LOBs can be an expensive operation. FALSE does not fetch the value of LOBs during conflict detection and resolution. record_conflicts TRUE records the conflict in the DBA_APPLY_ERROR and DBA_APPLY_ERROR_MESSAGES views. FALSE , the default, does not record the conflict. use_custom_handlers 0 , the default, indicates that automatic conflict handlers are used. 1 indicates that automatic conflict handlers are not used and that a custom error handler must be specified using the SET_DML_HANDLER procedure in the DBMS_APPLY_ADM package.