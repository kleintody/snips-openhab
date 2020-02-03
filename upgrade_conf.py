from assistant.config import read_configuration_file, write_configuration_file

CURRENT = "2.1"
if __name__ == "__main__":
    conf = read_configuration_file()
    write = False

    if "static" not in conf:
        write = True
        conf["static"] = {}

    if "secret" not in conf:
        write = True
        conf["secret"] = {}

    if "conf_version" not in conf["static"] or conf["static"]["conf_version"] != CURRENT:
        conf["static"]["conf_version"] = CURRENT
        write = True

    if "sound_feedback" not in conf["secret"]:
        write = True
        conf["secret"]["sound_feedback"] = "off"

    if "default_room" not in conf["secret"]:
        write = True
        if "room_of_device_default" in conf["secret"]:
            conf["secret"]["default_room"] = conf["secret"]["room_of_device_default"]
            del conf["secret"]["room_of_device_default"]
        else:
            conf["secret"]["default_room"] = "Wohnzimmer"
    
    if "siteid2room_mapping" not in conf["secret"]:
        write = True
        conf["secret"]["siteid2room_mapping"] = '{ "default": "Wohnzimmer" }'
    
    if write:
        conf["static"]["conf_version"] = CURRENT
        write_configuration_file(conf)
