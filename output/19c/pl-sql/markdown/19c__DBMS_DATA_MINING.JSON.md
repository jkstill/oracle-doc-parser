---
id: 19c__DBMS_DATA_MINING.JSON
name: DBMS_DATA_MINING.JSON
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING
tags: [dbms_data_mining]
source_file: DBMS_DATA_MINING.html
---

# DBMS_DATA_MINING.JSON

Follow JSON schema when creating a new JSON object with flexibility.

## Syntax

```sql
{
    "type": "object",
    "properties": {
        "algo_name_display": { "type" : "object",
                                               "properties" : {
                                               "language" : { "type" : "string",
                                                                       "enum" : ["English", "Spanish", "French"],
                                                                       "default" : "English"},
                                               "name" : { "type" : "string"}}
                                             },

        "function_language": {"type": "string" },
        "mining_function": {
                 "type" : "array",
                 "items" : [
                     { "type" : "object",
                        "properties" : {
                           "mining_function_name"  : { "type" : "string"},
                           "build_function": {  
                                   "type": "object",
                                   "properties": {
                                        "function_body": { "type": "CLOB" }
                                                        }
                                    },

        "detail_function": {  
                 "type" : "array",
                  "items" : [
                      {"type": "object",
                        "properties": {
                             "function_body": { "type": "CLOB" },
                             "view_columns": { "type" : "array",
                                                                   "items" : {
                                                                           "type" : "object",
                                                                           "properties" : {
                                                                               "name" : { "type" : "string"},
                                                                               "type" : { "type" : "string",
                                                                                               "enum" : ["VARCHAR2",
                                                                                                                "NUMBER",
                                                                                                                "DATE",
                                                                                                                "BOOLEAN"]
                                                                                             }
                                                                            }
                                                          }
                                            }
                                 }
                     ]
        },

       "score_function": {  
                 "type": "object",
                 "properties": {
                       "function_body": { "type": "CLOB" }
                        }
                 },
        "weight_function": {
                        "type": "object",
                        "properties": {
                            "function_body": { "type": "CLOB" },
                        }
                 }
                               }
           }]
        },  

       "algo_setting": {
                "type" : "array",
                "items" : [
                    { "type" : "object",
                       "properties" : {
                          "name"              : { "type" : "string"},
                          "name_display": { "type" : "object",
                                                         "properties" : {
                                                         "language" : { "type" : "string",
                                                                                 "enum" : ["English", "Spanish", "French"],
                                                                                 "default" : "English"},
                                                         "name" : { "type" : "string"}}
                                                      },
                          "type" : { "type" : "string",
                                          "enum" : ["string", "integer", "number", "boolean"]},

                          "optional": {"type" : "BOOLEAN",
                                               "default" : "FALSE"},
   
                          "value" : { "type" :  "string"},  

                          "min_value" : { "type": "object",
                                                      "properties": {
                                                            "min_value": {"type": "number"},
                                                             "inclusive": { "type": "boolean",
                                                                                   "default" : TRUE},
                                                       }
                                                  },
                           "max_value" : {"type": "object",
                                                     "properties": {
                                                          "max_value": {"type": "number"},
                                                          "inclusive": { "type": "boolean",
                                                                                 "default" : TRUE},
                                                            }
                                                    },

                          "categorical choices" : { "type": "array",
                                                                  "items": {
                                                                      "type": "string"
                                                                   }
                                                               },

                          "description_display": { "type" : "object",
                                                                  "properties" : {
                                                                  "language" : { "type" : "string",
                                                                                          "enum" : ["English", "Spanish", "French"],
                                                                                          "default" : "English"},
                                                                  "name" : { "type" : "string"}}
                                                               }
                        }
                    }
                 ]
          }    
    }
}
```

## Usage Notes

Usage Note Some flexibility when creating a new JSON object are as follows: Partial registration is allowed. For example, detail function can be missing. Different orders are allowed. For example, detail function can be written before build function or after the build function.