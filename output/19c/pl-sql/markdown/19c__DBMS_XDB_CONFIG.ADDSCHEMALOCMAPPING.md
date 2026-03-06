---
id: 19c__DBMS_XDB_CONFIG.ADDSCHEMALOCMAPPING
name: DBMS_XDB_CONFIG.ADDSCHEMALOCMAPPING
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_CONFIG
tags: [dbms_xdb_config]
source_file: DBMS_XDB_CONFIG.html
---

# DBMS_XDB_CONFIG.ADDSCHEMALOCMAPPING

This procedure adds the following schema location mapping to the XDB configuration:

## Syntax

```sql
<schemaLocation-mapping>
     <namespace>namespace</namespace>
     <element>element</element>
      <schemaURL>schemaURL</schemaURL>
</schemaLocation-mapping>
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| namespace |  |  | Namespace |
| element |  |  | Element |
| schemaURL |  |  | Schema URL |

## Usage Notes

<schemaLocation-mapping> <namespace>namespace</namespace> <element>element</element> <schemaURL>schemaURL</schemaURL> </schemaLocation-mapping> Syntax DBMS_XDB_CONFIG.ADDSCHEMALOCMAPPING( namespace IN VARCHAR2, element IN VARCHAR2, schemaURL IN VARCHAR2); Parameters Table 196-5 ADDSCHEMALOCMAPPING Procedure Parameters Parameter Description namespace Namespace element Element schemaURL Schema URL