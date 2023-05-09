# openapi_client.model.ship_engine.ShipEngine

The engine determines how quickly a ship travels between waypoints.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The engine determines how quickly a ship travels between waypoints. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**symbol** | str,  | str,  |  | must be one of ["ENGINE_IMPULSE_DRIVE_I", "ENGINE_ION_DRIVE_I", "ENGINE_ION_DRIVE_II", "ENGINE_HYPER_DRIVE_I", ] 
**requirements** | [**ShipRequirements**](ShipRequirements.md) | [**ShipRequirements**](ShipRequirements.md) |  | 
**name** | str,  | str,  |  | 
**description** | str,  | str,  |  | 
**speed** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
**condition** | [**ShipCondition**](ShipCondition.md) | [**ShipCondition**](ShipCondition.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

