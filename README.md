![version](https://img.shields.io/badge/Version-v0.1.0-blue.svg?style=plastic)
![PyTorch](https://img.shields.io/badge/PyTorch-v1.9.0-green.svg?style=plastic)
![PyTorch](https://img.shields.io/badge/horovod-v0.22.1-green.svg?style=plastic)
![license](https://img.shields.io/badge/license-CC_BY--NC-red.svg?style=plastic)

# DNNTrainerFlow
A demonstration of an automatic workflow for rapid DNN training using remote AI system resource.

The sample DNN used in the demo can be obtained from [BraggNN](https://github.com/lzhengchun/BraggNN)

# The big picture
![The Big Picture](figure/big-picture.png)

# The implementation 
![title](figure/workflow-demo.jpeg)

# Requirements
## AI system side
- funcx_endpoint=0.3.2
- PyTorch=1.9.0
- horovod=0.22.1
- h5py=2.10.0
- numpy=1.19.2

## Client/User side
- globus-automate-client=0.12.0
- funcx=0.3.2
