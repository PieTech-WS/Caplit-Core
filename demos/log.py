from coraos.log import file

logSession = file.LogFile("test", "log")

logSession.process("test")
logSession.child_process("test1")
