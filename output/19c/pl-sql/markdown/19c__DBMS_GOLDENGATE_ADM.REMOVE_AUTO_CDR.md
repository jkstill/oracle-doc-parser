---
id: 19c__DBMS_GOLDENGATE_ADM.REMOVE_AUTO_CDR
name: DBMS_GOLDENGATE_ADM.REMOVE_AUTO_CDR
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_GOLDENGATE_ADM
tags: [dbms_goldengate_adm]
source_file: DBMS_GOLDENGATE_ADM.html
---

# DBMS_GOLDENGATE_ADM.REMOVE_AUTO_CDR

This procedure removes Oracle GoldenGate automatic conflict detection and resolution for a table.

## Syntax

```sql
DBMS_GOLDENGATE_ADM.REMOVE_AUTO_CDR(
   schema_name             IN VARCHAR2,
   table_name              IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schema_name | VARCHAR2 | IN | The name of the table’s schema. |
| table_name | VARCHAR2) | IN | The name of the table. |

## Usage Notes

Syntax DBMS_GOLDENGATE_ADM.REMOVE_AUTO_CDR( schema_name IN VARCHAR2, table_name IN VARCHAR2); Parameters Table 76-10 REMOVE_AUTO_CDR Procedure Parameters Parameter Description schema_name The name of the table’s schema. table_name The name of the table.