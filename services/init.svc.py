import os
import shutil
from coraos.log.file import LogFile
from coraos.i18n import LangFile

logSession = LogFile("init.svc", "log")

confs = os.listdir("config")
if not os.path.isdir("tmp/config"):
    logSession.warn("tmp/config目录不存在.")
    logSession.process("创建中...")
    os.mkdir("tmp/config")

logSession.process("配置文件准备中...")
for i in confs:
    shutil.copy("config/{}".format(i), "tmp/config")
    logSession.child_process(
        "移动 {} 到 {}"
        .format(
            "config/{}".format(i),
            "tmp/config"
        )
    )

