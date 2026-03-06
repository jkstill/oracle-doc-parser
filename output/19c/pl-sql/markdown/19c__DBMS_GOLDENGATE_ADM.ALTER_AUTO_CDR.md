---
id: 19c__DBMS_GOLDENGATE_ADM.ALTER_AUTO_CDR
name: DBMS_GOLDENGATE_ADM.ALTER_AUTO_CDR
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_GOLDENGATE_ADM
tags: [dbms_goldengate_adm]
source_file: DBMS_GOLDENGATE_ADM.html
---

# DBMS_GOLDENGATE_ADM.ALTER_AUTO_CDR

This procedure alters the Oracle GoldenGate automatic conflict detection and resolution for a table.

## Syntax

```sql
DBMS_GOLDENGATE_ADM.ALTER_AUTO_CDR(
   schema_name             IN VARCHAR2,
   table_name              IN VARCHAR2,
   tombstone_deletes       IN BOOLEAN DEFAULT NULL,
   fetchcols               IN BOOLEAN DEFAULT NULL,
   record_conflicts        IN BOOLEAN DEFAULT NULL,
   use_custom_handlers     IN BINARY_INTEGER DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schema_name | VARCHAR2 | IN | The name of the table’s schema. |
| table_name | VARCHAR2 | IN | The name of the table. |
| tombstone_deletes | BOOLEAN | IN | TRUE tracks deleted rows in a tombstone table. Tracking deleted rows might be required to detect and resolve some conflicts, but tracking deleted rows requires additional database resources. FALSE does not track deleted rows in a tombstone table. NULL retains the current setting for the parameter. |
| fetchcols | BOOLEAN | IN | TRUE fetches the value of nonscalar columns during conflict detection and resolution. FALSE does not fetch the value of nonscalar columns during conflict detection and resolution. NULL retains the current setting for the parameter. |
| record_conflicts | BOOLEAN | IN | TRUE records the conflict. FALSE does not record the conflict. NULL retains the current setting for the parameter. |
| use_custom_handlers | BINARY_INTEGER | IN | 0 indicates that automatic conflict handlers are used. 1 indicates that automatic conflict handlers are not used and that a custom error handler must be specified using the SET_DML_HANDLER procedure in the DBMS_APPLY_ADM package. NULL , the default, retains the current setting for the parameter. |

## Usage Notes

Syntax DBMS_GOLDENGATE_ADM.ALTER_AUTO_CDR( schema_name IN VARCHAR2, table_name IN VARCHAR2, tombstone_deletes IN BOOLEAN DEFAULT NULL, fetchcols IN BOOLEAN DEFAULT NULL, record_conflicts IN BOOLEAN DEFAULT NULL, use_custom_handlers IN BINARY_INTEGER DEFAULT NULL); Parameters Table 76-5 ALTER_AUTO_CDR Procedure Parameters Parameter Description schema_name The name of the table’s schema. table_name The name of the table. tombstone_deletes TRUE tracks deleted rows in a tombstone table. Tracking deleted rows might be required to detect and resolve some conflicts, but tracking deleted rows requires additional database resources. FALSE does not track deleted rows in a tombstone table. NULL retains the current setting for the parameter. fetchcols TRUE fetches the value of nonscalar columns during conflict detection and resolution. FALSE does not fetch the value of nonscalar columns during conflict detection and resolution. NULL retains the current setting for the parameter. record_conflicts TRUE records the conflict. FALSE does not record the conflict. NULL retains the current setting for the parameter. use_custom_handlers 0 indicates that automatic conflict handlers are used. 1 indicates that automatic conflict handlers are not used and that a custom error handler must be specified using the SET_DML_HANDLER procedure in the DBMS_APPLY_ADM package. NULL , the default, retains the current setting for the parameter.