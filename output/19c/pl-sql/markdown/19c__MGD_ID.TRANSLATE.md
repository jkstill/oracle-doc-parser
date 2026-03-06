---
id: 19c__MGD_ID.TRANSLATE
name: MGD_ID.TRANSLATE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: MGD_ID
tags: [mgd_id]
source_file: MGD_ID-Package-Types.html
---

# MGD_ID.TRANSLATE

This static function translates between different representations directly without first constructing an MGD_ID object.

## Syntax

```sql
TRANSLATE (
   category_name    IN VARCHAR2,
   identifier       IN VARCHAR2,
   parameter_list   IN VARCHAR2,
   output_format    IN VARCHAR2)
 RETURN VARCHAR2 DETERMINISTIC;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| category_name | VARCHAR2 | IN | Name of category |
| category_version |  |  | Category version. If NULL , the latest version of the specified category name will be used. |
| identifier | VARCHAR2 | IN | EPC identifier, expressed as a string in accordance with one of the grammars or patterns in the TDT markup file. For example, a binary string consisting of characters 0 and 1 , a URI (either tag-encoding or pure-identity formats), or a serialized legacy code expressed as a string format for input, such as gtin=00037000302414;serial=10419703 for a SGTIN coding scheme. |
| parameter_list | VARCHAR2 | IN | List of additional parameters required to create the object in the representation. The list is expressed as a parameter string containing key-value pairs, separated by the semicolon (;) as a delimiter between key-value pairs. For example, for a GTIN code, the parameter string would look as follows: filter=3;companyprefixlength=7;taglength=96 |
| output_format | VARCHAR2) | IN | One of the supported output formats into which an MGD_ID component shall be converted: BINARY LEGACY TAG_ENCODING PURE_IDENTITY ONS_HOSTNAME |

**Returns:** `VARCHAR2`

## Usage Notes

This method is overloaded. The different functionality of each form of syntax is presented along with the definitions. Syntax Converts the identifier in one format to another given the category name, the tag identifier, the parameter list, and the output format. TRANSLATE ( category_name IN VARCHAR2, identifier IN VARCHAR2, parameter_list IN VARCHAR2, output_format IN VARCHAR2) RETURN VARCHAR2 DETERMINISTIC; Converts the identifier in one format to another given the category name, category version, the tag identifier, the parameter list, and the output format. TRANSLATE ( category_name IN VARCHAR2, category_version IN VARCHAR2, identifier IN VARCHAR2, parameter_list IN VARCHAR2, output_format IN VARCHAR2) RETURN VARCHAR2 DETERMINISTIC; Parameters Table 289-9 TRANSLATE Function Parameters Parameter Description category_name Name of category category_version Category version. If NULL , the latest version of the specified category name will be used. identifier EPC identifier, expressed as a string in accordance with one of the grammars or patterns in the TDT markup file. For example, a binary string consisting of characters 0 and 1 , a URI (either tag-encoding or pure-identity formats), or a serialized legacy code expressed as a string format for input, such as gtin=00037000302414;serial=10419703 for a SGTIN coding scheme. parameter_list List of additional parameters required to create the object in the representation. The list is expressed as a parameter string containing key-value pairs, separated by the semicolon (;) as a delimiter between key-value pairs. For example, for a GTIN code, the parameter string would look as follows: filter=3;companyprefixlength=7;taglength=96 output_format One of the supported output formats into which an MGD_ID component shall be converted: BINARY LEGACY TAG_ENCODING PURE_IDENTITY ONS_HOSTNAME Usage Notes When converting from a pure identity representation to a binary representation, the filter value must be supplied as a value using the parameter_list parameter. Examples The following examples translates one GID-96 representation into another: -- Contents of translate1.sql file call DBMS_MGD_ID_UTL.set_proxy('www-proxy.example.com', '80'); DECLARE id MGD_ID; BEGIN DBMS_MGD_ID_UTL.refresh_category(DBMS_MGD_ID_UTL.get_category_id('EPC', NULL)); dbms_output.put_line('Category ID is EPC, Identifier is BINARY, Output format is BINARY'); dbms_output.put_line( mgd_id.translate('EPC', NULL,'001101010000000000001001000010001000000000000111011000100001000000000000000011111110011000110010' , NULL, 'BINARY')); dbms_output.put_line('Category ID is EPC, Identifier is BINARY, Output format is PURE_IDENTITY'); dbms_output.put_line( mgd_id.translate('EPC', NULL,'001101010000000000001001000010001000000000000111011000100001000000000000000011111110011000110010' , NULL, 'PURE_IDENTITY')); dbms_output.put_line('Category ID is EPC, Identifier is BINARY, Output format is TAG_ENCODING'); dbms_output.put_line( mgd_id.translate('EPC', NULL,'001101010000000000001001000010001000000000000111011000100001000000000000000011111110011000110010' , NULL, 'TAG_ENCODING')); dbms_output.put_line('Category ID is EPC, Identifier is TAG_ENCODING, Output format is BINARY'); dbms_output.put_line( mgd_id.translate('EPC', NULL, 'urn:epc:tag:gid-96:0037000.30241.1041970', NULL, 'BINARY')); dbms_output.put_line('Category ID is EPC, Identifier is TAG_ENCODING, Output format is PURE_IDENTITY'); dbms_output.put_line( mgd_id.translate('EPC', NULL, 'urn:epc:tag:gid-96:0037000.30241.1041970', NULL, 'PURE_IDENTITY')); dbms_output.put_line('Category ID is EPC, Identifier is TAG_ENCODING, Output format is TAG_ENCODING'); dbms_output.put_line( mgd_id.translate('EPC', NULL, 'urn:epc:tag:gid-96:0037000.30241.1041970', NULL, 'TAG_ENCODING')); dbms_output.put_line('Category ID is EPC, Identifier is PURE_IDENTITY, Output format is BINARY'); dbms_output.put_line( mgd_id.translate('EPC', NULL, 'urn:epc:id:gid:0037000.30241.1041970', NULL, 'BINARY')); dbms_output.put_line('Category ID is EPC, Identifier is PURE_IDENTITY, Output format is PURE_IDENTITY'); dbms_output.put_line( mgd_id.translate('EPC', NULL, 'urn:epc:id:gid:0037000.30241.1041970', NULL, 'PURE_IDENTITY')); dbms_output.put_line('Category ID is EPC, Identifier is PURE_IDENTITY, Output format is TAG_ENCODING'); dbms_output.put_line( mgd_id.translate('EPC', NULL, 'urn:epc:id:gid:0037000.30241.1041970', NULL, 'TAG_ENCODING')); END; / SHOW ERRORS; call DBMS_MGD_ID_UTL.remove_proxy(); SQL> @translate1.sql . . . Category ID is EPC, Identifier is BINARY, Output format is BINARY 001101010000000000001001000010001000000000000111011000100001000000000000000011111110011000110010 Category ID is EPC, Identifier is BINARY, Output format is PURE_IDENTITY urn:epc:id:gid:37000.30241.1041970 Category ID is EPC, Identifier is BINARY, Output format is TAG_ENCODING urn:epc:tag:gid-96:37000.30241.1041970 Category ID is EPC, Identifier is TAG_ENCODING, Output format is BINARY 001101010000000000001001000010001000000000000111011000100001000000000000000011111110011000110010 Category ID is EPC, Identifier is TAG_ENCODING, Output format is PURE_IDENTITY urn:epc:id:gid:0037000.30241.1041970 Category ID is EPC, Identifier is TAG_ENCODING, Output format is TAG_ENCODING urn:epc:tag:gid-96:0037000.30241.1041970 Category ID is EPC, Identifier is PURE_IDENTITY, Output format is BINARY 001101010000000000001001000010001000000000000111011000100001000000000000000011111110011000110010 Category ID is EPC, Identifier is PURE_IDENTITY, Output format is PURE_IDENTITY urn:epc:id:gid:0037000.30241.1041970 Category ID is EPC, Identifier is PURE_IDENTITY, Output format is TAG_ENCODING urn:epc:tag:gid-96:0037000.30241.1041970 PL/SQL procedure successfully completed. . . .