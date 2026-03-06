---
id: 19c__DBMS_SYNC_REFRESH.REGISTER_MVIEWS
name: DBMS_SYNC_REFRESH.REGISTER_MVIEWS
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SYNC_REFRESH
tags: [dbms_sync_refresh]
source_file: DBMS_SYNC_REFRESH.html
---

# DBMS_SYNC_REFRESH.REGISTER_MVIEWS

This procedure registers a list of materialized views for synchronous refresh.

## Syntax

```sql
DBMS_SYNC_REFRESH.REGISTER_MVIEWS (
   mv_list   IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| mv_list | VARCHAR2) | IN | A comma-delimited list of materialized views to register. These names are optionally schema-qualified. |

## Usage Notes

It checks each materialized view in the list for eligibility and places it in the sync refresh group it belongs to. A sync refresh group is a set of related tables and materialized views defined on top of them. Two tables are considered related if there is a referential constraint between them. The eligibility rules of materialized views for synchronous refresh are described in detail in Oracle Database Data Warehousing Guide. The principal requirements are that the materialized view must be partitioned and its partition key must be derivable from the partition key of its fact table. The materialized view definition must specify the USING TRUSTED CONSTRAINTS clause because sync refresh trusts the foreign key and primary key relationships to perform various refresh optimizations. The materialized view's refresh policy must be specified as ON DEMAND . You have an option to register only some of the materialized views associated with a table, and leave some unregistered. Oracle Corporation does not recommend this, and in such a case, the user has to maintain the unregistered ones using the PCT or complete refresh methods. A staging table must have been created for each base table of each materialized view in the materialized view list ( mv_list ), or else an error is thrown. If any of the materialized views are not eligible for sync refresh, an error is thrown and the registration of all materialized views in the materialized view list fails. Syntax DBMS_SYNC_REFRESH.REGISTER_MVIEWS ( mv_list IN VARCHAR2); Parameter Table 173-12 REGISTER_MVIEWS Procedure Parameter Parameter Description mv_list A comma-delimited list of materialized views to register. These names are optionally schema-qualified.