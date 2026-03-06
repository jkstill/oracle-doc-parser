---
id: 19c__DBMS_XDB_CONFIG.ADDXMLEXTENSION
name: DBMS_XDB_CONFIG.ADDXMLEXTENSION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_CONFIG
tags: [dbms_xdb_config]
source_file: DBMS_XDB_CONFIG.html
---

# DBMS_XDB_CONFIG.ADDXMLEXTENSION

This procedure adds an XML extension to the XDB configuration under <xml-extensions> .

## Syntax

```sql
<extension>extension</extension>
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| extension |  |  | XML extension to be added |

## Usage Notes

It adds the following XML extension to the XDB configuration, under <xml-extensions> : <extension>extension</extension> Syntax DBMS_XDB_CONFIG.ADDXMLEXTENSION( extension IN VARCHAR2); Parameters Table 196-9 ADDXMLEXTENSION Procedure Parameters Parameter Description extension XML extension to be added