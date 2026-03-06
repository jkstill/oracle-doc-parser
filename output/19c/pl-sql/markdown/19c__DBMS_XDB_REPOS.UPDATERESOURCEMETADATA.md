---
id: 19c__DBMS_XDB_REPOS.UPDATERESOURCEMETADATA
name: DBMS_XDB_REPOS.UPDATERESOURCEMETADATA
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_REPOS
tags: [dbms_xdb_repos]
source_file: DBMS_XDB_REPOS.html
---

# DBMS_XDB_REPOS.UPDATERESOURCEMETADATA

This procedure updates metadata for a resource.

## Syntax

```sql
DBMS_XDB_REPOS.UPDATERESOURCEMETADATA(
   abspath  IN VARCHAR2,
   oldmetadata    IN   REF SYS.XMLTYPE,
   newmetadata    IN   REF SYS.XMLTYPE)
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| abspath | VARCHAR2 | IN | Absolute path of the resource |
| oldmetadata | REF | IN | REF to the old of metadata |
| newmetadata | REF | IN | REF to the new, replacement metadata (can be either schema-based or nonschema-based depending on the overload) |
| oldns |  |  | Namespace identifying old metadata |
| oldname |  |  | Local name identifying old metadata |

## Usage Notes

The procedure takes in a resource identified by absolute path and the metadata in it to replace identified by its REF . It replaces that piece of metadata with user-defined metadata which is either in the form of a REF to XMLTYPE or an XMLTYPE . Syntax Can be used to update schema-based metadata only. The new metadata must be schema-based: DBMS_XDB_REPOS.UPDATERESOURCEMETADATA( abspath IN VARCHAR2, oldmetadata IN REF SYS.XMLTYPE, newmetadata IN REF SYS.XMLTYPE) Can be used to update schema-based metadata only. The new metadata must be schema-based or nonschema-based: DBMS_XDB_REPOS.UPDATERESOURCEMETADATA( abspath IN VARCHAR2, oldmetadata IN REF SYS.XMLTYPE, newmetadata IN XMLTYPE); Can be used for both schema-based and nonschema-based metadata: DBMS_XDB_REPOS.UPDATERESOURCEMETADATA( abspath IN VARCHAR2, oldns IN VARCHAR2, oldname IN VARCHAR, newmetadata IN XMLTYPE); Can be used for both schema-based or nonschema-based metadata. New metadata must be schema-based: DBMS_XDB_REPOS.UPDATERESOURCEMETADATA( abspath IN VARCHAR2, oldns IN VARCHAR2, oldname IN VARCHAR, newmetadata IN REF SYS.XMLTYPE); Parameters Table 198-37 UPDATERESOURCEMETADATA Procedure Parameters Parameter Description abspath Absolute path of the resource oldmetadata REF to the old of metadata newmetadata REF to the new, replacement metadata (can be either schema-based or nonschema-based depending on the overload) oldns Namespace identifying old metadata oldname Local name identifying old metadata Usage Notes In the case of REF , it stores the REF in the resource and the metadata is stored in a separate table. Uniqueness of REFs is enforced. In the case where the XMLTYPE is passed in, data is parsed to determine if it is schema-based or not and is stored accordingly.