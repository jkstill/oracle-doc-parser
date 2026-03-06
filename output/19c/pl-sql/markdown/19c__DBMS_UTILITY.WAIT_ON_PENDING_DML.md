---
id: 19c__DBMS_UTILITY.WAIT_ON_PENDING_DML
name: DBMS_UTILITY.WAIT_ON_PENDING_DML
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_UTILITY
tags: [dbms_utility]
source_file: DBMS_UTILITY.html
---

# DBMS_UTILITY.WAIT_ON_PENDING_DML

This function waits until all transactions (other than the caller's own) that have locks on the listed tables and began prior to the specified scn have either committed or been rolled back.

## Syntax

```sql
DBMS_UTILITY.WAIT_ON_PENDING_DML (
    tables     IN       VARCHAR2,
    timeout    IN       BINARY_INTEGER,
    scn        IN OUT   NUMBER)
  RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| tables | VARCHAR2 | IN | Comma-separated list of one or more table names. The list must be valid for COMMA_TO_TABLE Procedures , and each item valid to the NAME_RESOLVE Procedure . Neither column specifiers nor DBLINK (database link) specifiers are allowed in the names, and each name must resolve to an existing table in the local database. |
| timeout | BINARY_INTEGER | IN | Maximum number of seconds to wait, totalled across all tables/transactions. A NULL or negative value will cause a very long wait. |
| scn | NUMBER) | IN OUT | SCN prior to which transactions must have begun to be considered relevant to this request. If the value is NULL or not recognized as a meaningful scn on input, the most current SCN across all instances will be used and will be set into the passed argument as an output. If a meaningful value is passed in, its value will be preserved in the output. |

**Returns:** `BOOLEAN`

## Usage Notes

Syntax DBMS_UTILITY.WAIT_ON_PENDING_DML ( tables IN VARCHAR2, timeout IN BINARY_INTEGER, scn IN OUT NUMBER) RETURN BOOLEAN; Parameters Table 187-35 WAIT_ON_PENDING_DML Function Parameters Parameter Description tables Comma-separated list of one or more table names. The list must be valid for COMMA_TO_TABLE Procedures , and each item valid to the NAME_RESOLVE Procedure . Neither column specifiers nor DBLINK (database link) specifiers are allowed in the names, and each name must resolve to an existing table in the local database. timeout Maximum number of seconds to wait, totalled across all tables/transactions. A NULL or negative value will cause a very long wait. scn SCN prior to which transactions must have begun to be considered relevant to this request. If the value is NULL or not recognized as a meaningful scn on input, the most current SCN across all instances will be used and will be set into the passed argument as an output. If a meaningful value is passed in, its value will be preserved in the output. Return Values TRUE if all relevant transactions have committed or been rolled back, FALSE if the timeout occurred prior to all relevant transactions committing or being rolled back