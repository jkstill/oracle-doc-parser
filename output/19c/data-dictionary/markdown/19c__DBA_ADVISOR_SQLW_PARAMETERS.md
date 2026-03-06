---
id: 19c__DBA_ADVISOR_SQLW_PARAMETERS
name: DBA_ADVISOR_SQLW_PARAMETERS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: sql
tags: [dba]
source_file: DBA_ADVISOR_SQLW_PARAMETERS.html
---

# DBA_ADVISOR_SQLW_PARAMETERS

DBA_ADVISOR_SQLW_PARAMETERS displays all workload parameters and their current values in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the task or workload object |
| WORKLOAD_ID | NUMBER | Unique identifier number of the workload object |
| WORKLOAD_NAME | VARCHAR2(128) | Name of the workload object |
| PARAMETER_NAME | VARCHAR2(128) | Name of the parameter |
| PARAMETER_VALUE | VARCHAR2(4000) | Value of the parameter. Numeric parameter values are converted to a string equivalent. Possible keywords as values: ALL UNLIMITED UNUSED |
| PARAMETER_TYPE | VARCHAR2(10) | Datatype of the parameter: NUMBER - Numeric value STRING - String value. If the string contains special characters, then it will be enclosed in single quotes. STRINGLIST - Comma-separated list of string elements. If a string element contains a comma or other special characters, then the element will be enclosed in single quotes. TABLE - Single table reference. A reference contains a schema name, followed by an optional table name. If the table name is omitted or is the character % , then the table name is interpreted as a wildcard. SQL quoted identifiers are supported. TABLELIST - List of one or more comma-separated table references. A reference contains a schema name, followed by an optional table name. If the table name is omitted or is the character % , then the table name is interpreted as a wildcard. SQL quoted identifiers are supported. |
| DESCRIPTION | VARCHAR2(4000) | Parameter description |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related View USER_ADVISOR_SQLW_PARAMETERS displays the workload parameters and their current values owned by the current user. This view does not display the OWNER column. See Also: " USER_ADVISOR_SQLW_PARAMETERS " See Also: " USER_ADVISOR_SQLW_PARAMETERS "