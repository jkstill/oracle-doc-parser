---
id: 19c__DBMS_UTILITY.IS_BIT_SET
name: DBMS_UTILITY.IS_BIT_SET
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_UTILITY
tags: [dbms_utility]
source_file: DBMS_UTILITY.html
---

# DBMS_UTILITY.IS_BIT_SET

This function checks the bit setting for the given bit in the given RAW value.

## Syntax

```sql
DBMS_UTILITY.IS_BIT_SET (
   r     IN    RAW,   n     IN    NUMBER)
 RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| r | RAW | IN | RAW source |
| n | NUMBER) | IN | Bit in r to check |

**Returns:** `NUMBER`

## Usage Notes

Syntax DBMS_UTILITY.IS_BIT_SET ( r IN RAW, n IN NUMBER) RETURN NUMBER; Parameters Table 187-28 IS_BET_SET Function Parameters Parameter Description r RAW source n Bit in r to check Return Values This function returns 1 if bit n in raw r is set, zero otherwise. Bits are numbered high to low with the lowest bit being bit number 1.