# openapi_client.model.shipyard.Shipyard

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[shipTypes](#shipTypes)** | list, tuple,  | tuple,  | The list of ship types available for purchase at this shipyard. | 
**symbol** | str,  | str,  | The symbol of the shipyard. The symbol is the same as the waypoint where the shipyard is located. | 
**[transactions](#transactions)** | list, tuple,  | tuple,  | The list of recent transactions at this shipyard. | [optional] 
**[ships](#ships)** | list, tuple,  | tuple,  | The ships that are currently available for purchase at the shipyard. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# shipTypes

The list of ship types available for purchase at this shipyard.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of ship types available for purchase at this shipyard. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | [**ShipType**](ShipType.md) | [**ShipType**](ShipType.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# transactions

The list of recent transactions at this shipyard.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of recent transactions at this shipyard. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ShipyardTransaction**](ShipyardTransaction.md) | [**ShipyardTransaction**](ShipyardTransaction.md) | [**ShipyardTransaction**](ShipyardTransaction.md) |  | 

# ships

The ships that are currently available for purchase at the shipyard.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The ships that are currently available for purchase at the shipyard. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ShipyardShip**](ShipyardShip.md) | [**ShipyardShip**](ShipyardShip.md) | [**ShipyardShip**](ShipyardShip.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

