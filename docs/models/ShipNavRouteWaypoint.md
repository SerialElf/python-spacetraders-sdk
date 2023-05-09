# openapi_client.model.ship_nav_route_waypoint.ShipNavRouteWaypoint

The destination or departure of a ships nav route.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The destination or departure of a ships nav route. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**symbol** | str,  | str,  |  | 
**systemSymbol** | str,  | str,  |  | 
**x** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**y** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**type** | [**WaypointType**](WaypointType.md) | [**WaypointType**](WaypointType.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

