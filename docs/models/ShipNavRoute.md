# openapi_client.model.ship_nav_route.ShipNavRoute

The routing information for the ship's most recent transit or current location.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The routing information for the ship&#x27;s most recent transit or current location. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**departureTime** | str, datetime,  | str,  | The date time of the ship&#x27;s departure. | value must conform to RFC-3339 date-time
**arrival** | str, datetime,  | str,  | The date time of the ship&#x27;s arrival. If the ship is in-transit, this is the expected time of arrival. | value must conform to RFC-3339 date-time
**destination** | [**ShipNavRouteWaypoint**](ShipNavRouteWaypoint.md) | [**ShipNavRouteWaypoint**](ShipNavRouteWaypoint.md) |  | 
**departure** | [**ShipNavRouteWaypoint**](ShipNavRouteWaypoint.md) | [**ShipNavRouteWaypoint**](ShipNavRouteWaypoint.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

