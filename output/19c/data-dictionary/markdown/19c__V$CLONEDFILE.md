---
id: 19c__V$CLONEDFILE
name: V$CLONEDFILE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-CLONEDFILE.html
---

# V$CLONEDFILE

V$CLONEDFILE provides CloneDB file information.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SNAPSHOTFILENAME | VARCHAR2(513) |  |
| CLONEFILENAME | VARCHAR2(513) |  |
| SNAPSHOTBLKREAD | NUMBER |  |
| SNAPSHOTREQUEST | NUMBER |  |
| FILENUMBER | NUMBER |  |
| CON_ID | NUMBER |  |
| BLOCKS_ALLOCATED | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Note: When this view is queried in an Oracle Database environment, rows are returned for every opened file, even those without a parent file backing them (in those cases the column is empty/NULL). In an Oracle ASM environement, rows are returned for files that an Oracle ASM instance has mounted in disk groups only if those files are children (a clonefile) of a parent snapshot file. Note: When this view is queried in an Oracle Database environment, rows are returned for every opened file, even those without a parent file backing them (in those cases the column is empty/NULL). In an Oracle ASM environement, rows are returned for files that an Oracle ASM instance has mounted in disk groups only if those files are children (a clonefile) of a parent snapshot file.