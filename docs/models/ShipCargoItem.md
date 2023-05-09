# openapi_client.model.ship_cargo_item.ShipCargoItem

The type of cargo item and the number of units.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The type of cargo item and the number of units. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**symbol** | str,  | str,  | The unique identifier of the cargo item type. | 
**name** | str,  | str,  | The name of the cargo item type. | 
**description** | str,  | str,  | The description of the cargo item type. | 
**units** | decimal.Decimal, int,  | decimal.Decimal,  | The number of units of the cargo item. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

