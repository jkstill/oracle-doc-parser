---
id: 19c__ANYDATASET.ADDINSTANCE
name: ANYDATASET.ADDINSTANCE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: ANYDATASET
tags: [anydataset]
source_file: ANYDATASET-TYPE.html
---

# ANYDATASET.ADDINSTANCE

This procedure adds a new data instance to an ANYDATASET .

## Syntax

```sql
MEMBER PROCEDURE AddInstance(
   self          IN OUT NOCOPY ANYDATASET);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| self | NOCOPY | IN OUT | The ANYDATASET being constructed. |

## Usage Notes

Syntax MEMBER PROCEDURE AddInstance( self IN OUT NOCOPY ANYDATASET); Parameters Table 281-2 ADDINSTANCE Procedure Parameter Parameter Description self The ANYDATASET being constructed. Exceptions DBMS_TYPES.invalid_parameters: Invalid parameters. DBMS_TYPES.incorrect_usage: On incorrect usage. Usage Notes The data instances have to be added sequentially. The previous data instance must be fully constructed (or set to NULL) before a new one can be added. This call DOES NOT automatically set the mode of construction to be piece-wise. The user has to explicitly call PIECEWISE if a piece-wise construction of the instance is intended.