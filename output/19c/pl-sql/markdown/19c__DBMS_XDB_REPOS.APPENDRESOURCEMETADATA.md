---
id: 19c__DBMS_XDB_REPOS.APPENDRESOURCEMETADATA
name: DBMS_XDB_REPOS.APPENDRESOURCEMETADATA
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_REPOS
tags: [dbms_xdb_repos]
source_file: DBMS_XDB_REPOS.html
---

# DBMS_XDB_REPOS.APPENDRESOURCEMETADATA

This procedure takes in user-defined metadata either as a REF to XMLTYPE or an XMLTYPE and adds it to the desired resource.

## Syntax

```sql
DBMS_XDB_REPOS.APPENDRESOURCEMETADATA (
 abspath   IN  VARCHAR2, 
 metadata  IN  XMLTYPE);

DBMS_XDB_REPOS.APPENDRESOURCEMETADATA (
 abspath   IN  VARCHAR2, 
 metadata  IN  REF SYS.XMLTYPE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| abspath | VARCHAR2 | IN | Absolute path of the resource |
| metadata | XMLTYPE) | IN | Metadata can be schema based or nonschema-based. Schema-based metadata is stored in its own table. |

## Usage Notes

Syntax DBMS_XDB_REPOS.APPENDRESOURCEMETADATA ( abspath IN VARCHAR2, metadata IN XMLTYPE); DBMS_XDB_REPOS.APPENDRESOURCEMETADATA ( abspath IN VARCHAR2, metadata IN REF SYS.XMLTYPE); Parameters Table 198-4 APPENDRESOURCEMETADATA Procedure Parameter Description abspath Absolute path of the resource metadata Metadata can be schema based or nonschema-based. Schema-based metadata is stored in its own table. Usage Notes In the case in which a REF is passed in, the procedure stores the REF in the resource, and the metadata is stored in a separate table. In this case you are responsible for populating the RESID column for the metadata table. Note that the REF passed in must be unique. In other words, there must not be a REF with the same value in the resource metadata, as this would violate uniqueness of properties. An error is thrown if users attempt to add a REF that already exists. In the case where the XMLTYPE is passed in, the data is parsed to determine if it is schema-based or not and stored accordingly.