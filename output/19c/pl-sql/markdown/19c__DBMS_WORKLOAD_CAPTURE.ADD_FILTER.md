---
id: 19c__DBMS_WORKLOAD_CAPTURE.ADD_FILTER
name: DBMS_WORKLOAD_CAPTURE.ADD_FILTER
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_CAPTURE
tags: [dbms_workload_capture]
source_file: DBMS_WORKLOAD_CAPTURE.html
---

# DBMS_WORKLOAD_CAPTURE.ADD_FILTER

This procedure adds a filter to capture a subset of the workload.

## Syntax

```sql
DBMS_WORKLOAD_CAPTURE.ADD_FILTER (
   fname           IN   VARCHAR2 NOT NULL, 
   fattribute      IN   VARCHAR2 NOT NULL, 
   fvalue          IN   VARCHAR2 NOT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| fname | VARCHAR2 | IN | Name for the filter to be added. Can be used to delete the filter later if it is not required. (Mandatory) |
| fattribute | VARCHAR2 | IN | Specifies the attribute on which the filter needs to be applied (Mandatory). The possible values are: INSTANCE_NUMBER - type NUMBER USER - type STRING MODULE - type STRING ACTION - type STRING PROGRAM - type STRING SERVICE - type STRING PDB_NAME - type STRING |
| fvalue | VARCHAR2 | IN | Specifies the value to which the given attribute should be equal to for the filter to be considered active. Wildcards like '%' are acceptable for all attributes that are of type STRING . This means that the filter for a NUMBER attribute is parsed as "attribute = value", with the filter for a STRING attribute parsed as "attribute like value" (Mandatory). |

## Usage Notes

Syntax DBMS_WORKLOAD_CAPTURE.ADD_FILTER ( fname IN VARCHAR2 NOT NULL, fattribute IN VARCHAR2 NOT NULL, fvalue IN VARCHAR2 NOT NULL); DBMS_WORKLOAD_CAPTURE.ADD_FILTER ( fname IN VARCHAR2 NOT NULL, fattribute IN VARCHAR2 NOT NULL, fvalue IN NUMBER NOT NULL); Parameters Table 190-2 ADD_FILTER Procedure Parameters Parameter Description fname Name for the filter to be added. Can be used to delete the filter later if it is not required. (Mandatory) fattribute Specifies the attribute on which the filter needs to be applied (Mandatory). The possible values are: INSTANCE_NUMBER - type NUMBER USER - type STRING MODULE - type STRING ACTION - type STRING PROGRAM - type STRING SERVICE - type STRING PDB_NAME - type STRING fvalue Specifies the value to which the given attribute should be equal to for the filter to be considered active. Wildcards like '%' are acceptable for all attributes that are of type STRING . This means that the filter for a NUMBER attribute is parsed as "attribute = value", with the filter for a STRING attribute parsed as "attribute like value" (Mandatory). Usage Notes The workload capture filters work in either the DEFAULT INCLUSION or the DEFAULT EXCLUSION mode as determined by the default_action input to the START_CAPTURE Procedure . ADD_FILTER adds a new filter that affects the next workload capture, and whether the filters are considered as INCLUSION filters or EXCLUSION filters depends on the value of the default_action input to START_CAPTURE Procedure . Filters once specified are valid only for the next workload capture. If the same set of filters need to be used for subsequent capture, they need to be specified each time before the START_CAPTURE Procedure is executed. All the filters are listed in the DBA_WORKLOAD_FILTERS view. You can capture the workload for a particular PDB by specifying a filter of PDB type. Examples By default, a capture works in an INCLUSION mode, which records everything except for those requests that satisfy conditions of specified filters. For example, if you want to exclude all requests from SCOTT , you can add the following filter before starting a capture. EXEC DBMS_WORKLOAD_CAPTURE.ADD_FILTER ('filter user1', 'USER', 'SCOTT'); Multiple filters are evaluated according to the logical disjunction operator OR . Therefore, if you want to record workload for both SCOTT and JOHN , you add an additional filter: EXEC DBMS_WORKLOAD_CAPTURE.ADD_FILTER ('filter user2', 'USER', 'JOHN'); In a CDB, you exclude the workload of a particular PDB by the filter: EXEC DBMS_WORKLOAD_CAPTURE.ADD_FILTER ('filter pdb workload', 'PDB_NAME', 'CDB1_PDB1'); To use DBMS_APPLICATION_INFO to identify workload that is issued to the database: DBMS_APPLICATION_INFO.SET_MODULE('ORDER_ENTRY', NULL); -- run some SQL here DBMS_APPLICATION_INFO.SET_ACTION('ORDER_ENTRY_LOG'); -- run logging SQL If having captured workload, you want to exclude the logging SQL from the captured, specify a filter for capture: DBMS_WORKLOAD_CAPTURE.ADD_FILTER('filter logging operations', 'ACTION', 'ORDER_ENTRY_LOG'); To filter out the full order entry transaction, define a filter: DBMS_WORKLOAD_CAPTURE.ADD_FILTER('filter order entry', 'MODULE', 'ORDER_ENTRY');