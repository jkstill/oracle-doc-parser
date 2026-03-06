---
id: 19c__OWA_UTIL.SHOWPAGE
name: OWA_UTIL.SHOWPAGE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: OWA_UTIL
tags: [owa_util]
source_file: OWA_UTIL.html
---

# OWA_UTIL.SHOWPAGE

This procedure prints out the HTML output of a procedure in SQL*Plus.

## Syntax

```sql
OWA_UTIL.SHOWPAGE;
```

## Usage Notes

The procedure must use the HTP or HTF packages to generate the HTML page, and this procedure must be issued after the HTP or HTF page-generating subprogram has been called and before any other HTP or HTF subprograms are directly or indirectly called. Syntax OWA_UTIL.SHOWPAGE; Usage Notes This method is useful for generating pages filled with static data. This procedure uses the DBMS_OUTPUT package and is limited to 32767 characters for each line and an overall buffer size of 1,000,000 bytes. Examples The output of htp procedure is displayed in SQL*Plus, SQL*DBA, or Oracle Server Manager. For example: SQL> set serveroutput on SQL> spool gretzky.html SQL> execute hockey.pass("Gretzky") SQL> execute owa_util.showpage SQL> exit This would generate an HTML page that could be accessed from Web browsers.