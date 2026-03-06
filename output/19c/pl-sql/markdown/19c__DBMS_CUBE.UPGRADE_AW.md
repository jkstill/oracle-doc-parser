---
id: 19c__DBMS_CUBE.UPGRADE_AW
name: DBMS_CUBE.UPGRADE_AW
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CUBE
tags: [dbms_cube]
source_file: DBMS_CUBE.html
---

# DBMS_CUBE.UPGRADE_AW

This procedure creates an Oracle OLAP 12 c analytic workspace from a copy of the metadata contained in an OLAP 10 g analytic workspace. The original OLAP 10 g analytic workspace is not affected and can exist at the same time and in the same schema as the OLAP 12 c analytic workspace.

## Syntax

```sql
DBMS_CUBE.UPGRADE_AW
       (sourceaw              IN  VARCHAR2,
        destaw                IN  VARCHAR2,
        upgoptions            IN  CLOB DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| sourceaw | VARCHAR2 | IN | The name of a 10 g analytic workspace. |
| destaw | VARCHAR2 | IN | A new name for the generated 12 c analytic workspace. It cannot be the same as sourceaw . |
| upgoptions | CLOB | IN | One or more of these upgrade options, as a string in the form ' OPTION = VALUE '. Separate multiple options with commas. PRESERVE_TABLE_OWNERS : YES preserves the original source table mappings. Use this option when creating an OLAP 12 c analytic workspace in a different schema from the 10 g analytic workspace, and you want the new objects mapped to tables in the original schema. (Default) NO removes the schema owner from the source table mappings. Use this option when creating an OLAP 12 c analytic workspace in a different schema from the 10 g analytic workspace, and you want the new objects mapped to tables in the destination schema. RENAME_TABLE : The name of a table that specifies new names for objects as they are created in OLAP 12 c format. These changes are in addition to those specified by the INITIALIZE_CUBE_UPGRADE procedure. See " CREATE_IMPORT_OPTIONS Procedure " for information about creating a rename table. TARGET_VERSION : The version of the upgrade, specified by a 2- to 5-part number, such as 11.2 or 11.2.0.2.0. If you enter an unsupported version number, then the closest version below it is used. |

## Usage Notes

UPGRADE_AW automatically runs INITIALIZE_CUBE_UPGRADE if the CUBE_UPGRADE_INFO table does not exist. If it does exist, then UPGRADE_AW does not overwrite it, thus preserving any changes you made to the table. See " DBMS_CUBE - Upgrading 10g Analytic Workspaces " . Syntax DBMS_CUBE.UPGRADE_AW (sourceaw IN VARCHAR2, destaw IN VARCHAR2, upgoptions IN CLOB DEFAULT NULL); Parameters Table 44-14 UPGRADE_AW Procedure Parameters Parameter Description sourceaw The name of a 10 g analytic workspace. destaw A new name for the generated 12 c analytic workspace. It cannot be the same as sourceaw . upgoptions One or more of these upgrade options, as a string in the form ' OPTION = VALUE '. Separate multiple options with commas. PRESERVE_TABLE_OWNERS : YES preserves the original source table mappings. Use this option when creating an OLAP 12 c analytic workspace in a different schema from the 10 g analytic workspace, and you want the new objects mapped to tables in the original schema. (Default) NO removes the schema owner from the source table mappings. Use this option when creating an OLAP 12 c analytic workspace in a different schema from the 10 g analytic workspace, and you want the new objects mapped to tables in the destination schema. RENAME_TABLE : The name of a table that specifies new names for objects as they are created in OLAP 12 c format. These changes are in addition to those specified by the INITIALIZE_CUBE_UPGRADE procedure. See " CREATE_IMPORT_OPTIONS Procedure " for information about creating a rename table. TARGET_VERSION : The version of the upgrade, specified by a 2- to 5-part number, such as 11.2 or 11.2.0.2.0. If you enter an unsupported version number, then the closest version below it is used. Examples This example upgrades an OLAP 10 g analytic workspace named GLOBAL10 to an OLAP 12 c analytic workspace named GLOBAL12 , using a rename table named MY_OBJECT_MAP : BEGIN -- Upgrade the analytic workspace dbms_cube.upgrade_aw(sourceaw =>'GLOBAL10', destaw => 'GLOBAL12', upgoptions => 'RENAME_TABLE=MY_OBJECT_MAP'); -- Load and aggregate the data dbms_cube.build(script=>'UNITS_CUBE, PRICE_AND_COST_CUBE'); END; /