---
id: 19c__V$DIAG_INCIDENT
name: V$DIAG_INCIDENT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-DIAG_INCIDENT.html
---

# V$DIAG_INCIDENT

V$DIAG_INCIDENT contains information about all incident metadata records present in the Automatic Diagnostic Repository (ADR) for the current container (PDB).

## Columns

| Column | Type | Description |
|--------|------|-------------|
| INCIDENT_ID | NUMBER |  |
| PROBLEM_ID | NUMBER |  |
| CREATE_TIME | TIMESTAMP(9) WITH TIME ZONE |  |
| CLOSE_TIME | TIMESTAMP(9) WITH TIME ZONE |  |
| STATUS | NUMBER |  |
| FLAGS | NUMBER |  |
| FLOOD_CONTROLLED | NUMBER |  |
| ERROR_FACILITY | VARCHAR2(12) |  |
| ERROR_NUMBER | NUMBER |  |
| ERROR_ARG1 | VARCHAR2(66) |  |
| ERROR_ARG2 | VARCHAR2(66) |  |
| ERROR_ARG3 | VARCHAR2(66) |  |
| ERROR_ARG4 | VARCHAR2(66) |  |
| ERROR_ARG5 | VARCHAR2(66) |  |
| ERROR_ARG6 | VARCHAR2(66) |  |
| ERROR_ARG7 | VARCHAR2(66) |  |
| ERROR_ARG8 | VARCHAR2(66) |  |
| SIGNALLING_COMPONENT | VARCHAR2(66) |  |
| SIGNALLING_SUBCOMPONENT | VARCHAR2(66) |  |
| SUSPECT_COMPONENT | VARCHAR2(66) |  |
| SUSPECT_SUBCOMPONENT | VARCHAR2(66) |  |
| ECID | VARCHAR2(66) |  |
| IMPACT | NUMBER |  |
| ERROR_ARG9 | VARCHAR2(66) |  |
| ERROR_ARG10 | VARCHAR2(66) |  |
| ERROR_ARG11 | VARCHAR2(66) |  |
| ERROR_ARG12 | VARCHAR2(66) |  |
| CON_UID | NUMBER |  |
| CON_ID | NUMBER |  |