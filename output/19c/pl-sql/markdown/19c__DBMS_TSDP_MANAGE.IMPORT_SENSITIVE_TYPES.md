---
id: 19c__DBMS_TSDP_MANAGE.IMPORT_SENSITIVE_TYPES
name: DBMS_TSDP_MANAGE.IMPORT_SENSITIVE_TYPES
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_TSDP_MANAGE
tags: [dbms_tsdp_manage]
source_file: DBMS_TSDP_MANAGE.html
---

# DBMS_TSDP_MANAGE.IMPORT_SENSITIVE_TYPES

This procedure imports a list of sensitive column types from a source.

## Syntax

```sql
DBMS_TSDP_MANAGE.IMPORT_SENSITIVE_TYPES (
  sensitive_types        IN CLOB,
  source                 IN VARCHAR2);  

DBMS_TSDP_MANAGE.IMPORT_SENSITIVE_TYPES (
  sensitive_types        IN XMLTYPE,
  source                 IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| sensitive_types | CLOB | IN | List of sensitive column types in XML Format (possibly as a CLOB ) |
| source | VARCHAR2) | IN | Source of the import. The source identifies the list of imported sensitive column types. In case of Application Data Model (ADM) from an Oracle Enterprise Manager Cloud Control instance, this should be the ADM name. |

## Usage Notes

Syntax DBMS_TSDP_MANAGE.IMPORT_SENSITIVE_TYPES ( sensitive_types IN CLOB, source IN VARCHAR2); DBMS_TSDP_MANAGE.IMPORT_SENSITIVE_TYPES ( sensitive_types IN XMLTYPE, source IN VARCHAR2); Parameters Table 181-9 IMPORT_SENSITIVE_TYPES Procedure Parameters Parameter Description sensitive_types List of sensitive column types in XML Format (possibly as a CLOB ) source Source of the import. The source identifies the list of imported sensitive column types. In case of Application Data Model (ADM) from an Oracle Enterprise Manager Cloud Control instance, this should be the ADM name. Examples Import the list of sensitive column types of ADM instance, ADM_Demo : DBMS_TSDP_MANAGE.IMPORT_SENSITIVE_TYPES ( sensitive_types => xml_adm_result, source => 'ADM_Demo');