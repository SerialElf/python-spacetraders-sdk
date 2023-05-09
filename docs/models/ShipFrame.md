# openapi_client.model.ship_frame.ShipFrame

The frame of the ship. The frame determines the number of modules and mounting points of the ship, as well as base fuel capacity. As the condition of the frame takes more wear, the ship will become more sluggish and less maneuverable.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The frame of the ship. The frame determines the number of modules and mounting points of the ship, as well as base fuel capacity. As the condition of the frame takes more wear, the ship will become more sluggish and less maneuverable. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**symbol** | str,  | str,  |  | must be one of ["FRAME_PROBE", "FRAME_DRONE", "FRAME_INTERCEPTOR", "FRAME_RACER", "FRAME_FIGHTER", "FRAME_FRIGATE", "FRAME_SHUTTLE", "FRAME_EXPLORER", "FRAME_MINER", "FRAME_LIGHT_FREIGHTER", "FRAME_HEAVY_FREIGHTER", "FRAME_TRANSPORT", "FRAME_DESTROYER", "FRAME_CRUISER", "FRAME_CARRIER", ] 
**moduleSlots** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**requirements** | [**ShipRequirements**](ShipRequirements.md) | [**ShipRequirements**](ShipRequirements.md) |  | 
**fuelCapacity** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**name** | str,  | str,  |  | 
**description** | str,  | str,  |  | 
**mountingPoints** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**condition** | [**ShipCondition**](ShipCondition.md) | [**ShipCondition**](ShipCondition.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

