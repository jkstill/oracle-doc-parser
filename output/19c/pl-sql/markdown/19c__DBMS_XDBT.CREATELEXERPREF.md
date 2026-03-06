---
id: 19c__DBMS_XDBT.CREATELEXERPREF
name: DBMS_XDBT.CREATELEXERPREF
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDBT
tags: [dbms_xdbt]
source_file: DBMS_XDBT.html
---

# DBMS_XDBT.CREATELEXERPREF

This procedure creates a BASIC lexer preference for the CONTEXT index on the XML DB hierarchy.

## Syntax

```sql
DBMS_XDBT.CREATELEXERPREF;
```

## Usage Notes

Syntax DBMS_XDBT.CREATELEXERPREF; Usage Notes The name of the lexer preference can be modified; see LexerPref configuration setting. No other configuration settings are provided. MultiLexer preferences are not supported. Base letter translation is turned on by default.