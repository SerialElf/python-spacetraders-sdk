# openapi_client.model.shipyard_ship.ShipyardShip

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**engine** | [**ShipEngine**](ShipEngine.md) | [**ShipEngine**](ShipEngine.md) |  | 
**reactor** | [**ShipReactor**](ShipReactor.md) | [**ShipReactor**](ShipReactor.md) |  | 
**name** | str,  | str,  |  | 
**description** | str,  | str,  |  | 
**[mounts](#mounts)** | list, tuple,  | tuple,  |  | 
**purchasePrice** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**[modules](#modules)** | list, tuple,  | tuple,  |  | 
**frame** | [**ShipFrame**](ShipFrame.md) | [**ShipFrame**](ShipFrame.md) |  | 
**type** | [**ShipType**](ShipType.md) | [**ShipType**](ShipType.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# modules

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ShipModule**](ShipModule.md) | [**ShipModule**](ShipModule.md) | [**ShipModule**](ShipModule.md) |  | 

# mounts

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ShipMount**](ShipMount.md) | [**ShipMount**](ShipMount.md) | [**ShipMount**](ShipMount.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

