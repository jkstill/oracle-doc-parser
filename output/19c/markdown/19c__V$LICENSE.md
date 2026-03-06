---
id: 19c__V$LICENSE
name: V$LICENSE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-LICENSE.html
---

# V$LICENSE

V$LICENSE displays information about license limits.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SESSIONS_MAX | NUMBER |  |
| SESSIONS_WARNING | NUMBER |  |
| SESSIONS_CURRENT | NUMBER |  |
| SESSIONS_HIGHWATER | NUMBER |  |
| USERS_MAX | NUMBER |  |
| CPU_COUNT_CURRENT | NUMBER |  |
| CPU_CORE_COUNT_CURRENT | NUMBER |  |
| CPU_SOCKET_COUNT_CURRENT | NUMBER |  |
| CPU_COUNT_HIGHWATER | NUMBER |  |
| CPU_CORE_COUNT_HIGHWATER | NUMBER |  |
| CPU_SOCKET_COUNT_HIGHWATER | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Note: The availability of the CPU core count and CPU socket count statistics is subject to the operating system platform on which the Oracle Database is running. If a statistic is unavailable, the view will return NULL for the statistic value. Note: The availability of the CPU core count and CPU socket count statistics is subject to the operating system platform on which the Oracle Database is running. If a statistic is unavailable, the view will return NULL for the statistic value.