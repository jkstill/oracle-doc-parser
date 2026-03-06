---
id: 19c__DBMS_LOGSTDBY.SET_TABLESPACE
name: DBMS_LOGSTDBY.SET_TABLESPACE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOGSTDBY
tags: [dbms_logstdby]
source_file: DBMS_LOGSTDBY.html
---

# DBMS_LOGSTDBY.SET_TABLESPACE

This procedure moves metadata tables required by SQL Apply to the user-specified tablespace.

## Syntax

```sql
DBMS_LOGSTDBY.SET_TABLESPACE(
           NEW_TABLESPACE IN VARCHAR2)
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| NEW_TABLESPACE | VARCHAR2) | IN | Name of the new tablespace where metadata tables will reside. |

## Usage Notes

By default, the metadata tables are created in the SYSAUX tablespace. SQL Apply cannot be running when you invoke this procedure. In a CDB, the SET_TABLESPACE procedure must be called from the root database. Syntax DBMS_LOGSTDBY.SET_TABLESPACE( NEW_TABLESPACE IN VARCHAR2) Parameters Table 102-12 SET_TABLE SPACE Procedure Parameters Parameter Description NEW_TABLESPACE Name of the new tablespace where metadata tables will reside. Exceptions Table 102-13 SET_TABLESPACE Procedure Exceptions Exception Description ORA-16103 Logical Standby apply must be stopped to allow this operation ORA-16236 Logical Standby metadata operation in progress Examples To move metadata tables to a new tablespace named LOGSTDBY_TBS , issue the following statement: SQL> EXECUTE DBMS_LOGSTDBY.SET_TABLESPACE (new_tablespace => 'LOGSTDBY_TBS');