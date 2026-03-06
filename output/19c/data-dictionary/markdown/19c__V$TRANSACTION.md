---
id: 19c__V$TRANSACTION
name: V$TRANSACTION
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-TRANSACTION.html
---

# V$TRANSACTION

V$TRANSACTION lists the active transactions in the system.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| ADDR | RAW(4 | 8) |  |
| XIDUSN | NUMBER |  |
| XIDSLOT | NUMBER |  |
| XIDSQN | NUMBER |  |
| UBAFIL | NUMBER |  |
| UBABLK | NUMBER |  |
| UBASQN | NUMBER |  |
| UBAREC | NUMBER |  |
| STATUS | VARCHAR2(16) |  |
| START_TIME | VARCHAR2(20) |  |
| START_SCNB | NUMBER |  |
| START_SCNW | NUMBER |  |
| START_UEXT | NUMBER |  |
| START_UBAFIL | NUMBER |  |
| START_UBABLK | NUMBER |  |
| START_UBASQN | NUMBER |  |
| START_UBAREC | NUMBER |  |
| SES_ADDR | RAW(4 | 8) |  |
| FLAG | NUMBER |  |
| SPACE | VARCHAR2(3) |  |
| RECURSIVE | VARCHAR2(3) |  |
| NOUNDO | VARCHAR2(3) |  |
| PTX | VARCHAR2(3) |  |
| NAME | VARCHAR2(256) |  |
| PRV_XIDUSN | NUMBER |  |
| PRV_XIDSLT | NUMBER |  |
| PRV_XIDSQN | NUMBER |  |
| PTX_XIDUSN | NUMBER |  |
| PTX_XIDSLT | NUMBER |  |
| PTX_XIDSQN | NUMBER |  |
| DSCN-B | NUMBER |  |
| DSCN-W | NUMBER |  |
| USED_UBLK | NUMBER |  |
| USED_UREC | NUMBER |  |
| LOG_IO | NUMBER |  |
| PHY_IO | NUMBER |  |
| CR_GET | NUMBER |  |
| CR_CHANGE | NUMBER |  |
| START_DATE | DATE |  |
| DSCN_BASE | NUMBER |  |
| DSCN_WRAP | NUMBER |  |
| START_SCN | NUMBER |  |
| DEPENDENT_SCN | NUMBER |  |
| XID | RAW(8) |  |
| PRV_XID | RAW(8) |  |
| PTX_XID | RAW(8) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content