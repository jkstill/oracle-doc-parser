---
id: 19c__DBMS_DBFS_CONTENT.TRACE
name: DBMS_DBFS_CONTENT.TRACE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.TRACE

This procedure outputs tracing to the current foreground trace file.

## Syntax

```sql
DBMS_DBFS_CONTENT.TRACE
   sev         IN              INTEGER,
   msg0        IN              VARCHAR2,
   msg1        IN              VARCHAR     DEFAULT '',
   msg2        IN              VARCHAR     DEFAULT '',
   msg3        IN              VARCHAR     DEFAULT '',
   msg4        IN              VARCHAR     DEFAULT '',
   msg5        IN              VARCHAR     DEFAULT '',
   msg6        IN              VARCHAR     DEFAULT '',
   msg7        IN              VARCHAR     DEFAULT '',
   msg8        IN              VARCHAR     DEFAULT '',
   msg9        IN              VARCHAR     DEFAULT '',
   msg10       IN              VARCHAR     DEFAULT '');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| sev | INTEGER | IN | Severity at which trace message is output |
| msg* |  |  | One or more message strings to be output. If more than one message is specified, all are output. |

## Usage Notes

Syntax DBMS_DBFS_CONTENT.TRACE sev IN INTEGER, msg0 IN VARCHAR2, msg1 IN VARCHAR DEFAULT '', msg2 IN VARCHAR DEFAULT '', msg3 IN VARCHAR DEFAULT '', msg4 IN VARCHAR DEFAULT '', msg5 IN VARCHAR DEFAULT '', msg6 IN VARCHAR DEFAULT '', msg7 IN VARCHAR DEFAULT '', msg8 IN VARCHAR DEFAULT '', msg9 IN VARCHAR DEFAULT '', msg10 IN VARCHAR DEFAULT ''); Parameters Table 52-75 TRACE Procedure Parameters Parameter Description sev Severity at which trace message is output msg* One or more message strings to be output. If more than one message is specified, all are output. Usage Notes Trace information is written to the foreground trace file, with varying levels of detail as specified by the trace level arguments. The global trace level consists of 2 components: "severity" and "detail". These can be thought of as additive bitmasks. The "severity" allows the separation of top level as compared to low-level tracing of different components, and allows the amount of tracing to be increased as needed. There are no semantics associated with different levels, and users are free to set trace at any severity they choose, although a good rule of thumb would use severity " 1 " for top level API entry and exit traces, " 2 " for internal operations, and " 3 " or greater for very low-level traces. The "detail" controls how much additional information: timestamps, short-stack, etc. is dumped along with each trace record.