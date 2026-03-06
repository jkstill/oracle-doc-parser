---
id: 19c__DBMS_TSDP_PROTECT.DISABLE_PROTECTION_TYPE
name: DBMS_TSDP_PROTECT.DISABLE_PROTECTION_TYPE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_TSDP_PROTECT
tags: [dbms_tsdp_protect]
source_file: DBMS_TSDP_PROTECT.html
---

# DBMS_TSDP_PROTECT.DISABLE_PROTECTION_TYPE

This procedure disables protection for a sensitive column type.

## Syntax

```sql
DBMS_TSDP_PROTECT.DISABLE_PROTECTION_TYPE (
   sensitive_type         IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| sensitive_type | VARCHAR2) | IN | Name of the sensitive column type |

## Usage Notes

Syntax DBMS_TSDP_PROTECT.DISABLE_PROTECTION_TYPE ( sensitive_type IN VARCHAR2); Parameters Table 182-8 DISABLE_PROTECTION_TYPE Procedure Parameters Parameter Description sensitive_type Name of the sensitive column type Examples Disable protection for all columns identified by SSN_TYPE : DBMS_TSDP_PROTECT.DISABLE_PROTECTION_TYPE ('SSN_TYPE');