# hass-roborock
Communicates with roborock using Tuya, so can be used alongside roborock app.
  
Use this guide to get tokens: https://github.com/redphx/roborock-tuya-token
  
Another method is running on a rooted device (bluestacks / genymotion should work and be the easiest way of doing it):

```
adb exec-out run-as com.roborock.smart find /data/data/com.roborock.smart/files/rr_cache/ | egrep rr_tuya_[0-9] | xargs -n1 adb exec-out run-as com.roborock.smart cat > roborock_details.gz 
gzip -d roborock_details.gz 
```

Then token is listed in the JSON structure under "localKey". The device ID is listed under "devId"

In Home Assistant goto HACS -> Integrations. In the upper right corner menu select "Custom Repositories".
Add the URL of this project https://github.com/redphx/hass-roborock and choose "Integration" as category.
Now restart Home Assistant
Next goto the Home Assistant -> Configuration -> Integrations and add the Roborock integration and enter a name, the localKey and devId you found and the IP off the Roborock.

The Roborock should now became available as an entity, not a device.


