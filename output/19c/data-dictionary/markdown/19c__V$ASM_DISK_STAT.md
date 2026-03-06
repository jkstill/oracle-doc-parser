---
id: 19c__V$ASM_DISK_STAT
name: V$ASM_DISK_STAT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-ASM_DISK_STAT.html
---

# V$ASM_DISK_STAT

V$ASM_DISK_STAT displays performance statistics in the same way that V$ASM_DISK does, but without performing discovery of new disks

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content This results in a less expensive operation. However, since discovery is not performed, the output of this view does not include any data about disks that are new to the system. The columns for V$ASM_DISK_STAT are the same as those for V$ASM_DISK . See Also: " V$ASM_DISK " See Also: " V$ASM_DISK "