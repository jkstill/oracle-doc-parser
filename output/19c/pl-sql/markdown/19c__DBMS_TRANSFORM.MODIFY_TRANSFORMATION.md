---
id: 19c__DBMS_TRANSFORM.MODIFY_TRANSFORMATION
name: DBMS_TRANSFORM.MODIFY_TRANSFORMATION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_TRANSFORM
tags: [dbms_transform]
source_file: DBMS_TRANSFORM.html
---

# DBMS_TRANSFORM.MODIFY_TRANSFORMATION

This procedure modifies the transformation expression for the given transformation.

## Syntax

```sql
DBMS_TRANSFORM.MODIFY_TRANSFORMATION (
   schema             VARCHAR2(30),
   name               VARCHAR2(30),
   attribute_number   INTEGER,
   transformation     VARCHAR2(4000));
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schema | VARCHAR2(30) | IN | Specifies the schema of the transformation. |
| name | VARCHAR2(30) | IN | Specifies the name of the transformation. |
| attribute_number | TEGER | IN | The attribute of the target type for which the new transformation expression is being specified. When specifying the new transformation as a single expression of the target type, specify a value of 0. |
| transformation | VARCHAR2(4000)) | IN | The transformation expression must be a SQL expression or a PL/SQL function returning the type of the specified attribute of the target type. If the attribute_number is 0, then the expression must be a PL/SQL function returning an object of the target type or a constructor expression for the target type. |

## Usage Notes

Syntax DBMS_TRANSFORM.MODIFY_TRANSFORMATION ( schema VARCHAR2(30), name VARCHAR2(30), attribute_number INTEGER, transformation VARCHAR2(4000)); Parameters Table 180-4 MODIFY_TRANSFORMATION Procedure Parameters Parameter Description schema Specifies the schema of the transformation. name Specifies the name of the transformation. attribute_number The attribute of the target type for which the new transformation expression is being specified. When specifying the new transformation as a single expression of the target type, specify a value of 0. transformation The transformation expression must be a SQL expression or a PL/SQL function returning the type of the specified attribute of the target type. If the attribute_number is 0, then the expression must be a PL/SQL function returning an object of the target type or a constructor expression for the target type. Usage Notes If the new transformation is a single expression of the target type, it may be specified with an attribute_number of 0. The new transformation may also be specified for each attribute of the target type. You can use this procedure to define the transformation as a separate expression for each attribute of the target type. For large transformations, this representation may be more readable and allow the application of fine grain control over the transformation. If the transformation expression was left unspecified for some of the attributes of the target type, they are evaluated to null when the transformation is applied.