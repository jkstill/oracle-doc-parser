---
id: 19c__DBMS_LOB.ERASE
name: DBMS_LOB.ERASE
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOB
tags: [dbms_lob]
source_file: DBMS_LOB.html
---

# DBMS_LOB.ERASE

This procedure erases an entire internal LOB or part of an internal LOB.

## Syntax

```sql
DBMS_LOB.ERASE (
   lob_loc           IN OUT   NOCOPY   BLOB,
   amount            IN OUT   NOCOPY   INTEGER,
   offset            IN                INTEGER := 1);

DBMS_LOB.ERASE (
   lob_loc           IN OUT   NOCOPY   CLOB CHARACTER SET ANY_CS,
   amount            IN OUT   NOCOPY   INTEGER,
   offset            IN                INTEGER := 1);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| lob_loc | NOCOPY | IN OUT | Locator for the LOB to be erased.For more information, see Operational Notes . |
| amount | NOCOPY | IN OUT | Number of bytes (for BLOBs or BFILES ) or characters (for CLOBs or NCLOBs ) to be erased. |
| offset | INTEGER | IN | Absolute offset (origin: 1) from the beginning of the LOB in bytes (for BLOBs ) or characters ( CLOBs ). |

## Usage Notes

Syntax DBMS_LOB.ERASE ( lob_loc IN OUT NOCOPY BLOB, amount IN OUT NOCOPY INTEGER, offset IN INTEGER := 1); DBMS_LOB.ERASE ( lob_loc IN OUT NOCOPY CLOB CHARACTER SET ANY_CS, amount IN OUT NOCOPY INTEGER, offset IN INTEGER := 1); Parameters Table 99-31 ERASE Procedure Parameters Parameter Description lob_loc Locator for the LOB to be erased.For more information, see Operational Notes . amount Number of bytes (for BLOBs or BFILES ) or characters (for CLOBs or NCLOBs ) to be erased. offset Absolute offset (origin: 1) from the beginning of the LOB in bytes (for BLOBs ) or characters ( CLOBs ). Usage Notes When data is erased from the middle of a LOB, zero-byte fillers or spaces are written for BLOBs or CLOBs respectively. The actual number of bytes or characters erased can differ from the number you specified in the amount parameter if the end of the LOB value is reached before erasing the specified number. The actual number of characters or bytes erased is returned in the amount parameter. ERASE gets the LOB if it is archived, unless the erase covers the entire LOB. If the LOB to be erased is a DBFS Link, an exception is thrown. Note: The length of the LOB is not decreased when a section of the LOB is erased. To decrease the length of the LOB value, see the " TRIM Procedures " . Note: The length of the LOB is not decreased when a section of the LOB is erased. To decrease the length of the LOB value, see the " TRIM Procedures " . Exceptions Table 99-32 ERASE Procedure Exceptions Exception Description VALUE_ERROR Any input parameter is NULL . INVALID_ARGVAL Either: - amount < 1 or amount > LOBMAXSIZE - offset < 1 or offset > LOBMAXSIZE QUERY_WRITE Cannot perform a LOB write inside a query or PDML parallel execution server BUFFERING_ENABLED Cannot perform operation with LOB buffering enabled if buffering is enabled on the LOB