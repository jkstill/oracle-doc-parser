---
id: 19c__OWA_OPT_LOCK.VERIFY_VALUES
name: OWA_OPT_LOCK.VERIFY_VALUES
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: OWA_OPT_LOCK
tags: [owa_opt_lock]
source_file: OWA_OPT_LOCK.html
---

# OWA_OPT_LOCK.VERIFY_VALUES

This function verifies whether values in the specified row have been updated since the last query.

## Syntax

```sql
OWA_OPT_LOCK.VERIFY_VALUES(
   p_old_values IN vcarray) 
 RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| p_old_values | vcarray) | IN | A PL/SQL table containing the following information: p_old_values(1) specifies the owner of the table. p_old_values(2) specifies the table. p_old_values(3) specifies the rowid of the row to verify. The remaining indexes contain values for the columns in the table. Typically, this parameter is passed in from the HTML form, where you have previously called the STORE_VALUES Procedure to store the row values on hidden form elements. |

**Returns:** `BOOLEAN`

## Usage Notes

Use this function with the STORE_VALUES Procedure . Syntax OWA_OPT_LOCK.VERIFY_VALUES( p_old_values IN vcarray) RETURN BOOLEAN; Parameters Table 226-5 VERIFY_VALUES Function Parameters Parameter Description p_old_values A PL/SQL table containing the following information: p_old_values(1) specifies the owner of the table. p_old_values(2) specifies the table. p_old_values(3) specifies the rowid of the row to verify. The remaining indexes contain values for the columns in the table. Typically, this parameter is passed in from the HTML form, where you have previously called the STORE_VALUES Procedure to store the row values on hidden form elements. Return Values TRUE if no other update has been performed, otherwise FALSE .