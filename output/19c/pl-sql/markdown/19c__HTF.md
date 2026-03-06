---
id: 19c__HTF
name: HTF
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: HTF
tags: [htf]
source_file: HTF.html
---

# HTF

The commands in this example generate a simple HTML document.

## Syntax

```sql
CREATE OR REPLACE PROCEDURE hello AS
BEGIN
   HTP.P (HTF.HTMLOPEN); -- generates <HTML>
   HTP.P (HTF.HEADOPEN); -- generates <HEAD>
   HTP.P (HTF.TITLE('Hello')); -- generates <TITLE>Hello</TITLE>
   HTP.P (HTF.HEADCLOSE); -- generates </HEAD>
   HTP.P (HTF.BODYOPEN); -- generates <BODY>
   HTP.P (HTF.HEADER(1, 'Hello')); -- generates <H1>Hello</H1>
   HTP.P (HTF.BODYCLOSE); -- generates </BODY>
   HTP.P (HTF.HTMLCLOSE); -- generates </HTML>
END;
```

## Usage Notes

CREATE OR REPLACE PROCEDURE hello AS BEGIN HTP.P (HTF.HTMLOPEN); -- generates <HTML> HTP.P (HTF.HEADOPEN); -- generates <HEAD> HTP.P (HTF.TITLE('Hello')); -- generates <TITLE>Hello</TITLE> HTP.P (HTF.HEADCLOSE); -- generates </HEAD> HTP.P (HTF.BODYOPEN); -- generates <BODY> HTP.P (HTF.HEADER(1, 'Hello')); -- generates <H1>Hello</H1> HTP.P (HTF.BODYCLOSE); -- generates </BODY> HTP.P (HTF.HTMLCLOSE); -- generates </HTML> END;