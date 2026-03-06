---
id: 19c__V$OFS_STATS
name: V$OFS_STATS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-OFS_STATS.html
---

# V$OFS_STATS

V$OFS_STATS displays performance statistics for various Oracle File System operations. These statistics are maintained at per mount level.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OFS_MNTPNT | VARCHAR2(4096) |  |
| OFS_LOOKUP | NUMBER |  |
| OFS_FORGET | NUMBER |  |
| OFS_GETATTR | NUMBER |  |
| OFS_SETATTR | NUMBER |  |
| OFS_READLINK | NUMBER |  |
| OFS_SYMLINK | NUMBER |  |
| OFS_MKNOD | NUMBER |  |
| OFS_MKDIR | NUMBER |  |
| OFS_UNLINK | NUMBER |  |
| OFS_RMDIR | NUMBER |  |
| OFS_RENAME | NUMBER |  |
| OFS_LINK | NUMBER |  |
| OFS_OPEN | NUMBER |  |
| OFS_READ | NUMBER |  |
| OFS_WRITE | NUMBER |  |
| OFS_STATFS | NUMBER |  |
| OFS_RELEASE | NUMBER |  |
| OFS_FSYNC | NUMBER |  |
| OFS_SETXATTR | NUMBER |  |
| OFS_GETXATTR | NUMBER |  |
| OFS_LISTXATTR | NUMBER |  |
| OFS_REMOVEXATTR | NUMBER |  |
| OFS_FLUSH | NUMBER |  |
| OFS_INIT | NUMBER |  |
| OFS_OPENDIR | NUMBER |  |
| OFS_READDIR | NUMBER |  |
| OFS_RELEASEDIR | NUMBER |  |
| OFS_FSYNCDIR | NUMBER |  |
| OFS_GETLK | NUMBER |  |
| OFS_SETLK | NUMBER |  |
| OFS_SETLKW | NUMBER |  |
| OFS_ACCESS | NUMBER |  |
| OFS_CREATE | NUMBER |  |
| OFS_INTERRUPT | NUMBER |  |
| OFS_BMAP | NUMBER |  |
| OFS_DESTROY | NUMBER |  |
| OFS_BYTES_READ | NUMBER |  |
| OFS_BYTES_WRITTEN | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Note: This database view is supported only on the Linux operating system. See Also: " V$OFSMOUNT " Note: This database view is supported only on the Linux operating system. See Also: " V$OFSMOUNT "