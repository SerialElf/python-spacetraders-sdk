# openapi_client.model.scanned_waypoint.ScannedWaypoint

A waypoint is a location that ships can travel to such as a Planet, Moon or Space Station.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A waypoint is a location that ships can travel to such as a Planet, Moon or Space Station. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**symbol** | str,  | str,  |  | 
**[traits](#traits)** | list, tuple,  | tuple,  | The traits of the waypoint. | 
**systemSymbol** | str,  | str,  |  | 
**x** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**y** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**type** | [**WaypointType**](WaypointType.md) | [**WaypointType**](WaypointType.md) |  | 
**[orbitals](#orbitals)** | list, tuple,  | tuple,  |  | 
**faction** | [**WaypointFaction**](WaypointFaction.md) | [**WaypointFaction**](WaypointFaction.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) | [**Chart**](Chart.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# orbitals

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**WaypointOrbital**](WaypointOrbital.md) | [**WaypointOrbital**](WaypointOrbital.md) | [**WaypointOrbital**](WaypointOrbital.md) |  | 

# traits

The traits of the waypoint.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The traits of the waypoint. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**WaypointTrait**](WaypointTrait.md) | [**WaypointTrait**](WaypointTrait.md) | [**WaypointTrait**](WaypointTrait.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

