---
id: 19c__DBMS_SYNC_REFRESH.CAN_SYNCREF_TABLE
name: DBMS_SYNC_REFRESH.CAN_SYNCREF_TABLE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SYNC_REFRESH
tags: [dbms_sync_refresh]
source_file: DBMS_SYNC_REFRESH.html
---

# DBMS_SYNC_REFRESH.CAN_SYNCREF_TABLE

This procedure advises on whether a table and its dependent materialized views are eligible for sync refresh. It provides an explanation of its analysis. If not eligible, you can examine the reasons and take appropriate action if possible.

## Syntax

```sql
DBMS_SYNC_REFRESH.CAN_SYNCREF_TABLE (
    schema_name    IN VARCHAR2,
    table_name     IN VARCHAR2,
    statement_id   IN VARCHAR2);

DBMS_SYNC_REFRESH.CAN_SYNCREF_TABLE (
    schema_name    IN VARCHAR2,
    table_name     IN VARCHAR2,
    output_array   IN OUT Sys.CanSyncRefTypeArray);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schema_name | VARCHAR2 | IN | The name of the schema of the base table. |
| table_name | VARCHAR2 | IN | The name of the base table. |
| statement_id | VARCHAR2) | IN | A string ( VARCHAR2(30) ) to identify the rows pertaining to an invocation of CAN_SYNCREF_TABLE when the output is directed to a table named SYNCREF_TABLE in the user's schema. |
| output_array | Sys.CanSyncRefTypeArray) | IN OUT | The output array into which CAN_SYNCREF_TABLE records the information on the eligibility of the base table and its dependent materialized views for synchronous refresh. |

## Usage Notes

This procedure lists all of the table's dependent materialized views and whether they qualify for sync refresh. Note that a materialized view may qualify for sync refresh even though the base table may not. The eligibility rules for materialized views for synchronous refresh are discussed in detail in Oracle Database Data Warehousing Guide. You can invoke CAN_SYNCREF_TABLE in two ways. The first is to use a table, while the second is to create a VARRAY . Syntax DBMS_SYNC_REFRESH.CAN_SYNCREF_TABLE ( schema_name IN VARCHAR2, table_name IN VARCHAR2, statement_id IN VARCHAR2); DBMS_SYNC_REFRESH.CAN_SYNCREF_TABLE ( schema_name IN VARCHAR2, table_name IN VARCHAR2, output_array IN OUT Sys.CanSyncRefTypeArray); Note that only one of statement_id or output_array need be provided to CAN_SYNCREF_TABLE . Parameters Table 173-4 CAN_SYNCREF_TABLE Procedure Parameters Parameter Description schema_name The name of the schema of the base table. table_name The name of the base table. statement_id A string ( VARCHAR2(30) ) to identify the rows pertaining to an invocation of CAN_SYNCREF_TABLE when the output is directed to a table named SYNCREF_TABLE in the user's schema. output_array The output array into which CAN_SYNCREF_TABLE records the information on the eligibility of the base table and its dependent materialized views for synchronous refresh. Using SYNCREF_TABLE The output of CAN_SYNCREF_TABLE can be directed to a table named SYNCREF_TABLE . The user is responsible for creating the SYNCREF_TABLE ; it can be dropped when it is no longer needed. Its structure is as follows: CREATE TABLE SYNCREF_TABLE ( statement_id VARCHAR2(30), schema_name VARCHAR2(30), table_name VARCHAR2(30), mv_schema_name VARCHAR2(30), mv_name VARCHAR2(30), eligible VARCHAR2(1), seq_num NUMBER, msg_number NUMBER, message VARCHAR2(4000)); Using a VARRAY You can save the output of CAN_SYNCREF_TABLE in a PL/SQL VARRAY . The elements of this array are of type CanSyncRefMessage , which is predefined in the SYS schema, as shown in the following: TYPE CanSyncRefMessage IS OBJECT ( schema_name VARCHAR2(30), table_name VARCHAR2(30), mv_schema_name VARCHAR2(30), mv_name VARCHAR2(30), eligible VARCHAR2(1), seq_num NUMBER, msg_number NUMBER, message VARCHAR2(4000)); The array type CanSyncRefArrayType , which is a varray of CanSyncRefMessage objects, is predefined in the SYS schema as follows: TYPE CanSyncRefArrayType AS VARRAY(256) OF CanSyncRefMessage; Each CanSyncRefMessage record provides a message concerning the eligibility of the base table or a dependent materialized view for synchronous refresh. The semantics of the fields is the same as that of the corresponding fields in the SYNCREF_TABLE . However, the SYNCREF_TABLE has a statement_id field which is absent in CanSyncRefMessage because no statement_id is supplied (because it is not required) when CAN_SYNCREF_TABLE is called with a VARRAY parameter.