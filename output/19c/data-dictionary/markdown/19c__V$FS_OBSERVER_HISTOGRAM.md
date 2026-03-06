---
id: 19c__V$FS_OBSERVER_HISTOGRAM
name: V$FS_OBSERVER_HISTOGRAM
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-FS_OBSERVER_HISTOGRAM.html
---

# V$FS_OBSERVER_HISTOGRAM

V$FS_OBSERVER_HISTOGRAM displays statistics that are based on the frequency of successful pings between the observer and primary database for different time intervals. The wait event in this histogram is the observer's wait until pings to the primary succeed.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OBSERVER_NAME | VARCHAR2(513) |  |
| OBSERVER_HOST | VARCHAR2(513) |  |
| WAIT_TIME | NUMBER |  |
| WAIT_COUNT | NUMBER |  |
| LAST_UPDATE_TIME | VARCHAR2(20) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content The histogram displays only when there were ping failures between the observer and the primary database. No rows are shown in this view for unregistered observers. These statistics can be used to select an appropriate value for the FastStartFailoverThreshold configuration property for your environment. See Also: Oracle Data Guard Broker for more information about the FastStartFailoverThreshold configuration property See Also: Oracle Data Guard Broker for more information about the FastStartFailoverThreshold configuration property Example Assume that the following shows the status of observer’s pings to the primary: Ping time Ping result --------- ----------- 1:00:00 SUCCESS 1:00:03 FAIL 1:00:06 FAIL 1:00:09 SUCCESS => Wait time of 6 seconds 1:00:12 SUCCESS 1:00:15 FAIL 1:00:18 FAIL 1:00:21 SUCCESS => Wait time of 6 seconds 1:00:24 SUCCESS 1:00:27 FAIL 1:00:30 SUCCESS => Wait time of 3 seconds These ping results will result in the histogram view below: WAIT_TIME WAIT_COUNT LAST_UPDATE_TIME 3 1 1:00:30 6 2 1:00:21 9 0 12 0 ... In this case, the FastStartFailoverThreshold value should be set to larger than 6 because communication between the observer and the primary sometimes fails for 6 seconds.