---
id: 19c__DBMS_SESSION.SET_NLS
name: DBMS_SESSION.SET_NLS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SESSION
tags: [dbms_session]
source_file: DBMS_SESSION.html
---

# DBMS_SESSION.SET_NLS

This procedure sets up your Globalization Support (NLS). It is equivalent to the SQL statement: ALTER SESSION SET <nls_parameter> = <value> .

## Syntax

```sql
DBMS_SESSION.SET_NLS (
   param VARCHAR2, 
   value VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| param | VARCHAR2 | IN | Globalization Support parameter. The parameter name must begin with 'NLS'. |
| value | VARCHAR2) | IN | Parameter value. If the parameter is a text literal, then it needs embedded single-quotes. For example, " set_nls (' nls_date_format ',''' DD-MON-YY ''')". |

## Usage Notes

Syntax DBMS_SESSION.SET_NLS ( param VARCHAR2, value VARCHAR2); Parameters Table 154-21 SET_NLS Procedure Parameters Parameter Description param Globalization Support parameter. The parameter name must begin with 'NLS'. value Parameter value. If the parameter is a text literal, then it needs embedded single-quotes. For example, " set_nls (' nls_date_format ',''' DD-MON-YY ''')".