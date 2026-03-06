---
id: 19c__DBMS_DBFS_CONTENT.NORMALIZEPATH
name: DBMS_DBFS_CONTENT.NORMALIZEPATH
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.NORMALIZEPATH

This function converts a store-specific or full-absolute path name into normalized form.

## Syntax

```sql
DBMS_DBFS_CONTENT.NORMALIZEPATH (
   path        IN              VARCHAR2,
   parent      OUT NOCOPY      VARCHAR2,
   tpath       OUT NOCOPY      VARCHAR2)
  RETURN VARCHAR2;

DBMS_DBFS_CONTENT.NORMALIZEPATH (
   path        IN              VARCHAR2,
   store_name  OUT NOCOPY      VARCHAR2,
   parent      OUT NOCOPY      VARCHAR2,
   tpath       OUT NOCOPY      VARCHAR2)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| path | VARCHAR2 | IN | Name of path to file items |
| store_name | NOCOPY | OUT | Name of store |
| parent | NOCOPY | OUT | Parent path name |
| tpath | NOCOPY | OUT | Name of trailing path item |

**Returns:** `VARCHAR2`

## Usage Notes

It does the following: verifies that the path name is absolute, and so starts with " / " collapses multiple consecutive " / " into a single " / " strips trailing " / " breaks up a store-specific normalized path name into 2 components - parent pathname, trailing component name breaks up a full-absolute normalized path name into 3 components - store name, parent pathname, trailing component name Syntax DBMS_DBFS_CONTENT.NORMALIZEPATH ( path IN VARCHAR2, parent OUT NOCOPY VARCHAR2, tpath OUT NOCOPY VARCHAR2) RETURN VARCHAR2; DBMS_DBFS_CONTENT.NORMALIZEPATH ( path IN VARCHAR2, store_name OUT NOCOPY VARCHAR2, parent OUT NOCOPY VARCHAR2, tpath OUT NOCOPY VARCHAR2) RETURN VARCHAR2; Parameters Table 52-51 NORMALIZEPATH Function Parameters Parameter Description path Name of path to file items store_name Name of store parent Parent path name tpath Name of trailing path item Return Values The completely normalized store-specific or full-absolute path name