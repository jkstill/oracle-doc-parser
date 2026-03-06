---
id: 19c__DBA_LOGSTDBY_SKIP
name: DBA_LOGSTDBY_SKIP
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: logging
tags: [dba]
source_file: DBA_LOGSTDBY_SKIP.html
---

# DBA_LOGSTDBY_SKIP

DBA_LOGSTDBY_SKIP displays the skip rules that are used by SQL Apply.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| ERROR | VARCHAR2(1) | Indicates how the skip rule was created: Y - For rules from DBMS_LOGSTDBY.SKIP_ERROR N - For rules from DBMS_LOGSTDBY.SKIP |
| STATEMENT_OPT | VARCHAR2(128) | Specifies the type of statement that should be skipped |
| OWNER | VARCHAR2(128) | Name of the schema under which the skip option should be used |
| NAME | VARCHAR2(261) | Name of the object that is being skipped |
| USE_LIKE | VARCHAR2(1) | Indicates whether the statement should use a SQL wildcard search when matching names ( Y ) or not ( N ) |
| ESC | VARCHAR2(1) | Escape character used when performing wildcard matches |
| PROC | VARCHAR2(392) | Name of a stored procedure that will be executed when processing the skip option |

## Usage Notes

This view is for logical standby databases only. See Also: Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_LOGSTDBY.SKIP_ERROR procedure Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_LOGSTDBY.SKIP procedure See Also: Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_LOGSTDBY.SKIP_ERROR procedure Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_LOGSTDBY.SKIP procedure