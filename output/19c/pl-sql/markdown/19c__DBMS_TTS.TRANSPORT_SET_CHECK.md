---
id: 19c__DBMS_TTS.TRANSPORT_SET_CHECK
name: DBMS_TTS.TRANSPORT_SET_CHECK
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_TTS
tags: [dbms_tts]
source_file: DBMS_TTS.html
---

# DBMS_TTS.TRANSPORT_SET_CHECK

This procedure checks if a set of tablespaces (to be transported) is self-contained. After calling this procedure, the user may select from a view to see a list of violations, if there are any.

## Syntax

```sql
DBMS_TTS.TRANSPORT_SET_CHECK (
   ts_list          IN CLOB, 
   incl_constraints IN BOOLEAN DEFAULT FALSE,
   full_check       IN BOOLEAN DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ts_list | CLOB | IN | List of one or more tablespaces, separated by comma. |
| incl_constraints | BOOLEAN | IN | TRUE if you want to count in referential integrity constraints when examining if the set of tablespaces is self-contained. (The incl_constraints parameter is a default so that TRANSPORT_SET_CHECK will work if it is called with only the ts_list argument.) |
| full_check | BOOLEAN | IN | Indicates whether a full or partial dependency check is required. If TRUE, treats all IN and OUT pointers (dependencies) and captures them as violations if they are not self-contained in the transportable set. The parameter should be set to TRUE for TSPITR or if a strict version of transportable is desired. By default the parameter is set to FALSE . It will only consider OUT pointers as violations. |

## Usage Notes

Syntax DBMS_TTS.TRANSPORT_SET_CHECK ( ts_list IN CLOB, incl_constraints IN BOOLEAN DEFAULT FALSE, full_check IN BOOLEAN DEFAULT FALSE); Parameters Table 183-2 TRANSPORT_SET_CHECK Procedure Parameters Parameter Description ts_list List of one or more tablespaces, separated by comma. incl_constraints TRUE if you want to count in referential integrity constraints when examining if the set of tablespaces is self-contained. (The incl_constraints parameter is a default so that TRANSPORT_SET_CHECK will work if it is called with only the ts_list argument.) full_check Indicates whether a full or partial dependency check is required. If TRUE, treats all IN and OUT pointers (dependencies) and captures them as violations if they are not self-contained in the transportable set. The parameter should be set to TRUE for TSPITR or if a strict version of transportable is desired. By default the parameter is set to FALSE . It will only consider OUT pointers as violations. Examples If the view does not return any rows, then the set of tablespaces is self-contained. For example, SQLPLUS> EXECUTE DBMS_TTS.TRANSPORT_SET_CHECK('foo,bar', TRUE); SQLPLUS> SELECT * FROM TRANSPORT_SET_VIOLATIONS;