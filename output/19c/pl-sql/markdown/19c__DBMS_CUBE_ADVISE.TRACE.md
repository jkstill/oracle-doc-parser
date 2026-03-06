---
id: 19c__DBMS_CUBE_ADVISE.TRACE
name: DBMS_CUBE_ADVISE.TRACE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CUBE_ADVISE
tags: [dbms_cube_advise]
source_file: DBMS_CUBE_ADVISE.html
---

# DBMS_CUBE_ADVISE.TRACE

This procedure turns on and off diagnostic messages to server output for the MV_CUBE_ADVICE function.

## Syntax

```sql
DBMS_CUBE_ADVISE.TRACE (
     diaglevel       IN  BINARY_INTEGER DEFAULT 0);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| diaglevel | BINARY_INTEGER | IN | 0 to turn tracing off, or 1 to turn tracing on. |

## Usage Notes

Syntax DBMS_CUBE_ADVISE.TRACE ( diaglevel IN BINARY_INTEGER DEFAULT 0); Parameters Table 45-5 TRACE Procedure Parameters Parameter Description diaglevel 0 to turn tracing off, or 1 to turn tracing on. Examples The following example directs the diagnostic messages to server output. The SQL*Plus SERVEROUTPUT setting displays the messages. SQL> SET SERVEROUT ON FORMAT WRAPPED SQL> EXECUTE dbms_cube_advise.trace(1); DBMS_COAD_DIAG: Changing diagLevel from [0] to [1] PL/SQL procedure successfully completed. SQL> SELECT sqlobject, sqltext, droptext FROM TABLE( dbms_cube_advise.mv_cube_advice('GLOBAL', 'CB$UNITS_CUBE')) WHERE apiobject='UNITS_CUBE'; SQLOBJECT SQLTEXT DROPTEXT --------------- ---------------------------------------- ---------------------------------------- UNITS_FACT alter table "GLOBAL"."UNITS_FACT" add co alter table "GLOBAL"."UNITS_FACT" drop c nstraint "COAD_PK000222" PRIMARY KEY ("C onstraint "COAD_PK000222" cascade HANNEL_ID", "ITEM_ID", "SHIP_TO_ID", "MO NTH_ID") rely disable novalidate CB$UNITS_CUBE alter materialized view "GLOBAL"."CB$UNI alter materialized view "GLOBAL"."CB$UNI TS_CUBE" compile TS_CUBE" compile 20070706 07:25:27.462780000 DBMS_COAD_DIAG NOTE: Parameter mvOwner : GLOBAL 20070706 07:25:27.462922000 DBMS_COAD_DIAG NOTE: Parameter mvName : CB$UNITS_CUBE 20070706 07:25:27.462967000 DBMS_COAD_DIAG NOTE: Parameter factTab : . 20070706 07:25:27.463011000 DBMS_COAD_DIAG NOTE: Parameter cubeName : UNITS_CUBE 20070706 07:25:27.463053000 DBMS_COAD_DIAG NOTE: Parameter cnsState : rely disable novalidate 20070706 07:25:27.463094000 DBMS_COAD_DIAG NOTE: Parameter NNState : disable novalidate 20070706 07:25:27.462368000 DBMS_COAD_DIAG NOTE: Begin NN: 20070706 07:25:27.833530000 DBMS_COAD_DIAG NOTE: End NN: 20070706 07:25:27.833620000 DBMS_COAD_DIAG NOTE: Begin PK: 20070706 07:25:28.853418000 DBMS_COAD_DIAG NOTE: End PK: 20070706 07:25:28.853550000 DBMS_COAD_DIAG NOTE: Begin FK: 20070706 07:25:28.853282000 DBMS_COAD_DIAG NOTE: End FK: 20070706 07:25:28.853359000 DBMS_COAD_DIAG NOTE: Begin RD: 20070706 07:25:29.660471000 DBMS_COAD_DIAG NOTE: End RD: 20070706 07:25:29.661363000 DBMS_COAD_DIAG NOTE: Begin CM: 20070706 07:25:29.665106000 DBMS_COAD_DIAG NOTE: End CM: SQL> EXECUTE dbms_cube_advise.trace(0); DBMS_COAD_DIAG: Changing diagLevel from [1] to [0] PL/SQL procedure successfully completed.