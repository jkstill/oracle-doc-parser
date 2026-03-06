---
id: 19c__UTL_RAW.COMPARE
name: UTL_RAW.COMPARE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_RAW
tags: [utl_raw]
source_file: UTL_RAW.html
---

# UTL_RAW.COMPARE

This function compares two RAW values. If they differ in length, then the shorter is extended on the right according to the optional pad parameter.

## Syntax

```sql
UTL_RAW.COMPARE (
   r1  IN RAW,
   r2  IN RAW,
   pad IN RAW DEFAULT NULL) 
  RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| r1 | RAW | IN | 1st RAW to be compared, may be NULL or 0 length |
| r2 | RAW | IN | 2nd RAW to be compared, may be NULL or 0 length |
| pad | RAW | IN | This is an optional parameter. Byte to extend whichever of r1 or r2 is shorter. The default: x'00' |

**Returns:** `NUMBER`

## Usage Notes

Syntax UTL_RAW.COMPARE ( r1 IN RAW, r2 IN RAW, pad IN RAW DEFAULT NULL) RETURN NUMBER; Pragmas pragma restrict_references(compare, WNDS, RNDS, WNPS, RNPS); Parameters Table 272-24 COMPARE Function Parameters Parameter Description r1 1st RAW to be compared, may be NULL or 0 length r2 2nd RAW to be compared, may be NULL or 0 length pad This is an optional parameter. Byte to extend whichever of r1 or r2 is shorter. The default: x'00' Return Values Table 272-25 COMPARE Function Return Values Return Description NUMBER Equals 0 if RAW byte strings are both NULL or identical; or, Equals position (numbered from 1) of the first mismatched byte