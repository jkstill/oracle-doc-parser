---
id: 19c__DBMS_XSTREAM_ADM.SET_MESSAGE_TRACKING
name: DBMS_XSTREAM_ADM.SET_MESSAGE_TRACKING
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XSTREAM_ADM
tags: [dbms_xstream_adm]
source_file: DBMS_XSTREAM_ADM.html
---

# DBMS_XSTREAM_ADM.SET_MESSAGE_TRACKING

This procedure sets the tracking label for logical change records (LCRs) produced by the current session.

## Syntax

```sql
DBMS_XSTREAM_ADM.SET_MESSAGE_TRACKING(
   tracking_label IN VARCHAR2  DEFAULT 'Streams_tracking',
   actions        IN NUMBER    DEFAULT DBMS_XSTREAM_ADM.ACTION_MEMORY);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| tracking_label | VARCHAR2 | IN | The label used to track the LCRs produced by the session. Set this parameter to NULL to stop message tracking in the current session. The size limit for a label is 4,000 bytes. |
| actions | NUMBER | IN | When DBMS_XSTREAM_ADM.ACTION_MEMORY is specified, the LCRs are tracked in memory. Currently, DBMS_XSTREAM_ADM.ACTION_MEMORY is the only valid setting for this parameter. The value specified for this parameter is an enumerated constant. Enumerated constants must be prefixed with the package name. |

## Usage Notes

This procedure affects only the current session. Any LCRs produced by the current session are tracked, including captured LCRs and persistent LCRs. Note: The tracking label set by this procedure does not track non-LCR messages. See Also: KAWGET_MESSAGE_TRACKING Note: The tracking label set by this procedure does not track non-LCR messages. See Also: KAWGET_MESSAGE_TRACKING Syntax DBMS_XSTREAM_ADM.SET_MESSAGE_TRACKING( tracking_label IN VARCHAR2 DEFAULT 'Streams_tracking', actions IN NUMBER DEFAULT DBMS_XSTREAM_ADM.ACTION_MEMORY); Parameters Table 217-32 SET_MESSAGE_TRACKING Procedure Parameters Parameter Description tracking_label The label used to track the LCRs produced by the session. Set this parameter to NULL to stop message tracking in the current session. The size limit for a label is 4,000 bytes. actions When DBMS_XSTREAM_ADM.ACTION_MEMORY is specified, the LCRs are tracked in memory. Currently, DBMS_XSTREAM_ADM.ACTION_MEMORY is the only valid setting for this parameter. The value specified for this parameter is an enumerated constant. Enumerated constants must be prefixed with the package name.