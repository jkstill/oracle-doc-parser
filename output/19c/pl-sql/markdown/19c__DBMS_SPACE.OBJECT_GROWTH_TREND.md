---
id: 19c__DBMS_SPACE.OBJECT_GROWTH_TREND
name: DBMS_SPACE.OBJECT_GROWTH_TREND
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SPACE
tags: [dbms_space]
source_file: DBMS_SPACE.html
---

# DBMS_SPACE.OBJECT_GROWTH_TREND

This is a table function. The output is one or more rows where each row describes the space usage of the object at a specific point in time.

## Syntax

```sql
DBMS_SPACE.OBJECT_GROWTH_TREND (
   object_owner           IN    VARCHAR2,
   object_name            IN    VARCHAR2,
   object_type            IN    VARCHAR2,
   partition_name         IN    VARCHAR2 DEFAULT NULL,
   start_time             IN    TIMESTAMP DEFAULT NULL,
   end_time               IN    TIMESTAMP DEFAULT NULL,
   interval               IN    DSINTERVAL_UNCONSTRAINED DEFAULT NULL,
   skip_interpolated      IN    VARCHAR2 DEFAULT 'FALSE',
   timeout_seconds        IN    NUMBER DEFAULT NULL,
   single_datapoint_flag  IN    VARCHAR2 DEFAULT 'TRUE') 
 RETURN object_growth_trend_table PIPELINED;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| object_owner | VARCHAR2 | IN | The schema containing the object |
| object_name | VARCHAR2 | IN | The name of the object |
| object_type | VARCHAR2 | IN | The type of the object |
| partition_name | VARCHAR2 | IN | The name of the partition |
| start_time | TIMESTAMP | IN | Statistics generated after this time will be used in generating the growth trend |
| end_time | TIMESTAMP | IN | Statistics generated until this time will be used in generating the growth trend |
| interval | DSINTERVAL_UNCONSTRAINED | IN | The interval at which to sample |
| skip_interpolated | VARCHAR2 | IN | Whether interpolation of missing values should be skipped |
| timeout_seconds | NUMBER | IN | The time-out value for the function in seconds |
| single_data_point_flag |  |  | Whether in the absence of statistics the segment should be sampled |

**Returns:** `object_growth_trend_table`

## Usage Notes

Either the space usage totals will be retrieved from Automatic Workload Repository Facilities (AWRF), or the current space usage will be computed and combined with space usage deltas retrieved from AWRF. Syntax DBMS_SPACE.OBJECT_GROWTH_TREND ( object_owner IN VARCHAR2, object_name IN VARCHAR2, object_type IN VARCHAR2, partition_name IN VARCHAR2 DEFAULT NULL, start_time IN TIMESTAMP DEFAULT NULL, end_time IN TIMESTAMP DEFAULT NULL, interval IN DSINTERVAL_UNCONSTRAINED DEFAULT NULL, skip_interpolated IN VARCHAR2 DEFAULT 'FALSE', timeout_seconds IN NUMBER DEFAULT NULL, single_datapoint_flag IN VARCHAR2 DEFAULT 'TRUE') RETURN object_growth_trend_table PIPELINED; Parameters Table 158-12 OBJECT_GROWTH_TREND Function Parameters Parameter Description object_owner The schema containing the object object_name The name of the object object_type The type of the object partition_name The name of the partition start_time Statistics generated after this time will be used in generating the growth trend end_time Statistics generated until this time will be used in generating the growth trend interval The interval at which to sample skip_interpolated Whether interpolation of missing values should be skipped timeout_seconds The time-out value for the function in seconds single_data_point_flag Whether in the absence of statistics the segment should be sampled Return Values The object_growth_trend_row and object_growth_trend_table are used by the OBJECT_GROWTH_TREND table function to describe its output. TYPE object_growth_trend_row IS RECORD( timepoint TIMESTAMP, space_usage NUMBER, space_alloc NUMBER, quality VARCHAR(20)); Table 158-13 OBJECT_GROWTH_TREND_ROW Type Parameters Parameter Description timepoint The time at which the statistic was recorded space_usage The space used by data space_alloc The size of the segment including overhead and unused space quality The quality of result: " GOOD ", " INTERPOLATED ", " PROJECTION " TYPE object_growth_trend_table IS TABLE OF object_growth_trend_row;