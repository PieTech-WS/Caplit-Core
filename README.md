# CoreApps Platform-Core
projectFlamingo

构建以应用为中心的生态平台

## 写在前面
我不期待这个项目会给我带来什么, 
也不期待这个项目会不会成功, 效果到底好不好.
因为这个顶多算个练手的项目, 没有多余的什么先
进技术啊什么的, 有人骂它我会接受, 因为路还很长.

就只是一个模拟操作系统结构的程序的内核, 仅此而已.

我想为什么不能用python来写一个应用框架呢?也许这能让使用python构建一个应用程序更简单,也更安全.

## 启动流程

启动文件(boot.exe/boot) --切换目录并拉起--> init.svc.py 
--> kernel.py(xmlrpc Service主机)

init.svc.py的作用是准备必要的
启动时文件到tmp目录供kernel使用.

kernel(kernel.py)实际上是服务主机(运行应用/Caplit所需的服务), 应用/Caplit系统组件通过xmlrpc与其通讯.

## 核心API(目前已被使用的)

- connect(通讯库)
- i18n(多语言支持)
- service(服务API)
- log(日志, 现已支持输出到文档)
