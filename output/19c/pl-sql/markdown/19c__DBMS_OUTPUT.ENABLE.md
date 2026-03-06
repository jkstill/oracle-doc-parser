---
id: 19c__DBMS_OUTPUT.ENABLE
name: DBMS_OUTPUT.ENABLE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_OUTPUT
tags: [dbms_output]
source_file: DBMS_OUTPUT.html
---

# DBMS_OUTPUT.ENABLE

This procedure enables calls to PUT , PUT_LINE , NEW_LINE , GET_LINE , and GET_LINES .

## Syntax

```sql
DBMS_OUTPUT.ENABLE (
   buffer_size IN INTEGER DEFAULT 20000);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| buffer_size | INTEGER | IN | Upper limit, in bytes, the amount of buffered information. Setting buffer_size to NULL specifies that there should be no limit. |

## Usage Notes

Calls to these procedures are ignored if the DBMS_OUTPUT package is not activated. Syntax DBMS_OUTPUT.ENABLE ( buffer_size IN INTEGER DEFAULT 20000); Pragmas pragma restrict_references(enable,WNDS,RNDS); Parameters Table 120-3 ENABLE Procedure Parameters Parameter Description buffer_size Upper limit, in bytes, the amount of buffered information. Setting buffer_size to NULL specifies that there should be no limit. Usage Notes It is not necessary to call this procedure when you use the SET SERVEROUTPUT option of SQL*Plus. If there are multiple calls to ENABLE , then buffer_size is the last of the values specified. The maximum size is 1,000,000, and the minimum is 2,000 when the user specifies buffer_size ( NOT NULL ). NULL is expected to be the usual choice. The default is 20,000 for backwards compatibility with earlier database versions that did not support unlimited buffering.