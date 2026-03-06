---
id: 19c__DBMS_XDB.DELETERESOURCEMETADATA
name: DBMS_XDB.DELETERESOURCEMETADATA
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB
tags: [dbms_xdb]
source_file: DBMS_XDB.html
---

# DBMS_XDB.DELETERESOURCEMETADATA

This deprecated procedure takes in a resource by absolute path and removes either the schema-based metadata identified by the REF, or the metadata identified by the namespace and name combination, which can be either schema-based or non-schema based. It also takes an additional (optional) parameter that specifies how to delete it. This parameter is only relevant for schema-based resource metadata that needs to be deleted. For non-schema based metadata, this parameter is ignored.

## Syntax

```sql
DBMS_XDB.DELETERESOURCEMETADATA (
   abspath        IN  VARCHAR2, 
   metadata       IN  REF SYS.XMLTYPE,
   delete_option  IN  pls_integer := dbms_xdb.DELETE_RESOURCE_METADATA_CASCADE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| abspath | VARCHAR2 | IN | Absolute path of the resource |
| metadata | REF | IN | REF to the piece of metadata (schema based) to be deleted |
| mettadatans |  |  | Namespace of the metadata fragment to be removed |
| mettadataname |  |  | Local name of the metadata fragment to be removed |
| delete_option | pls_integer | IN | Only applicable for schema-based metadata, this can be one of the following: DELETE_RES_METADATA_CASCADE - deletes the corresponding row in the metadata table DELETE_RES_METADATA_NOCASCADE - does not delete the row in the metadata table |

## Usage Notes

Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the DELETERESOURCEMETADATA Procedures . Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the DELETERESOURCEMETADATA Procedures . Syntax Can be used only for schema-based metadata: DBMS_XDB.DELETERESOURCEMETADATA ( abspath IN VARCHAR2, metadata IN REF SYS.XMLTYPE, delete_option IN pls_integer := dbms_xdb.DELETE_RESOURCE_METADATA_CASCADE); Can be used for schema-based or nonschema-based metadata: DBMS_XDB.DELETERESOURCEMETADATA ( abspath IN VARCHAR2, metadatans IN VARCHAR2, metadataname IN VARCHAR2, delete_option IN pls_integer := dbms_xdb.DELETE_RESOURCE_METADATA_CASCADE); Parameters Table 194-12 DELETERESOURCEMETADATA Procedure Parameters Parameter Description abspath Absolute path of the resource metadata REF to the piece of metadata (schema based) to be deleted mettadatans Namespace of the metadata fragment to be removed mettadataname Local name of the metadata fragment to be removed delete_option Only applicable for schema-based metadata, this can be one of the following: DELETE_RES_METADATA_CASCADE - deletes the corresponding row in the metadata table DELETE_RES_METADATA_NOCASCADE - does not delete the row in the metadata table