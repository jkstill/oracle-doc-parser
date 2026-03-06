---
id: 19c__DBMS_XMLINDEX.SYNCINDEX
name: DBMS_XMLINDEX.SYNCINDEX
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLINDEX
tags: [dbms_xmlindex]
source_file: DBMS_XMLINDEX.html
---

# DBMS_XMLINDEX.SYNCINDEX

This function synchronizes an asynchronously maintained XMLIndex.

## Syntax

```sql
DBMS_XMLINDEX.SYNCINDEX (
   xml_index_schema      IN VARCHAR2,
   xml_index_name        IN VARCHAR2,
   partition_name        IN VARCHAR2 DEFAULT NULL,
   reindex               IN BOOLEAN DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| xml_index_schema | VARCHAR2 | IN | Name of the owner of the XMLIndex |
| xml_schema_name |  |  | Name of the XMLIndex |
| partition_name | VARCHAR2 | IN | [Currently not supported] |
| reindex | BOOLEAN | IN | Default is FALSE . If set to TRUE , this drops the secondary indexes and recreates them later so that they can be bulk-loaded. |

## Usage Notes

It applies to the XMLIndex changes that are logged in the pending table, and brings the path table up-to-date with the base XMLTYPE column. Syntax DBMS_XMLINDEX.SYNCINDEX ( xml_index_schema IN VARCHAR2, xml_index_name IN VARCHAR2, partition_name IN VARCHAR2 DEFAULT NULL, reindex IN BOOLEAN DEFAULT FALSE); Parameters Table 206-8 SYNCINDEX Procedure Parameters Parameter Description xml_index_schema Name of the owner of the XMLIndex xml_schema_name Name of the XMLIndex partition_name [Currently not supported] reindex Default is FALSE . If set to TRUE , this drops the secondary indexes and recreates them later so that they can be bulk-loaded. Examples EXEC DBMS_XMLINDEX.SYNCINDEX('USER1', 'SS_TAB_XMLI', REINDEX=>TRUE);