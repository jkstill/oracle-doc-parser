---
id: 19c__RESOURCE_VIEW
name: RESOURCE_VIEW
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: objects
source_file: RESOURCE_VIEW.html
---

# RESOURCE_VIEW

RESOURCE_VIEW contains one row for each resource in the Oracle XML DB repository.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| RES | XMLTYPE(XMLSchema "http://xmlns.oracle.com/xdb/XDBResource.xsd" Element "Resource") | A resource in the repository |
| ANY_PATH | VARCHAR2(4000) | An (absolute) path to the resource |
| RESID | RAW(16) | Resource OID, which is a unique handle to the resource |

## Usage Notes

See Also: Oracle XML DB Developer’s Guide for information about using this view See Also: Oracle XML DB Developer’s Guide for information about using this view