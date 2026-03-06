---
id: 19c__DBMS_OUTPUT.GET_LINES
name: DBMS_OUTPUT.GET_LINES
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_OUTPUT
tags: [dbms_output]
source_file: DBMS_OUTPUT.html
---

# DBMS_OUTPUT.GET_LINES

This procedure retrieves an array of lines from the buffer.

## Syntax

```sql
DBMS_OUTPUT.GET_LINES (
   lines       OUT     CHARARR,
   numlines    IN OUT  INTEGER);

DBMS_OUTPUT.GET_LINES (
   lines       OUT     DBMSOUTPUT_LINESARRAY,
   numlines    IN OUT INTEGER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| lines | CHARARR | OUT | Returns an array of lines of buffered information. The maximum length of each line in the array is 32767 bytes. It is recommended that you use the VARRAY overload version in a 3GL host program to execute the procedure from a PL/SQL anonymous block. |
| numlines | INTEGER) | IN OUT | Number of lines you want to retrieve from the buffer. After retrieving the specified number of lines, the procedure returns the number of lines actually retrieved. If this number is less than the number of lines requested, then there are no more lines in the buffer. |

## Usage Notes

Syntax DBMS_OUTPUT.GET_LINES ( lines OUT CHARARR, numlines IN OUT INTEGER); DBMS_OUTPUT.GET_LINES ( lines OUT DBMSOUTPUT_LINESARRAY, numlines IN OUT INTEGER); Parameters Table 120-5 GET_LINES Procedure Parameters Parameter Description lines Returns an array of lines of buffered information. The maximum length of each line in the array is 32767 bytes. It is recommended that you use the VARRAY overload version in a 3GL host program to execute the procedure from a PL/SQL anonymous block. numlines Number of lines you want to retrieve from the buffer. After retrieving the specified number of lines, the procedure returns the number of lines actually retrieved. If this number is less than the number of lines requested, then there are no more lines in the buffer. Usage Notes You can choose to retrieve from the buffer a single line or an array of lines. Call the GET_LINE procedure to retrieve a single line of buffered information. To reduce the number of calls to the server, call the GET_LINES procedure to retrieve an array of lines from the buffer. You can choose to automatically display this information if you are using SQL*Plus by using the special SET SERVEROUTPUT ON command. After calling GET_LINE or GET_LINES , any lines not retrieved before the next call to PUT , PUT_LINE , or NEW_LINE are discarded to avoid confusing them with the next message.