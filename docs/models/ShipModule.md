# openapi_client.model.ship_module.ShipModule

A module can be installed in a ship and provides a set of capabilities such as storage space or quarters for crew. Module installations are permanent.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A module can be installed in a ship and provides a set of capabilities such as storage space or quarters for crew. Module installations are permanent. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**symbol** | str,  | str,  |  | must be one of ["MODULE_MINERAL_PROCESSOR_I", "MODULE_CARGO_HOLD_I", "MODULE_CREW_QUARTERS_I", "MODULE_ENVOY_QUARTERS_I", "MODULE_PASSENGER_CABIN_I", "MODULE_MICRO_REFINERY_I", "MODULE_ORE_REFINERY_I", "MODULE_FUEL_REFINERY_I", "MODULE_SCIENCE_LAB_I", "MODULE_JUMP_DRIVE_I", "MODULE_JUMP_DRIVE_II", "MODULE_JUMP_DRIVE_III", "MODULE_WARP_DRIVE_I", "MODULE_WARP_DRIVE_II", "MODULE_WARP_DRIVE_III", "MODULE_SHIELD_GENERATOR_I", "MODULE_SHIELD_GENERATOR_II", ] 
**requirements** | [**ShipRequirements**](ShipRequirements.md) | [**ShipRequirements**](ShipRequirements.md) |  | 
**name** | str,  | str,  |  | 
**capacity** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**range** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

