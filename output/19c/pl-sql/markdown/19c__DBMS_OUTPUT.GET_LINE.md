---
id: 19c__DBMS_OUTPUT.GET_LINE
name: DBMS_OUTPUT.GET_LINE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_OUTPUT
tags: [dbms_output]
source_file: DBMS_OUTPUT.html
---

# DBMS_OUTPUT.GET_LINE

This procedure retrieves a single line of buffered information.

## Syntax

```sql
DBMS_OUTPUT.GET_LINE (
   line    OUT VARCHAR2,
   status  OUT INTEGER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| line | VARCHAR2 | OUT | Returns a single line of buffered information, excluding a final newline character. You should declare the actual for this parameter as VARCHAR2 (32767) to avoid the risk of " ORA-06502 : PL/SQL: numeric or value error: character string buffer too small". |
| status | INTEGER) | OUT | If the call completes successfully, then the status returns as 0. If there are no more lines in the buffer, then the status is 1. |

## Usage Notes

Syntax DBMS_OUTPUT.GET_LINE ( line OUT VARCHAR2, status OUT INTEGER); Parameters Table 120-4 GET_LINE Procedure Parameters Parameter Description line Returns a single line of buffered information, excluding a final newline character. You should declare the actual for this parameter as VARCHAR2 (32767) to avoid the risk of " ORA-06502 : PL/SQL: numeric or value error: character string buffer too small". status If the call completes successfully, then the status returns as 0. If there are no more lines in the buffer, then the status is 1. Usage Notes You can choose to retrieve from the buffer a single line or an array of lines. Call the GET_LINE procedure to retrieve a single line of buffered information. To reduce the number of calls to the server, call the GET_LINES procedure to retrieve an array of lines from the buffer. You can choose to automatically display this information if you are using SQL*Plus by using the special SET SERVEROUTPUT ON command. After calling GET_LINE or GET_LINES , any lines not retrieved before the next call to PUT , PUT_LINE , or NEW_LINE are discarded to avoid confusing them with the next message.