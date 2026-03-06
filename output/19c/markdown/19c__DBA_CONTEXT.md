---
id: 19c__DBA_CONTEXT
name: DBA_CONTEXT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_CONTEXT.html
---

# DBA_CONTEXT

DBA_CONTEXT provides all context namespace information in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| NAMESPACE | VARCHAR2(128) | Name of the context namespace |
| SCHEMA | VARCHAR2(128) | Schema name of the designated package that can set attributes using this namespace |
| PACKAGE | VARCHAR2(128) | Package name of the designated package that can set attributes using this namespace |
| TYPE | VARCHAR2(22) | Type of the context create |
| ORIGIN_CON_ID | NUMBER | The ID of the container where the data originates. Possible values include: 0 : This value is used for rows in non-CDBs. This value is not used for CDBs. n : This value is used for rows containing data that originate in the container with container ID n ( n = 1 if the row originates in root) |

## Usage Notes

Related View ALL_CONTEXT describes all context namespaces in the current session for which attributes and values have been specified using the DBMS_SESSION.SET_CONTEXT procedure. This view does not describe the TYPE and ORIGIN_CON_ID columns. Column Datatype NULL Description NAMESPACE VARCHAR2(128) NOT NULL Name of the context namespace SCHEMA VARCHAR2(128) NOT NULL Schema name of the designated package that can set attributes using this namespace PACKAGE VARCHAR2(128) NOT NULL Package name of the designated package that can set attributes using this namespace TYPE VARCHAR2(22) Type of the context create ORIGIN_CON_ID NUMBER The ID of the container where the data originates. Possible values include: 0 : This value is used for rows in non-CDBs. This value is not used for CDBs. n : This value is used for rows containing data that originate in the container with container ID n ( n = 1 if the row originates in root) See Also: " ALL_CONTEXT " See Also: " ALL_CONTEXT "