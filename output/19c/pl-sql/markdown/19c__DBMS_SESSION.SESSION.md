---
id: 19c__DBMS_SESSION.SESSION
name: DBMS_SESSION.SESSION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SESSION
tags: [dbms_session]
source_file: DBMS_SESSION.html
---

# DBMS_SESSION.SESSION

This procedure enables session-level SQL trace for the invoking session. Invoking this procedure results in SQL tracing of every SQL statement issued by the session.

## Syntax

```sql
DBMS_SESSION.SESSION_TRACE_ENABLE(
   waits     IN   BOOLEAN DEFAULT TRUE,
   binds     IN   BOOLEAN DEFAULT FALSE, 
   plan_stat IN   VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| waits | BOOLEAN | IN | Specifies if wait information is to be traced |
| binds | BOOLEAN | IN | Specifies if bind information is to be traced |
| plan_stat | VARCHAR2 | IN | Frequency at which we dump row source statistics. Value should be ' NEVER ', ' FIRST_EXECUTION ' (equivalent to NULL ) or ' ALL_EXECUTIONS '. |

## Usage Notes

Syntax DBMS_SESSION.SESSION_TRACE_ENABLE( waits IN BOOLEAN DEFAULT TRUE, binds IN BOOLEAN DEFAULT FALSE, plan_stat IN VARCHAR2 DEFAULT NULL); Parameters Table 154-17 SESSION_TRACE_ENABLE Procedure Parameters Parameter Description waits Specifies if wait information is to be traced binds Specifies if bind information is to be traced plan_stat Frequency at which we dump row source statistics. Value should be ' NEVER ', ' FIRST_EXECUTION ' (equivalent to NULL ) or ' ALL_EXECUTIONS '.