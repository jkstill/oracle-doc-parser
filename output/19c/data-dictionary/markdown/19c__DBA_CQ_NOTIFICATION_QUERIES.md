---
id: 19c__DBA_CQ_NOTIFICATION_QUERIES
name: DBA_CQ_NOTIFICATION_QUERIES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_CQ_NOTIFICATION_QUERIES.html
---

# DBA_CQ_NOTIFICATION_QUERIES

DBA_CQ_NOTIFICATION_QUERIES describes the registered queries for all CQ notifications in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| QUERYID | NUMBER | ID of the query |
| QUERYTEXT | CLOB | Text of the query |
| REGID | NUMBER | Registration ID that the query is registered with |
| USERNAME | VARCHAR2(31) | Name of the user who registered the query |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related View USER_CQ_NOTIFICATION_QUERIES describes the registered queries for the CQ notifications owned by the current user. This view does not display the USERNAME column. See Also: " USER_CQ_NOTIFICATION_QUERIES " See Also: " USER_CQ_NOTIFICATION_QUERIES "