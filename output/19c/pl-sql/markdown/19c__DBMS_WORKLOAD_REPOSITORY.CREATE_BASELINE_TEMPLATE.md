---
id: 19c__DBMS_WORKLOAD_REPOSITORY.CREATE_BASELINE_TEMPLATE
name: DBMS_WORKLOAD_REPOSITORY.CREATE_BASELINE_TEMPLATE
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPOSITORY
tags: [dbms_workload_repository]
source_file: DBMS_WORKLOAD_REPOSITORY.html
---

# DBMS_WORKLOAD_REPOSITORY.CREATE_BASELINE_TEMPLATE

This procedure specifies a template for how they would like baselines to be created for future time periods.

## Syntax

```sql
DBMS_WORKLOAD_REPOSITORY.CREATE_BASELINE_TEMPLATE(
   start_time              IN DATE,
   end_time                IN DATE,
   baseline_name           IN VARCHAR2,
   template_name           IN VARCHAR2,
   expiration              IN NUMBER,
   dbid                    IN NUMBER   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| start_time | DATE | IN | Start Time for the baseline to be created' |
| end_time | DATE | IN | End Time for the baseline to be created |
| baseline_name | VARCHAR2 | IN | Name of baseline to be created |
| template_name | VARCHAR2 | IN | Name for the template |
| expiration | NUMBER | IN | Expiration in number of days for the baseline. If NULL , then expiration is infinite, meaning do not drop baseline ever. Defaults to NULL |
| dbid | NUMBER | IN | Database ID for which the baseline template needs to be used. If NULL , this takes the database identifier of the local database. Defaults to NULL . |
| day_of_week |  |  | Day of week that the baseline should repeat on. Specify one of the following values: SUNDAY , MONDAY , TUESDAY , WEDNESDAY , THURSDAY , FRIDAY , SATURDAY . |
| hour_in_day |  |  | Value of 0-23 to specify the Hour in the Day the baseline should start |
| duration |  |  | Duration (in number of hours) after hour in the day that the baseline should last |
| baseline_name_prefix |  |  | Name for baseline prefix. When creating the baseline, the name of the baseline will be the prefix appended with the date information. |

## Usage Notes

Syntax Specifies a template for generating a baseline for a single time period in the future. DBMS_WORKLOAD_REPOSITORY.CREATE_BASELINE_TEMPLATE( start_time IN DATE, end_time IN DATE, baseline_name IN VARCHAR2, template_name IN VARCHAR2, expiration IN NUMBER, dbid IN NUMBER DEFAULT NULL); Specifies a template for creating and dropping baseline based on repeating time periods: DBMS_WORKLOAD_REPOSITORY.CREATE_BASELINE_TEMPLATE( day_of_week IN VARCHAR2, hour_in_day IN NUMBER, duration IN NUMBER, start_time IN DATE, end_time IN DATE, baseline_name_prefix IN VARCHAR2, template_name IN VARCHAR2, expiration IN NUMBER, dbid IN NUMBER DEFAULT NULL); Parameters Table 192-28 CREATE_BASELINE_TEMPLATE Procedure Parameters Parameter Description start_time Start Time for the baseline to be created' end_time End Time for the baseline to be created baseline_name Name of baseline to be created template_name Name for the template expiration Expiration in number of days for the baseline. If NULL , then expiration is infinite, meaning do not drop baseline ever. Defaults to NULL dbid Database ID for which the baseline template needs to be used. If NULL , this takes the database identifier of the local database. Defaults to NULL . day_of_week Day of week that the baseline should repeat on. Specify one of the following values: SUNDAY , MONDAY , TUESDAY , WEDNESDAY , THURSDAY , FRIDAY , SATURDAY . hour_in_day Value of 0-23 to specify the Hour in the Day the baseline should start duration Duration (in number of hours) after hour in the day that the baseline should last baseline_name_prefix Name for baseline prefix. When creating the baseline, the name of the baseline will be the prefix appended with the date information.