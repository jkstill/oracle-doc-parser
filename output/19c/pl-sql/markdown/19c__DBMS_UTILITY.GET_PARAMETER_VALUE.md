---
id: 19c__DBMS_UTILITY.GET_PARAMETER_VALUE
name: DBMS_UTILITY.GET_PARAMETER_VALUE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_UTILITY
tags: [dbms_utility]
source_file: DBMS_UTILITY.html
---

# DBMS_UTILITY.GET_PARAMETER_VALUE

This deprecated function gets the value of specified init.ora parameter.

## Syntax

```sql
DBMS_UTILITY.GET_PARAMETER_VALUE (
   parnam     IN        VARCHAR2,
   intval     IN OUT    BINARY_INTEGER,
   strval     IN OUT    VARCHAR2,
   listno     IN        BINARY_INTEGER DEFAULT 1)
  RETURN BINARY_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| parnam | VARCHAR2 | IN | Parameter name |
| intval | BINARY_INTEGER | IN OUT | Value of an integer parameter or the value length of a string parameter |
| strval | VARCHAR2 | IN OUT | Value of a string parameter |
| listno | BINARY_INTEGER | IN | List item number. If retrieving parameter values for a parameter that can be specified multiple times to accumulate values, use this parameter to get each individual parameter. |

**Returns:** `BINARY_INTEGER`

## Usage Notes

Note: This subprogram has been deprecated and replaced by improved technology. It is maintained only for purposes of backward compatibility. As an alternative, you can query v$_parameter directly. Note: This subprogram has been deprecated and replaced by improved technology. It is maintained only for purposes of backward compatibility. As an alternative, you can query v$_parameter directly. Syntax DBMS_UTILITY.GET_PARAMETER_VALUE ( parnam IN VARCHAR2, intval IN OUT BINARY_INTEGER, strval IN OUT VARCHAR2, listno IN BINARY_INTEGER DEFAULT 1) RETURN BINARY_INTEGER; Parameters Table 187-22 GET_PARAMETER_VALUE Function Parameters Parameter Description parnam Parameter name intval Value of an integer parameter or the value length of a string parameter strval Value of a string parameter listno List item number. If retrieving parameter values for a parameter that can be specified multiple times to accumulate values, use this parameter to get each individual parameter. Return Values Parameter type: 0 if parameter is an INTEGER / BOOLEAN parameter 1 if parameter is a string/file parameter