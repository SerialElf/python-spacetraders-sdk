# openapi_client.model.ship_reactor.ShipReactor

The reactor of the ship. The reactor is responsible for powering the ship's systems and weapons.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The reactor of the ship. The reactor is responsible for powering the ship&#x27;s systems and weapons. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**symbol** | str,  | str,  |  | must be one of ["REACTOR_SOLAR_I", "REACTOR_FUSION_I", "REACTOR_FISSION_I", "REACTOR_CHEMICAL_I", "REACTOR_ANTIMATTER_I", ] 
**requirements** | [**ShipRequirements**](ShipRequirements.md) | [**ShipRequirements**](ShipRequirements.md) |  | 
**name** | str,  | str,  |  | 
**description** | str,  | str,  |  | 
**powerOutput** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**condition** | [**ShipCondition**](ShipCondition.md) | [**ShipCondition**](ShipCondition.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

