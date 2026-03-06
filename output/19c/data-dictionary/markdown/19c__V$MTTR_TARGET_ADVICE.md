---
id: 19c__V$MTTR_TARGET_ADVICE
name: V$MTTR_TARGET_ADVICE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-MTTR_TARGET_ADVICE.html
---

# V$MTTR_TARGET_ADVICE

V$MTTR_TARGET_ADVICE displays rows that predict the number of physical I/Os for the MTTR corresponding to each row.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| MTTR_TARGET_FOR_ESTIMATE | NUMBER |  |
| ADVICE_STATUS | VARCHAR2(5) |  |
| DIRTY_LIMIT | NUMBER |  |
| ESTD_CACHE_WRITES | NUMBER |  |
| ESTD_CACHE_WRITE_FACTOR | NUMBER |  |
| ESTD_TOTAL_WRITES | NUMBER |  |
| ESTD_TOTAL_WRITE_FACTOR | NUMBER |  |
| ESTD_TOTAL_IOS | NUMBER |  |
| ESTD_TOTAL_IO_FACTOR | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content The rows also compute a physical I/O factor, which is the ratio of the number of estimated I/Os to the number of I/Os actually performed by the current MTTR setting during the measurement interval. The content of the view is empty if MTTR advisory has not been turned on since database startup. Otherwise, it returns the advisory information collected. If advisory is currently off, then this information comes from the last time MTTR advisory was on. FAST_START_MTTR_TARGET must be set to a nonzero value if the STATISTICS_LEVEL parameter is dynamically modified to turn MTTR advisory on. If the FAST_START_MTTR_TARGET parameter is changed while MTTR advisory is on, then MTTR advisory is temporarily turned off until the new FAST_START_MTTR_TARGET setting takes effect. During this transition period, the contents of V$MTTR_TARGET_ADVICE reflect the simulation result for the old MTTR setting. See Also: " FAST_START_MTTR_TARGET " " STATISTICS_LEVEL " See Also: " FAST_START_MTTR_TARGET " " STATISTICS_LEVEL "