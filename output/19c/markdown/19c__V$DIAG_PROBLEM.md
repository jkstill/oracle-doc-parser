---
id: 19c__V$DIAG_PROBLEM
name: V$DIAG_PROBLEM
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-DIAG_PROBLEM.html
---

# V$DIAG_PROBLEM

V$DIAG_PROBLEM contains information about all problem metadata records present in the Automatic Diagnostic Repository (ADR) for the current container (PDB).

## Columns

| Column | Type | Description |
|--------|------|-------------|
| PROBLEM_ID | NUMBER |  |
| PROBLEM_KEY | VARCHAR2(552) |  |
| FIRST_INCIDENT | NUMBER |  |
| FIRSTINC_TIME | TIMESTAMP(9) WITH TIME ZONE |  |
| LAST_INCIDENT | NUMBER |  |
| LASTINC_TIME | TIMESTAMP(9) WITH TIME ZONE |  |
| IMPACT1 | NUMBER |  |
| IMPACT2 | NUMBER |  |
| IMPACT3 | NUMBER |  |
| IMPACT4 | NUMBER |  |
| SERVICE_REQUEST | VARCHAR2(66) |  |
| BUG_NUMBER | VARCHAR2(66) |  |
| CON_UID | NUMBER |  |
| CON_ID | NUMBER |  |