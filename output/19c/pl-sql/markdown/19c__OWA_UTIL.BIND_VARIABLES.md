---
id: 19c__OWA_UTIL.BIND_VARIABLES
name: OWA_UTIL.BIND_VARIABLES
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: OWA_UTIL
tags: [owa_util]
source_file: OWA_UTIL.html
---

# OWA_UTIL.BIND_VARIABLES

This function prepares a SQL query by binding variables to it, and stores the output in an opened cursor. Use this function as a parameter to a procedure sending a dynamically generated query. Specify up to 25 bind variables.

## Syntax

```sql
OWA_UTIL.BIND_VARIABLES(
   theQuery       IN       VARCHAR2   DEFAULT NULL,
   bv1Name        IN       VARCHAR2   DEFAULT NULL,
   bv1Value       IN       VARCHAR2   DEFAULT NULL,
   bv2Name        IN       VARCHAR2   DEFAULT NULL,
   bv2Value       IN       VARCHAR2   DEFAULT NULL,
   bv3Name        IN       VARCHAR2   DEFAULT NULL,
   bv3Value       IN       VARCHAR2   DEFAULT NULL,
        ...
   bv25Name       IN       VARCHAR2   DEFAULT NULL,
   bv25Value      IN       VARCHAR2   DEFAULT NULL)
 RETURN INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| theQuery | VARCHAR2 | IN | The SQL query statement which must be a SELECT statement |
| bv1Name | VARCHAR2 | IN | The name of the variable |
| bv1Value | VARCHAR2 | IN | The value of the variable |

**Returns:** `INTEGER`

## Usage Notes

Syntax OWA_UTIL.BIND_VARIABLES( theQuery IN VARCHAR2 DEFAULT NULL, bv1Name IN VARCHAR2 DEFAULT NULL, bv1Value IN VARCHAR2 DEFAULT NULL, bv2Name IN VARCHAR2 DEFAULT NULL, bv2Value IN VARCHAR2 DEFAULT NULL, bv3Name IN VARCHAR2 DEFAULT NULL, bv3Value IN VARCHAR2 DEFAULT NULL, ... bv25Name IN VARCHAR2 DEFAULT NULL, bv25Value IN VARCHAR2 DEFAULT NULL) RETURN INTEGER; Parameters Table 230-2 BIND_VARIABLES Function Parameters Parameter Description theQuery The SQL query statement which must be a SELECT statement bv1Name The name of the variable bv1Value The value of the variable Return Values An integer identifying the opened cursor.