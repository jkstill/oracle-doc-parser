---
id: 19c__ALL_MEASURE_FOLDER_CONTENTS
name: ALL_MEASURE_FOLDER_CONTENTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_MEASURE_FOLDER_CONTENTS.html
---

# ALL_MEASURE_FOLDER_CONTENTS

ALL_MEASURE_FOLDER_CONTENTS describes the contents of the OLAP measure folders accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the measure folder |
| MEASURE_FOLDER_NAME | VARCHAR2(128) | Name of a measure folder |
| CUBE_OWNER | VARCHAR2(128) | Owner of the cube |
| CUBE_NAME | VARCHAR2(128) | Name of a cube included in the measure folder |
| MEASURE_NAME | VARCHAR2(128) | Name of a measure in the cube |
| ORDER_NUM | NUMBER | Order number of the measure in the folder |

## Usage Notes

Related Views DBA_MEASURE_FOLDER_CONTENTS describes the contents of all OLAP measure folders in the database. USER_MEASURE_FOLDER_CONTENTS describes the contents of the OLAP measure folders owned by the current user. This view does not display the OWNER column. See Also: " DBA_MEASURE_FOLDER_CONTENTS " " USER_MEASURE_FOLDER_CONTENTS " See Also: " DBA_MEASURE_FOLDER_CONTENTS " " USER_MEASURE_FOLDER_CONTENTS "