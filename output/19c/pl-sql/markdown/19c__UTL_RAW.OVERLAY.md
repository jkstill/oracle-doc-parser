---
id: 19c__UTL_RAW.OVERLAY
name: UTL_RAW.OVERLAY
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_RAW
tags: [utl_raw]
source_file: UTL_RAW.html
---

# UTL_RAW.OVERLAY

This function overlays the specified portion of target RAW with overlay_str RAW , starting from byte position pos of target and proceeding for len bytes.

## Syntax

```sql
UTL_RAW.OVERLAY (
   overlay_str IN RAW,
   target      IN RAW,
   pos         IN BINARY_INTEGER DEFAULT 1,
   len         IN BINARY_INTEGER DEFAULT NULL,
   pad         IN RAW            DEFAULT NULL) 
  RETURN RAW;
```

**Returns:** `RAW`

## Usage Notes

Syntax UTL_RAW.OVERLAY ( overlay_str IN RAW, target IN RAW, pos IN BINARY_INTEGER DEFAULT 1, len IN BINARY_INTEGER DEFAULT NULL, pad IN RAW DEFAULT NULL) RETURN RAW; Pragmas pragma restrict_references(overlay, WNDS, RNDS, WNPS, RNPS); Parameters Table 272-34 OVERLAY Function Parameters Parameters Description overlay_str Byte-string used to overlay target target Byte-string which is to be overlaid pos Position in target (numbered from 1) to start overlay len The number of target bytes to overlay pad Pad byte used when overlay len exceeds overlay_str length or pos exceeds target length Defaults and Optional Parameters Table 272-35 OVERLAY Function Optional Parameters Optional Parameter Description pos 1 len To the length of overlay_str pad x'00' Return Values Table 272-36 OVERLAY Function Return Values Return Description RAW The target byte_string overlaid as specified.