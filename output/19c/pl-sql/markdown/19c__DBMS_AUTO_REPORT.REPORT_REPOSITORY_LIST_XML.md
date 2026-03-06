---
id: 19c__DBMS_AUTO_REPORT.REPORT_REPOSITORY_LIST_XML
name: DBMS_AUTO_REPORT.REPORT_REPOSITORY_LIST_XML
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AUTO_REPORT
tags: [dbms_auto_report]
source_file: DBMS_AUTO_REPORT.html
---

# DBMS_AUTO_REPORT.REPORT_REPOSITORY_LIST_XML

This procedure obtains an XML report of the list of SQL Monitor and Real-time ADDM data captured in AWR.

## Syntax

```sql
DBMS_AUTO_REPORT.REPORT_REPOSITORY_LIST_XML (
    active_since              IN DATE     DEFAULT NULL,
    active_upto               IN DATE     DEFAULT NULL,
    snapshot_id               IN NUMBER   DEFAULT NULL,
    dbid                      IN NUMBER   DEFAULT NULL,
    inst_id                   IN NUMBER   DEFAULT NULL,
    con_dbid                  IN NUMBER   DEFAULT NULL,
    session_id                IN NUMBER   DEFAULT NULL,
    session_serial            IN NUMBER   DEFAULT NULL,
    component_name            IN VARCHAR2 DEFAULT NULL,
    key1                      IN VARCHAR2 DEFAULT NULL,
    key2                      IN VARCHAR2 DEFAULT NULL,
    key3                      IN VARCHAR2 DEFAULT NULL,
    report_level              IN VARCHAR2 DEFAULT 'TYPICAL',
    base_path                 IN VARCHAR2 DEFAULT NULL)
RETURNS XMLTYPE
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| active_since | DATE | IN | Start of a time range used to select data. When a time range is specified, only those data are included in the list that were active during the time range. When no value is specified the time range is chosen as the last 24 hours ending at the current system time. |
| active_upto | DATE | IN | Same as active_since except that it is the end of the time range |
| snapshot_id | NUMBER | IN | If a value is specified, only those data captured during the specified snapshot ID are included in the list report. If no value is specified, no filtering is performed on snapshot ID. |
| dbid | NUMBER | IN | If a value is specified, only those data captured for the specified database ID are included in the list report. If no value is specified, no filtering is performed on database ID |
| inst_id | NUMBER | IN | If a value is specified, only those data captured on the specified instance number are included in the list report. If no value is specified, no filtering is performed on the instance ID. |
| con_dbid | NUMBER | IN | If a value is specified, only those data captured on the specified container DBID are included in the list report. If no value is specified, no filtering is performed on the container DBID. |
| session_id | NUMBER | IN | If a value is specified, only those data captured for the specified session ID are included in the list report. If no value is specified, no filtering is performed on session ID. |
| session_serial | NUMBER | IN | If a value is specified, only those data captured for the specified session are included in the list report. If no value is specified, no filtering is performed on session serial number. This parameter should be used in conjunction with the session_id parameter. |
| component_name | VARCHAR2 | IN | Can be 'sqlmonitor' for SQL Monitor data or 'rtaddm' for Real-time ADDM data. If a value is specified then data pertaining only to the specified component will be included in the list report. If no value is specified, no filtering is performed. |
| key1 | VARCHAR2 | IN | Key value relevant to a component. For SQL Monitor, key1 is the SQL ID of the captured SQL statement. If a value is specified, only those data having specified value for key1 are included, else no filtering is performed on key1 . |
| key2 | VARCHAR2 | IN | Key value relevant to a component. For SQL Monitor, key2 is the SQL execution ID of the captured SQL statement. If a value is specified, only those data having specified value for key2 are included, else no filtering is performed on key2 . |
| key3 | VARCHAR2 | IN | Key value relevant to a component. For SQL Monitor, key3 is the SQL execution start time of the captured SQL statement. If a value is specified, then only those data having specified value for key3 are included, else no filtering is performed on key3 . |
| report_level | VARCHAR2 | IN | Currently only 'TYPICAL' is used |
| base_path | VARCHAR2 | IN | Unused/Non-operative |

**Returns:** `UNKNOWN`

## Usage Notes

The input parameters can be used to select and restrict which captured data will be included in the list report. All parameters are optional. Syntax DBMS_AUTO_REPORT.REPORT_REPOSITORY_LIST_XML ( active_since IN DATE DEFAULT NULL, active_upto IN DATE DEFAULT NULL, snapshot_id IN NUMBER DEFAULT NULL, dbid IN NUMBER DEFAULT NULL, inst_id IN NUMBER DEFAULT NULL, con_dbid IN NUMBER DEFAULT NULL, session_id IN NUMBER DEFAULT NULL, session_serial IN NUMBER DEFAULT NULL, component_name IN VARCHAR2 DEFAULT NULL, key1 IN VARCHAR2 DEFAULT NULL, key2 IN VARCHAR2 DEFAULT NULL, key3 IN VARCHAR2 DEFAULT NULL, report_level IN VARCHAR2 DEFAULT 'TYPICAL', base_path IN VARCHAR2 DEFAULT NULL) RETURNS XMLTYPE Parameters Table 31-4 REPORT_REPOSITORY_LIST_XML Function Parameters Parameter Description active_since Start of a time range used to select data. When a time range is specified, only those data are included in the list that were active during the time range. When no value is specified the time range is chosen as the last 24 hours ending at the current system time. active_upto Same as active_since except that it is the end of the time range snapshot_id If a value is specified, only those data captured during the specified snapshot ID are included in the list report. If no value is specified, no filtering is performed on snapshot ID. dbid If a value is specified, only those data captured for the specified database ID are included in the list report. If no value is specified, no filtering is performed on database ID inst_id If a value is specified, only those data captured on the specified instance number are included in the list report. If no value is specified, no filtering is performed on the instance ID. con_dbid If a value is specified, only those data captured on the specified container DBID are included in the list report. If no value is specified, no filtering is performed on the container DBID. session_id If a value is specified, only those data captured for the specified session ID are included in the list report. If no value is specified, no filtering is performed on session ID. session_serial If a value is specified, only those data captured for the specified session are included in the list report. If no value is specified, no filtering is performed on session serial number. This parameter should be used in conjunction with the session_id parameter. component_name Can be 'sqlmonitor' for SQL Monitor data or 'rtaddm' for Real-time ADDM data. If a value is specified then data pertaining only to the specified component will be included in the list report. If no value is specified, no filtering is performed. key1 Key value relevant to a component. For SQL Monitor, key1 is the SQL ID of the captured SQL statement. If a value is specified, only those data having specified value for key1 are included, else no filtering is performed on key1 . key2 Key value relevant to a component. For SQL Monitor, key2 is the SQL execution ID of the captured SQL statement. If a value is specified, only those data having specified value for key2 are included, else no filtering is performed on key2 . key3 Key value relevant to a component. For SQL Monitor, key3 is the SQL execution start time of the captured SQL statement. If a value is specified, then only those data having specified value for key3 are included, else no filtering is performed on key3 . report_level Currently only 'TYPICAL' is used base_path Unused/Non-operative