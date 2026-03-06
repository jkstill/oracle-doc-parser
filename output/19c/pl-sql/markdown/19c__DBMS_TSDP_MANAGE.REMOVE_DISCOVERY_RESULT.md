---
id: 19c__DBMS_TSDP_MANAGE.REMOVE_DISCOVERY_RESULT
name: DBMS_TSDP_MANAGE.REMOVE_DISCOVERY_RESULT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_TSDP_MANAGE
tags: [dbms_tsdp_manage]
source_file: DBMS_TSDP_MANAGE.html
---

# DBMS_TSDP_MANAGE.REMOVE_DISCOVERY_RESULT

This procedure removes sensitive columns corresponding to an Application Data Model (ADM) from an Oracle Enterprise Manager Cloud Control instance.

## Syntax

```sql
DBMS_TSDP_MANAGE.REMOVE_DISCOVERY_RESULT (
  discovery_source     IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| discovery_source | VARCHAR2) | IN | Source of the import. In case of ADM, this should be the ADM name, the results of which is to be removed. |

## Usage Notes

Syntax DBMS_TSDP_MANAGE.REMOVE_DISCOVERY_RESULT ( discovery_source IN VARCHAR2); Parameters Table 181-10 REMOVE_DISCOVERY_RESULT Procedure Parameters Parameter Description discovery_source Source of the import. In case of ADM, this should be the ADM name, the results of which is to be removed. Examples Remove the sensitive columns corresponding to ADM instance, ADM_Demo : DBMS_TSDP_MANAGE.REMOVE_DISCOVERY_RESULT ( discovery_source => 'ADM_Demo');