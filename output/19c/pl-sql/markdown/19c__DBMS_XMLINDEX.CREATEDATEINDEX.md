---
id: 19c__DBMS_XMLINDEX.CREATEDATEINDEX
name: DBMS_XMLINDEX.CREATEDATEINDEX
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLINDEX
tags: [dbms_xmlindex]
source_file: DBMS_XMLINDEX.html
---

# DBMS_XMLINDEX.CREATEDATEINDEX

This procedure creates a secondary index for date values in the VALUE column of a PATH TABLE which is the storage table of an XMLIndex . The second form of the procedure allows for the date_index_clause to be set to an empty string.

## Syntax

```sql
DBMS_XMLINDEX.CREATEDATEINDEX  (
   xml_index_schema   IN   VARCHAR2,
   xml_index_name     IN   VARCHAR2,
   date_index_name    IN   VARCHAR2,
   xmltypename        IN   VARCHAR2,
   date_index_clause  IN   VARCHAR2);

DBMS_XMLINDEX.CREATEDATEINDEX  (
   xml_index_schema   IN   VARCHAR2
   xml_index_name     IN   VARCHAR2,
   date_index_name    IN   VARCHAR2,
   xmltypename        IN   VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| xml_index_schema | VARCHAR2 | IN | Name of the owner of the XMLIndex |
| xml_index_name | VARCHAR2 | IN | Name of the XMLIndex |
| date_index_name | VARCHAR2 | IN | Name of the secondary index to be created for date values in the VALUE column of the PATH TABLE of XMLIndex named xml_index_name and owned by xml_index_schema |
| xmltypename | VARCHAR2 | IN | The type to which values in the VALUE column of the path table are to be cast. Acceptable values are the following strings: DATETIME , TIME , DATE , GDAY , GMONTH , GYEAR , GYEARMONTH , GMONTHDAY . |
| date_index_clause | VARCHAR2) | IN | Storage clause to be applied to the date index during its creation. This is a string argument appended to the CREATE INDEX statement for creating the date index |

## Usage Notes

Syntax DBMS_XMLINDEX.CREATEDATEINDEX ( xml_index_schema IN VARCHAR2, xml_index_name IN VARCHAR2, date_index_name IN VARCHAR2, xmltypename IN VARCHAR2, date_index_clause IN VARCHAR2); DBMS_XMLINDEX.CREATEDATEINDEX ( xml_index_schema IN VARCHAR2 xml_index_name IN VARCHAR2, date_index_name IN VARCHAR2, xmltypename IN VARCHAR2); Parameters Table 206-2 CREATEDATEINDEX Procedure Parameters Parameter Description xml_index_schema Name of the owner of the XMLIndex xml_index_name Name of the XMLIndex date_index_name Name of the secondary index to be created for date values in the VALUE column of the PATH TABLE of XMLIndex named xml_index_name and owned by xml_index_schema xmltypename The type to which values in the VALUE column of the path table are to be cast. Acceptable values are the following strings: DATETIME , TIME , DATE , GDAY , GMONTH , GYEAR , GYEARMONTH , GMONTHDAY . date_index_clause Storage clause to be applied to the date index during its creation. This is a string argument appended to the CREATE INDEX statement for creating the date index