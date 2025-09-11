---
title: mmdetection框架学习
date: 2025-6-3
---



# 答疑解惑

### 配置文件的背后

mmdetection框架通过配置文件就能做到模型搭建, 那么他是如何得知这些模块在哪的呢? 这就涉及到了python的装饰类, 我们会发现很多类似这样的代码

```python
@MODELS.register_module()  # 后续版本貌似检测头主干那些全部用这个了
@DATASETS.register_module()
.....
```

这个会把定义的模块注册到mmdet框架管理的容器中, 其实就是一个字典, 名字到包名的对应

最后通过懒加载(这里也算不上真正的懒加载, 因为只要使用其中任意一个模块, 就会把所有模块全部导入) 把预先定义好的模块全部加载进去, 这个是mmdet/model/\_\_init\_\_.py

```
# Copyright (c) OpenMMLab. All rights reserved.
from .backbones import *  # noqa: F401,F403
from .data_preprocessors import *  # noqa: F401,F403
from .dense_heads import *  # noqa: F401,F403
from .detectors import *  # noqa: F401,F403
from .language_models import *  # noqa: F401,F403
from .layers import *  # noqa: F401,F403
from .losses import *  # noqa: F401,F403
from .mot import *  # noqa: F401,F403
from .necks import *  # noqa: F401,F403
from .reid import *  # noqa: F401,F403
from .roi_heads import *  # noqa: F401,F403
from .seg_heads import *  # noqa: F401,F403
from .task_modules import *  # noqa: F401,F403
from .test_time_augs import *  # noqa: F401,F403
from .trackers import *  # noqa: F401,F403
from .tracking_heads import *  # noqa: F401,F403
from .vis import *  # noqa: F401,F403
```

