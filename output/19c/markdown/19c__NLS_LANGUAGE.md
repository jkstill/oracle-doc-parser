---
id: 19c__NLS_LANGUAGE
name: NLS_LANGUAGE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
source_file: NLS_LANGUAGE.html
---

# NLS_LANGUAGE

NLS_LANGUAGE specifies the default language of the database.

## Usage Notes

This language specified by NLS_LANGUAGE is used for messages, day and month names, symbols for AD, BC, a.m., and p.m., and the default sorting mechanism. This parameter also determines the default values of the parameters NLS_DATE_LANGUAGE and NLS_SORT . Note: The value of this initialization parameter NLS_LANGUAGE is used to initialize the session value of this parameter, which is the actual value referenced by the SQL query processing. This initial value is overridden by a client-side value if the client uses the Oracle JDBC driver or if the client is OCI-based and the NLS_LANG client setting (environment variable) is defined. The initialization parameter value is, therefore, usually ignored. Note: The value of this initialization parameter NLS_LANGUAGE is used to initialize the session value of this parameter, which is the actual value referenced by the SQL query processing. This initial value is overridden by a client-side value if the client uses the Oracle JDBC driver or if the client is OCI-based and the NLS_LANG client setting (environment variable) is defined. The initialization parameter value is, therefore, usually ignored. See these examples of using the NLS_LANGUAGE parameter: For an example of setting NLS_LANGUAGE to Italian, see Oracle Database Globalization Support Guide . For an example of overriding default values for NLS_LANGUAGE and NLS_TERRITORY during a session, see Oracle Database Globalization Support Guide . See Also: Oracle Database Globalization Support Guide for more information about this parameter. Oracle Database Globalization Support Guide for a complete list of languages that can be specified using this parameter Oracle Database Globalization Support Guide for information on overriding the default values for this parameter Your operating system-specific Oracle documentation and the release notes for your country See Also: Oracle Database Globalization Support Guide for more information about this parameter. Oracle Database Globalization Support Guide for a complete list of languages that can be specified using this parameter Oracle Database Globalization Support Guide for information on overriding the default values for this parameter Your operating system-specific Oracle documentation and the release notes for your country