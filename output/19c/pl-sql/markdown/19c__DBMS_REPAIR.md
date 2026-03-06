---
id: 19c__DBMS_REPAIR
name: DBMS_REPAIR
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_REPAIR
tags: [dbms_repair]
source_file: DBMS_REPAIR.html
---

# DBMS_REPAIR

This topic shows examples of DBMS_REPAIR usage.

## Syntax

```sql
/* Fix the bitmap status for all the blocks in table mytab in schema sys */

EXECUTE DBMS_REPAIR.SEGMENT_FIX_STATUS('SYS', 'MYTAB'); 

/* Mark block number 45, filenumber 1 for table mytab in sys schema as FULL.*/ 

EXECUTE DBMS_REPAIR.SEGMENT_FIX_STATUS('SYS', 'MYTAB', TABLE_OBJECT,1, 45, 1);
```

## Usage Notes

/* Fix the bitmap status for all the blocks in table mytab in schema sys */ EXECUTE DBMS_REPAIR.SEGMENT_FIX_STATUS('SYS', 'MYTAB'); /* Mark block number 45, filenumber 1 for table mytab in sys schema as FULL.*/ EXECUTE DBMS_REPAIR.SEGMENT_FIX_STATUS('SYS', 'MYTAB', TABLE_OBJECT,1, 45, 1);