---
id: 19c__DBMS_SPM.MIGRATE_STORED_OUTLINE
name: DBMS_SPM.MIGRATE_STORED_OUTLINE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SPM
tags: [dbms_spm]
source_file: DBMS_SPM.html
---

# DBMS_SPM.MIGRATE_STORED_OUTLINE

This function migrates stored outlines for one or more SQL statements to plan baselines in the SQL management base (SMB). Users can specify which stored outline(s) to be migrated based on outline name, SQL text, or outline category, or migrate all stored outlines in the system to SQL plan baselines.

## Syntax

```sql
DBMS_SPM.MIGRATE_STORED_OUTLINE (
   attribute_name     IN  VARCHAR2,
   attribute_value    IN  CLOB,
   fixed              IN  VARCHAR2 := 'NO')
 RETURN CLOB;

DBMS_SPM.MIGRATE_STORED_OUTLINE (
   outln_list         IN  DBMS_SPM.NAME_LIST,
   fixed              IN  VARCHAR2 := 'NO')
 RETURN CLOB;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| attribute_name | VARCHAR2 | IN | Specifies the type of parameter used in attribute_value to identify the migrated stored outlines. It is case insensitive. Possible values: outline_name sql_text category all |
| attribute_value | CLOB | IN | Based on attribute_name , this can be: Name of stored outline to be migrated SQL text of stored outlines to be migrated Category of stored outlines to be migrated NULL if attribute_name is all |
| fixed | VARCHAR2 | IN | NO (default) or YES . Specifies the "fixed" status of the plans generated during migration. By default, plans are generated as "non-fixed" plans. |
| outln_list | DBMS_SPM.NAME_LIST | IN | List of outline names to be migrated |

**Returns:** `CLOB`

## Usage Notes

This second overload of the function migrates stored outlines for one or more SQL statements to plan baselines in the SQL management base (SMB) given one or more outline names. Syntax DBMS_SPM.MIGRATE_STORED_OUTLINE ( attribute_name IN VARCHAR2, attribute_value IN CLOB, fixed IN VARCHAR2 := 'NO') RETURN CLOB; DBMS_SPM.MIGRATE_STORED_OUTLINE ( outln_list IN DBMS_SPM.NAME_LIST, fixed IN VARCHAR2 := 'NO') RETURN CLOB; Parameters Table 161-21 MIGRATE_STORED_OUTLINE Function Parameters Parameter Description attribute_name Specifies the type of parameter used in attribute_value to identify the migrated stored outlines. It is case insensitive. Possible values: outline_name sql_text category all attribute_value Based on attribute_name , this can be: Name of stored outline to be migrated SQL text of stored outlines to be migrated Category of stored outlines to be migrated NULL if attribute_name is all fixed NO (default) or YES . Specifies the "fixed" status of the plans generated during migration. By default, plans are generated as "non-fixed" plans. outln_list List of outline names to be migrated Return Values A CLOB containing a formatted report to describe the statistics during the migration, including: Number of stored outlines successfully migrated Number of stored outlines (and also the corresponding outline names) failed to be migrated and the reasons for the failure Usage Note When the user specifies an outline name, the function migrates stored outlines to plan baseline based on given outline name, which uniquely identifies a single stored outline to be migrated. When the user specifies SQL text, the function migrates all stored outlines created for a given SQL statement. A single SQL statement can have multiple stored outlines created for it under different category names. One plan baseline plan is created for each stored outline. The new plan baselines have category names set to DEFAULT . The module name of a plan baseline is set to be the same as the stored outline. When the user specifies a category name, the function migrates all stored outlines with the given category name. Only one stored outline exists per category per SQL statement. One plan baseline is created for each stored outline. When user specifies to migrate all , the function migrates all stored outlines in the system to plan baselines. One plan baseline is created for each stored outline.