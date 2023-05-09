# openapi_client.model.ship_cargo.ShipCargo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**units** | decimal.Decimal, int,  | decimal.Decimal,  | The number of items currently stored in the cargo hold. | 
**[inventory](#inventory)** | list, tuple,  | tuple,  | The items currently in the cargo hold. | 
**capacity** | decimal.Decimal, int,  | decimal.Decimal,  | The max number of items that can be stored in the cargo hold. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# inventory

The items currently in the cargo hold.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The items currently in the cargo hold. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ShipCargoItem**](ShipCargoItem.md) | [**ShipCargoItem**](ShipCargoItem.md) | [**ShipCargoItem**](ShipCargoItem.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

