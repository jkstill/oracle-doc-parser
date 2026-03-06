---
id: 19c__DBMS_XDB_VERSION.CHECKOUT
name: DBMS_XDB_VERSION.CHECKOUT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_VERSION
tags: [dbms_xdb_version]
source_file: DBMS_XDB_VERSION.html
---

# DBMS_XDB_VERSION.CHECKOUT

This procedure checks out a VCR before updating or deleting it.

## Syntax

```sql
DBMS_XDB_VERSION.Checkout(
   pathname    VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| pathname | VARCHAR2) | IN | The path name of the VCR to be checked out. |

## Usage Notes

Syntax DBMS_XDB_VERSION.Checkout( pathname VARCHAR2); Parameters Table 199-3 CHECKOUT Procedure Parameters Parameter Description pathname The path name of the VCR to be checked out. Usage Notes This is not an auto-commit SQL operation. Two users of the same workspace cannot CHECKOUT Procedure the same VCR at the same time. If this happens, one user must rollback. As a result, it is good practice to commit the CHECKOUT Procedure operation before updating a resource and avoid loss of the update if the transaction is rolled back. An exception is raised if the given resource is not a VCR, if the VCR is already checked out, if the resource doesn't exist.