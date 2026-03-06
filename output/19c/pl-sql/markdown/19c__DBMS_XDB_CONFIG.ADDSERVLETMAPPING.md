---
id: 19c__DBMS_XDB_CONFIG.ADDSERVLETMAPPING
name: DBMS_XDB_CONFIG.ADDSERVLETMAPPING
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_CONFIG
tags: [dbms_xdb_config]
source_file: DBMS_XDB_CONFIG.html
---

# DBMS_XDB_CONFIG.ADDSERVLETMAPPING

This procedure adds a servlet mapping to XDB configuration.

## Syntax

```sql
<servlet-mapping>
     <servlet-pattern>pattern</servlet-pattern>
     <servlet-name>name</servlet-name>
</servlet-mapping>
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| pattern |  |  | Sservlet pattern |
| name |  |  | Servlet name |

## Usage Notes

It adds the following servlet mapping: <servlet-mapping> <servlet-pattern>pattern</servlet-pattern> <servlet-name>name</servlet-name> </servlet-mapping> Syntax DBMS_XDB_CONFIG.ADDSERVLETMAPPING( pattern IN VARCHAR2, name IN VARCHAR2); Parameters Table 196-7 ADDSERVLETMAPPING Procedure Parameters Parameter Description pattern Sservlet pattern name Servlet name