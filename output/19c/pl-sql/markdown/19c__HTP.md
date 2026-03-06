---
id: 19c__HTP
name: HTP
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTP
tags: [htp]
source_file: HTP.html
---

# HTP

These commands generate a simple HTML document.

## Syntax

```sql
CREATE OR REPLACE PROCEDURE hello AS
BEGIN
    HTP.HTMLOPEN;           -- generates <HTML>
    HTP.HEADOPEN;           -- generates <HEAD>
    HTP.TITLE('Hello');     -- generates <TITLE>Hello</TITLE>
    HTP.HEADCLOSE;          -- generates </HEAD>
    HTP.BODYOPEN;           -- generates <BODY>
    HTP.HEADER(1, 'Hello'); -- generates <H1>Hello</H1>
    HTP.BODYCLOSE;          -- generates </BODY>
    HTP.HTMLCLOSE;          -- generates </HTML>
END;
```

## Usage Notes

CREATE OR REPLACE PROCEDURE hello AS BEGIN HTP.HTMLOPEN; -- generates <HTML> HTP.HEADOPEN; -- generates <HEAD> HTP.TITLE('Hello'); -- generates <TITLE>Hello</TITLE> HTP.HEADCLOSE; -- generates </HEAD> HTP.BODYOPEN; -- generates <BODY> HTP.HEADER(1, 'Hello'); -- generates <H1>Hello</H1> HTP.BODYCLOSE; -- generates </BODY> HTP.HTMLCLOSE; -- generates </HTML> END;