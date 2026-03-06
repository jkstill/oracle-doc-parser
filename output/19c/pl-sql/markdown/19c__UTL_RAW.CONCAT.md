---
id: 19c__UTL_RAW.CONCAT
name: UTL_RAW.CONCAT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_RAW
tags: [utl_raw]
source_file: UTL_RAW.html
---

# UTL_RAW.CONCAT

This function concatenates up to 12 RAWs into a single RAW . If the concatenated size exceeds 32K, then an error is returned

## Syntax

```sql
UTL_RAW.CONCAT (  
   r1  IN RAW DEFAULT NULL,
   r2  IN RAW DEFAULT NULL,
   r3  IN RAW DEFAULT NULL,
   r4  IN RAW DEFAULT NULL,
   r5  IN RAW DEFAULT NULL,
   r6  IN RAW DEFAULT NULL,
   r7  IN RAW DEFAULT NULL,
   r8  IN RAW DEFAULT NULL,
   r9  IN RAW DEFAULT NULL,
   r10 IN RAW DEFAULT NULL,
   r11 IN RAW DEFAULT NULL,
   r12 IN RAW DEFAULT NULL) 
  RETURN RAW;
```

**Returns:** `RAW`

## Usage Notes

Syntax UTL_RAW.CONCAT ( r1 IN RAW DEFAULT NULL, r2 IN RAW DEFAULT NULL, r3 IN RAW DEFAULT NULL, r4 IN RAW DEFAULT NULL, r5 IN RAW DEFAULT NULL, r6 IN RAW DEFAULT NULL, r7 IN RAW DEFAULT NULL, r8 IN RAW DEFAULT NULL, r9 IN RAW DEFAULT NULL, r10 IN RAW DEFAULT NULL, r11 IN RAW DEFAULT NULL, r12 IN RAW DEFAULT NULL) RETURN RAW; Pragmas pragma restrict_references(concat, WNDS, RNDS, WNPS, RNPS); Parameters r1 .... r12 are the RAW items to concatenate. Return Values Table 272-26 CONCAT Function Return Values Return Description RAW Containing the items concatenated Exceptions There is an error if the sum of the lengths of the inputs exceeds the maximum allowable length for a RAW , which is 32767 bytes.