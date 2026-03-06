---
id: 19c__NLS_COMP
name: NLS_COMP
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
source_file: NLS_COMP.html
---

# NLS_COMP

NLS_COMP specifies the collation behavior of the database session.

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content BINARY Normally, comparisons in the WHERE clause and in PL/SQL blocks is binary unless you specify the NLSSORT function. LINGUISTIC Comparisons for all SQL operations in the WHERE clause and in PL/SQL blocks should use the linguistic sort specified in the NLS_SORT parameter. To improve the performance, you can also define a linguistic index on the column for which you want linguistic comparisons. ANSI A setting of ANSI is for backward compatibility; in general, you should set NLS_COMP to LINGUISTIC Note: Unless you explicitly set the value for NLS_COMP in your initialization parameter file, a default value of NULL is shown in the following views: V$PARAMETER , V$SYSTEM_PARAMETER , V$PARAMETER2 , V$SYSTEM_PARAMETER2 , and NLS_INSTANCE_PARAMETERS . However, the actual default value, and behavior, is BINARY . Note that you cannot change the default to NULL, because NULL is not among the valid values. Note: Unless you explicitly set the value for NLS_COMP in your initialization parameter file, a default value of NULL is shown in the following views: V$PARAMETER , V$SYSTEM_PARAMETER , V$PARAMETER2 , V$SYSTEM_PARAMETER2 , and NLS_INSTANCE_PARAMETERS . However, the actual default value, and behavior, is BINARY . Note that you cannot change the default to NULL, because NULL is not among the valid values. See Oracle Database Globalization Support Guide for examples of using this parameter. Note: The value of this initialization parameter NLS_COMP is used to initialize the session value of this parameter, which is the actual value referenced by the SQL query processing. This initial value is overridden by a client-side value if the client uses the Oracle JDBC driver or if the client is OCI-based and the NLS_LANG client setting (environment variable) is defined. The initialization parameter value is, therefore, usually ignored. Note: The value of this initialization parameter NLS_COMP is used to initialize the session value of this parameter, which is the actual value referenced by the SQL query processing. This initial value is overridden by a client-side value if the client uses the Oracle JDBC driver or if the client is OCI-based and the NLS_LANG client setting (environment variable) is defined. The initialization parameter value is, therefore, usually ignored.