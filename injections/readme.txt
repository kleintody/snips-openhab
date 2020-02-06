# see Dialog Reference (https://docs.snips.ai/reference/dialogue)

#adding a single entity value:
mosquitto_pub -t hermes/injection/perform -f  openhab_device.json.single

#adding a set of entity values:
mosquitto_pub -t hermes/injection/perform -f  openhab_device.json

#resetting the added entity values
#(does not reset the ones that were part of the assistant):
mosquitto_pub -t hermes/injection/reset/perform -f  openhab_device.json.clean

