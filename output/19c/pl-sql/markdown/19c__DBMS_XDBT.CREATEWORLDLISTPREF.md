---
id: 19c__DBMS_XDBT.CREATEWORLDLISTPREF
name: DBMS_XDBT.CREATEWORLDLISTPREF
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDBT
tags: [dbms_xdbt]
source_file: DBMS_XDBT.html
---

# DBMS_XDBT.CREATEWORLDLISTPREF

This procedure creates a word list preference for the CONTEXT index on the XML DB hierarchy.

## Syntax

```sql
DBMS_XDBT.CREATEWORDLISTPREF;
```

## Usage Notes

Syntax DBMS_XDBT.CREATEWORDLISTPREF; Usage Notes The name of the word list preference can be modified; see the WordlistPref configuration setting. No other configuration settings are provided. FUZZY_MATCH and STEMMER attributes are set to AUTO (auto-language detection)