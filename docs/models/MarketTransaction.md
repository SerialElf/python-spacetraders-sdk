# openapi_client.model.market_transaction.MarketTransaction

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**tradeSymbol** | str,  | str,  | The symbol of the trade good. | 
**totalPrice** | decimal.Decimal, int,  | decimal.Decimal,  | The total price of the transaction. | 
**waypointSymbol** | str,  | str,  | The symbol of the waypoint where the transaction took place. | 
**shipSymbol** | str,  | str,  | The symbol of the ship that made the transaction. | 
**units** | decimal.Decimal, int,  | decimal.Decimal,  | The number of units of the transaction. | 
**type** | str,  | str,  | The type of transaction. | must be one of ["PURCHASE", "SELL", ] 
**pricePerUnit** | decimal.Decimal, int,  | decimal.Decimal,  | The price per unit of the transaction. | 
**timestamp** | str, datetime,  | str,  | The timestamp of the transaction. | value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

