# Domain Randomization

One of the benefits of simulation is the ability to chop and change a number of aspects that would otherwise be expensive or time-consuming to do in the real world. This document demonstrates a number of simple tools for randomization.

### During Reconfiguration

Simply providing batched data to the CameraConfigs of your sensors as done below (pose, intrinsic, fov, near, and far are supported) will randomize the camera configuration across parallel scenes. The example below does it for camera poses by modifying the `_default_sensor_configs` property of the task class
