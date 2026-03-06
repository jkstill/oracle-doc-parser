---
id: 19c__DBMS_PREPROCESSOR.GET_POST_PROCESSED_SOURCE
name: DBMS_PREPROCESSOR.GET_POST_PROCESSED_SOURCE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PREPROCESSOR
tags: [dbms_preprocessor]
source_file: DBMS_PREPROCESSOR.html
---

# DBMS_PREPROCESSOR.GET_POST_PROCESSED_SOURCE

This overloaded function returns the post-processed source text. The different functionality of each form of syntax is presented along with the definition.

## Syntax

```sql
DBMS_PREPROCESSOR.GET_POST_PROCESSED_SOURCE (
   object_type    IN VARCHAR2,
   schema_name    IN VARCHAR2,
   object_name    IN VARCHAR2)
  RETURN source_lines_t;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| object_type | VARCHAR2 | IN | Must be one of PACKAGE , PACKAGE BODY , PROCEDURE , FUNCTION , TYPE , TYPE , BODY or TRIGGER . Case sensitive. |
| schema_name | VARCHAR2 | IN | The schema name. Case insensitive unless a quoted identifier is used. If NULL , use current schema. |
| object_name | VARCHAR2) | IN | The name of the object.The object_type is always case insensitive. Case insensitive unless a quoted identifier is used. |
| source |  |  | The source text of the compilation unit |
| source_lines_t |  |  | INDEX-BY table containing the source text of the compilation unit. The source text is a concatenation of all the non- NULL INDEX-BY table elements in ascending index order. |

**Returns:** `source_lines_t`

## Usage Notes

Syntax Returns post-processed source text of a stored PL/SQL unit: DBMS_PREPROCESSOR.GET_POST_PROCESSED_SOURCE ( object_type IN VARCHAR2, schema_name IN VARCHAR2, object_name IN VARCHAR2) RETURN source_lines_t; Returns post-processed source text of a compilation unit: DBMS_PREPROCESSOR.GET_POST_PROCESSED_SOURCE ( source IN VARCHAR2) RETURN source_lines_t; Returns post-processed source text of an INDEX-BY table containing the source text of the compilation unit: DBMS_PREPROCESSOR.GET_POST_PROCESSED_SOURCE ( source IN source_lines_t) RETURN source_lines_t; Parameters Table 130-2 GET_POST_PROCESSED_SOURCE Function Parameters Parameter Description object_type Must be one of PACKAGE , PACKAGE BODY , PROCEDURE , FUNCTION , TYPE , TYPE , BODY or TRIGGER . Case sensitive. schema_name The schema name. Case insensitive unless a quoted identifier is used. If NULL , use current schema. object_name The name of the object.The object_type is always case insensitive. Case insensitive unless a quoted identifier is used. source The source text of the compilation unit source_lines_t INDEX-BY table containing the source text of the compilation unit. The source text is a concatenation of all the non- NULL INDEX-BY table elements in ascending index order. Return Values The function returns an INDEX-BY table containing the lines of the post-processed source text starting from index 1. Usage Notes Newline characters are not removed. Each line in the post-processed source text is mapped to a row in the INDEX-BY table. In the post-processed source, unselected text will have blank lines. Exceptions Table 130-3 GET_POST_PROCESSED_SOURCE Function Exceptions Exception Description ORA-24234 Insufficient privileges or object does not exist ORA-24235 Bad value for object type. Should be one of PACKAGE , PACKAGE BODY , PROCEDURE , FUNCTION , TYPE , TYPE , BODY or TRIGGER . ORA-24236 The source text is empty ORA-00931 Missing identifier. The object_name should not be NULL . ORA-06502 Numeric or value error: Character string buffer too small A line is too long (> 32767 bytes)