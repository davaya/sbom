# SPDX License List converter

The make script reads the SPDX license list data in JSON format from GitHub, extracts the fields needed
to create **LicenseList** and **ExceptionList** enums, and creates a JADN schema module that can
be referenced by other schemas.

* **license_list_source.jidl:** JADN Schema for the SPDX license list, derived from the current contents.
If additional fields are populated, or if some fields shown as required are not populated, the schema should
be modified accordingly.

* **license_list_source.json:** derived JSON Schema file for the SPDX license list.

* **data/** output directory containing License List and ExceptionList enumerations:
    * JADN schema module created by the *make* script
    * JIDL, HTML, and Markdown documentation formats
    * JSON schema
