---
id: 19c__DBMS_SESSION.GET_PACKAGE_MEMORY_UTILIZATION
name: DBMS_SESSION.GET_PACKAGE_MEMORY_UTILIZATION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SESSION
tags: [dbms_session]
source_file: DBMS_SESSION.html
---

# DBMS_SESSION.GET_PACKAGE_MEMORY_UTILIZATION

This procedure describes static package memory usage.

## Syntax

```sql
DBMS_SESSION.GET_PACKAGE_MEMORY_UTILIZATION (
   owner_names     OUT NOCOPY LNAME_ARRAY,
   unit_names      OUT NOCOPY LNAME_ARRAY,
   unit_types      OUT NOCOPY INTEGER_ARRAY,
   used_amounts    OUT NOCOPY INTEGER_ARRAY,
   free_amounts    OUT NOCOPY INTEGER_ARRAY);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| owner_name |  |  | Owner of package |
| unit_name |  |  | Name of package |
| unit_types | NOCOPY | OUT | Value of the type# columns of the dictionary table obj$ |
| used_amounts | NOCOPY | OUT | Amount of allocated memory specified in bytes |
| free_amounts | NOCOPY | OUT | Amount of available memory specified in bytes |

## Usage Notes

The output collections describe memory usage in each instantiated package. Each package is described by its owner name, package name, used memory amount, and unused allocated memory amount. The amount of unused memory is greater than zero because of memory fragmentation and also because once used free memory chunks initially go to a free list owned by the package memory heap. They are released back to the parent heap only when the FREE_UNUSED_USER_MEMORY Procedure is invoked. Syntax DBMS_SESSION.GET_PACKAGE_MEMORY_UTILIZATION ( owner_names OUT NOCOPY LNAME_ARRAY, unit_names OUT NOCOPY LNAME_ARRAY, unit_types OUT NOCOPY INTEGER_ARRAY, used_amounts OUT NOCOPY INTEGER_ARRAY, free_amounts OUT NOCOPY INTEGER_ARRAY); Parameters Table 154-7 GET_PACKAGE_MEMORY_UTILIZATION Function Parameters Parameter Description owner_name Owner of package unit_name Name of package unit_types Value of the type# columns of the dictionary table obj$ used_amounts Amount of allocated memory specified in bytes free_amounts Amount of available memory specified in bytes