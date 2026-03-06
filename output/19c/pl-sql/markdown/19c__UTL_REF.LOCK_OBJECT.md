---
id: 19c__UTL_REF.LOCK_OBJECT
name: UTL_REF.LOCK_OBJECT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_REF
tags: [utl_ref]
source_file: UTL_REF.html
---

# UTL_REF.LOCK_OBJECT

This procedure locks an object given a reference. In addition, this procedure lets the program select the locked object.

## Syntax

```sql
SELECT VALUE(t) 
  INTO object 
  FROM object_table t 
  WHERE REF(t) = reference 
  FOR UPDATE;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| reference | FOR | IN | Reference of the object to lock. |
| object | FROM | IN | The PL/SQL variable that stores the locked object. This variable should be of the same object type as the locked object. |

## Usage Notes

The semantic of this subprogram is similar to the following SQL statement: SELECT VALUE(t) INTO object FROM object_table t WHERE REF(t) = reference FOR UPDATE; Unlike the preceding SQL statement, this subprogram does not require you to specify the object table name where the object resides. It is not necessary to lock an object before updating/deleting it. Syntax UTL_REF.LOCK_OBJECT ( reference IN REF "<typename>"); UTL_REF.LOCK_OBJECT ( reference IN REF "<typename>", object IN OUT "<typename>"); Parameters Table 274-4 LOCK_OBJECT Procedure Parameters Parameter Description reference Reference of the object to lock. object The PL/SQL variable that stores the locked object. This variable should be of the same object type as the locked object. Exceptions May be raised.