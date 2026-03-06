---
id: 19c__DBMS_XMLINDEX.CREATENUMBERINDEX
name: DBMS_XMLINDEX.CREATENUMBERINDEX
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLINDEX
tags: [dbms_xmlindex]
source_file: DBMS_XMLINDEX.html
---

# DBMS_XMLINDEX.CREATENUMBERINDEX

This procedure creates a secondary index for number values in the VALUE column of a PATH TABLE which is the storage table of an XMLIndex .

## Syntax

```sql
DBMS_XMLINDEX.CREATENUMBERINDEX (
   xml_index_schema   IN   VARCHAR2,
   xml_index_name     IN   VARCHAR2,
   num_index_name     IN   VARCHAR2,
   num_index_clause   IN   VARCHAR2,
   xmltypename        IN   VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| xml_index_schema | VARCHAR2 | IN | Name of the owner of the XMLIndex |
| xml_index_name | VARCHAR2 | IN | Name of the XMLIndex |
| num_index_name | VARCHAR2 | IN | Name of the secondary index to be created for number values in the VALUE column of the PATH TABLE of XMLIndex named xml_index_name and owned by xml_index_schema |
| num_index_clause | VARCHAR2 | IN | Storage clause to be applied to the number index during its creation. This is a string argument appended to the CREATE INDEX statement for creating the number index. |
| xmltypename | VARCHAR2) | IN | The type to which values in the VALUE column of the path table are to be cast. Acceptable values are the following strings: FLOAT , DOUBLE , DECIMAL , INTEGER , NONPOSITIVEINTEGER , NEGATIVEINTEGER , LONG , INT , SHORT , BYTE , NONNEGATIVEINTEGER , UNSIGNEDLONG , UNSIGNEDINT , UNSIGNEDSHORT , UNSIGNEDBYTE , POSITIVEINTEGER . |

## Usage Notes

Syntax DBMS_XMLINDEX.CREATENUMBERINDEX ( xml_index_schema IN VARCHAR2, xml_index_name IN VARCHAR2, num_index_name IN VARCHAR2, num_index_clause IN VARCHAR2, xmltypename IN VARCHAR2); Parameters Table 206-3 CREATENUMBERINDEX Procedure Parameters Parameter Description xml_index_schema Name of the owner of the XMLIndex xml_index_name Name of the XMLIndex num_index_name Name of the secondary index to be created for number values in the VALUE column of the PATH TABLE of XMLIndex named xml_index_name and owned by xml_index_schema num_index_clause Storage clause to be applied to the number index during its creation. This is a string argument appended to the CREATE INDEX statement for creating the number index. xmltypename The type to which values in the VALUE column of the path table are to be cast. Acceptable values are the following strings: FLOAT , DOUBLE , DECIMAL , INTEGER , NONPOSITIVEINTEGER , NEGATIVEINTEGER , LONG , INT , SHORT , BYTE , NONNEGATIVEINTEGER , UNSIGNEDLONG , UNSIGNEDINT , UNSIGNEDSHORT , UNSIGNEDBYTE , POSITIVEINTEGER .