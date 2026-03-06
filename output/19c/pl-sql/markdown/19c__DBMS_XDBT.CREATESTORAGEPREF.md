---
id: 19c__DBMS_XDBT.CREATESTORAGEPREF
name: DBMS_XDBT.CREATESTORAGEPREF
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDBT
tags: [dbms_xdbt]
source_file: DBMS_XDBT.html
---

# DBMS_XDBT.CREATESTORAGEPREF

This procedure creates a BASIC_STORAGE preference for the CONTEXT index on the XML DB hierarchy.

## Syntax

```sql
DBMS_XDBT.CREATESTORAGEPREF;
```

## Usage Notes

Syntax DBMS_XDBT.CREATESTORAGEPREF; Usage Notes The name of the storage preference can be modified; see the StoragePref configuration setting. A tablespace can be specified for the tables and indexes comprising the CONTEXT index; see the IndexTablespace configuration setting. Prefix and Substring indexing are not turned on by default. The I_INDEX_CLAUSE uses key compression.