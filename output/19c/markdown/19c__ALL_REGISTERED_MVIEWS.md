---
id: 19c__ALL_REGISTERED_MVIEWS
name: ALL_REGISTERED_MVIEWS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: objects
tags: [all]
source_file: ALL_REGISTERED_MVIEWS.html
---

# ALL_REGISTERED_MVIEWS

ALL_REGISTERED_MVIEWS describes all registered materialized views (registered at a master site or a master materialized view site) accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the materialized view |
| NAME | VARCHAR2(128) | Name of the materialized view |
| MVIEW_SITE | VARCHAR2(128) | Global name of the materialized view site |
| CAN_USE_LOG | VARCHAR2(3) | Indicates whether the materialized view can use a materialized view log ( YES ) or the materialized view is too complex to use a log ( NO ) |
| UPDATABLE | VARCHAR2(3) | Indicates whether the materialized view is updatable ( YES ) or not and the materialized view is read only ( NO ) |
| REFRESH_METHOD | VARCHAR2(11) | Indicates whether the materialized view uses primary key ( PRIMARY KEY ), rowids ( ROWID ), or object identifiers ( OBJECT ID ) for fast refresh |
| MVIEW_ID | NUMBER(38) | Identifier for the materialized view used by the masters for fast refresh |
| VERSION | VARCHAR2(26) | Oracle version of the materialized view Note: Oracle Database materialized views show ORACLE 8 MATERIALIZED VIEW . |
| QUERY_TXT | LONG | Query that defines the materialized view |

## Usage Notes

A materialized view created with the BUILD DEFERRED option of the CREATE MATERIALIZED VIEW statement is only registered with ALL_REGISTERED_MVIEWS if that materialized view has been completely refreshed at least once. Related Views DBA_REGISTERED_MVIEWS describes all registered materialized views in the database. USER_REGISTERED_MVIEWS describes all registered materialized views owned by the current user. See Also: " DBA_REGISTERED_MVIEWS " " USER_REGISTERED_MVIEWS " See Also: " DBA_REGISTERED_MVIEWS " " USER_REGISTERED_MVIEWS "