---
id: 19c__DBMS_TRANSFORM.CREATE_TRANSFORMATION
name: DBMS_TRANSFORM.CREATE_TRANSFORMATION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_TRANSFORM
tags: [dbms_transform]
source_file: DBMS_TRANSFORM.html
---

# DBMS_TRANSFORM.CREATE_TRANSFORMATION

This procedure creates a transformation that maps an object of the source type to an object of the target type. The transformation expression can be a SQL expression or a PL/SQL function. It must return an object of the target type.

## Syntax

```sql
DBMS_TRANSFORM.CREATE_TRANSFORMATION (
    schema               VARCHAR2(30),
    name                 VARCHAR2(30),
    from_schema          VARCHAR2(30),
    from_type            VARCHAR2(30),
    to_schema            VARCHAR2(30),
    to_type              VARCHAR2(30),
    transformation       VARCHAR2(4000));
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schema | VARCHAR2(30) | IN | Specifies the schema of the transformation. |
| name | VARCHAR2(30) | IN | Specifies the name of the transformation. |
| from_schema | VARCHAR2(30) | IN | Specifies the schema of the source type. |
| from_type | VARCHAR2(30) | IN | Specifies the source type. |
| to_schema | VARCHAR2(30) | IN | Specifies the target type schema. |
| to_type | VARCHAR2(30) | IN | Specifies the target type. |
| transformation | VARCHAR2(4000)) | IN | Specifies the transformation expression, returning an object of the target type. The expression must be a function returning an object of the target type or a constructor expression for the target type. You can choose not to specify a transformation expression and instead specify transformations for attributes of the target type using MODIFY_TRANSFORMATION . |

## Usage Notes

Syntax DBMS_TRANSFORM.CREATE_TRANSFORMATION ( schema VARCHAR2(30), name VARCHAR2(30), from_schema VARCHAR2(30), from_type VARCHAR2(30), to_schema VARCHAR2(30), to_type VARCHAR2(30), transformation VARCHAR2(4000)); Parameters Table 180-2 CREATE_TRANSFORMATION Procedure Parameters Parameter Description schema Specifies the schema of the transformation. name Specifies the name of the transformation. from_schema Specifies the schema of the source type. from_type Specifies the source type. to_schema Specifies the target type schema. to_type Specifies the target type. transformation Specifies the transformation expression, returning an object of the target type. The expression must be a function returning an object of the target type or a constructor expression for the target type. You can choose not to specify a transformation expression and instead specify transformations for attributes of the target type using MODIFY_TRANSFORMATION . Usage Notes The transformation expression must be a SQL expression or a PL/SQL function returning the type of the specified attribute of the target type. To create, modify or drop transformations, a user must be granted execute privileges on DBMS_TRANSFORM . The user must also have execute privileges on the user defined types that are the source and destination types of the transformation. In addition, the user must also have execute privileges on any PLSQL function being used in the transformation function. The transformation cannot write database state (perform DML) or commit or rollback the current transaction. The transformation must be a SQL function with source type as input type, returning an object of the target type. It could also be a SQL expression of target type, referring to a source type. All references to the source type must be of the form source.user_data . Both source and target types must be non-scalar database types. A null transformation expression maps to a null target object. For using the transformation at enqueue and dequeue time, the login user invoking the operation must have execute privileges on the PLSQL functions used by the transformation. For propagation, the owning schema of the queue must have these privileges.