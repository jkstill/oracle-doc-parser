---
id: 19c__DBMS_DIMENSION.DESCRIBE_DIMENSION
name: DBMS_DIMENSION.DESCRIBE_DIMENSION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DIMENSION
tags: [dbms_dimension]
source_file: DBMS_DIMENSION.html
---

# DBMS_DIMENSION.DESCRIBE_DIMENSION

This procedure displays the definition of the dimension, including dimension name, levels, hierarchies, and attributes. It displays the output using the DBMS_OUTPUT package.

## Syntax

```sql
DBMS_DIMENSION.DESCRIBE_DIMENSION (
   dimension  IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| dimension | VARCHAR2) | IN | The owner and name of the dimension in the format of owner.name . |

## Usage Notes

Syntax DBMS_DIMENSION.DESCRIBE_DIMENSION ( dimension IN VARCHAR2); Parameters Table 62-2 DESCRIBE_DIMENSION Procedure Parameter Parameter Description dimension The owner and name of the dimension in the format of owner.name .