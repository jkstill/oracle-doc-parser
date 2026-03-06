---
id: 19c__DBMS_COMPRESSION.GET_COMPRESSION_RATIO
name: DBMS_COMPRESSION.GET_COMPRESSION_RATIO
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_COMPRESSION
tags: [dbms_compression]
source_file: DBMS_COMPRESSION.html
---

# DBMS_COMPRESSION.GET_COMPRESSION_RATIO

This procedure analyzes the compression ratio of a table or an index, and gives information about compressibility of the object. Various parameters can be provided by the user to selectively analyze different compression types.

## Syntax

```sql
DBMS_COMPRESSION.GET_COMPRESSION_RATIO (
   scratchtbsname        IN     VARCHAR2, 
   ownname               IN     VARCHAR2, 
   objname               IN     VARCHAR2,
   subobjname            IN     VARCHAR2,
   comptype              IN     NUMBER,
   blkcnt_cmp            OUT    PLS_INTEGER,
   blkcnt_uncmp          OUT    PLS_INTEGER,
   row_cmp               OUT    PLS_INTEGER,
   row_uncmp             OUT    PLS_INTEGER,
   cmp_ratio             OUT    NUMBER,
   comptype_str          OUT    VARCHAR2,
   subset_numrows        IN     NUMBER  DEFAULT COMP_RATIO_MINROWS,
   objtype               IN     PLS_INTEGER DEFAULT OBJTYPE_TABLE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| scratchtbsname | VARCHAR2 | IN | Temporary scratch tablespace that can be used for analysis |
| ownname / tabowner |  |  | Schema of the table to analyze |
| tabname |  |  | Name of the table to analyze |
| objname | VARCHAR2 | IN | Name of the object |
| subobjname | VARCHAR2 | IN | Name of the partition or sub-partition of the object |
| comptype | NUMBER | IN | Compression types for which analysis should be performed When the object is an index, only the following compression types are valid: COMP_INDEX_ADVANCED_HIGH (value 1024 ) and COMP_INDEX_ADVANCED_LOW (value 2048 ). Note: The following compression types cannot be specified in this parameter for any type of object: COMP_BLOCK (value 64 ) and COMP_BASIC (value 4096 ). |
| blkcnt_cmp | PLS_INTEGER | OUT | Number of blocks used by compressed sample of the table |
| blkcnt_uncmp | PLS_INTEGER | OUT | Number of blocks used by uncompressed sample of the table |
| row_cmp | PLS_INTEGER | OUT | Number of rows in a block in compressed sample of the table |
| row_uncmp | PLS_INTEGER | OUT | Number of rows in a block in uncompressed sample of the table |
| cmp_ratio | NUMBER | OUT | Compression ratio, blkcnt_uncmp divided by blkcnt_cmp |
| comptype_str | VARCHAR2 | OUT | String describing the compression type |
| subset_numrows | NUMBER | IN | Number of rows sampled to estimate compression ratio. |
| objtype | PLS_INTEGER | IN | Type of the object, either OBJTYPE_TABLE or OBJTYPE_INDEX |
| lobname |  |  | Name of the LOB column |
| partname |  |  | In case of partitioned tables, the related partition name |
| lobcnt |  |  | Number of lobs actually sampled to estimate compression ratio |
| index_cr |  |  | List of indexes and their estimated compression ratios |

## Usage Notes

Syntax Get compression ratio for an object (table or index, default is table): DBMS_COMPRESSION.GET_COMPRESSION_RATIO ( scratchtbsname IN VARCHAR2, ownname IN VARCHAR2, objname IN VARCHAR2, subobjname IN VARCHAR2, comptype IN NUMBER, blkcnt_cmp OUT PLS_INTEGER, blkcnt_uncmp OUT PLS_INTEGER, row_cmp OUT PLS_INTEGER, row_uncmp OUT PLS_INTEGER, cmp_ratio OUT NUMBER, comptype_str OUT VARCHAR2, subset_numrows IN NUMBER DEFAULT COMP_RATIO_MINROWS, objtype IN PLS_INTEGER DEFAULT OBJTYPE_TABLE); Get compression ratio for LOBs: DBMS_COMPRESSION.GET_COMPRESSION_RATIO ( scratchtbsname IN VARCHAR2, tabowner IN VARCHAR2, tabname IN VARCHAR2, lobname IN VARCHAR2, partname IN VARCHAR2, comptype IN NUMBER, blkcnt_cmp OUT PLS_INTEGER, blkcnt_uncmp OUT PLS_INTEGER, lobcnt OUT PLS_INTEGER, cmp_ratio OUT NUMBER, comptype_str OUT VARCHAR2, subset_numrows IN number DEFAULT COMP_RATIO_LOB_MAXROWS); Get compression ratio for all indexes on a table. The compression ratios are returned as a collection. DBMS_COMPRESSION.GET_COMPRESSION_RATIO ( scratchtbsname IN VARCHAR2, ownname IN VARCHAR2, tabname IN VARCHAR2, comptype IN NUMBER, index_cr OUT DBMS_COMPRESSION.COMPRECLIST, comptype_str OUT VARCHAR2, subset_numrows IN NUMBER DEFAULT COMP_RATIO_INDEX_MINROWS); Parameters Table 38-4 GET_COMPRESSION_RATIO Procedure Parameters Parameter Description scratchtbsname Temporary scratch tablespace that can be used for analysis ownname / tabowner Schema of the table to analyze tabname Name of the table to analyze objname Name of the object subobjname Name of the partition or sub-partition of the object comptype Compression types for which analysis should be performed When the object is an index, only the following compression types are valid: COMP_INDEX_ADVANCED_HIGH (value 1024 ) and COMP_INDEX_ADVANCED_LOW (value 2048 ). Note: The following compression types cannot be specified in this parameter for any type of object: COMP_BLOCK (value 64 ) and COMP_BASIC (value 4096 ). blkcnt_cmp Number of blocks used by compressed sample of the table blkcnt_uncmp Number of blocks used by uncompressed sample of the table row_cmp Number of rows in a block in compressed sample of the table row_uncmp Number of rows in a block in uncompressed sample of the table cmp_ratio Compression ratio, blkcnt_uncmp divided by blkcnt_cmp comptype_str String describing the compression type subset_numrows Number of rows sampled to estimate compression ratio. objtype Type of the object, either OBJTYPE_TABLE or OBJTYPE_INDEX lobname Name of the LOB column partname In case of partitioned tables, the related partition name lobcnt Number of lobs actually sampled to estimate compression ratio index_cr List of indexes and their estimated compression ratios Examples The following example shows how to estimate the compression ratio for advanced row compression: SET SERVEROUTPUT ON DECLARE 1_blkcnt_cmp PLS_INTEGER; 1_blkcnt_uncmp PLS_INTEGER; 1_row_cmp PLS_INTEGER; 1_row_uncmp PLS_INTEGER; 1_cmp_ratio NUMBER; 1_comptype_str VARCHAR2(32767); BEGIN DBMS_COMPRESSION.GET_COMPRESSION_RATIO ( scratchtbsname => 'USERS' , ownname => 'TEST' , objname => 'SALES' , subobjname => NULL , comptype => DBMS_COMPRESSION.COMP_ADVANCED, blkcnt_cmp => 1_blkcnt_cmp, blkcnt_uncmp => 1_blkcnt_uncmp, row_cmp => 1_row_cmp, row_uncmp => 1_row_uncmp, cmp_ratio => 1_cmp_ratio, comptype_str => 1_comptype_str, subset_numrows => DBMS_COMPRESSION.comp_ratio_minrows, objtype => DBMS_COMPRESSION.objtype_table ); DBMS_OUTPUT.put_line( 'Number of blocks used by the compressed sample of the object : ' || 1_blkcnt_cmp); DBMS_OUTPUT.put_line( 'Number of blocks used by the uncompressed sample of the object : ' || 1_blkcnt_uncmp); DBMS_OUTPUT.put_line( 'Number of rows in a block in compressed sample of the object : ' || 1_row_cmp); DBMS_OUTPUT.put_line( 'Number of rows in a block in uncompressed sample of the object : ' || 1_row_uncmp); DBMS_OUTPUT.put_line( 'Estimated Compression Ratio of Sample : ' || 1_cmp_ratio); DBMS_OUTPUT.put_line( 'Compression Type : ' || 1_comptype_str); END; / Output of compression advisor estimate for advanced row compression (entire table): Number of blocks used by the compressed sample of the object : 165 Number of blocks used by the uncompressed sample of the object : 629 Number of rows in a block in compressed sample of the object : 599 Number of rows in a block in uncompressed sample of the object : 157 Estimated Compression Ratio of Sample : 3.8 Compression Type : “Compress Advanced” The following example shows how to estimate the compression ratio for advanced index compression (Low): SET SERVEROUTPUT ON DECLARE 1_blkcnt_cmp PLS_INTEGER; 1_blkcnt_uncmp PLS_INTEGER 1_row_cmp PLS_INTEGER; 1_row_uncmp PLS_INTEGER; 1_cmp_ratio NUMBER; 1_comptype_str VARCHAR2(32767); BEGIN DBMS_COMPRESSION.GET_COMPRESSION_RATIO ( scratchtbsname => 'USERS' , ownname => 'TEST' , objname => 'SALES_IDX' , subobjname => NULL , comptype => DBMS_COMPRESSION.COMP_INDEX_ADVANCED_LOW, blkcnt_cmp => 1_blkcnt_cmp, blkcnt_uncmp => 1_blkcnt_uncmp, row_cmp => 1_row_cmp, row_uncmp => 1_row_uncmp, cmp_ratio => 1_cmp_ratio, comptype_str => 1_comptype_str, subset_numrows => DBMS_COMPRESSION.comp_ratio_minrows, objtype => DBMS_COMPRESSION.objtype_index ); DBMS_OUTPUT.put_line( 'Number of blocks used by the compressed sample of the object : ' || 1_blkcnt_cmp); DBMS_OUTPUT.put_line( 'Number of blocks used by the uncompressed sample of the object : ' || 1_blkcnt_uncmp); DBMS_OUTPUT.put_line( 'Number of rows in a block in compressed sample of the object : ' || 1_row_cmp); DBMS_OUTPUT.put_line( 'Number of rows in a block in uncompressed sample of the object : ' || 1_row_uncmp); DBMS_OUTPUT.put_line( 'Estimated Compression Ratio of Sample : ' || 1_cmp_ratio); DBMS_OUTPUT.put_line( 'Compression Type : ' || 1_comptype_str); END; / Output of compression advisor estimate for advanced index compression (Low): Number of blocks used by the compressed sample of the object : 243 Number of blocks used by the uncompressed sample of the object : 539 Number of rows in a block in compressed sample of the object : 499 Number of rows in a block in uncompressed sample of the object : 145 Estimated Compression Ratio of Sample : 2.2 Compression Type : “Compress Advanced Low” The following example shows how to estimate the compression ratio for advanced LOB compression (Medium): SET SERVEROUTPUT ON DECLARE 1_blkcnt_cmp PLS_INTEGER; 1_blkcnt_uncmp PLS_INTEGER; 1_row_cmp PLS_INTEGER; 1_lobcnt PLS_INTEGER; 1_cmp_ratio NUMBER; 1_comptype_str VARCHAR2(32767); BEGIN DBMS_COMPRESSION.GET_COMPRESSION_RATIO ( scratchtbsname => 'USERS' , tabowner => 'TEST' , tabname => 'PARTS' , lobname => 'PART_DESCRIPTION' , partname => NULL , comptype => DBMS_COMPRESSION.COMP_LOB_MEDIUM, blkcnt_cmp => 1_blkcnt_cmp, blkcnt_uncmp => 1_blkcnt_uncmp, row_cmp => 1_row_cmp, lobcnt => 1_lobcnt, cmp_ratio => 1_cmp_ratio, comptype_str => 1_comptype_str, subset_numrows => DBMS_COMPRESSION.comp_ratio_lob_maxrows ); DBMS_OUTPUT.put_line( 'Number of blocks used by the compressed sample of the object : ' || 1_blkcnt_cmp); DBMS_OUTPUT.put_line( 'Number of blocks used by the uncompressed sample of the object : ' || 1_blkcnt_uncmp); DBMS_OUTPUT.put_line( 'Number of rows in a block in compressed sample of the object : ' || 1_row_cmp); DBMS_OUTPUT.put_line( 'Number of LOBS actually sampled : ' || 1_lobcnt); DBMS_OUTPUT.put_line( 'Estimated Compression Ratio of Sample : ' || 1_cmp_ratio); DBMS_OUTPUT.put_line( 'Compression Type : ' || 1_comptype_str); END; / Output of compression advisor estimate for advanced LOB compression (Medium): Number of blocks used by the compressed sample of the object : 199 Number of blocks used by the uncompressed sample of the object : 389 Number of rows in a block in compressed sample of the object : 293 Number of LOBS actually sampled : 55 Estimated Compression Ratio of Sample : 1.9 Compression Type : “Compress Medium” Usage Notes The procedure creates different tables in the scratch tablespace and runs analysis on these objects. It does not modify anything in the user-specified tables.