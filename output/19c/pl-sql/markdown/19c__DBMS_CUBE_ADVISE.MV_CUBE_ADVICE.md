---
id: 19c__DBMS_CUBE_ADVISE.MV_CUBE_ADVICE
name: DBMS_CUBE_ADVISE.MV_CUBE_ADVICE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CUBE_ADVISE
tags: [dbms_cube_advise]
source_file: DBMS_CUBE_ADVISE.html
---

# DBMS_CUBE_ADVISE.MV_CUBE_ADVICE

This table function evaluates the metadata for a specified cube materialized view. It generates recommendations and returns them as a SQL result set. These SQL statements can be used to create constraints, SQL dimension objects, and materialized view logs that allow the broadest range of query rewrite transformations and log-based fast refresh of the cube materialized view.

## Syntax

```sql
DBMS_CUBE_ADVISE.MV_CUBE_ADVICE (
          owner        IN  VARCHAR2  DEFAULT USER,
          mvname       IN  VARCHAR2,
          reqtype      IN  VARCHAR2  DEFAULT '0',
          validate     IN  NUMBER    DEFAULT 0)
     RETURN COAD_ADVICE_T  PIPELINED;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| owner | VARCHAR2 | IN | Owner of the cube materialized view |
| mvname | VARCHAR2 | IN | Name of the cube, such as UNITS_CUBE , or the cube materialized view, such as CB$UNITS_CUBE |
| reqtype | VARCHAR2 | IN | Type of advice to generate: 0 : All applicable advice types 1 : Column NOT NULL constraints 2 : Primary key constraints 3 : Foreign key constraints 4 : Relational dimension objects 5 : Cube materialized view logs with primary key |
| validate | NUMBER | IN | Validation option: 0 : Validate the constraints 1 : Do not validate the constraints |

**Returns:** `COAD_ADVICE_T`

## Usage Notes

Syntax DBMS_CUBE_ADVISE.MV_CUBE_ADVICE ( owner IN VARCHAR2 DEFAULT USER, mvname IN VARCHAR2, reqtype IN VARCHAR2 DEFAULT '0', validate IN NUMBER DEFAULT 0) RETURN COAD_ADVICE_T PIPELINED; Parameters Table 45-2 MV_CUBE_ADVICE Function Parameters Parameter Description owner Owner of the cube materialized view mvname Name of the cube, such as UNITS_CUBE , or the cube materialized view, such as CB$UNITS_CUBE reqtype Type of advice to generate: 0 : All applicable advice types 1 : Column NOT NULL constraints 2 : Primary key constraints 3 : Foreign key constraints 4 : Relational dimension objects 5 : Cube materialized view logs with primary key validate Validation option: 0 : Validate the constraints 1 : Do not validate the constraints Returns A table of type COAD_ADVICE_T , consisting of a set of rows of type COAD_ADVICE_REC . Table 45-3 describes the columns. Table 45-3 MV_CUBE_ADVICE Return Values Column Datatype Description OWNER VARCHAR2(30) Owner of the dimensional object identified in APIOBJECT . APIOBJECT VARCHAR2(30) Name of a cube enhanced with materialized view capabilities, such as UNITS_CUBE . SQLOBJOWN VARCHAR2(30) Owner of the relational object identified in SQLOBJECT . SQLOBJECT VARCHAR2(65) Name of the master table, such as UNITS_FACT , or the cube materialized view, such as CB$UNITS_CUBE . ADVICETYPE NUMBER(38,0) Type of recommendation: 1 : Create NOT NULL constraints on the foreign key columns 2 : Create primary key constraints on the master table 3 : Create primary key constraints on the master view 4 : Create foreign key constraints on the master table 5 : Create foreign key constraints on the master view 6 : Create relational dimensions on the master dimension tables 7 : Create a materialized view log 8 : Compile the materialized view DISPOSITION CLOB Pre-existing conditions that conflict with the recommendations and should be resolved before SQLTEXT can be executed. SQLTEXT CLOB SQL statement that implements the recommendation. DROPTEXT CLOB SQL statement that reverses SQLTEXT . Pre-existing conditions may prevent these statements from restoring the schema to its previous state. Usage Notes This function is available in Analytic Workspace Manager as the Materialized View Advisor, which will generate a SQL script with the recommendations. You can query the returned rows the same as any other table, as shown in the example. MV_CUBE_ADVICE generates unique object names each time it is called. You should execute the function once, capture the results, and work with those SQL statements. Take care when dropping database objects. If a table already has a materialized view log, it will have the same name used in the SQL DROP MATERIALIZED VIEW LOG statement in the DROPTEXT column. You should avoid inadvertently dropping materialized view logs, especially when they may be used for remote data replication. Examples The following query displays the SQL statements recommended by MV_CUBE_ADVICE . UNITS_FACT is the master table for UNITS_CUBE , and MV_CUBE_ADVICE generates an ALTER TABLE command to add primary key constraints. It also generates an ALTER MATERIALIZED VIEW command to compile the CB$UNITS_CUBE cube materialized view. SQL> SELECT apiobject, sqlobject, sqltext FROM TABLE(dbms_cube_advise.mv_cube_advice('GLOBAL', 'CB$UNITS_CUBE')); APIOBJECT SQLOBJECT SQLTEXT ------------ --------------- --------------------------------------------- UNITS_CUBE UNITS_FACT alter table "GLOBAL"."UNITS_FACT" add constra int "COAD_PK000208" PRIMARY KEY ("CHANNEL_ID" , "ITEM_ID", "SHIP_TO_ID", "MONTH_ID") rely d isable novalidate UNITS_CUBE CB$UNITS_CUBE alter materialized view "GLOBAL"."CB$UNITS_CU BE" compile