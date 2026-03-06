---
id: 19c__DBMS_ILM_ADMIN.CUSTOMIZE_ILM
name: DBMS_ILM_ADMIN.CUSTOMIZE_ILM
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ILM_ADMIN
tags: [dbms_ilm_admin]
source_file: DBMS_ILM_ADMIN.html
---

# DBMS_ILM_ADMIN.CUSTOMIZE_ILM

This procedure customizes environment for ILM execution by specifying the values for ILM execution related parameters. These values take effect for the next background scheduling.

## Syntax

```sql
DBMS_ILM_ADMIN.CUSTOMIZE_ILM  (
   parameter            IN       NUMBER,
   value                IN       NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| parameter | NUMBER | IN | One of the parameter constants defined in DBMS_ILM_ADMIN package |
| value | NUMBER) | IN | Value of parameter |

## Usage Notes

Syntax DBMS_ILM_ADMIN.CUSTOMIZE_ILM ( parameter IN NUMBER, value IN NUMBER); Parameters Table 87-5 CUSTOMIZE_ILM Procedure Parameters Parameter Description parameter One of the parameter constants defined in DBMS_ILM_ADMIN package value Value of parameter