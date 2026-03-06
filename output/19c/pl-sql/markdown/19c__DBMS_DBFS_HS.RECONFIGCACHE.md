---
id: 19c__DBMS_DBFS_HS.RECONFIGCACHE
name: DBMS_DBFS_HS.RECONFIGCACHE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_HS
tags: [dbms_dbfs_hs]
source_file: DBMS_DBFS_HS.html
---

# DBMS_DBFS_HS.RECONFIGCACHE

This procedure reconfigures the parameters of the database cache being used by the store.

## Syntax

```sql
DBMS_DBFS_HS.RECONFIGCACHE (
   store_name              IN    VARCHAR2,
   cache_size              IN    NUMBER DEFAULT NULL,
   lobcache_quota          IN    NUMBER DEFAULT NULL,
   optimal_tarball_size    IN    NUMBER DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| store_name | VARCHAR2 | IN | Name of store |
| cache_size | NUMBER | IN | Cumulative cache size used for the Hierarchical Store |
| lobcache_quota | NUMBER | IN | Fraction of the cache size that are assigned to level 1 cache |
| optimal_tarball_size | NUMBER | IN | Maximum possible size of an archive file. Since creating one file for every content file in the store is a prohibitively expensive operation, multiple content files are bundled together into one archive file for transfer to tape or Amazon S3. |

## Usage Notes

Syntax DBMS_DBFS_HS.RECONFIGCACHE ( store_name IN VARCHAR2, cache_size IN NUMBER DEFAULT NULL, lobcache_quota IN NUMBER DEFAULT NULL, optimal_tarball_size IN NUMBER DEFAULT NULL); Parameters Table 54-13 RECONFIGCACHE Procedure Parameters Parameter Description store_name Name of store cache_size Cumulative cache size used for the Hierarchical Store lobcache_quota Fraction of the cache size that are assigned to level 1 cache optimal_tarball_size Maximum possible size of an archive file. Since creating one file for every content file in the store is a prohibitively expensive operation, multiple content files are bundled together into one archive file for transfer to tape or Amazon S3. Usage Notes The specified store must already have been created before reconfiguration. The Hierarchical Store uses a level 1 cache and a level 2 cache. The level 1 cache subsumes most of the working set and the level 2 cache is used to perform bulk writes to the backend device. If any of the last 3 parameters is NULL , its value specified during store creation is used. If the parameter was NULL when the call to the CREATESTORE Procedure was issued, the DBMS_DBFS_HS package assigns a default value. The DBMS_DBFS_HS package optimistically tries to allocate more than 1 tarball's worth of size for level 2 cache to facilitate concurrency, though a minimum of 1 tarball size is necessary for level 2 cache. The values for cumulative cache size and LOB cache quota decide allocation of space for the two caches. If values are not provided, a user might see an INSUFFICIENT_CACHE exception. In that case, it is better to revise the cache parameters in order to have a working store. If this subprogram successfully executes, its actions cannot be rolled back by the user. In that case, the user should call RECONFIGCACHE again with new or modified parameters.