---
id: 19c__V$ROLLNAME
name: V$ROLLNAME
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-ROLLNAME.html
---

# V$ROLLNAME

V$ROLLNAME lists the names of all online rollback segments. It can only be accessed when the database is open.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| USN | NUMBER | Rollback (undo) segment number |
| NAME | VARCHAR2(30) | Rollback segment name |
| CON_ID | NUMBER | The ID of the container to which the data pertains. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content