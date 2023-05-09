# openapi_client.model.ship_mount.ShipMount

A mount is installed on the exterier of a ship.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A mount is installed on the exterier of a ship. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**symbol** | str,  | str,  |  | must be one of ["MOUNT_GAS_SIPHON_I", "MOUNT_GAS_SIPHON_II", "MOUNT_GAS_SIPHON_III", "MOUNT_SURVEYOR_I", "MOUNT_SURVEYOR_II", "MOUNT_SURVEYOR_III", "MOUNT_SENSOR_ARRAY_I", "MOUNT_SENSOR_ARRAY_II", "MOUNT_SENSOR_ARRAY_III", "MOUNT_MINING_LASER_I", "MOUNT_MINING_LASER_II", "MOUNT_MINING_LASER_III", "MOUNT_LASER_CANNON_I", "MOUNT_MISSILE_LAUNCHER_I", "MOUNT_TURRET_I", ] 
**requirements** | [**ShipRequirements**](ShipRequirements.md) | [**ShipRequirements**](ShipRequirements.md) |  | 
**name** | str,  | str,  |  | 
**description** | str,  | str,  |  | [optional] 
**strength** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[deposits](#deposits)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# deposits

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["QUARTZ_SAND", "SILICON_CRYSTALS", "PRECIOUS_STONES", "ICE_WATER", "AMMONIA_ICE", "IRON_ORE", "COPPER_ORE", "SILVER_ORE", "ALUMINUM_ORE", "GOLD_ORE", "PLATINUM_ORE", "DIAMONDS", "URANITE_ORE", "MERITIUM_ORE", ] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

