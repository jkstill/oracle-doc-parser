---
id: 19c__DBMS_GOLDENGATE_ADM.ADD_AUTO_CDR_COLUMN_GROUP
name: DBMS_GOLDENGATE_ADM.ADD_AUTO_CDR_COLUMN_GROUP
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_GOLDENGATE_ADM
tags: [dbms_goldengate_adm]
source_file: DBMS_GOLDENGATE_ADM.html
---

# DBMS_GOLDENGATE_ADM.ADD_AUTO_CDR_COLUMN_GROUP

This procedure adds a column group to a table that is configured for Oracle GoldenGate automatic conflict detection and resolution.

## Syntax

```sql
DBMS_GOLDENGATE_ADM.ADD_AUTO_CDR_COLUMN_GROUP(
   schema_name             IN VARCHAR2,
   table_name              IN VARCHAR2,
   column_list             IN VARCHAR2,
   column_group_name       IN VARCHAR2 DEFAULT NULL,
   existing_data_timestamp IN TIMESTAMP WITH TIME ZONE DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schema_name | VARCHAR2 | IN | The name of the table’s schema. |
| table_name | VARCHAR2 | IN | The name of the table. |
| column_list | VARCHAR2 | IN | Group of columns for which the conflict detection and resolution is configured. Specify the columns in a comma-separated list. The same column cannot be in more than one column group. Also, the same column cannot be in a column group and specified in a delta resolution. |
| column_group_name | VARCHAR2 | IN | The name of the column group. If NULL , the column group name is system generated. |
| existing_data_timestamp | TIMESTAMP | IN | The time value for the added TIMESTAMP columns for existing table data. |

## Usage Notes

For a table that has been configured for timestamp conflict detection and resolution, this procedure adds a column group that includes a specified subset of columns in the table. Any columns in the table that are not part of a column group remain in the default column group for the table. When you add a column group to a table, conflict detection and resolution is performed on the columns in the column group separately from the other columns in the table. Column groups enable different databases to update different columns in the same row at nearly the same time without causing a conflict. For example, a replicated table that contains employee information might have a salary column and a bonus column as well as other columns that identify the employee and a location column for the employees office number. Assume that one department in the company updates its database to change the employee's salary while another department updates its database to change the employee's location. If the salary and bonus columns are in a column group, these changes are applied to the replicated table in each database without requiring conflict resolution. The procedure automatically places the columns in the column group into an unconditional supplemental log group, excluding nonscalar columns. Before this procedure can be run on a table, the DBMS_GOLDENGATE_ADM.ADD_AUTO_CDR procedure must be run in the table with ROW specified for the resolution_granularity parameter. Syntax DBMS_GOLDENGATE_ADM.ADD_AUTO_CDR_COLUMN_GROUP( schema_name IN VARCHAR2, table_name IN VARCHAR2, column_list IN VARCHAR2, column_group_name IN VARCHAR2 DEFAULT NULL, existing_data_timestamp IN TIMESTAMP WITH TIME ZONE DEFAULT NULL); Parameters Table 76-3 ADD_AUTO_CDR_COLUMN_GROUP Procedure Parameters Parameter Description schema_name The name of the table’s schema. table_name The name of the table. column_list Group of columns for which the conflict detection and resolution is configured. Specify the columns in a comma-separated list. The same column cannot be in more than one column group. Also, the same column cannot be in a column group and specified in a delta resolution. column_group_name The name of the column group. If NULL , the column group name is system generated. existing_data_timestamp The time value for the added TIMESTAMP columns for existing table data.