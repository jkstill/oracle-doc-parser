---
id: 19c__DBA_REDEFINITION_ERRORS
name: DBA_REDEFINITION_ERRORS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: configuration
tags: [dba]
source_file: DBA_REDEFINITION_ERRORS.html
---

# DBA_REDEFINITION_ERRORS

DBA_REDEFINITION_ERRORS is an online redefinition view. It displays the dependent objects for which errors were raised while attempting to create similar objects on the interim table of the redefinition.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OBJECT_TYPE | VARCHAR2(12) | Type of the redefinition object: TABLE INDEX CONSTRAINT TRIGGER NESTED TABLE PARTITION MV LOG |
| OBJECT_OWNER | VARCHAR2(4000) | Owner of the redefinition object |
| OBJECT_NAME | VARCHAR2(128) | Name of the redefinition object |
| BASE_TABLE_OWNER | VARCHAR2(128) | Owner of the base table of the redefinition object |
| BASE_TABLE_NAME | VARCHAR2(128) | Name of the base table of the redefinition object |
| DDL_TXT | CLOB | DDL used to create the corresponding interim redefinition object |
| EDITION_NAME | VARCHAR2(128) | Reserved for future use |
| ERR_NO | NUMBER(38) | Oracle error number corresponding to this error |
| ERR_TXT | VARCHAR2(1000) | Oracle error text corresponding to this error |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content See Also: Oracle Database Administrator’s Guide for more information about online redefinition See Also: Oracle Database Administrator’s Guide for more information about online redefinition