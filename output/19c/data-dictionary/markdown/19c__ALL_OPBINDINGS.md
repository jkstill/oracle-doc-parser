---
id: 19c__ALL_OPBINDINGS
name: ALL_OPBINDINGS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_OPBINDINGS.html
---

# ALL_OPBINDINGS

ALL_OPBINDINGS describes the binding functions and methods on the operators accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the operator |
| OPERATOR_NAME | VARCHAR2(128) | Name of the operator |
| BINDING# | NUMBER | Binding number of the operator |
| FUNCTION_NAME | VARCHAR2(92) | Name of the binding function or method as specified by the user |
| RETURN_SCHEMA | VARCHAR2(128) | Name of the schema of the return type if the return type of the binding is an object type |
| RETURN_TYPE | VARCHAR2(128) | Name of the return type |
| IMPLEMENTATION_TYPE_SCHEMA | VARCHAR2(128) | If the operator was created WITH INDEX CONTEXT or SCAN CONTEXT , then this column displays the schema of the implementation type used by the functional implementation of the operator as a scan context (null if the operator was created without this syntax). See Also: the CREATE OPERATOR statement in Oracle Database SQL Language Reference |
| IMPLEMENTATION_TYPE | VARCHAR2(128) | If the operator was created WITH INDEX CONTEXT or SCAN CONTEXT , then this column displays the name of the implementation type used by the functional implementation of the operator as a scan context (null if the operator was created without this syntax). See Also: the CREATE OPERATOR statement in Oracle Database SQL Language Reference |
| PROPERTY | VARCHAR2(43) | Property of the operator binding: WITH INDEX CONTEXT COMPUTE ANCILLARY DATA ANCILLARY TO WITH COLUMN CONTEXT WITH INDEX, COLUMN CONTEXT COMPUTE ANCILLARY DATA, WITH COLUMN CONTEXT |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_OPBINDINGS describes the binding functions and methods on all operators in the database. USER_OPBINDINGS describes the binding functions and methods on the operators owned by the current user. See Also: " DBA_OPBINDINGS " " USER_OPBINDINGS " See Also: " DBA_OPBINDINGS " " USER_OPBINDINGS "