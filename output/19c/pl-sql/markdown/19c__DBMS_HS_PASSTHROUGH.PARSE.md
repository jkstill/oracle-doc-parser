---
id: 19c__DBMS_HS_PASSTHROUGH.PARSE
name: DBMS_HS_PASSTHROUGH.PARSE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_HS_PASSTHROUGH
tags: [dbms_hs_passthrough]
source_file: DBMS_HS_PASSTHROUGH.html
---

# DBMS_HS_PASSTHROUGH.PARSE

This procedure parses an SQL statement at a non-Oracle system.

## Syntax

```sql
DBMS_HS_PASSTHROUGH.PARSE (
   c       IN  BINARY_INTEGER NOT NULL,
   stmt    IN  VARCHAR2 NOT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c | BINARY_INTEGER | IN | Cursor associated with the passthrough SQL statement. Cursor must be opened using function OPEN_CURSOR . |
| stmt | VARCHAR2 | IN | Statement to be parsed. |

## Usage Notes

Syntax DBMS_HS_PASSTHROUGH.PARSE ( c IN BINARY_INTEGER NOT NULL, stmt IN VARCHAR2 NOT NULL); Pragmas Purity level defined : WNDS, RNDS Parameters Table 85-27 PARSE Procedure Parameters Parameter Description c Cursor associated with the passthrough SQL statement. Cursor must be opened using function OPEN_CURSOR . stmt Statement to be parsed. Exceptions Table 85-28 PARSE Procedure Exceptions Exception Description ORA-28550 The cursor passed is invalid. ORA-28551 SQL statement is illegal. ORA-28555 A NULL value was passed for a NOT NULL parameter.