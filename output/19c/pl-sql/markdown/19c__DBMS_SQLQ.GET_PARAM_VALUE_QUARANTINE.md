---
id: 19c__DBMS_SQLQ.GET_PARAM_VALUE_QUARANTINE
name: DBMS_SQLQ.GET_PARAM_VALUE_QUARANTINE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLQ
tags: [dbms_sqlq]
source_file: DBMS_SQLQ.html
---

# DBMS_SQLQ.GET_PARAM_VALUE_QUARANTINE

This function returns the quarantine threshold for a resource specified in a quarantine configuration.

## Syntax

```sql
DBMS_SQLQ.GET_PARAM_VALUE_QUARANTINE (
   quarantine_name   IN VARCHAR2,
   parameter_name    IN VARCHAR2)
RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| quarantine_name | VARCHAR2 | IN | Name of the quarantine configuration. |
| parameter_name | VARCHAR2) | IN | Resource for which the quarantine threshold needs to be retrieved. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_SQLQ.GET_PARAM_VALUE_QUARANTINE ( quarantine_name IN VARCHAR2, parameter_name IN VARCHAR2) RETURN VARCHAR2; Parameters Table 167-7 GET_PARAM_VALUE_QUARANTINE Function Parameters Parameter Description quarantine_name Name of the quarantine configuration. parameter_name Resource for which the quarantine threshold needs to be retrieved. Return Value Returns the quarantine threshold for a resource specified in a quarantine configuration. Examples The following example returns the quarantine threshold for CPU time specified in the quarantine configuration having the name SQL_QUARANTINE_3z0mwuq3aqsm8cfe7a0e4 . DECLARE quarantine_config_setting_value VARCHAR2(30); BEGIN quarantine_config_setting_value := DBMS_SQLQ.GET_PARAM_VALUE_QUARANTINE( QUARANTINE_NAME => 'SQL_QUARANTINE_3z0mwuq3aqsm8cfe7a0e4', PARAMETER_NAME => 'CPU_TIME'); END; /