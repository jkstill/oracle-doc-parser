---
id: 19c__ALL_XSTREAM_INBOUND
name: ALL_XSTREAM_INBOUND
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_XSTREAM_INBOUND.html
---

# ALL_XSTREAM_INBOUND

ALL_XSTREAM_INBOUND displays information about the XStream inbound servers accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SERVER_NAME | VARCHAR2(128) | Name of the inbound server |
| QUEUE_OWNER | VARCHAR2(128) | Owner of the queue associated with the inbound server |
| QUEUE_NAME | VARCHAR2(128) | Name of the queue associated with the inbound server |
| APPLY_USER | VARCHAR2(128) | Name of the user who can connect to the inbound server and apply messages |
| USER_COMMENT | VARCHAR2(4000) | User comment |
| CREATE_DATE | TIMESTAMP(6) | Date when the inbound server was created |
| STATUS | VARCHAR2(8) | Status of the inbound server: DISABLED - The inbound server is not running. DETACHED - The inbound server is running, but the XStream client application is not attached to it. ATTACHED - The inbound server is running, and the XStream client application is attached to it. ABORTED - The inbound server became disabled because it encountered an error. |
| COMMITTED_DATA_ONLY | VARCHAR2(3) | YES - means the inbound server can receive only LCRs in committed transactions from the XStream client application. A committed transaction is an assembled, noninterleaving transaction with no rollbacks. |

## Usage Notes

Related View DBA_XSTREAM_INBOUND displays information about all XStream inbound servers in the database. See Also: " DBA_XSTREAM_INBOUND " See Also: " DBA_XSTREAM_INBOUND "