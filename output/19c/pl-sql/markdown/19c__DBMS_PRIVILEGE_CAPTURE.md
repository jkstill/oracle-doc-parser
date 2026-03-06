---
id: 19c__DBMS_PRIVILEGE_CAPTURE
name: DBMS_PRIVILEGE_CAPTURE
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PRIVILEGE_CAPTURE
tags: [dbms_privilege_capture]
source_file: DBMS_PRIVILEGE_CAPTURE.html
---

# DBMS_PRIVILEGE_CAPTURE

These examples illustrate using the DBMS_PRIVILEGE_CAPTURE.CREATE_CAPTURE procedure to create various types of privilege analysis, like database analysis, role analysis, and context-specific analysis. The examples also illustrate combining different conditions in context-specific analysis.

## Syntax

```sql
--Create a database privilege analysis policy
BEGIN
DBMS_PRIVILEGE_CAPTURE.CREATE_CAPTURE(
        name         => 'all_priv_analysis_pol',
        description  => 'database-wide policy to analyze all privileges',
        type         => DBMS_PRIVILEGE_CAPTURE.G_DATABASE);
END;

--Create a privilege analysis policy to analyze privileges from the role PUBLIC
BEGIN
DBMS_PRIVILEGE_CAPTURE.CREATE_CAPTURE(
       name         => 'pub_analysis_pol',
       description  => 'Policy to record privilege use by PUBLIC',
       type         => DBMS_PRIVILEGE_CAPTURE.G_ROLE,
       roles        => role_name_list('PUBLIC'));
END;

-- Create a policy to analyze privileges from the application module, "Account
-- Payable"
BEGIN
DBMS_PRIVILEGE_CAPTURE.CREATE_CAPTURE(
  name         => 'acc_pay_analysis_pol',
  type         => DBMS_PRIVILEGE_CAPTURE.G_CONTEXT,
  condition    => 'SYS_CONTEXT(''USERENV'', ''MODULE'') = ''Account Payable''');
END;

-- Create a policy that records privileges for session user APPS when running the
-- application module "Account Payable"
BEGIN
DBMS_PRIVILEGE_CAPTURE.CREATE_CAPTURE(
  name         => 'acc_pay_analysis_pol',
  type         => DBMS_PRIVILEGE_CAPTURE.G_CONTEXT,
  condition    => 'SYS_CONTEXT(''USERENV'', ''MODULE'') = ''Account Payable'' AND
                   SYS_CONTEXT(''USERENV'', ''SESSION_USER'') = ''APPS''');
END;
```

## Usage Notes

--Create a database privilege analysis policy BEGIN DBMS_PRIVILEGE_CAPTURE.CREATE_CAPTURE( name => 'all_priv_analysis_pol', description => 'database-wide policy to analyze all privileges', type => DBMS_PRIVILEGE_CAPTURE.G_DATABASE); END; --Create a privilege analysis policy to analyze privileges from the role PUBLIC BEGIN DBMS_PRIVILEGE_CAPTURE.CREATE_CAPTURE( name => 'pub_analysis_pol', description => 'Policy to record privilege use by PUBLIC', type => DBMS_PRIVILEGE_CAPTURE.G_ROLE, roles => role_name_list('PUBLIC')); END; -- Create a policy to analyze privileges from the application module, "Account -- Payable" BEGIN DBMS_PRIVILEGE_CAPTURE.CREATE_CAPTURE( name => 'acc_pay_analysis_pol', type => DBMS_PRIVILEGE_CAPTURE.G_CONTEXT, condition => 'SYS_CONTEXT(''USERENV'', ''MODULE'') = ''Account Payable'''); END; -- Create a policy that records privileges for session user APPS when running the -- application module "Account Payable" BEGIN DBMS_PRIVILEGE_CAPTURE.CREATE_CAPTURE( name => 'acc_pay_analysis_pol', type => DBMS_PRIVILEGE_CAPTURE.G_CONTEXT, condition => 'SYS_CONTEXT(''USERENV'', ''MODULE'') = ''Account Payable'' AND SYS_CONTEXT(''USERENV'', ''SESSION_USER'') = ''APPS'''); END;