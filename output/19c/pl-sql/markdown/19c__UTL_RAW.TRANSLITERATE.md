---
id: 19c__UTL_RAW.TRANSLITERATE
name: UTL_RAW.TRANSLITERATE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_RAW
tags: [utl_raw]
source_file: UTL_RAW.html
---

# UTL_RAW.TRANSLITERATE

This function converts the bytes in the input RAW r according to the bytes in the transliteration RAWs from_set and to_set .

## Syntax

```sql
UTL_RAW.TRANSLITERATE (
   r        IN RAW,
   to_set   IN RAW DEFAULT NULL,
   from_set IN RAW DEFAULT NULL,
   pad      IN RAW DEFAULT NULL)
  RETURN RAW;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| r | RAW | IN | RAW input byte-string to be converted |
| to_set | RAW | IN | RAW byte-codes to which corresponding from_set bytes are converted (any length) |
| from_set | RAW | IN | RAW byte-codes to be converted, if presenting r (any length) |
| pad | RAW | IN | 1 byte used when to-set is shorter than the from_set |

**Returns:** `RAW`

## Usage Notes

Successive bytes in r are looked up in the from_set , and, if not found, copied unaltered to the result RAW . If found, then they are replaced in the result RAW by either corresponding bytes in the to_set , or the pad byte when no correspondence exists. Bytes in r , but undefined in from_set , are copied to the result. Only the first (leftmost) occurrence of a byte in from_set is used. Subsequent duplicates are not scanned and are ignored. The result RAW is always the same length as r . Syntax UTL_RAW.TRANSLITERATE ( r IN RAW, to_set IN RAW DEFAULT NULL, from_set IN RAW DEFAULT NULL, pad IN RAW DEFAULT NULL) RETURN RAW; Note: Be aware that to_set and from_set are reversed in the calling sequence compared to TRANSLATE . Note: Be aware that to_set and from_set are reversed in the calling sequence compared to TRANSLATE . Pragmas pragma restrict_references(transliterate, WNDS, RNDS, WNPS, RNPS); Parameters Table 272-48 TRANSLITERATE Function Parameters Parameter Description r RAW input byte-string to be converted to_set RAW byte-codes to which corresponding from_set bytes are converted (any length) from_set RAW byte-codes to be converted, if presenting r (any length) pad 1 byte used when to-set is shorter than the from_set