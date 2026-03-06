---
id: 19c__DBMS_GOLDENGATE_ADM.REMOVE_AUTO_CDR_DELTA_RES
name: DBMS_GOLDENGATE_ADM.REMOVE_AUTO_CDR_DELTA_RES
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_GOLDENGATE_ADM
tags: [dbms_goldengate_adm]
source_file: DBMS_GOLDENGATE_ADM.html
---

# DBMS_GOLDENGATE_ADM.REMOVE_AUTO_CDR_DELTA_RES

This procedure removes Oracle GoldenGate automatic conflict detection and delta resolution for the column.

## Syntax

```sql
DBMS_GOLDENGATE_ADM.REMOVE_AUTO_CDR_DELTA_RES(
   schema_name IN VARCHAR2,
   table_name  IN VARCHAR2,
   column_name IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schema_name | VARCHAR2 | IN | The name of the table’s schema. |
| table_name | VARCHAR2 | IN | The name of the table. |
| column_name | VARCHAR2) | IN | The name of the column. |

## Usage Notes

Syntax DBMS_GOLDENGATE_ADM.REMOVE_AUTO_CDR_DELTA_RES( schema_name IN VARCHAR2, table_name IN VARCHAR2, column_name IN VARCHAR2); Parameters Table 76-12 REMOVE_AUTO_CDR_DELTA_RES Procedure Parameters Parameter Description schema_name The name of the table’s schema. table_name The name of the table. column_name The name of the column.