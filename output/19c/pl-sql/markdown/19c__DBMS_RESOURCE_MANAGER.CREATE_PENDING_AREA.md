---
id: 19c__DBMS_RESOURCE_MANAGER.CREATE_PENDING_AREA
name: DBMS_RESOURCE_MANAGER.CREATE_PENDING_AREA
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RESOURCE_MANAGER
tags: [dbms_resource_manager]
source_file: DBMS_RESOURCE_MANAGER.html
---

# DBMS_RESOURCE_MANAGER.CREATE_PENDING_AREA

This procedure makes changes to resource manager objects.

## Syntax

```sql
DBMS_RESOURCE_MANAGER.CREATE_PENDING_AREA;
```

## Usage Notes

All changes to the plan schema must be done within a pending area. The pending area can be thought of as a "scratch" area for plan schema changes. The administrator creates this pending area, makes changes as necessary, possibly validates these changes, and only when the submit is completed do these changes become active. Syntax DBMS_RESOURCE_MANAGER.CREATE_PENDING_AREA; Usage Notes You may, at any time while the pending area is active, view the current plan schema with your changes by selecting from the appropriate user views. At any time, you may clear the pending area if you want to stop the current changes. You may also call the VALIDATE procedure to confirm whether the changes you have made are valid. You do not have to perform your changes in a given order to maintain a consistent group of entries. These checks are also implicitly done when the pending area is submitted. Note: Oracle allows "orphan" consumer groups (in other words, consumer groups that have no plan directives that refer to them). This is in anticipation that an administrator may want to create a consumer group that is not currently being used, but will be used in the future. For resource plans, the following rules must be adhered to, and they are checked whenever the validate or submit procedures are executed: No plan schema may contain any loops. All plans and consumer groups referred to by plan directives must exist. All plans must have plan directives that refer to either plans or consumer groups. All percentages in any given level must not add up to greater than 100 for the emphasis resource allocation method. No plan may be deleted that is currently being used as a top plan by an active instance. The plan directive parameter, parallel_degree_limit_p1 , may only appear in plan directives that refer to consumer groups (that is, not at subplans). There cannot be more than 28 plan directives coming from any given plan (that is, no plan can have more than 28 children). There cannot be more than 28 consumer groups in any active plan schema. Plans and consumer groups use the same namespace; therefore, no plan can have the same name as any consumer group. There must be a plan directive for OTHER_GROUPS somewhere in any active plan schema.This ensures that a session not covered by the currently active plan is allocated resources as specified by the OTHER_GROUPS directive. Note: These rules are not applicable for CDB resource plans. If any of the preceding rules are broken when checked by the VALIDATE or SUBMIT procedures, then an informative error message is returned. You may then make changes to fix one or more problems and reissue the validate or submit procedures. Note: Oracle allows "orphan" consumer groups (in other words, consumer groups that have no plan directives that refer to them). This is in anticipation that an administrator may want to create a consumer group that is not currently being used, but will be used in the future. Note: These rules are not applicable for CDB resource plans.