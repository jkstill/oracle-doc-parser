---
id: 19c__V$OSSTAT
name: V$OSSTAT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-OSSTAT.html
---

# V$OSSTAT

V$OSSTAT displays system utilization statistics from the operating system. One row is returned for each system statistic.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| STAT_NAME | VARCHAR2(64) |  |
| VALUE | NUMBER |  |
| OSSTAT_ID | NUMBER |  |
| COMMENTS | VARCHAR2(64) |  |
| CUMULATIVE | VARCHAR2(3) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Note: The availability of all statistics except for NUM_CPUS and RSRC_MGR_CPU_WAIT_TIME is subject to the operating system platform on which the Oracle Database is running. Note: The availability of all statistics except for NUM_CPUS and RSRC_MGR_CPU_WAIT_TIME is subject to the operating system platform on which the Oracle Database is running.