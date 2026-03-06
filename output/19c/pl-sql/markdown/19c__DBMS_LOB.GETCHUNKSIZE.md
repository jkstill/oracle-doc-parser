---
id: 19c__DBMS_LOB.GETCHUNKSIZE
name: DBMS_LOB.GETCHUNKSIZE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOB
tags: [dbms_lob]
source_file: DBMS_LOB.html
---

# DBMS_LOB.GETCHUNKSIZE

When creating the table, you can specify the chunking factor, a multiple of tablespace blocks in bytes. This corresponds to the chunk size used by the LOB data layer when accessing or modifying the LOB value. Part of the chunk is used to store system-related information, and the rest stores the LOB value. This function returns the amount of space used in the LOB chunk to store the LOB value.

## Syntax

```sql
DBMS_LOB.GETCHUNKSIZE (
   lob_loc IN BLOB) 
  RETURN INTEGER; 

DBMS_LOB.GETCHUNKSIZE (
   lob_loc IN CLOB CHARACTER SET ANY_CS) 
  RETURN INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| lob_loc | BLOB) | IN | LOB locator. For more information, see Operational Notes . |

**Returns:** `INTEGER`

## Usage Notes

Syntax DBMS_LOB.GETCHUNKSIZE ( lob_loc IN BLOB) RETURN INTEGER; DBMS_LOB.GETCHUNKSIZE ( lob_loc IN CLOB CHARACTER SET ANY_CS) RETURN INTEGER; Pragmas PRAGMA RESTRICT_REFERENCES(getchunksize, WNDS, RNDS, WNPS, RNPS); Parameters Table 99-61 GETCHUNKSIZE Function Parameters Parameter Description lob_loc LOB locator. For more information, see Operational Notes . Return Values The return value is a usable chunk size in bytes. Usage Notes With regard to basic LOB files, performance is improved if you enter read/write requests using a multiple of this chunk size. For writes, there is an added benefit, because LOB chunks are versioned, and if all writes are done on a chunk basis, then no extra or excess versioning is done or duplicated. You could batch up the WRITE until you have enough for a chunk, instead of issuing several WRITE calls for the same chunk. These tactics of performance improvement do not apply to SecureFiles. Note that chunk size is independent of LOB type ( BLOB , CLOB , NCLOB , Unicode or other character set). See Also: Oracle Database SecureFiles and Large Objects Developer's Guide for additional details on usage of this procedure