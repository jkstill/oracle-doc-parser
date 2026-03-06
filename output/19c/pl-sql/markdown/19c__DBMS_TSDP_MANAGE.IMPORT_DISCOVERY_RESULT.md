---
id: 19c__DBMS_TSDP_MANAGE.IMPORT_DISCOVERY_RESULT
name: DBMS_TSDP_MANAGE.IMPORT_DISCOVERY_RESULT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_TSDP_MANAGE
tags: [dbms_tsdp_manage]
source_file: DBMS_TSDP_MANAGE.html
---

# DBMS_TSDP_MANAGE.IMPORT_DISCOVERY_RESULT

This procedure can be used to import sensitive columns, along with the associated sensitive types, from an external source. The external source can be an Application Data Model (ADM) instance from Oracle Enterprise Manager Cloud Control.

## Syntax

```sql
DBMS_TSDP_MANAGE.IMPORT_DISCOVERY_RESULT (
  discovery_result         IN  CLOB,
  discovery_source         IN  VARCHAR2,
  force                    IN  FORCE DEFAULT FALSE); 

DBMS_TSDP_MANAGE.IMPORT_DISCOVERY_RESULT (
  discovery_result         IN  XMLTYPE,
  discovery_source         IN  VARCHAR2,
  force                    IN  FORCE DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| discovery_result | CLOB | IN | List of sensitive columns, along with the optional list of (the definitions of) the sensitive column types in XML format (possibly as a CLOB ). |
| discovery_source | VARCHAR2 | IN | Source of the import. The discovery_sourcename identifies the list of imported sensitive columns. In case of ADM, this should be the ADM name. |
| force | FORCE | IN | Specifies if the discovery result should be imported or not when the discovery result contains columns sensitive columns that are already identified as sensitive by another source. FALSE (default) - the discovery result will not be imported in case of conflicting columns. None of the columns and the sensitive types are imported. TRUE - the discovery result is imported and the attributes of the conflicting columns is set based on the incoming discovery result |

## Usage Notes

Syntax DBMS_TSDP_MANAGE.IMPORT_DISCOVERY_RESULT ( discovery_result IN CLOB, discovery_source IN VARCHAR2, force IN FORCE DEFAULT FALSE); DBMS_TSDP_MANAGE.IMPORT_DISCOVERY_RESULT ( discovery_result IN XMLTYPE, discovery_source IN VARCHAR2, force IN FORCE DEFAULT FALSE); Parameters Table 181-8 IMPORT_DISCOVERY_RESULT Procedure Parameters Parameter Description discovery_result List of sensitive columns, along with the optional list of (the definitions of) the sensitive column types in XML format (possibly as a CLOB ). discovery_source Source of the import. The discovery_sourcename identifies the list of imported sensitive columns. In case of ADM, this should be the ADM name. force Specifies if the discovery result should be imported or not when the discovery result contains columns sensitive columns that are already identified as sensitive by another source. FALSE (default) - the discovery result will not be imported in case of conflicting columns. None of the columns and the sensitive types are imported. TRUE - the discovery result is imported and the attributes of the conflicting columns is set based on the incoming discovery result Examples Import the list of sensitive columns of ADM instance, ADM_Demo : DBMS_TSDP_MANAGE.IMPORT_DISCOVERY_RESULT ( discovery_results => xml_adm_result, discovery_source => 'ADM_Demo');