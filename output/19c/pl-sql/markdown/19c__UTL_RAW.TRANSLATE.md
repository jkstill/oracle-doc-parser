---
id: 19c__UTL_RAW.TRANSLATE
name: UTL_RAW.TRANSLATE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_RAW
tags: [utl_raw]
source_file: UTL_RAW.html
---

# UTL_RAW.TRANSLATE

This function translates the bytes in the input RAW r according to the bytes in the translation RAWs from_set and to_set .

## Syntax

```sql
UTL_RAW.TRANSLATE (
   r        IN RAW,
   from_set IN RAW,
   to_set   IN RAW) 
  RETURN RAW;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| r | RAW | IN | RAW source byte-string to be translated |
| from_set | RAW | IN | RAW byte-codes to be translated, if present in r |
| to_set | RAW) | IN | RAW byte-codes to which corresponding from_str bytes are translated |

**Returns:** `RAW`

## Usage Notes

If a byte in r has a matching byte in from_set , then it is replaced by the byte in the corresponding position in to_set , or deleted. Bytes in r , but undefined in from_set , are copied to the result. Only the first (leftmost) occurrence of a byte in from_set is used. Subsequent duplicates are not scanned and are ignored. Syntax UTL_RAW.TRANSLATE ( r IN RAW, from_set IN RAW, to_set IN RAW) RETURN RAW; Note: Be aware that to_set and from_set are reversed in the calling sequence compared to TRANSLITERATE . Note: Be aware that to_set and from_set are reversed in the calling sequence compared to TRANSLITERATE . Pragmas pragma restrict_references(translate, WNDS, RNDS, WNPS, RNPS); Parameters Table 272-45 TRANSLATE Function Parameters Parameter Description r RAW source byte-string to be translated from_set RAW byte-codes to be translated, if present in r to_set RAW byte-codes to which corresponding from_str bytes are translated