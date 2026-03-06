---
id: 19c__V$EMX_USAGE_STATS
name: V$EMX_USAGE_STATS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-EMX_USAGE_STATS.html
---

# V$EMX_USAGE_STATS

V$EMX_USAGE_STATS is used to track how often each report in Oracle Enterprise Manager Database Express (EM Express) is used and how long the EM Express servlet takes to serve these reports to the client.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| REPORT | VARCHAR2(400) |  |
| COUNT | NUMBER |  |
| LOGIN_ELAPSED_TIME | NUMBER |  |
| INITREQ_ELAPSED_TIME | NUMBER |  |
| SQL_ELAPSED_TIME | NUMBER |  |
| SEND_ELAPSED_TIME | NUMBER |  |
| TOTAL_ELAPSED_TIME | NUMBER |  |
| LAST_REQ_TIME | DATE |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content This view contains statistics such as the number of requests captured in the EM Express servlet for each report, total elapsed time for the EM Express servlet to render each report, as well as a detailed time breakdown including database login time, request initialization time, time to run the SQL query, and time to stream and send the query result back to the client. All statistics are accumulated over all requests for each EM Express report since the last time the database instance was restarted. It also includes the timestamp of the last request for each report.