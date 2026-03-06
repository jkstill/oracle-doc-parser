---
id: 19c__DBMS_SPD.PACK_STGTAB_DIRECTIVE
name: DBMS_SPD.PACK_STGTAB_DIRECTIVE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SPD
tags: [dbms_spd]
source_file: DBMS_SPD.html
---

# DBMS_SPD.PACK_STGTAB_DIRECTIVE

This function packs (exports) SQL plan directives into a staging table.

## Syntax

```sql
DBMS_SPD.PACK_STGTAB_DIRECTIVE (
   table_name         IN VARCHAR2,
   table_owner        IN VARCHAR2  := USER
   directive_id       IN NUMBER    := NULL,
   obj_list           IN OBJECTTAB := NULL) 
 RETURN NUMBER
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| table_name | VARCHAR2 | IN | Name of staging table |
| table_owner | VARCHAR2 | IN | Name of schema owner of staging table. Default is current schema. |
| directive_id | NUMBER | IN | SQL plan directive ID. Default NULL means all directives in the system. |
| obj_list | OBJECTTAB | IN | Used to filter the directives to be packed based on the objects used in directives. If obj_list is not NULL , a directive is packed only if all the objects in the directive exist in obj_list . |

**Returns:** `NUMBER`

## Usage Notes

Syntax DBMS_SPD.PACK_STGTAB_DIRECTIVE ( table_name IN VARCHAR2, table_owner IN VARCHAR2 := USER directive_id IN NUMBER := NULL, obj_list IN OBJECTTAB := NULL) RETURN NUMBER Parameters Table 160-6 PACK_STGTAB_DIRECTIVE Function Parameters Parameter Description table_name Name of staging table table_owner Name of schema owner of staging table. Default is current schema. directive_id SQL plan directive ID. Default NULL means all directives in the system. obj_list Used to filter the directives to be packed based on the objects used in directives. If obj_list is not NULL , a directive is packed only if all the objects in the directive exist in obj_list . Return Values Number of SQL plan directives packed. Exceptions ORA-38171 INSUFFICIENT_PRIVILEGE : The user does not have proper privilege to perform the operation. ORA-28104 INVALID_INPUT : The input value is not valid. ORA-44001 INVALID_SCHEMA : The input schema does not exist. ORA-29304 INVALID_STGTAB : The specified staging table is invalid or does not exist. ORA-13158 OBJECT_DOES_NOT_EXIST : The specified object does not exist. Usage Notes The ADMINISTER SQL MANAGEMENT OBJECT privilege is required to execute this procedure.