---
id: 19c__DBMS_REDEFINITION.REDEF_TABLE
name: DBMS_REDEFINITION.REDEF_TABLE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_REDEFINITION
tags: [dbms_redefinition]
source_file: DBMS_REDEFINITION.html
---

# DBMS_REDEFINITION.REDEF_TABLE

This procedure provides a single interface that integrates several redefinition steps including the CAN_REDEF_TABLE Procedure, the START_REDEF_TABLE Procedure, the COPY_TABLE_DEPENDENTS Procedure and the FINISH_REDEF_TABLE Procedure.

## Syntax

```sql
DBMS_REDEFINITION.REDEF_TABLE (
   uname                       IN  VARCHAR2,
   tname                       IN  VARCHAR2,    
   table_compression_type      IN  VARCHAR2 := NULL, 
   table_part_tablespace       IN  VARCHAR2 := NULL, 
   index_key_compression_type  IN  VARCHAR2 := NULL,
   index_tablespace            IN  VARCHAR2 := NULL,
   lob_compression_type        IN  VARCHAR2 := NULL,
   lob_tablespace              IN  VARCHAR2 := NULL,
   lob_store_as                IN  VARCHAR2 := NULL,
   refresh_dep_mviews          IN  VARCHAR2 := 'N',
   dml_lock_timeout            IN  PLS_INTEGER := NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| uname | VARCHAR2 | IN | Schema name of the table |
| tname | VARCHAR2 | IN | Name of the table to be redefined |
| table_compression_type | VARCHAR2 | IN | Text string of the table compression clause. NULL means there is no change. |
| table_part_tablespace | VARCHAR2 | IN | Tablespace name for the entire table or partitions. NULL means there is no change. |
| index_key_compression_type | VARCHAR2 | IN | Text string of the compression clause for all indexes on the table. NULL means there is no change. |
| index_tablespace | VARCHAR2 | IN | Tablespace name for all indexes on the table. NULL means there is no change. |
| lob_compression_type | VARCHAR2 | IN | Text string of the compression clause for all LOBs in the entire table. NULL means there is no change. |
| lob_tablespace | VARCHAR2 | IN | Tablespace name for all LOBs in the table. NULL means there is no change. |
| lob_store_as | VARCHAR2 | IN | Specifies LOB store as 'SECUREFILE' or 'BASICFILE' . NULL means there is no change. |
| refresh_dep_mviews | VARCHAR2 | IN | When set to 'Y' , fast refresh of dependent materialized views is performed once at the end of the redefinition operation. |
| dml_lock_timeout | PLS_INTEGER | IN | Specifies the number of seconds the procedure waits for its required locks before failing. The permissible range of values for timeout is 0 to 1,000,000. The default is NULL (wait mode). |

## Usage Notes

This procedure can change data storage properties including tablespaces (for table, partition, subpartition, index, LOB column), compress type (for table, partition, subpartition, index, LOB column) and STORE_AS clause for the LOB column. Syntax DBMS_REDEFINITION.REDEF_TABLE ( uname IN VARCHAR2, tname IN VARCHAR2, table_compression_type IN VARCHAR2 := NULL, table_part_tablespace IN VARCHAR2 := NULL, index_key_compression_type IN VARCHAR2 := NULL, index_tablespace IN VARCHAR2 := NULL, lob_compression_type IN VARCHAR2 := NULL, lob_tablespace IN VARCHAR2 := NULL, lob_store_as IN VARCHAR2 := NULL, refresh_dep_mviews IN VARCHAR2 := 'N', dml_lock_timeout IN PLS_INTEGER := NULL); Parameters Table 138-10 REDEF_TABLE Procedure Parameters Parameter Description uname Schema name of the table tname Name of the table to be redefined table_compression_type Text string of the table compression clause. NULL means there is no change. table_part_tablespace Tablespace name for the entire table or partitions. NULL means there is no change. index_key_compression_type Text string of the compression clause for all indexes on the table. NULL means there is no change. index_tablespace Tablespace name for all indexes on the table. NULL means there is no change. lob_compression_type Text string of the compression clause for all LOBs in the entire table. NULL means there is no change. lob_tablespace Tablespace name for all LOBs in the table. NULL means there is no change. lob_store_as Specifies LOB store as 'SECUREFILE' or 'BASICFILE' . NULL means there is no change. refresh_dep_mviews When set to 'Y' , fast refresh of dependent materialized views is performed once at the end of the redefinition operation. dml_lock_timeout Specifies the number of seconds the procedure waits for its required locks before failing. The permissible range of values for timeout is 0 to 1,000,000. The default is NULL (wait mode). Examples BEGIN DBMS_REDEFINITION.REDEF_TABLE( uname => 'TABOWNER2', tname => 'EMP2', table_compression_type => 'ROW STORE COMPRESS ADVANCED', table_part_tablespace => 'NEWTBS', index_key_compression_type => 'COMPRESS 1', index_tablespace => 'NEWIDXTBS', lob_compression_type => 'COMPRESS HIGH', lob_tablespace => 'SLOBTBS', lob_store_as => 'SECUREFILE'); END; See Also: Oracle Database Administrator's Guide regarding "Performing Online Redefinition with the REDEF_TABLE Procedure"