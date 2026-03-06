---
id: 19c__DBMS_GOLDENGATE_ADM.ADD_AUTO_CDR_DELTA_RES
name: DBMS_GOLDENGATE_ADM.ADD_AUTO_CDR_DELTA_RES
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_GOLDENGATE_ADM
tags: [dbms_goldengate_adm]
source_file: DBMS_GOLDENGATE_ADM.html
---

# DBMS_GOLDENGATE_ADM.ADD_AUTO_CDR_DELTA_RES

This procedure configures Oracle GoldenGate automatic conflict detection and delta resolution for the column.

## Syntax

```sql
DBMS_GOLDENGATE_ADM.ADD_AUTO_CDR_DELTA_RES(
   schema_name IN VARCHAR2,
   table_name  IN VARCHAR2,
   column_name IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schema_name | VARCHAR2 | IN | The name of the table’s schema. |
| table_name | VARCHAR2 | IN | The name of the table. |
| column_name | VARCHAR2) | IN | The name of the column. The specified column must be a NUMBER or FLOAT data type column. The same column cannot be in a column group. |

## Usage Notes

The resolution method does not depend on a timestamp or an extra resolution column. With delta conflict resolution, the conflict is resolved by adding the difference between the new and old values in the LCR to the value in the table. For example, if a bank balance is updated at two sites concurrently, then the converged value accounts for all debits and credits. This resolution method is generally used for financial data such as an account balance. The procedure automatically places the column into an unconditional supplemental log group. Before this procedure can be run on a table, the DBMS_GOLDENGATE_ADM.ADD_AUTO_CDR procedure must be run in the table with ROW specified for the resolution_granularity parameter. Syntax DBMS_GOLDENGATE_ADM.ADD_AUTO_CDR_DELTA_RES( schema_name IN VARCHAR2, table_name IN VARCHAR2, column_name IN VARCHAR2); Parameters Table 76-4 ADD_AUTO_CDR_DELTA_RES Procedure Parameters Parameter Description schema_name The name of the table’s schema. table_name The name of the table. column_name The name of the column. The specified column must be a NUMBER or FLOAT data type column. The same column cannot be in a column group.