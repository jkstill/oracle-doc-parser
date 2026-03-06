---
id: 19c__V$DIAG_TRACE_FILE_CONTENTS
name: V$DIAG_TRACE_FILE_CONTENTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-DIAG_TRACE_FILE_CONTENTS.html
---

# V$DIAG_TRACE_FILE_CONTENTS

V$DIAG_TRACE_FILE_CONTENTS contains trace data that is present in the trace files that are part of the current Automatic Diagnostic Repository (ADR). This view also supports GV$ global views.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| ADR_HOME | VARCHAR2(444) |  |
| TRACE_FILENAME | VARCHAR2(68) |  |
| RECORD_LEVEL | NUMBER |  |
| PARENT_LEVEL | NUMBER |  |
| RECORD_TYPE | NUMBER |  |
| TIMESTAMP | TIMESTAMP(3) WITH TIME ZONE |  |
| PAYLOAD | VARCHAR2(4000) |  |
| SECTION_ID | NUMBER |  |
| SECTION_NAME | VARCHAR2(64) |  |
| COMPONENT_NAME | VARCHAR2(64) |  |
| OPERATION_NAME | VARCHAR2(64) |  |
| FILE_NAME | VARCHAR2(64) |  |
| FUNCTION_NAME | VARCHAR2(64) |  |
| LINE_NUMBER | NUMBER |  |
| THREAD_ID | VARCHAR2(64) |  |
| SESSION_ID | NUMBER |  |
| SERIAL# | NUMBER |  |
| CON_UID | NUMBER |  |
| CONTAINER_NAME | VARCHAR2(64) |  |
| CON_ID | NUMBER |  |