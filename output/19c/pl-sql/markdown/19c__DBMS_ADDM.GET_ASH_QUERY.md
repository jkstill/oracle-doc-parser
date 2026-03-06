---
id: 19c__DBMS_ADDM.GET_ASH_QUERY
name: DBMS_ADDM.GET_ASH_QUERY
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ADDM
tags: [dbms_addm]
source_file: DBMS_ADDM.html
---

# DBMS_ADDM.GET_ASH_QUERY

The function returns a string containing the SQL text of an ASH query identifying the rows in ASH with impact for the finding.

## Syntax

```sql
DBMS_ADDM.GET_ASH_QUERY (
   task_name           IN   VARCHAR2,
   finding_id          IN   NUMBER)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2 | IN | Name of the task |
| finding |  |  | ID of the finding within the task |

**Returns:** `VARCHAR2`

## Usage Notes

For most types of findings this identifies the exact rows in ASH corresponding to the finding. For some types of findings the query is an approximation and should not be used for exact identification of the finding's impact or the finding's specific activity. Syntax DBMS_ADDM.GET_ASH_QUERY ( task_name IN VARCHAR2, finding_id IN NUMBER) RETURN VARCHAR2; Parameters Table 14-14 GET_ASH_QUERY Function Parameters Parameter Description task_name Name of the task finding ID of the finding within the task Return Values A VARCHAR containing an ASH query identifying the rows in ASH with impact for the finding