---
id: 19c__DBMS_OUTPUT.PUT
name: DBMS_OUTPUT.PUT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_OUTPUT
tags: [dbms_output]
source_file: DBMS_OUTPUT.html
---

# DBMS_OUTPUT.PUT

This procedure places a partial line in the buffer.

## Syntax

```sql
DBMS_OUTPUT.PUT (
    item IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| item | VARCHAR2) | IN | Item to buffer. |

## Usage Notes

Note: The PUT procedure that takes a NUMBER is obsolete and, while currently supported, is included in this release for legacy reasons only. Note: The PUT procedure that takes a NUMBER is obsolete and, while currently supported, is included in this release for legacy reasons only. Syntax DBMS_OUTPUT.PUT ( item IN VARCHAR2); Parameters Table 120-6 PUT Procedure Parameters Parameter Description item Item to buffer. Exceptions Table 120-7 PUT Procedure Exceptions Error Description ORA-20000, ORU-10027: Buffer overflow, limit of < buf_limit > bytes. ORA-20000, ORU-10028: Line length overflow, limit of 32767 bytes for each line.