---
id: 19c__DBMS_OUTPUT.PUT_LINE
name: DBMS_OUTPUT.PUT_LINE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_OUTPUT
tags: [dbms_output]
source_file: DBMS_OUTPUT.html
---

# DBMS_OUTPUT.PUT_LINE

This procedure places a line in the buffer.

## Syntax

```sql
DBMS_OUTPUT.PUT_LINE (
   item IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| item | VARCHAR2) | IN | Item to buffer. |

## Usage Notes

Note: The PUT_LINE procedure that takes a NUMBER is obsolete and, while currently supported, is included in this release for legacy reasons only. Note: The PUT_LINE procedure that takes a NUMBER is obsolete and, while currently supported, is included in this release for legacy reasons only. Syntax DBMS_OUTPUT.PUT_LINE ( item IN VARCHAR2); Parameters Table 120-8 PUT_LINE Procedure Parameters Parameter Description item Item to buffer. Exceptions Table 120-9 PUT_LINE Procedure Exceptions Error Description ORA-20000, ORU-10027: Buffer overflow, limit of < buf_limit > bytes. ORA-20000, ORU-10028: Line length overflow, limit of 32767 bytes for each line.