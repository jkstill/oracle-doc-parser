---
id: 19c__OWA_OPT_LOCK.STORE_VALUES
name: OWA_OPT_LOCK.STORE_VALUES
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: OWA_OPT_LOCK
tags: [owa_opt_lock]
source_file: OWA_OPT_LOCK.html
---

# OWA_OPT_LOCK.STORE_VALUES

This procedure stores the column values of the row that you want to update later. The values are stored in hidden HTML form elements.

## Syntax

```sql
OWA_OPT_LOCK.STORE_VALUES(
   p_owner        IN       VARCHAR2,
   p_tname        IN       VARCHAR2,
   p_rowid        IN       ROWID);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| p_owner | VARCHAR2 | IN | The owner of the table. |
| p_tname | VARCHAR2 | IN | The name of the table. |
| p_rowid | ROWID) | IN | The row where you want to store values. |

## Usage Notes

Syntax OWA_OPT_LOCK.STORE_VALUES( p_owner IN VARCHAR2, p_tname IN VARCHAR2, p_rowid IN ROWID); Parameters Table 226-4 STORE_VALUES Procedure Parameters Parameter Description p_owner The owner of the table. p_tname The name of the table. p_rowid The row where you want to store values. Usage Notes Before updating the row, compare these values with the current row values to ensure that the values in the row have not been changed. If the values have changed, you can warn the users and let them decide if the update should take place. The procedure generates series of hidden form elements: One hidden form element is created for the table owner. The name of the element is " old _p_tname ", where p_tname is the name of the table. The value of the element is the owner name. One hidden form element is created for the table name. The name of the element is " old _p_tname ", where p_tname is the name of the table. The value of the element is the table name. One element is created for each column in the row. The name of the element is " old _p_tname ", where p_tname is the name of the table. The value of the element is the column value. See also the VERIFY_VALUES Function .