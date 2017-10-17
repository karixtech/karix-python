# MessageResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** | Unique ID for a message sent or received | [optional] 
**source** | **str** | Sender ID for the message | [optional] 
**destination** | **str** | Destination number for the message | [optional] 
**status** | **str** | Current status of the message. Possible values: - &#x60;queued&#x60;: Message has been queued in CPaaS system             (for either &#x60;inbound&#x60; or &#x60;outbound&#x60; direction) - &#x60;sent&#x60;: The &#x60;outbound&#x60; message has been sent to carriers for delivery - &#x60;failed&#x60;: In case of &#x60;outbound&#x60; message, this means that CPaaS failed             to send the message to a carrier.             In case of &#x60;inbound&#x60; message, this means that CPaaS failed             to send the message to its webhook, if configured. - &#x60;delivered&#x60;: The &#x60;outbound&#x60; message was delivered to its receiver. - &#x60;undelivered&#x60;: The &#x60;outbound&#x60; message falied to be delivered to its receiver. - &#x60;rejected&#x60;: The &#x60;outbound&#x60; message was rejected by the chosen carrier.  | [optional] 
**text** | **str** |  | [optional] 
**queued_time** | **datetime** |  | [optional] 
**sent_time** | **datetime** |  | [optional] 
**delivered_time** | **datetime** |  | [optional] 
**direction** | **str** |  | [optional] 
**error_code** | **str** |  | [optional] 
**cost** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


