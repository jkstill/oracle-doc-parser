---
id: 19c__V$NFS_OPEN_FILES
name: V$NFS_OPEN_FILES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-NFS_OPEN_FILES.html
---

# V$NFS_OPEN_FILES

V$NFS_OPEN_FILES displays information about all the files currently opened by clients at the NFS server.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| CLIENTID | NUMBER |  |
| OPENOWNEROPAQUE | VARCHAR2(2000) |  |
| OPENSTATEID | RAW(16) |  |
| FILEHANDLE | RAW(32) |  |
| OPENSEQUENCEID | NUMBER |  |
| OPENREAD | VARCHAR2(5) |  |
| OPENWRITE | VARCHAR2(5) |  |
| SHAREACCESS | VARCHAR2(15) |  |
| SHAREDENY | VARCHAR2(13) |  |
| CONFIRMED | VARCHAR2(5) |  |
| CON_ID | NUMBER |  |