---
id: 19c__DBMS_DBFS_HS.STOREPUSH
name: DBMS_DBFS_HS.STOREPUSH
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_HS
tags: [dbms_dbfs_hs]
source_file: DBMS_DBFS_HS.html
---

# DBMS_DBFS_HS.STOREPUSH

This procedure pushes locally staged data to the remote storage.

## Syntax

```sql
DBMS_DBFS_HS.STOREPUSH (
   store_name   IN        VARCHAR2,
   path         IN        VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| store_name | VARCHAR2 | IN | Name of store whose content the client writes from local cache to the external store |
| path | VARCHAR2 | IN | A non-mount qualified (without mount point) path within the store. By default, its value is NULL which corresponds to the root path of the store. |

## Usage Notes

Syntax DBMS_DBFS_HS.STOREPUSH ( store_name IN VARCHAR2, path IN VARCHAR2 DEFAULT NULL); Parameters Table 54-17 STOREPUSH Procedure Parameters Parameter Description store_name Name of store whose content the client writes from local cache to the external store path A non-mount qualified (without mount point) path within the store. By default, its value is NULL which corresponds to the root path of the store. Usage Notes The Hierarchical Store caches the content files locally in database tables. When enough content is amassed in the cache to make it efficient to write to the external storage device (or the cache is completely filled), the Hierarchical Store creates a tarball out of the local content and writes these tarballs as files on the external device. The size of the tarball created by the Hierarchical Store is controlled by the store property PROPNAME_OPTTARBALLSIZE . When the amount of free space in the cache is such that the caching of a content file will push the space used above cache_size , the Hierarchical Store will internally call STOREPUSH . The STOREPUSH Procedure creates tarball(s) out of the existing dirty or modified content files in the cache and writes them out to the external device. A STOREPUSH call is not guaranteed to write all the dirty content from local cache to the external storage, since some files may be locked by other sessions. STOREPUSH has a built-in ability feature allowing it to automatically resume operation. If a STOREPUSH call is interrupted (say by a network outage) after it has transferred some tarballs to the external device, it can be restarted after the outage and will then resume transferring data from the point it was interrupted. In other words, work done before the outage is not lost. STOREPUSH can safely be restarted and the effect is such as if the outage never occurred. If this method successfully executes, its actions cannot be rolled back by the user. By default, when path is NULL , all files in the store are candidates for STOREPUSH . If path has a valid input value, all files which are under the namespace of given path are written from the local cache to the external store. If a given path is an existing file, it is pushed out again to the remote store.