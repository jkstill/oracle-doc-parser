---
id: 19c__DBMS_EPG.SET_DAD_ATTRIBUTE
name: DBMS_EPG.SET_DAD_ATTRIBUTE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_EPG
tags: [dbms_epg]
source_file: DBMS_EPG.html
---

# DBMS_EPG.SET_DAD_ATTRIBUTE

This procedure sets the value for a DAD.

## Syntax

```sql
DBMS_EPG.SET_DAD_ATTRIBUTE (
   dad_name    IN  VARCHAR2,
   attr_name   IN  VARCHAR2,   attr_value  IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| dad_name | VARCHAR2 | IN | The name of the DAD for which to set the attribute |
| attr_name | VARCHAR2 | IN | The name of the attribute to set |
| attr_value | VARCHAR2) | IN | The attribute value to set |

## Usage Notes

See Also: Configuration Subprograms for other subprograms in this group See Also: Configuration Subprograms for other subprograms in this group Syntax DBMS_EPG.SET_DAD_ATTRIBUTE ( dad_name IN VARCHAR2, attr_name IN VARCHAR2, attr_value IN VARCHAR2); Parameters Table 67-18 SET_DAD_ATTRIBUTE Procedure Parameters Parameter Description dad_name The name of the DAD for which to set the attribute attr_name The name of the attribute to set attr_value The attribute value to set Table 67-19 Mapping Between mod_plsql and Embedded PL/SQL Gateway DAD Attributes mod_plsql DAD Attribute Embedded PL/SQL Gateway DAD Attribute Allows Multiple Occurr-ences Legal Values PlsqlAfterProcedure after-procedure No String PlsqlAlwaysDescribeProcedure always-describe-procedure No Enumeration of On, Off PlsqlAuthenticationMode authentication-mode No Enumeration of Basic, SingleSignOn, GlobalOwa, CustomOwa, PerPackageOwa PlsqlBeforeProcedure before-procedure No String PlsqlBindBucketLengths bind-bucket-lengths Yes Unsigned integer PlsqlBindBucketWidths bind-bucket-widths Yes Unsigned integer PlsqlCGIEnvironmentList cgi-environment-list Yes String PlsqlCompatibilityMode compatibility-mode No Unsigned integer PlsqlDatabaseUsername database-usernam e No String PlsqlDefaultPage default-page No String PlsqlDocumentPath document-path No String PlsqlDocumentProcedure document-procedure No String PlsqlDocumentTablename document-table-name No String PlsqlErrorStyle error-style No Enumeration of ApacheStyle, ModplsqlStyle, DebugStyle PlsqlExclusionList exclusion-list Yes String PlsqlFetchBufferSize fetch-buffer-size No Unsigned integer PlsqlInfoLogging i nfo-logging No Enumeration of InfoDebug PlsqlOWADebugEnable owa-debug-enable No Enumeration of On, Off PlsqlMaxRequestsPerSession max-requests-per-session No Unsigned integer PlsqlNLSLanguage nls-language No String PlsqlPathAlias path-alias No String PlsqlPathAliasProcedure path-alias-procedure No String PlsqlRequestValidationFunction request-validation-function No String PlsqlSessionCookieName session-cookie-name No String PlsqlSessionStateManagement session-state-management No Enumeration of StatelessWithResetPackageState, StatelessWithFastRestPackageState, StatelessWithPreservePackageState PlsqlTransferMode transfer-mode No Enumeration of Char, Raw PlsqlUploadAsLongRaw upload-as-long-raw No String Exceptions Raises an error if DAD does not exist or the attribute is unknown.