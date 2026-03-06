---
id: 19c__V$DIAG_ALERT_EXT
name: V$DIAG_ALERT_EXT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-DIAG_ALERT_EXT.html
---

# V$DIAG_ALERT_EXT

V$DIAG_ALERT_EXT shows the contents of the XML-based alert log in the Automatic Diagnostic Repository (ADR) for the current container (PDB).

## Columns

| Column | Type | Description |
|--------|------|-------------|
| ORIGINATING_TIMESTAMP | TIMESTAMP(9) WITH TIME ZONE |  |
| NORMALIZED_TIMESTAMP | TIMESTAMP(9) WITH TIME ZONE |  |
| ORGANIZATION_ID | VARCHAR2(67) |  |
| COMPONENT_ID | VARCHAR2(67) |  |
| HOST_ID | VARCHAR2(67) |  |
| HOST_ADDRESS | VARCHAR2(49) |  |
| MESSAGE_TYPE | NUMBER |  |
| MESSAGE_LEVEL | NUMBER |  |
| MESSAGE_ID | VARCHAR2(67) |  |
| MESSAGE_GROUP | VARCHAR2(67) |  |
| CLIENT_ID | VARCHAR2(67) |  |
| MODULE_ID | VARCHAR2(67) |  |
| PROCESS_ID | VARCHAR2(35) |  |
| THREAD_ID | VARCHAR2(67) |  |
| USER_ID | VARCHAR2(131) |  |
| INSTANCE_ID | VARCHAR2(67) |  |
| DETAILED_LOCATION | VARCHAR2(163) |  |
| UPSTREAM_COMP_ID | VARCHAR2(103) |  |
| DOWNSTREAM_COMP_ID | VARCHAR2(103) |  |
| EXECUTION_CONTEXT_ID | VARCHAR2(103) |  |
| EXECUTION_CONTEXT_SEQUENCE | NUMBER |  |
| ERROR_INSTANCE_ID | NUMBER |  |
| ERROR_INSTANCE_SEQUENCE | NUMBER |  |
| MESSAGE_TEXT | VARCHAR2(2051) |  |
| MESSAGE_ARGUMENTS | VARCHAR2(515) |  |
| SUPPLEMENTAL_ATTRIBUTES | VARCHAR2(515) |  |
| SUPPLEMENTAL_DETAILS | VARCHAR2(515) |  |
| PARTITION | NUMBER |  |
| RECORD_ID | NUMBER |  |
| FILENAME | VARCHAR2(515) |  |
| LOG_NAME | VARCHAR2(67) |  |
| PROBLEM_KEY | VARCHAR2(553) |  |
| VERSION | NUMBER |  |
| CON_UID | NUMBER |  |
| CONTAINER_ID | NUMBER |  |
| CONTAINER_NAME | VARCHAR2(33) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content