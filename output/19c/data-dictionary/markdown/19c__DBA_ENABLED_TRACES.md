---
id: 19c__DBA_ENABLED_TRACES
name: DBA_ENABLED_TRACES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_ENABLED_TRACES.html
---

# DBA_ENABLED_TRACES

DBA_ENABLED_TRACES displays information about enabled SQL traces.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| TRACE_TYPE | VARCHAR2(21) | Type of the trace: CLIENT_ID SERVICE SERVICE_MODULE SERVICE_MODULE_ACTION DATABASE |
| PRIMARY_ID | VARCHAR2(64) | Primary qualifier (specific client identifier or service name) |
| QUALIFIER_ID1 | VARCHAR2(64) | Secondary qualifier (specific module name) |
| QUALIFIER_ID2 | VARCHAR2(64) | Additional qualifier (specific action name) |
| WAITS | VARCHAR2(5) | Indicates whether waits are traced ( TRUE ) or not ( FALSE ) |
| BINDS | VARCHAR2(5) | Indicates whether binds are traced ( TRUE ) or not ( FALSE ) |
| PLAN_STATS | VARCHAR2(10) | Indicates whether cursor execution statistics are traced. Possible values include: ALL_EXEC : Execution statistics are dumped at each cursor execution NEVER : Execution statistics are never dumped FIRST_EXEC : Execution statistics are dumped during the first execution of the cursor. This is the default behavior. |
| INSTANCE_NAME | VARCHAR2(16) | Instance name for tracing restricted to named instances |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content See Also: Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_MONITOR package See Also: Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_MONITOR package