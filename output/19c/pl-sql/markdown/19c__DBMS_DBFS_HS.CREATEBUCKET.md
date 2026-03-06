---
id: 19c__DBMS_DBFS_HS.CREATEBUCKET
name: DBMS_DBFS_HS.CREATEBUCKET
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_HS
tags: [dbms_dbfs_hs]
source_file: DBMS_DBFS_HS.html
---

# DBMS_DBFS_HS.CREATEBUCKET

This procedure creates an AWS bucket, associated with a store of type STORETYPE_AMAZONS3 into which the Hierarchical Store can then move data.

## Syntax

```sql
DBMS_DBFS_HS.CREATEBUCKET  (
   store_name    IN     VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| store_name | VARCHAR2) | IN | Name of store |

## Usage Notes

Syntax DBMS_DBFS_HS.CREATEBUCKET ( store_name IN VARCHAR2); Parameters Table 54-7 CREATEBUCKET Procedure Parameters Parameter Description store_name Name of store Usage Notes The PROPNAME_BUCKET property of the store should be set before this subprogram is called. Once this procedure has successfully created a bucket in Amazon S3, the bucket can only be deleted using out-of-band methods, such as logging-in to S3 and deleting data (directories, files, and other items) for the bucket.