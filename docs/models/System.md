# openapi_client.model.system.System

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**symbol** | str,  | str,  |  | 
**sectorSymbol** | str,  | str,  |  | 
**x** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**y** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**type** | [**SystemType**](SystemType.md) | [**SystemType**](SystemType.md) |  | 
**[waypoints](#waypoints)** | list, tuple,  | tuple,  |  | 
**[factions](#factions)** | list, tuple,  | tuple,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# waypoints

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SystemWaypoint**](SystemWaypoint.md) | [**SystemWaypoint**](SystemWaypoint.md) | [**SystemWaypoint**](SystemWaypoint.md) |  | 

# factions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SystemFaction**](SystemFaction.md) | [**SystemFaction**](SystemFaction.md) | [**SystemFaction**](SystemFaction.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

