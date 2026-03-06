---
id: 19c__DBMS_SPACE.CREATE_TABLE_COST
name: DBMS_SPACE.CREATE_TABLE_COST
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SPACE
tags: [dbms_space]
source_file: DBMS_SPACE.html
---

# DBMS_SPACE.CREATE_TABLE_COST

This procedure is used in capacity planning to determine the size of the table given various attributes. The size of the object can vary widely based on the tablespace storage attributes, tablespace block size, and so on. There are two overloads of this procedure.

## Syntax

```sql
DBMS_SPACE.CREATE_TABLE_COST (
   tablespace_name    IN VARCHAR2,
   avg_row_size       IN NUMBER,
   row_count          IN NUMBER,
   pct_free           IN NUMBER,
   used_bytes         OUT NUMBER,
   alloc_bytes        OUT NUMBER);

DBMS_SPACE.CREATE_TABLE_COST (
   tablespace_name    IN VARCHAR2,
   colinfos           IN CREATE_TABLE_COST_COLUMNS,
   row_count          IN NUMBER,
   pct_free           IN NUMBER,
   used_bytes         OUT NUMBER,
   alloc_bytes        OUT NUMBER);

CREATE TYPE create_table_cost_colinfo IS OBJECT (
   COL_TYPE   VARCHAR(200),
   COL_SIZE   NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| tablespace_name | VARCHAR2 | IN | The tablespace in which the object will be created. The default is SYSTEM tablespace. |
| avg_row_size | NUMBER | IN | The anticipated average row size in the table |
| colinfos | CREATE_TABLE_COST_COLUMNS | IN | The description of the columns |
| row_count | NUMBER | IN | The anticipated number of rows in the table |
| pct_free | NUMBER | IN | The percentage of free space in each block for future expansion of existing rows due to updates |
| used_bytes | NUMBER | OUT | The space used by user data |
| alloc_bytes | NUMBER) | OUT | The size of the object taking into account the tablespace extent characteristics |

## Usage Notes

The first version takes the column information of the table as argument and outputs the table size. The second version takes the average row size of the table as argument and outputs the table size. This procedure can be used on tablespace of dictionary managed and locally managed extent management as well as manual and auto segment space management. Syntax DBMS_SPACE.CREATE_TABLE_COST ( tablespace_name IN VARCHAR2, avg_row_size IN NUMBER, row_count IN NUMBER, pct_free IN NUMBER, used_bytes OUT NUMBER, alloc_bytes OUT NUMBER); DBMS_SPACE.CREATE_TABLE_COST ( tablespace_name IN VARCHAR2, colinfos IN CREATE_TABLE_COST_COLUMNS, row_count IN NUMBER, pct_free IN NUMBER, used_bytes OUT NUMBER, alloc_bytes OUT NUMBER); CREATE TYPE create_table_cost_colinfo IS OBJECT ( COL_TYPE VARCHAR(200), COL_SIZE NUMBER); Parameters Table 158-7 CREATE_TABLE_COST Procedure Parameters Parameter Description tablespace_name The tablespace in which the object will be created. The default is SYSTEM tablespace. avg_row_size The anticipated average row size in the table colinfos The description of the columns row_count The anticipated number of rows in the table pct_free The percentage of free space in each block for future expansion of existing rows due to updates used_bytes The space used by user data alloc_bytes The size of the object taking into account the tablespace extent characteristics Usage Notes The used_bytes represent the actual bytes used by the data. This includes the overhead due to the block metadata, pctfree etc. The alloc_bytes represent the size of the table when it is created in the tablespace. This takes into account, the size of the extents in the tablespace and tablespace extent management properties. Examples -- review the parameters SELECT argument_name, data_type, type_owner, type_name FROM all_arguments WHERE object_name = 'CREATE_TABLE_COST' AND overload = 2 -- examine the input parameter type SELECT text FROM dba_source WHERE name = 'CREATE_TABLE_COST_COLUMNS'; -- drill down further into the input parameter type SELECT text FROM dba_source WHERE name = 'create_table_cost_colinfo'; set serveroutput on DECLARE ub NUMBER; ab NUMBER; cl sys.create_table_cost_columns; BEGIN cl := sys.create_table_cost_columns( sys.create_table_cost_colinfo('NUMBER',10), sys.create_table_cost_colinfo('VARCHAR2',30), sys.create_table_cost_colinfo('VARCHAR2',30), sys.create_table_cost_colinfo('DATE',NULL)); DBMS_SPACE.CREATE_TABLE_COST('SYSTEM',cl,100000,0,ub,ab); DBMS_OUTPUT.PUT_LINE('Used Bytes: ' || TO_CHAR(ub)); DBMS_OUTPUT.PUT_LINE('Alloc Bytes: ' || TO_CHAR(ab)); END; /