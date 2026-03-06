---
id: 19c__DBA_WORKLOAD_TRACKED_COMMITS
name: DBA_WORKLOAD_TRACKED_COMMITS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_WORKLOAD_TRACKED_COMMITS.html
---

# DBA_WORKLOAD_TRACKED_COMMITS

DBA_WORKLOAD_TRACKED_COMMITS displays the commits tracked every second during a database replay.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| REPLAY_DIR_NUMBER | NUMBER | The numerical value that is associated with the subdirectory under the replay directory. See REPLAY_DIR_NUMBER in DBA_WORKLOAD_REPLAYS |
| INSTANCE_NUMBER | NUMBER(38) | The instance where the commit is executed |
| FILE_ID | NUMBER(38) | The file ID |
| CALL_CTR | NUMBER(38) | The call counter of the commit |
| COMMIT_SCN | NUMBER(38) | The recorded commit SCN value |
| PREV_GLOBAL_COMMIT_FILE_ID | NUMBER(38) | The file ID of the latest commit across all sessions |
| PREV_GLOBAL_COMMIT_SCN | NUMBER(38) | The recorded SCN of the latest commit across all sessions |
| PREV_LOCAL_COMMIT_CALL_CTR | NUMBER(38) | The call counter of the latest commit in the same session |
| CAPTURE_COMMIT_TIME | NUMBER(38) | The time in seconds since the capture started |
| CAPTURE_COMMIT_TIME_DELTA | NUMBER(38) | The elapsed time in seconds since the previous commit across all sessions during capture |
| REPLAY_COMMIT_TIME | NUMBER(38) | The time in seconds since the replay started |
| REPLAY_COMMIT_TIME_DELTA | NUMBER(38) | The elapsed time in seconds since the previous commit across all sessions during the replay |

## Usage Notes

See Also: DBA_WORKLOAD_REPLAYS See Also: DBA_WORKLOAD_REPLAYS