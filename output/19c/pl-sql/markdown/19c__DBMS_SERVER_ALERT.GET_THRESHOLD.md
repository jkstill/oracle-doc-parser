---
id: 19c__DBMS_SERVER_ALERT.GET_THRESHOLD
name: DBMS_SERVER_ALERT.GET_THRESHOLD
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SERVER_ALERT
tags: [dbms_server_alert]
source_file: DBMS_SERVER_ALERT.html
---

# DBMS_SERVER_ALERT.GET_THRESHOLD

This procedure gets the current threshold settings for the specified metric.

## Syntax

```sql
DBMS_SERVER_ALERT.GET_THRESHOLD(
   metrics_id               IN   BINARY_INTEGER,
   warning_operator         OUT  BINARY_INTEGER,
   warning_value            OUT  VARCHAR2,
   critical_operator        OUT  BINARY_INTEGER,
   critical_value           OUT  VARCHAR2,
   observation_period       OUT  BINARY_INTEGER,
   consecutive_occurrences  OUT  BINARY_INTEGER,
   instance_name            IN   VARCHAR2,
   object_type              IN   BINARY_INTEGER,
   object_name              IN   VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| metrics_id | BINARY_INTEGER | IN | The internal name of the metric. See " Supported Metrics " . |
| warning_operator | BINARY_INTEGER | OUT | The operator for the compa3ring the actual value with the warning threshold. |
| warning_value | VARCHAR2 | OUT | The warning threshold value. |
| critical_operator | BINARY_INTEGER | OUT | The operator for the comparing the actual value with the critical threshold. |
| critical_value | VARCHAR2 | OUT | The critical threshold value. |
| observation_period | BINARY_INTEGER | OUT | The period at which the metric values are computed and verified against the threshold setting. |
| consecutive_occurrences | BINARY_INTEGER | OUT | The number of observation periods the metric value should violate the threshold value before the alert is issued. |
| instance_name | VARCHAR2 | IN | The name of the instance for which the threshold is set. This is NULL for database-wide alerts. In cases in which this parameter is not NULL , this should be set to one of the INSTANCE_NAME values found in the GV$INSTANCE View. |
| object_type | BINARY_INTEGER | IN | Either OBJECT_TYPE_SYSTEM or OBJECT_TYPE_SERVICE . |
| object_name | VARCHAR2) | IN | The name of the object. |

## Usage Notes

Syntax DBMS_SERVER_ALERT.GET_THRESHOLD( metrics_id IN BINARY_INTEGER, warning_operator OUT BINARY_INTEGER, warning_value OUT VARCHAR2, critical_operator OUT BINARY_INTEGER, critical_value OUT VARCHAR2, observation_period OUT BINARY_INTEGER, consecutive_occurrences OUT BINARY_INTEGER, instance_name IN VARCHAR2, object_type IN BINARY_INTEGER, object_name IN VARCHAR2); Parameters Table 152-6 GET_THRESHOLD Procedure Parameters Parameter Description metrics_id The internal name of the metric. See " Supported Metrics " . warning_operator The operator for the compa3ring the actual value with the warning threshold. warning_value The warning threshold value. critical_operator The operator for the comparing the actual value with the critical threshold. critical_value The critical threshold value. observation_period The period at which the metric values are computed and verified against the threshold setting. consecutive_occurrences The number of observation periods the metric value should violate the threshold value before the alert is issued. instance_name The name of the instance for which the threshold is set. This is NULL for database-wide alerts. In cases in which this parameter is not NULL , this should be set to one of the INSTANCE_NAME values found in the GV$INSTANCE View. object_type Either OBJECT_TYPE_SYSTEM or OBJECT_TYPE_SERVICE . object_name The name of the object. Usage Notes Note that this subprogram does not check if the value of the instance_name parameter is meaningful or valid.