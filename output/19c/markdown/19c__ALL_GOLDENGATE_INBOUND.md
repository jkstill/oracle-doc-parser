---
id: 19c__ALL_GOLDENGATE_INBOUND
name: ALL_GOLDENGATE_INBOUND
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_GOLDENGATE_INBOUND.html
---

# ALL_GOLDENGATE_INBOUND

ALL_GOLDENGATE_INBOUND displays information about the GoldenGate inbound servers accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| REPLICAT_NAME | VARCHAR2(4000) | The name of the replicat group created from GGSCI using GoldenGate |
| SERVER_NAME | VARCHAR2(128) | Name of the inbound server |
| APPLY_USER | VARCHAR2(128) | Name of the user who can connect to the inbound server and apply messages |
| USER_COMMENT | VARCHAR2(4000) | User comment |
| CREATE_DATE | TIMESTAMP(6) | Date when inbound server was created |
| STATUS | VARCHAR2(8) | Status of the inbound server: DISABLED - The inbound server is not running. DETACHED - The inbound server is running, but the GoldenGate client application is not attached to it. ATTACHED - The inbound server is running, and the GoldenGate client application is attached to it. ABORTED - The inbound server became disabled because it encountered an error. |

## Usage Notes

Related View DBA_GOLDENGATE_INBOUND displays information about all GoldenGate inbound servers in the database. See Also: " DBA_GOLDENGATE_INBOUND " See Also: " DBA_GOLDENGATE_INBOUND "