---
id: 19c__V$WAITCLASSMETRIC
name: V$WAITCLASSMETRIC
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-WAITCLASSMETRIC.html
---

# V$WAITCLASSMETRIC

V$WAITCLASSMETRIC displays metric values of wait classes for the most recent 60-second interval. A history of the last one hour will be kept in the system.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| BEGIN_TIME | DATE |  |
| END_TIME | DATE |  |
| INTSIZE_CSEC | NUMBER |  |
| WAIT_CLASS# | NUMBER |  |
| WAIT_CLASS_ID | NUMBER |  |
| AVERAGE_WAITER_COUNT | NUMBER |  |
| DBTIME_IN_WAIT | NUMBER |  |
| TIME_WAITED | NUMBER |  |
| WAIT_COUNT | NUMBER |  |
| TIME_WAITED_FG | NUMBER |  |
| WAIT_COUNT_FG | NUMBER |  |
| CON_ID | NUMBER |  |