---
id: 19c__DBMS_WORKLOAD_REPLAY.ADD_FILTER
name: DBMS_WORKLOAD_REPLAY.ADD_FILTER
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPLAY
tags: [dbms_workload_replay]
source_file: DBMS_WORKLOAD_REPLAY.html
---

# DBMS_WORKLOAD_REPLAY.ADD_FILTER

This procedure adds a filter to replay only a subset of the captured workload.

## Syntax

```sql
DBMS_WORKLOAD_REPLAY.ADD_FILTER (
   fname          IN VARCHAR2,
   fattribute     IN VARCHAR2,
   fvalue         IN VARCHAR2);

DBMS_WORKLOAD_REPLAY.ADD_FILTER (
   fname          IN VARCHAR2,
   fattribute     IN VARCHAR2,
   fvalue         IN NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| fname | VARCHAR2 | IN | (Mandatory) Name of the filter. Can be used to delete the filter later if it is not required. |
| fattribute | VARCHAR2 | IN | (Mandatory) Specifies the attribute on which the filter is defined as one of the following values of type STRING : USER MODULE ACTION PROGRAM SERVICE CONNECTION_STRING |
| fvalue | VARCHAR2) | IN | (Mandatory) Specifies the value to which the given 'attribute' must be equal to for the filter to be considered active. Wildcards such as '%' are acceptable for all attributes that are of type STRING . Currently all the listed values of fattribute are of type STRING . INSTANCE_NUMBER is a NUMBER attribute. It is currently only supported for capture. |

## Usage Notes

The procedure adds a new filter that is used in the next replay filter set created using the CREATE_FILTER_SET Procedure . This filter will be considered an " INCLUSION " or " EXCLUSION " filter depending on the argument passed to CREATE_FILTER_SET when creating the filter set. Syntax DBMS_WORKLOAD_REPLAY.ADD_FILTER ( fname IN VARCHAR2, fattribute IN VARCHAR2, fvalue IN VARCHAR2); DBMS_WORKLOAD_REPLAY.ADD_FILTER ( fname IN VARCHAR2, fattribute IN VARCHAR2, fvalue IN NUMBER); Parameters Table 191-3 ADD_FILTER Procedure Parameters Parameter Description fname (Mandatory) Name of the filter. Can be used to delete the filter later if it is not required. fattribute (Mandatory) Specifies the attribute on which the filter is defined as one of the following values of type STRING : USER MODULE ACTION PROGRAM SERVICE CONNECTION_STRING fvalue (Mandatory) Specifies the value to which the given 'attribute' must be equal to for the filter to be considered active. Wildcards such as '%' are acceptable for all attributes that are of type STRING . Currently all the listed values of fattribute are of type STRING . INSTANCE_NUMBER is a NUMBER attribute. It is currently only supported for capture.