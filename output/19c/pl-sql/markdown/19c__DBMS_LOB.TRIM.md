---
id: 19c__DBMS_LOB.TRIM
name: DBMS_LOB.TRIM
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOB
tags: [dbms_lob]
source_file: DBMS_LOB.html
---

# DBMS_LOB.TRIM

This procedure trims the value of the internal LOB to the length you specify in the newlen parameter.

## Syntax

```sql
DBMS_LOB.TRIM (
   lob_loc        IN OUT  NOCOPY BLOB,
   newlen         IN             INTEGER);

DBMS_LOB.TRIM (
   lob_loc        IN OUT  NOCOPY CLOB CHARACTER SET ANY_CS,
   newlen         IN             INTEGER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| lob_loc | NOCOPY | IN OUT | Locator for the internal LOB whose length is to be trimmed. For more information, see Operational Notes . |
| newlen | INTEGER) | IN | New, trimmed length of the LOB value in bytes for BLOBs or characters for CLOBs . |

## Usage Notes

Specify the length in bytes for BLOBs , and specify the length in characters for CLOBs . Note: The TRIM procedure decreases the length of the LOB to the value specified in the newlen parameter. If you attempt to TRIM an empty LOB, then nothing occurs, and TRIM returns no error. If the new length that you specify in newlen is greater than the size of the LOB, then an exception is raised. Note: The TRIM procedure decreases the length of the LOB to the value specified in the newlen parameter. Syntax DBMS_LOB.TRIM ( lob_loc IN OUT NOCOPY BLOB, newlen IN INTEGER); DBMS_LOB.TRIM ( lob_loc IN OUT NOCOPY CLOB CHARACTER SET ANY_CS, newlen IN INTEGER); Parameters Table 99-98 TRIM Procedure Parameters Parameter Description lob_loc Locator for the internal LOB whose length is to be trimmed. For more information, see Operational Notes . newlen New, trimmed length of the LOB value in bytes for BLOBs or characters for CLOBs . Exceptions Table 99-99 TRIM Procedure Exceptions Exception Description VALUE_ERROR lob_loc is NULL . INVALID_ARGVAL Either: - new_len < 0 - new_len > LOBMAXSIZE QUERY_WRITE Cannot perform a LOB write inside a query or PDML parallel execution server BUFFERING_ENABLED Cannot perform operation with LOB buffering enabled if buffering is enabled on the LOB