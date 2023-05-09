# openapi_client.model.survey.Survey

A resource survey of a waypoint, detailing a specific extraction location and the types of resources that can be found there.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A resource survey of a waypoint, detailing a specific extraction location and the types of resources that can be found there. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**symbol** | str,  | str,  | The symbol of the waypoint that this survey is for. | 
**size** | str,  | str,  | The size of the deposit. This value indicates how much can be extracted from the survey before it is exhausted. | must be one of ["SMALL", "MODERATE", "LARGE", ] 
**signature** | str,  | str,  | A unique signature for the location of this survey. This signature is verified when attempting an extraction using this survey. | 
**expiration** | str, datetime,  | str,  | The date and time when the survey expires. After this date and time, the survey will no longer be available for extraction. | value must conform to RFC-3339 date-time
**[deposits](#deposits)** | list, tuple,  | tuple,  | A list of deposits that can be found at this location. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# deposits

A list of deposits that can be found at this location.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of deposits that can be found at this location. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SurveyDeposit**](SurveyDeposit.md) | [**SurveyDeposit**](SurveyDeposit.md) | [**SurveyDeposit**](SurveyDeposit.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

