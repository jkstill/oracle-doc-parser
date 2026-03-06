---
id: 19c__DBMS_DATA_MINING_TRANSFORM.GET_EXPRESSION
name: DBMS_DATA_MINING_TRANSFORM.GET_EXPRESSION
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING_TRANSFORM
tags: [dbms_data_mining_transform]
source_file: DBMS_DATA_MINING_TRANSFORM.html
---

# DBMS_DATA_MINING_TRANSFORM.GET_EXPRESSION

This function returns a row from a VARCHAR2 array that stores a transformation expression. The array is built by calls to the SET_EXPRESSION Procedure.

## Syntax

```sql
DBMS_DATA_MINING_TRANSFORM.GET_EXPRESSION (
     expression           IN EXPRESSION_REC,
     chunk_num            IN PLS_INTEGER DEFAULT NULL);
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| expression | EXPRESSION_REC | IN | An expression record ( EXPRESSION_REC ) that specifies a transformation expression or a reverse transformation expression for an attribute. Each expression record includes a VARCHAR2 array and index fields for specifying upper and lower boundaries within the array. There are two EXPRESSION_REC fields within a transformation record ( TRANSFORM_REC ): one for the transformation expression; the other for the reverse transformation expression. See Table 48-1 for a description of the EXPRESSION_REC type. |
| chunk |  |  | A VARCHAR2 chunk (row) to be appended to expression . |

**Returns:** `VARCHAR2`

## Usage Notes

The array can be used for specifying SQL expressions that are too long to be used with the SET_TRANSFORM Procedure. Syntax DBMS_DATA_MINING_TRANSFORM.GET_EXPRESSION ( expression IN EXPRESSION_REC, chunk_num IN PLS_INTEGER DEFAULT NULL); RETURN VARCHAR2; Parameters Table 48-19 GET_EXPRESSION Function Parameters Parameter Description expression An expression record ( EXPRESSION_REC ) that specifies a transformation expression or a reverse transformation expression for an attribute. Each expression record includes a VARCHAR2 array and index fields for specifying upper and lower boundaries within the array. There are two EXPRESSION_REC fields within a transformation record ( TRANSFORM_REC ): one for the transformation expression; the other for the reverse transformation expression. See Table 48-1 for a description of the EXPRESSION_REC type. chunk A VARCHAR2 chunk (row) to be appended to expression . Usage Notes Chunk numbering starts with one. For chunks outside of the range, the return value is null. When a chunk number is null the whole expression is returned as a string. If the expression is too big, a VALUE_ERROR is raised. See " About Transformation Lists " . See " Operational Notes " . Examples See the example for the SET_EXPRESSION Procedure .