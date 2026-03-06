---
id: 19c__UTL_URL
name: UTL_URL
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_URL
tags: [utl_url]
source_file: UTL_URL.html
---

# UTL_URL

UTL_URL can be used for encoding and decoding.

## Syntax

```sql
CREATE OR REPLACE FUNCTION form_url_encode (
   data    IN VARCHAR2,
   charset IN VARCHAR2) RETURN VARCHAR2 AS 
BEGIN 
  RETURN utl_url.escape(data, TRUE, charset); -- note use of TRUE
END;
```

**Returns:** `VARCHAR2`

## Usage Notes

You can implement the x-www-form-urlencoded encoding using the UTL_URL.ESCAPE function as follows: CREATE OR REPLACE FUNCTION form_url_encode ( data IN VARCHAR2, charset IN VARCHAR2) RETURN VARCHAR2 AS BEGIN RETURN utl_url.escape(data, TRUE, charset); -- note use of TRUE END; For decoding data encoded with the form-URL-encode scheme , the following function implements the decording scheme: CREATE OR REPLACE FUNCTION form_url_decode( data IN VARCHAR2, charset IN VARCHAR2) RETURN VARCHAR2 AS BEGIN RETURN utl_url.unescape( replace(data, '+', ' '), charset); END;