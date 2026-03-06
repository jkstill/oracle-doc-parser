---
id: 19c__DBMS_LOB.SETCONTENTTYPE
name: DBMS_LOB.SETCONTENTTYPE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOB
tags: [dbms_lob]
source_file: DBMS_LOB.html
---

# DBMS_LOB.SETCONTENTTYPE

This procedure sets the content type string for the data in the LOB.

## Syntax

```sql
DBMS_LOB.SETCONTENTTYPE (
   lob_loc      IN OUT NOCOPY BLOB,
   contenttype  IN            VARCHAR2);

DBMS_LOB.SETCONTENTTYPE (
   lob_loc     IN OUT NOCOPY CLOB CHARACTER SET ANY_CS,
   contenttype IN            VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| lob_loc | NOCOPY | IN OUT | LOB to be assigned the content type |
| contenttype | VARCHAR2) | IN | String to be assigned |

## Usage Notes

Syntax DBMS_LOB.SETCONTENTTYPE ( lob_loc IN OUT NOCOPY BLOB, contenttype IN VARCHAR2); DBMS_LOB.SETCONTENTTYPE ( lob_loc IN OUT NOCOPY CLOB CHARACTER SET ANY_CS, contenttype IN VARCHAR2); Parameters Table 99-91 SETCONTENTTYPE Procedure Parameters Parameter Description lob_loc LOB to be assigned the content type contenttype String to be assigned Exceptions Table 99-92 SETCONTENTTYPE Procedure Exceptions Exception Description SECUREFILE_BADLOB lob_loc is not a SECUREFILE Usage Notes To clear an existing content type associated with a SECUREFILE , invoke SETCONTENTTYPE with contenttype set to empty string.