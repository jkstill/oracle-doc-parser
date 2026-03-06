---
id: 19c__ALL_SUBPARTITION_TEMPLATES
name: ALL_SUBPARTITION_TEMPLATES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: partitioning
tags: [all]
source_file: ALL_SUBPARTITION_TEMPLATES.html
---

# ALL_SUBPARTITION_TEMPLATES

ALL_SUBPARTITION_TEMPLATES describes the subpartition templates accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| USER_NAME | VARCHAR2(128) | Owner of the table |
| TABLE_NAME | VARCHAR2(128) | Name of the table |
| SUBPARTITION_NAME | VARCHAR2(132) | Name of the subpartition |
| SUBPARTITION_POSITION | NUMBER | Position of the subpartition |
| TABLESPACE_NAME | VARCHAR2(30) | Tablespace name of the subpartition |
| HIGH_BOUND | LONG | Literal list values of the subpartition |
| COMPRESSION | VARCHAR2(4) | Compression values of COMPRESSION or NOCOMPRESSION can be specified in a subpartition template. The value in this column indicates whether the subpartition template specifies that for each new added composite partition, its subpartition data will be stored in compressed format ( YES ) or not ( NO ). If compression is not specified in the subpartition template, then the default is that data stored in newly-added subpartitions will not be stored in compressed format ( NO ). |
| INDEXING | VARCHAR2(4) | Indexing values of INDEXING ON or INDEXING OFF can be specified in a subpartition template. The value in this column indicates whether the subpartition template specifies that for each new added composite partition, its subpartition data will be considered for a partial index ( ON ) or not ( OFF ). If indexing is not specified in the subpartition template, then the default is that data stored in newly-added subpartitions will considered for a partial index ( ON ). |
| READ_ONLY | VARCHAR2(4) | Values of READ ONLY or READ WRITE can be specified in a subpartition template. The value in this column indicates whether the subpartition template specifies that for each new added composite partition, its subpartition data will be read only ( YES ) or not ( NO ). If the read clause is not specified in the subpartition template, then the default is that data stored in newly-added subpartitions will be read/write ( NO ). |

## Usage Notes

Related Views DBA_SUBPARTITION_TEMPLATES describes all subpartition templates in the database. USER_SUBPARTITION_TEMPLATES describes the subpartition templates owned by the current user. This view does not display the USER_NAME column. See Also: " DBA_SUBPARTITION_TEMPLATES " " USER_SUBPARTITION_TEMPLATES " See Also: " DBA_SUBPARTITION_TEMPLATES " " USER_SUBPARTITION_TEMPLATES "