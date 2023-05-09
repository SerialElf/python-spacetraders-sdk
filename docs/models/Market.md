# openapi_client.model.market.Market

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**symbol** | str,  | str,  | The symbol of the market. The symbol is the same as the waypoint where the market is located. | 
**[imports](#imports)** | list, tuple,  | tuple,  | The list of goods that are sought as imports in this market. | 
**[exports](#exports)** | list, tuple,  | tuple,  | The list of goods that are exported from this market. | 
**[exchange](#exchange)** | list, tuple,  | tuple,  | The list of goods that are bought and sold between agents at this market. | 
**[transactions](#transactions)** | list, tuple,  | tuple,  | The list of recent transactions at this market. Visible only when a ship is present at the market. | [optional] 
**[tradeGoods](#tradeGoods)** | list, tuple,  | tuple,  | The list of goods that are traded at this market. Visible only when a ship is present at the market. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# exports

The list of goods that are exported from this market.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of goods that are exported from this market. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**TradeGood**](TradeGood.md) | [**TradeGood**](TradeGood.md) | [**TradeGood**](TradeGood.md) |  | 

# imports

The list of goods that are sought as imports in this market.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of goods that are sought as imports in this market. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**TradeGood**](TradeGood.md) | [**TradeGood**](TradeGood.md) | [**TradeGood**](TradeGood.md) |  | 

# exchange

The list of goods that are bought and sold between agents at this market.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of goods that are bought and sold between agents at this market. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**TradeGood**](TradeGood.md) | [**TradeGood**](TradeGood.md) | [**TradeGood**](TradeGood.md) |  | 

# transactions

The list of recent transactions at this market. Visible only when a ship is present at the market.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of recent transactions at this market. Visible only when a ship is present at the market. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**MarketTransaction**](MarketTransaction.md) | [**MarketTransaction**](MarketTransaction.md) | [**MarketTransaction**](MarketTransaction.md) |  | 

# tradeGoods

The list of goods that are traded at this market. Visible only when a ship is present at the market.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of goods that are traded at this market. Visible only when a ship is present at the market. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**MarketTradeGood**](MarketTradeGood.md) | [**MarketTradeGood**](MarketTradeGood.md) | [**MarketTradeGood**](MarketTradeGood.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

