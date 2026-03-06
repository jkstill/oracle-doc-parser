---
id: 19c__V$BACKUP_DEVICE
name: V$BACKUP_DEVICE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-BACKUP_DEVICE.html
---

# V$BACKUP_DEVICE

V$BACKUP_DEVICE displays information about supported backup devices.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| DEVICE_TYPE | VARCHAR2(17) |  |
| DEVICE_NAME | VARCHAR2(513) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content If a device type does not support named devices, then one row with the device type and a null device name is returned for that device type. If a device type supports named devices then one row is returned for each available device of that type. The special device type DISK is not returned by this view because it is always available.