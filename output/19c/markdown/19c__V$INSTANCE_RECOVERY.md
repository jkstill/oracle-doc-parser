---
id: 19c__V$INSTANCE_RECOVERY
name: V$INSTANCE_RECOVERY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-INSTANCE_RECOVERY.html
---

# V$INSTANCE_RECOVERY

Set the LOG_CHECKPOINT_TIMEOUT initialization parameter

## Columns

| Column | Type | Description |
|--------|------|-------------|
| RECOVERY_ESTIMATED_IOS | NUMBER |  |
| ACTUAL_REDO_BLKS | NUMBER |  |
| TARGET_REDO_BLKS | NUMBER |  |
| LOG_FILE_SIZE_REDO_BLKS | NUMBER |  |
| LOG_CHKPT_TIMEOUT_REDO_BLKS | NUMBER |  |
| LOG_CHKPT_INTERVAL_REDO_BLKS | NUMBER |  |
| FAST_START_IO_TARGET_REDO_BLKS | NUMBER |  |
| TARGET_MTTR | NUMBER |  |
| ESTIMATED_MTTR | NUMBER |  |
| CKPT_BLOCK_WRITES | NUMBER |  |
| OPTIMAL_LOGFILE_SIZE | NUMBER |  |
| ESTD_CLUSTER_AVAILABLE_TIME | NUMBER |  |
| WRITES_MTTR | NUMBER |  |
| WRITES_LOGFILE_SIZE | NUMBER |  |
| WRITES_LOG_CHECKPOINT_SETTINGS | NUMBER |  |
| WRITES_OTHER_SETTINGS | NUMBER |  |
| WRITES_AUTOTUNE | NUMBER |  |
| WRITES_FULL_THREAD_CKPT | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Set the LOG_CHECKPOINT_TIMEOUT initialization parameter Set the LOG_CHECKPOINT_INTERVAL initialization parameter Set the FAST_START_MTTR_TARGET initialization parameter Set the size of the smallest redo log