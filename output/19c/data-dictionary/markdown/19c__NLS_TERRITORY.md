---
id: 19c__NLS_TERRITORY
name: NLS_TERRITORY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
source_file: NLS_TERRITORY.html
---

# NLS_TERRITORY

NLS_TERRITORY specifies the name of the territory whose conventions are to be followed for day and week numbering.

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content This parameter also establishes the default date format, the default decimal character and group separator, and the default ISO and local currency symbols. For information on these settings, see " NLS_DATE_FORMAT " , " NLS_NUMERIC_CHARACTERS " , " NLS_CURRENCY " , and " NLS_ISO_CURRENCY " . Note: The value of this initialization parameter NLS_TERRITORY is used to initialize the session value of this parameter, which is the actual value referenced by the SQL query processing. This initial value is overridden by a client-side value if the client uses the Oracle JDBC driver or if the client is OCI-based and the NLS_LANG client setting (environment variable) is defined. The initialization parameter value is, therefore, usually ignored. Note: The value of this initialization parameter NLS_TERRITORY is used to initialize the session value of this parameter, which is the actual value referenced by the SQL query processing. This initial value is overridden by a client-side value if the client uses the Oracle JDBC driver or if the client is OCI-based and the NLS_LANG client setting (environment variable) is defined. The initialization parameter value is, therefore, usually ignored. For an example of overriding the default value for the NLS_TERRITORY parameter, see Oracle Database Globalization Support Guide . See Also: Oracle Database Globalization Support Guide for a complete list of territories Your operating system-specific Oracle documentation for the territory-dependent default values for these parameters See Also: Oracle Database Globalization Support Guide for a complete list of territories Your operating system-specific Oracle documentation for the territory-dependent default values for these parameters