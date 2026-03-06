---
id: 19c__V$OBJECT_USAGE
name: V$OBJECT_USAGE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: objects
tags: [dynamic_performance]
source_file: V-OBJECT_USAGE.html
---

# V$OBJECT_USAGE

The V$OBJECT_USAGE view is deprecated in Oracle Database 12 c Release 1 (12.1) and maintained for backward compatibility. Support for this view may be removed in a future release. Oracle recommends that you use the USER_OBJECT_USAGE view instead of the V$OBJECT_USAGE view.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| INDEX_NAME | VARCHAR2 | Index name in sys.obj$.name |
| TABLE_NAME | VARCHAR2 | Table name in sys.obj$.name |
| MONITORING | VARCHAR2 | YES | NO |
| USED | VARCHAR2 | YES | NO |
| START_MONITORING | VARCHAR2 | Start monitoring time in sys.object_stats.start_monitoring |
| END_MONITORING | VARCHAR2 | End monitoring time in sys.object_stats.end_monitoring |

## Usage Notes

Note: The V$OBJECT_USAGE view is deprecated in Oracle Database 12 c Release 1 (12.1) and maintained for backward compatibility. Support for this view may be removed in a future release. Oracle recommends that you use the USER_OBJECT_USAGE view instead of the V$OBJECT_USAGE view. Note: The V$OBJECT_USAGE view is deprecated in Oracle Database 12 c Release 1 (12.1) and maintained for backward compatibility. Support for this view may be removed in a future release. Oracle recommends that you use the USER_OBJECT_USAGE view instead of the V$OBJECT_USAGE view. See Also: " USER_OBJECT_USAGE " " DBA_OBJECT_USAGE " See Also: " USER_OBJECT_USAGE " " DBA_OBJECT_USAGE "