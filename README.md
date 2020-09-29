# hass-roborock
Communicates with roborock using Tuya, so can be used alongside roborock app.

To get token from roborock app, run on rooted device (bluestacks / genymotion should work and be the easiest way of doing it):

```
adb exec-out run-as com.roborock.smart find /data/data/com.roborock.smart/files/rr_cache/ | egrep rr_tuya_[0-9] | xargs -n1 adb exec-out run-as com.roborock.smart cat > roborock_details.gz 
gzip -d roborock_details.gz 
```

Then token is listed in the JSON structure under "localKey". The device ID is listed under "devId"

In integrations, add roborock, enter the details from above and the vacuum's IP address.

