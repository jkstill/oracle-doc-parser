---
id: 19c__DBMS_ILM_ADMIN
name: DBMS_ILM_ADMIN
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ILM_ADMIN
tags: [dbms_ilm_admin]
source_file: DBMS_ILM_ADMIN.html
---

# DBMS_ILM_ADMIN

The table in this topic describes constants used by the DBMS_ILM_ADMIN package.

## Usage Notes

The value column refers to the numeric or character value that the constants resolve to. The DBMS_ILM_ADMIN package uses the constants as parameter values shown in Table 87-2 . Table 87-2 DBMS_ILM_ADMIN Constants Used as Parameter Values Constant Value Type Description ILM_EXECUTION_OFFLINE 1 NUMBER Specifies that the object may be offline while ADO action is performed. ILM_EXECUTION_ONLINE 2 NUMBER Specifies that the object should be online while ADO action is performed ILM_ENABLED 1 NUMBER Indicates automatic ADO policy evaluation and execution is enabled ILM_DISABLED 2 NUMBER Indicates automatic ADO policy evaluation and execution is disabled ILM_POLICY_IN_DAYS 0 NUMBER Indicates policy is specified in days. This is the default. ILM_POLICY_IN_SECONDS 1 NUMBER Indicates policy unit is changed from days to seconds. This could be used to test ADO policy evaluation quickly instead of waiting for the policy duration. Note: Setting ILM_POLICY_IN_SECONDS does not compress the blocks within the specified seconds. Setting ILM_POLICY_IN_SECONDS is for test ADO and should not be set in the production environment. Note: Setting ILM_POLICY_IN_SECONDS does not compress the blocks within the specified seconds. Setting ILM_POLICY_IN_SECONDS is for test ADO and should not be set in the production environment.