# openapi_client.model.ship_crew.ShipCrew

The ship's crew service and maintain the ship's systems and equipment.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The ship&#x27;s crew service and maintain the ship&#x27;s systems and equipment. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**wages** | decimal.Decimal, int,  | decimal.Decimal,  | The amount of credits per crew member paid per hour. Wages are paid when a ship docks at a civilized waypoint. | 
**current** | decimal.Decimal, int,  | decimal.Decimal,  | The current number of crew members on the ship. | 
**rotation** | str,  | str,  | The rotation of crew shifts. A stricter shift improves the ship&#x27;s performance. A more relaxed shift improves the crew&#x27;s morale. | must be one of ["STRICT", "RELAXED", ] if omitted the server will use the default value of "STRICT"
**morale** | decimal.Decimal, int,  | decimal.Decimal,  | A rough measure of the crew&#x27;s morale. A higher morale means the crew is happier and more productive. A lower morale means the ship is more prone to accidents. | 
**required** | decimal.Decimal, int,  | decimal.Decimal,  | The minimum number of crew members required to maintain the ship. | 
**capacity** | decimal.Decimal, int,  | decimal.Decimal,  | The maximum number of crew members the ship can support. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

