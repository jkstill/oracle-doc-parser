---
id: 19c__OWA_OPT_LOCK.CHECKSUM
name: OWA_OPT_LOCK.CHECKSUM
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: OWA_OPT_LOCK
tags: [owa_opt_lock]
source_file: OWA_OPT_LOCK.html
---

# OWA_OPT_LOCK.CHECKSUM

This function returns a checksum value for a specified string, or for a row in a table. For a row in a table, the function calculates the checksum value based on the values of the columns in the row. This function comes in two versions.

## Syntax

```sql
OWA_OPT_LOCK.CHECKSUM(
   p_buff        IN       VARCHAR2) 
 RETURN NUMBER;

OWA_OPT_LOCK.CHECKSUM(
   p_owner       IN      VARCHAR2,
   p_tname       IN       VARCHAR2,
   p_rowid       IN       ROWID) 
  RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| p_buff | VARCHAR2) | IN | The nstring where you want to calculate the checksum . |
| p_owner | VARCHAR2 | IN | The owner of the table. |
| p_tname | VARCHAR2 | IN | The table name. |
| p_rowid | ROWID) | IN | The row in p_tname where you want to calculate the checksum value. Use the GET_ROWID Function to convert VCARRAY values to proper rowids. |

**Returns:** `NUMBER`

## Usage Notes

The first version returns a checksum based on the specified string. This is a "pure" 32-bit checksum executed by the database and based on the Internet 1 protocol. The second version returns a checksum based on the values of a row in a table. This is a "impure" 32-bit checksum based on the Internet 1 protocol. Syntax OWA_OPT_LOCK.CHECKSUM( p_buff IN VARCHAR2) RETURN NUMBER; OWA_OPT_LOCK.CHECKSUM( p_owner IN VARCHAR2, p_tname IN VARCHAR2, p_rowid IN ROWID) RETURN NUMBER; Parameters Table 226-2 CHECKSUM Function Parameters Parameter Description p_buff The nstring where you want to calculate the checksum . p_owner The owner of the table. p_tname The table name. p_rowid The row in p_tname where you want to calculate the checksum value. Use the GET_ROWID Function to convert VCARRAY values to proper rowids.