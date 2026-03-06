---
id: 19c__DBMS_SPM.CREATE_STGTAB_BASELINE
name: DBMS_SPM.CREATE_STGTAB_BASELINE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SPM
tags: [dbms_spm]
source_file: DBMS_SPM.html
---

# DBMS_SPM.CREATE_STGTAB_BASELINE

This procedure creates a staging table used for transporting SQL plan baselines from one system to another.

## Syntax

```sql
DBMS_SPM.CREATE_STGTAB_BASELINE (
   table_name        IN VARCHAR2,
   table_owner       IN VARCHAR2 := NULL,
   tablespace_name   IN VARCHAR2 := NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| table_name | VARCHAR2 | IN | Name of staging table to create for the purpose of packing and unpacking SQL plan baselines |
| table_owner | VARCHAR2 | IN | Name of owner of the staging table. Default NULL means current schema is the table owner. |
| tablespace_name | VARCHAR2 | IN | Name of tablespace. Default NULL means create staging table in the default tablespace. |

## Usage Notes

Syntax DBMS_SPM.CREATE_STGTAB_BASELINE ( table_name IN VARCHAR2, table_owner IN VARCHAR2 := NULL, tablespace_name IN VARCHAR2 := NULL); Parameters Table 161-11 CREATE_STGTAB_BASELINE Procedure Parameters Parameter Description table_name Name of staging table to create for the purpose of packing and unpacking SQL plan baselines table_owner Name of owner of the staging table. Default NULL means current schema is the table owner. tablespace_name Name of tablespace. Default NULL means create staging table in the default tablespace. Usage Notes The creation of staging table is the first step. To migrate SQL plan baselines from one system to another, the user/DBA has to perform a series of steps as follows: Create a staging table in the source system Select SQL plan baselines in the source system and pack them into the staging table Export staging table into a flat file using Oracle EXP utility or Data Pump Transfer flat file to the target system Import staging table from the flat file using Oracle IMP utility or Data Pump Select SQL plan baselines from the staging table and unpack them into the target system