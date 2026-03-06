---
id: 19c__DBMS_TRACE
name: DBMS_TRACE
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_TRACE
tags: [dbms_trace]
source_file: DBMS_TRACE.html
---

# DBMS_TRACE

Certain operational notes apply to DBMS_TRACE .

## Syntax

```sql
alter session set plsql_debug=true; 
create or replace ... /* create the library units - debug information will be generated */
```

## Usage Notes

These are described in the following sections: Controlling Data Volume Creating Database Tables to Collect DBMS_TRACE Output Collecting Trace Data Collected Data Trace Control Controlling Data Volume Profiling large applications may produce a large volume of data. You can control the volume of data collected by enabling specific program units for trace data collection. You can enable a program unit by compiling it debug. This can be done in one of two ways: alter session set plsql_debug=true; create or replace ... /* create the library units - debug information will be generated */ or: /* recompile specific library unit with debug option */ alter [PROCEDURE | FUNCTION | PACKAGE BODY] <libunit-name> compile debug; Note: You cannot use the second method for anonymous blocks. You can limit the amount of storage used in the database by retaining only the most recent 8,192 records (approximately) by including TRACE_LIMIT in the TRACE_LEVEL parameter of the SET_PLSQL_TRACE procedure. Note: You cannot use the second method for anonymous blocks. Creating Database Tables to Collect DBMS_TRACE Output You must create database tables into which the DBMS_TRACE package writes output. Otherwise, the data is not collected. To create these tables, run the script TRACETAB.SQL . The tables this script creates are owned by SYS. Collecting Trace Data The PL/SQL features you can trace are described in the script DBMSPBT.SQL . Some of the key tracing features are: Tracing Calls Tracing Exceptions Tracing SQL Tracing Lines Additional features of DBMS_TRACE also allow pausing and resuming trace, and limiting the output.