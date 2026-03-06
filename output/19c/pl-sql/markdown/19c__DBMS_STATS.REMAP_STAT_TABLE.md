---
id: 19c__DBMS_STATS.REMAP_STAT_TABLE
name: DBMS_STATS.REMAP_STAT_TABLE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.REMAP_STAT_TABLE

This procedure remaps the names of objects in the user statistics table. It allows you to import the statistics to objects with same definition but with different names.

## Syntax

```sql
DBMS_STATS.REMAP_STAT_TABLE (
   ownname    IN    VARCHAR2,
   stattab    IN    VARCHAR2, 
   src_own    IN    VARCHAR2, 
   src_tab    IN    VARCHAR2, 
   tgt_own    IN    VARCHAR2, 
   tgt_tab    IN    VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ownname | VARCHAR2 | IN | Owner of the statistics table. NULL means the current schema. |
| stattab | VARCHAR2 | IN | User statistics table identifier |
| src_own | VARCHAR2 | IN | Owner of the table to be renamed. This argument cannot be NULL . |
| src_tab | VARCHAR2 | IN | Name of the table to be renamed. If NULL , all tables are owned by src_own . |
| tgt_own | VARCHAR2 | IN | New name of the owner of the table. The owner name is also updated for the dependent objects such as columns and indexes. Note that an index of src_tab not owned by src_own is not renamed.This argument cannot be NULL . |
| tgt_tab | VARCHAR2) | IN | New name of the table. This argument is valid only if src_tab is not NULL . |

## Usage Notes

Syntax DBMS_STATS.REMAP_STAT_TABLE ( ownname IN VARCHAR2, stattab IN VARCHAR2, src_own IN VARCHAR2, src_tab IN VARCHAR2, tgt_own IN VARCHAR2, tgt_tab IN VARCHAR2); Parameters Table 171-97 REMAP_STAT_TABLE Procedure Parameters Parameter Description ownname Owner of the statistics table. NULL means the current schema. stattab User statistics table identifier src_own Owner of the table to be renamed. This argument cannot be NULL . src_tab Name of the table to be renamed. If NULL , all tables are owned by src_own . tgt_own New name of the owner of the table. The owner name is also updated for the dependent objects such as columns and indexes. Note that an index of src_tab not owned by src_own is not renamed.This argument cannot be NULL . tgt_tab New name of the table. This argument is valid only if src_tab is not NULL . Exceptions ORA-20000 : Insufficient privileges ORA-20001 : Invalid input Examples The following statement remaps all objects of sh to shsave in user statistics table sh.ustat : DBMS_STATS.REMAP_STAT_TABLE ('sh', 'ustat', 'sh', NULL, 'shsave', NULL); The following statement can be used to import statistics into objects of shsave once the preceding remap procedure is completed: DBMS_STATS.IMPORT_SCHEMA_STATS ('shsave', 'ustat', statown => 'sh'); The following statement remaps sh.customers to shsave.customers_sav : DBMS_STATS.REMAP_STAT_TABLE ('sh', 'ustat', 'sh', 'customers','shsave', 'customers_sav');