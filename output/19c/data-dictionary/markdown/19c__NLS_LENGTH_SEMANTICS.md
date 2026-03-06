---
id: 19c__NLS_LENGTH_SEMANTICS
name: NLS_LENGTH_SEMANTICS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
source_file: NLS_LENGTH_SEMANTICS.html
---

# NLS_LENGTH_SEMANTICS

NLS_LENGTH_SEMANTICS is used to specify length semantics.

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content The session-level value of NLS_LENGTH_SEMANTICS specifies the default length semantics to use for VARCHAR2 and CHAR table columns, user-defined object attributes, and PL/SQL variables in database objects created in the session. This default may be overridden by the explicit length semantics qualifiers BYTE and CHAR in column, attribute, and variable definitions. The instance-level value of NLS_LENGTH_SEMANTICS provides a default for the session-level value if NLS_LENGTH_SEMANTICS is not set explicitly by the database client through the NLS_LENGTH_SEMANTICS client environment variable (does not apply to JDBC Thin clients), or the ALTER SESSION SET NLS_LENGTH_SEMANTICS statement. NCHAR , NVARCHAR2 , CLOB , and NCLOB columns are always character-based. Sessions logged in as SYS do not use the NLS_LENGTH_SEMANTICS parameter. They use BYTE length semantics for all created objects unless overridden by the explicit BYTE and CHAR qualifiers in object definitions (SQL DDL statements). Note: Oracle strongly recommends that you do NOT set the NLS_LENGTH_SEMANTICS parameter to CHAR in the instance or server parameter file. This may cause many existing installation scripts to unexpectedly create columns with character length semantics, resulting in run-time errors, including buffer overflows. See Also: Oracle Database Globalization Support Guide for more information about this parameter Note: Oracle strongly recommends that you do NOT set the NLS_LENGTH_SEMANTICS parameter to CHAR in the instance or server parameter file. This may cause many existing installation scripts to unexpectedly create columns with character length semantics, resulting in run-time errors, including buffer overflows. See Also: Oracle Database Globalization Support Guide for more information about this parameter