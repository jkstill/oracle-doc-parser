---
id: 19c__DBMS_XDB_CONFIG.ADDMIMEMAPPING
name: DBMS_XDB_CONFIG.ADDMIMEMAPPING
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_CONFIG
tags: [dbms_xdb_config]
source_file: DBMS_XDB_CONFIG.html
---

# DBMS_XDB_CONFIG.ADDMIMEMAPPING

This procedure adds the following mime mapping to XDB configuration:

## Syntax

```sql
<mime-mapping>
<extension>extension</extension>
<mime-type>mimetype</mime-type>
</mime-mapping>
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| extension |  |  | Extension for which a mime type is being added |
| mimetype |  |  | Mime type |

## Usage Notes

<mime-mapping> <extension>extension</extension> <mime-type>mimetype</mime-type> </mime-mapping> Syntax DBMS_XDB_CONFIG.ADDMIMEMAPPING( extension IN VARCHAR2, mimetype IN VARCHAR2); Parameters Table 196-4 ADDMIMEMAPPING Procedure Parameters Parameter Description extension Extension for which a mime type is being added mimetype Mime type