---
id: 19c__DBA_HIST_BASELINE_TEMPLATE
name: DBA_HIST_BASELINE_TEMPLATE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_HIST_BASELINE_TEMPLATE.html
---

# DBA_HIST_BASELINE_TEMPLATE

DBA_HIST_BASELINE_TEMPLATE displays the templates used by the system for baseline generation.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| DBID | NUMBER | Database ID |
| TEMPLATE_ID | NUMBER | Internal ID for the template |
| TEMPLATE_NAME | VARCHAR2(128) | Name of the template |
| TEMPLATE_TYPE | VARCHAR2(9) | Type of the template, as follows: SINGLE - one time period REPEATING - maintain a time period |
| BASELINE_NAME_PREFIX | VARCHAR2(128) | Name to use for the baselines that are created: For a template type of SINGLE , the BASELINE_NAME _PREFIX is the name that will be used. For a template type of REPEATING , the BASELINE_NAME will be the prefix to the name. |
| START_TIME | DATE | For a template type of SINGLE , this is the start time for future baselines For a template type of REPEATING , this is the effective start time that baselines should start being generated. |
| END_TIME | DATE | For a template type of SINGLE , this is the end time for future baselines. For a template type of REPEATING , this is the effective end time that baselines should stop being generated. |
| DAY_OF_WEEK | VARCHAR2(9) | For a template type of REPEATING , this indicates the day of the week to create the baseline: SUNDAY , MONDAY , TUESDAY , WEDNESDAY , THURSDAY , FRIDAY , SATURDAY , ALL . |
| HOUR_IN_DAY | NUMBER | For a template type of REPEATING , a value from 0 - 23 to indicate the hour of the day to create the baseline for. |
| DURATION | NUMBER | For a template type of REPEATING , the length of time for the baseline to be created. |
| EXPIRATION | NUMBER | How long to keep the baseline, in number of days |
| REPEAT_INTERVAL | VARCHAR2(128) | String that represents the time repeating information in the format used by the DBMS_SCHEDULER package |
| LAST_GENERATED | DATE | Last time a baseline was generated for this template |
| CON_ID | NUMBER | The ID of the container to which the data pertains. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

The system uses this information to determine which baselines should be automatically created or removed. See Also: Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_SCHEDULER package See Also: Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_SCHEDULER package