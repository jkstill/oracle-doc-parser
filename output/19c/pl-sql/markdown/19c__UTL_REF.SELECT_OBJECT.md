---
id: 19c__UTL_REF.SELECT_OBJECT
name: UTL_REF.SELECT_OBJECT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_REF
tags: [utl_ref]
source_file: UTL_REF.html
---

# UTL_REF.SELECT_OBJECT

This procedure selects an object given its reference. The selected object is retrieved from the database and its value is put into the PL/SQL variable 'object'.

## Syntax

```sql
SELECT VALUE(t) 
INTO object 
FROM object_table t 
WHERE REF(t) = reference;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| reference |  |  | Reference to the object to select or retrieve. |
| object | FROM | IN | The PL/SQL variable that stores the selected object; this variable should be of the same object type as the referenced object. |

## Usage Notes

The semantic of this subprogram is similar to the following SQL statement: SELECT VALUE(t) INTO object FROM object_table t WHERE REF(t) = reference; Unlike the preceding SQL statement, this subprogram does not require you to specify the object table name where the object resides. Syntax UTL_REF.SELECT_OBJECT ( reference IN REF "<typename>", object IN OUT "<typename>"); Parameters Table 274-5 SELECT_OBJECT Procedure Parameters Parameter Description reference Reference to the object to select or retrieve. object The PL/SQL variable that stores the selected object; this variable should be of the same object type as the referenced object. Exceptions May be raised.