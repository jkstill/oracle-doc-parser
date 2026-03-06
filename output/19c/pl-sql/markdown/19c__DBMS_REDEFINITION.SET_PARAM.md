---
id: 19c__DBMS_REDEFINITION.SET_PARAM
name: DBMS_REDEFINITION.SET_PARAM
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_REDEFINITION
tags: [dbms_redefinition]
source_file: DBMS_REDEFINITION.html
---

# DBMS_REDEFINITION.SET_PARAM

This procedure sets a new value for a specified parameter used by the redefinition process identified by a redefinition ID.

## Syntax

```sql
DBMS_REDEFINITION.SET_PARAM (
   redefinition_id  IN  VARCHAR2,
   param_name       IN  VARCHAR2,
   param_value      IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| redefinition_id | VARCHAR2 | IN | The redefinition ID that identifies the redefinition process |
| param_name | VARCHAR2 | IN | The parameter name |
| param_value | VARCHAR2) | IN | The new parameter value |

## Usage Notes

Note: Currently, the only value that can be changed by this procedure is the value for the of the refresh_dep_mviews parameter that is specified in the REDEF_TABLE procedure or the START_REDEF_TABLE procedure. You can determine the redefinition ID and check the value of the refresh_dep_mviews parameter for an online table redefinition operation by querying the DBA_REDEFINITION_STATUS view. Note: Currently, the only value that can be changed by this procedure is the value for the of the refresh_dep_mviews parameter that is specified in the REDEF_TABLE procedure or the START_REDEF_TABLE procedure. You can determine the redefinition ID and check the value of the refresh_dep_mviews parameter for an online table redefinition operation by querying the DBA_REDEFINITION_STATUS view. Syntax DBMS_REDEFINITION.SET_PARAM ( redefinition_id IN VARCHAR2, param_name IN VARCHAR2, param_value IN VARCHAR2); Parameters Table 138-13 SET_PARAM Procedure Parameters Parameter Description redefinition_id The redefinition ID that identifies the redefinition process param_name The parameter name param_value The new parameter value See Also: Oracle Database Administrator's Guide