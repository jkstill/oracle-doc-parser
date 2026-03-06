---
id: 19c__V$ASM_DISKGROUP_STAT
name: V$ASM_DISKGROUP_STAT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-ASM_DISKGROUP_STAT.html
---

# V$ASM_DISKGROUP_STAT

V$ASM_DISKGROUP_STAT displays performance statistics in the same way that V$ASM_DISKGROUP does, but without performing discovery of new disk groups.

## Usage Notes

This results in a less expensive operation. However, since discovery is not performed, the output of this view does not include any data about disk groups that are new to the system. The columns for V$ASM_DISKGROUP_STAT are the same as those for V$ASM_DISKGROUP . See Also: " V$ASM_DISKGROUP " See Also: " V$ASM_DISKGROUP "