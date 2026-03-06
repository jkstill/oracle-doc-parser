---
id: 19c__DBMS_TSDP_PROTECT.DISABLE_PROTECTION_SOURCE
name: DBMS_TSDP_PROTECT.DISABLE_PROTECTION_SOURCE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_TSDP_PROTECT
tags: [dbms_tsdp_protect]
source_file: DBMS_TSDP_PROTECT.html
---

# DBMS_TSDP_PROTECT.DISABLE_PROTECTION_SOURCE

This procedure disables protection based on the source of truth for the sensitive columns.

## Syntax

```sql
DBMS_TSDP_PROTECT.DISABLE_PROTECTION_SOURCE (
   discovery_sourcename      IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| discovery_sourcename | VARCHAR2) | IN | Name of the discovery source. This could be the Application Data Model (ADM) name or the database user. |

## Usage Notes

Syntax DBMS_TSDP_PROTECT.DISABLE_PROTECTION_SOURCE ( discovery_sourcename IN VARCHAR2); Parameters Table 182-7 DISABLE_PROTECTION_SOURCE Procedure Parameters Parameter Description discovery_sourcename Name of the discovery source. This could be the Application Data Model (ADM) name or the database user. Examples Disable protection for all columns corresponding to ADM_Demo : DBMS_TSDP_PROTECT.DISABLE_PROTECTION_SOURCE ('ADM_Demo');