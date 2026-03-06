---
id: 19c__DBMS_MGWADM.SET_LOG_LEVEL
name: DBMS_MGWADM.SET_LOG_LEVEL
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MGWADM
tags: [dbms_mgwadm]
source_file: DBMS_MGWADM.html
---

# DBMS_MGWADM.SET_LOG_LEVEL

This procedure dynamically alters the Messaging Gateway agent logging level. The Messaging Gateway agent must be running.

## Syntax

```sql
DBMS_MGWADM.SET_LOG_LEVEL (
   log_level    IN   BINARY_INTEGER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| log_level | BINARY_INTEGER) | IN | Level at which the Messaging Gateway agent logs information. DBMS_MGWADM.BASIC_LOGGING generates the least information while DBMS_MGWADM.TRACE_DEBUG_LOGGING generates the most information. |
| agent_name |  |  | Identifies the Messaging Gateway agent. DBMS_MGWADM . DEFAULT_AGENT specifies the default agent. |

## Usage Notes

Syntax DBMS_MGWADM.SET_LOG_LEVEL ( log_level IN BINARY_INTEGER); DBMS_MGWADM.SET_LOG_LEVEL ( agent_name IN VARCHAR2, log_level IN BINARY_INTEGER); Parameters Table 110-46 SET_LOG_LEVEL Procedure Parameters Parameter Description log_level Level at which the Messaging Gateway agent logs information. DBMS_MGWADM.BASIC_LOGGING generates the least information while DBMS_MGWADM.TRACE_DEBUG_LOGGING generates the most information. agent_name Identifies the Messaging Gateway agent. DBMS_MGWADM . DEFAULT_AGENT specifies the default agent. See Also: Table 110-3 for details on the log_level parameter See Also: Table 110-3 for details on the log_level parameter