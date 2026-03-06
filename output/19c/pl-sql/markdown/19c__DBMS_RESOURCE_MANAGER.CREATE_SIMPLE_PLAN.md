---
id: 19c__DBMS_RESOURCE_MANAGER.CREATE_SIMPLE_PLAN
name: DBMS_RESOURCE_MANAGER.CREATE_SIMPLE_PLAN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RESOURCE_MANAGER
tags: [dbms_resource_manager]
source_file: DBMS_RESOURCE_MANAGER.html
---

# DBMS_RESOURCE_MANAGER.CREATE_SIMPLE_PLAN

This procedure creates a single-level resource plan containing up to eight consumer groups in one step. You do not need to create a pending area manually before creating a resource plan, or use the CREATE_CONSUMER_GROUP and CREATE_RESOURCE_PLAN_DIRECTIVES procedures separately.

## Syntax

```sql
DBMS_RESOURCE_MANAGER.CREATE_SIMPLE_PLAN (
   simple_plan      IN  VARCHAR2  DEFAULT NULL,
   consumer_group1  IN  VARCHAR2  DEFAULT NULL,
   group1_cpu       IN  NUMBER    DEFAULT NULL,   -- deprecated
   consumer_group2  IN  VARCHAR2  DEFAULT NULL,
   group2_cpu       IN  NUMBER    DEFAULT NULL,   -- deprecated
   consumer_group3  IN  VARCHAR2  DEFAULT NULL,
   group3_cpu       IN  NUMBER    DEFAULT NULL,   -- deprecated
   consumer_group4  IN  VARCHAR2  DEFAULT NULL,
   group4_cpu       IN  NUMBER    DEFAULT NULL,   -- deprecated
   consumer_group5  IN  VARCHAR2  DEFAULT NULL,
   group5_cpu       IN  NUMBER    DEFAULT NULL,   -- deprecated
   consumer_group6  IN  VARCHAR2  DEFAULT NULL,
   group6_cpu       IN  NUMBER    DEFAULT NULL,   -- deprecated
   consumer_group7  IN  VARCHAR2  DEFAULT NULL,
   group7_cpu       IN  NUMBER    DEFAULT NULL,   -- deprecated
   consumer_group8  IN  VARCHAR2  DEFAULT NULL,
   group8_cpu       IN  NUMBER    DEFAULT NULL,   -- deprecated
   group1_percent   IN  NUMBER    DEFAULT NULL,
   group2_percent   IN  NUMBER    DEFAULT NULL,
   group3_percent   IN  NUMBER    DEFAULT NULL,
   group4_percent   IN  NUMBER    DEFAULT NULL,
   group5_percent   IN  NUMBER    DEFAULT NULL,
   group6_percent   IN  NUMBER    DEFAULT NULL,
   group7_percent   IN  NUMBER    DEFAULT NULL,
   group8_percent   IN  NUMBER    DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| simple_plan | VARCHAR2 | IN | Name of the resource plan |
| consumer_group1 | VARCHAR2 | IN | Name of the consumer group |
| group1_cpu | NUMBER | IN | Percentage for group (deprecated) |
| consumer_group2 | VARCHAR2 | IN | Name of the consumer group |
| group2_cpu | NUMBER | IN | Percentage for group (deprecated) |
| consumer_group3 | VARCHAR2 | IN | Name of the consumer group |
| group3_cpu | NUMBER | IN | Percentage for group (deprecated) |
| consumer_group4 | VARCHAR2 | IN | Name of the consumer group |
| group4_cpu | NUMBER | IN | Percentage for group (deprecated) |
| consumer_group5 | VARCHAR2 | IN | Name of the consumer group |
| group5_cpu | NUMBER | IN | Percentage for group (deprecated) |
| consumer_group6 | VARCHAR2 | IN | Name of the consumer group |
| group6_cpu | NUMBER | IN | Percentage for group (deprecated) |
| consumer_group7 | VARCHAR2 | IN | Name of the consumer group |
| group7_cpu | NUMBER | IN | Percentage for group (deprecated) |
| consumer_group8 | VARCHAR2 | IN | OTHER_GROUPS - all sessions that aren't mapped to a consumer group. |
| group8_cpu | NUMBER | IN | Percentage for group (deprecated) |
| group1_percent | NUMBER | IN | Percentage of resources allocated for this consumer group |
| group2_percent | NUMBER | IN | Percentage of resources allocated for this consumer group |
| group3_percent | NUMBER | IN | Percentage of resources allocated for this consumer group |
| group4_percent | NUMBER | IN | Percentage of resources allocated for this consumer group |
| group5_percent | NUMBER | IN | Percentage of resources allocated for this consumer group |
| group6_percent | NUMBER | IN | Percentage of resources allocated for this consumer group |
| group7_percent | NUMBER | IN | Percentage of resources allocated for this consumer group |
| group8_percent | NUMBER | IN | Percentage of resources allocated to other groups |

## Usage Notes

Syntax DBMS_RESOURCE_MANAGER.CREATE_SIMPLE_PLAN ( simple_plan IN VARCHAR2 DEFAULT NULL, consumer_group1 IN VARCHAR2 DEFAULT NULL, group1_cpu IN NUMBER DEFAULT NULL, -- deprecated consumer_group2 IN VARCHAR2 DEFAULT NULL, group2_cpu IN NUMBER DEFAULT NULL, -- deprecated consumer_group3 IN VARCHAR2 DEFAULT NULL, group3_cpu IN NUMBER DEFAULT NULL, -- deprecated consumer_group4 IN VARCHAR2 DEFAULT NULL, group4_cpu IN NUMBER DEFAULT NULL, -- deprecated consumer_group5 IN VARCHAR2 DEFAULT NULL, group5_cpu IN NUMBER DEFAULT NULL, -- deprecated consumer_group6 IN VARCHAR2 DEFAULT NULL, group6_cpu IN NUMBER DEFAULT NULL, -- deprecated consumer_group7 IN VARCHAR2 DEFAULT NULL, group7_cpu IN NUMBER DEFAULT NULL, -- deprecated consumer_group8 IN VARCHAR2 DEFAULT NULL, group8_cpu IN NUMBER DEFAULT NULL, -- deprecated group1_percent IN NUMBER DEFAULT NULL, group2_percent IN NUMBER DEFAULT NULL, group3_percent IN NUMBER DEFAULT NULL, group4_percent IN NUMBER DEFAULT NULL, group5_percent IN NUMBER DEFAULT NULL, group6_percent IN NUMBER DEFAULT NULL, group7_percent IN NUMBER DEFAULT NULL, group8_percent IN NUMBER DEFAULT NULL); Parameters Table 142-11 CREATE_SIMPLE_PLAN Procedure Parameters Parameter Description simple_plan Name of the resource plan consumer_group1 Name of the consumer group group1_cpu Percentage for group (deprecated) consumer_group2 Name of the consumer group group2_cpu Percentage for group (deprecated) consumer_group3 Name of the consumer group group3_cpu Percentage for group (deprecated) consumer_group4 Name of the consumer group group4_cpu Percentage for group (deprecated) consumer_group5 Name of the consumer group group5_cpu Percentage for group (deprecated) consumer_group6 Name of the consumer group group6_cpu Percentage for group (deprecated) consumer_group7 Name of the consumer group group7_cpu Percentage for group (deprecated) consumer_group8 OTHER_GROUPS - all sessions that aren't mapped to a consumer group. group8_cpu Percentage for group (deprecated) group1_percent Percentage of resources allocated for this consumer group group2_percent Percentage of resources allocated for this consumer group group3_percent Percentage of resources allocated for this consumer group group4_percent Percentage of resources allocated for this consumer group group5_percent Percentage of resources allocated for this consumer group group6_percent Percentage of resources allocated for this consumer group group7_percent Percentage of resources allocated for this consumer group group8_percent Percentage of resources allocated to other groups