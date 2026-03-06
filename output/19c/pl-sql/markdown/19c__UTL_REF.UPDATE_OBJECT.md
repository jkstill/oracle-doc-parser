---
id: 19c__UTL_REF.UPDATE_OBJECT
name: UTL_REF.UPDATE_OBJECT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_REF
tags: [utl_ref]
source_file: UTL_REF.html
---

# UTL_REF.UPDATE_OBJECT

This procedure updates an object given a reference. The referenced object is updated with the value contained in the PL/SQL variable 'object'.

## Syntax

```sql
UPDATE object_table t 
SET VALUE(t) = object 
WHERE REF(t) = reference;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| reference |  |  | Reference of the object to update. |
| object | WHERE | IN | The PL/SQL variable that contains the new value of the object. This variable should be of the same object type as the object to update. |

## Usage Notes

The semantic of this subprogram is similar to the following SQL statement: UPDATE object_table t SET VALUE(t) = object WHERE REF(t) = reference; Unlike the preceding SQL statement, this subprogram does not require you to specify the object table name where the object resides. Syntax UTL_REF.UPDATE_OBJECT ( reference IN REF "<typename>", object IN "<typename>"); Parameters Table 274-6 UPDATE_OBJECT Procedure Parameters Parameter Description reference Reference of the object to update. object The PL/SQL variable that contains the new value of the object. This variable should be of the same object type as the object to update. Exceptions May be raised.