# openapi_client.model.ship_nav.ShipNav

The navigation information of the ship.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The navigation information of the ship. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**route** | [**ShipNavRoute**](ShipNavRoute.md) | [**ShipNavRoute**](ShipNavRoute.md) |  | 
**systemSymbol** | str,  | str,  | The system symbol of the ship&#x27;s current location. | 
**waypointSymbol** | str,  | str,  | The waypoint symbol of the ship&#x27;s current location, or if the ship is in-transit, the waypoint symbol of the ship&#x27;s destination. | 
**flightMode** | [**ShipNavFlightMode**](ShipNavFlightMode.md) | [**ShipNavFlightMode**](ShipNavFlightMode.md) |  | 
**status** | [**ShipNavStatus**](ShipNavStatus.md) | [**ShipNavStatus**](ShipNavStatus.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

