---
id: 19c__UTL_RAW.XRANGE
name: UTL_RAW.XRANGE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_RAW
tags: [utl_raw]
source_file: UTL_RAW.html
---

# UTL_RAW.XRANGE

This function returns a RAW value containing the succession of one-byte encodings beginning and ending with the specified byte-codes. The specified byte-codes must be single-byte RAW values. If the start_byte value is greater than the end_byte value, then the succession of resulting bytes begins with start_byte , wraps through x'FF' back to x'00' , then ends at end_byte .

## Syntax

```sql
UTL_RAW.XRANGE (
   start_byte IN RAW DEFAULT NULL,
   end_byte   IN RAW DEFAULT NULL) 
  RETURN RAW;
```

**Returns:** `RAW`

## Usage Notes

Syntax UTL_RAW.XRANGE ( start_byte IN RAW DEFAULT NULL, end_byte IN RAW DEFAULT NULL) RETURN RAW; Pragmas pragma restrict_references(xrange, WNDS, RNDS, WNPS, RNPS); Parameters Table 272-52 XRANGE Function Parameters Parameters Description start_byte Beginning byte-code value of resulting sequence. The default is x'00' . end_byte Ending byte-code value of resulting sequence. The default is x'FF' . Return Values Table 272-53 XRANGE Function Return Values Return Description RAW Containing succession of 1-byte hexadecimal encodings