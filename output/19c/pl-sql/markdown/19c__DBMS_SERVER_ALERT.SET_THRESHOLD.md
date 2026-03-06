---
id: 19c__DBMS_SERVER_ALERT.SET_THRESHOLD
name: DBMS_SERVER_ALERT.SET_THRESHOLD
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SERVER_ALERT
tags: [dbms_server_alert]
source_file: DBMS_SERVER_ALERT.html
---

# DBMS_SERVER_ALERT.SET_THRESHOLD

This procedure sets the warning and critical thresholds for a specified metric.

## Syntax

```sql
DBMS_SERVER_ALERT.SET_THRESHOLD(
   metrics_id               IN   BINARY_INTEGER,
   warning_operator         IN   BINARY_INTEGER,
   warning_value            IN   VARCHAR2,
   critical_operator        IN   BINARY_INTEGER,
   critical_value           IN   VARCHAR2,
   observation_period       IN   BINARY_INTEGER,
   consecutive_occurrences  IN   BINARY_INTEGER,
   instance_name            IN   VARCHAR2,
   object_type              IN   BINARY_INTEGER,
   object_name              IN   VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| metrics_id | BINARY_INTEGER | IN | The internal name of the metric. See " Supported Metrics " . |
| warning_operator | BINARY_INTEGER | IN | The operator for the comparing the actual value with the warning threshold (such as OPERATOR_GE ). See " Relational Operators " . |
| warning_value | VARCHAR2 | IN | The warning threshold value. This is NULL if no warning threshold is set. A list of values may be specified for OPERATOR_CONTAINS . |
| critical_operator | BINARY_INTEGER | IN | The operator for the comparing the actual value with the critical threshold. See " Relational Operators " . |
| critical_value | VARCHAR2 | IN | The critical threshold value. This is NULL if not set. A list of values may be specified for OPERATOR_CONTAINS . |
| observation_period | BINARY_INTEGER | IN | The period at which the metric values are computed and verified against the threshold setting. The valid range is 1 to 60 minutes. |
| consecutive_occurrences | BINARY_INTEGER | IN | The number of observation periods the metric value should violate the threshold value before the alert is issued. |
| instance_name | VARCHAR2 | IN | The name of the instance for which the threshold is set. This is NULL for database-wide alerts. |
| object_type | BINARY_INTEGER | IN | See " Object Types " . |
| object_name | VARCHAR2) | IN | The name of the object. This is NULL for SYSTEM . |

## Usage Notes

Syntax DBMS_SERVER_ALERT.SET_THRESHOLD( metrics_id IN BINARY_INTEGER, warning_operator IN BINARY_INTEGER, warning_value IN VARCHAR2, critical_operator IN BINARY_INTEGER, critical_value IN VARCHAR2, observation_period IN BINARY_INTEGER, consecutive_occurrences IN BINARY_INTEGER, instance_name IN VARCHAR2, object_type IN BINARY_INTEGER, object_name IN VARCHAR2); Parameters Table 152-7 SET_THRESHOLD Procedure Parameters Parameter Description metrics_id The internal name of the metric. See " Supported Metrics " . warning_operator The operator for the comparing the actual value with the warning threshold (such as OPERATOR_GE ). See " Relational Operators " . warning_value The warning threshold value. This is NULL if no warning threshold is set. A list of values may be specified for OPERATOR_CONTAINS . critical_operator The operator for the comparing the actual value with the critical threshold. See " Relational Operators " . critical_value The critical threshold value. This is NULL if not set. A list of values may be specified for OPERATOR_CONTAINS . observation_period The period at which the metric values are computed and verified against the threshold setting. The valid range is 1 to 60 minutes. consecutive_occurrences The number of observation periods the metric value should violate the threshold value before the alert is issued. instance_name The name of the instance for which the threshold is set. This is NULL for database-wide alerts. object_type See " Object Types " . object_name The name of the object. This is NULL for SYSTEM . Usage Notes Note that this subprogram does not check if the value of the instance_name parameter is meaningful or valid. Passing a name that does not identify a valid instance will result in a threshold that is not used by any by any instance although the threshold setting will be visible in the DBA_THRESHOLDS view. The exception is the lower-case string 'database_wide' which is semantically equivalent to passing NULL for the instance name, the latter being the preferred usage.