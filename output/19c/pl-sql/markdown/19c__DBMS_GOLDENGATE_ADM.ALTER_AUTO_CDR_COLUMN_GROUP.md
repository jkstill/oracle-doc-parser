---
id: 19c__DBMS_GOLDENGATE_ADM.ALTER_AUTO_CDR_COLUMN_GROUP
name: DBMS_GOLDENGATE_ADM.ALTER_AUTO_CDR_COLUMN_GROUP
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_GOLDENGATE_ADM
tags: [dbms_goldengate_adm]
source_file: DBMS_GOLDENGATE_ADM.html
---

# DBMS_GOLDENGATE_ADM.ALTER_AUTO_CDR_COLUMN_GROUP

This procedure alters a column group for Oracle GoldenGate automatic conflict detection and resolution.

## Syntax

```sql
DBMS_GOLDENGATE_ADM.ALTER_AUTO_CDR_COLUMN_GROUP(
   schema_name        IN VARCHAR2,
   table_name         IN VARCHAR2,
   column_group_name  IN VARCHAR2,
   add_column_list    IN VARCHAR2,
   remove_column_list IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schema_name | VARCHAR2 | IN | The name of the table’s schema. |
| table_name | VARCHAR2 | IN | The name of the table. |
| column_group_name | VARCHAR2 | IN | The name of the column group. |
| add_column_list | VARCHAR2 | IN | A comma-separated list of columns to add to the column group. |
| remove_column_list | VARCHAR2) | IN | A comma-separated list of columns to remove from the column group. |

## Usage Notes

Syntax DBMS_GOLDENGATE_ADM.ALTER_AUTO_CDR_COLUMN_GROUP( schema_name IN VARCHAR2, table_name IN VARCHAR2, column_group_name IN VARCHAR2, add_column_list IN VARCHAR2, remove_column_list IN VARCHAR2); Parameters Table 76-6 ALTER_AUTO_CDR_COLUMN_GROUP Procedure Parameters Parameter Description schema_name The name of the table’s schema. table_name The name of the table. column_group_name The name of the column group. add_column_list A comma-separated list of columns to add to the column group. remove_column_list A comma-separated list of columns to remove from the column group.