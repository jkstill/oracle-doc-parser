---
id: 19c__DBMS_DIMENSION.VALIDATE_DIMENSION
name: DBMS_DIMENSION.VALIDATE_DIMENSION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DIMENSION
tags: [dbms_dimension]
source_file: DBMS_DIMENSION.html
---

# DBMS_DIMENSION.VALIDATE_DIMENSION

This procedure verifies that the relationships specified in a dimension are valid. The rowid for any row that is found to be invalid will be stored in the table DIMENSION_EXCEPTIONS in the user's schema.

## Syntax

```sql
DBMS_DIMENSION.VALIDATE_DIMENSION (
   dimension               IN VARCHAR2,
   incremental             IN BOOLEAN := TRUE,
   check_nulls             IN BOOLEAN := FALSE,
   statement_id            IN VARCHAR2 := NULL );
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| dimension | VARCHAR2 | IN | The owner and name of the dimension in the format of owner.name . |
| incremental | BOOLEAN | IN | If TRUE , check only the new rows for tables of this dimension. If FALSE , check all the rows. |
| check_nulls | BOOLEAN | IN | If TRUE , then all level columns are verified to be non-null. If FALSE , this check is omitted. Specify FALSE when non- NULL ness is guaranteed by other means, such as NOT NULL constraints. |
| statement_id | VARCHAR2 | IN | A client-supplied unique identifier to associate output rows with specific invocations of the procedure. |

## Usage Notes

Syntax DBMS_DIMENSION.VALIDATE_DIMENSION ( dimension IN VARCHAR2, incremental IN BOOLEAN := TRUE, check_nulls IN BOOLEAN := FALSE, statement_id IN VARCHAR2 := NULL ); Parameters Table 62-3 VALIDATE_DIMENSION Procedure Parameters Parameter Description dimension The owner and name of the dimension in the format of owner.name . incremental If TRUE , check only the new rows for tables of this dimension. If FALSE , check all the rows. check_nulls If TRUE , then all level columns are verified to be non-null. If FALSE , this check is omitted. Specify FALSE when non- NULL ness is guaranteed by other means, such as NOT NULL constraints. statement_id A client-supplied unique identifier to associate output rows with specific invocations of the procedure.