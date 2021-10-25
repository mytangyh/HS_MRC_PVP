# HS_MRC_PVP
炉石佣兵pvp自动投降，极低概率暴雪秋后算账。

### python3.7依赖
```bash
python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyautogui Pillow
python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pymouse PyUserinput pypiwin32
```

### 使用说明
1. 炉石窗口大小548 * 439，使用 `SetHearthstonePos.exe`初始化即可。
2. 进入匹配界面，执行`python pvp.py`即可正常挂机。

### 启用power.log
  如果使用过炉石盒子、官方插件、HDT等记牌器，忽略这一步。
  在目录`%LOCALAPPDATA%\Blizzard\Hearthstone`下创建一个`log.config`，内容如下
```config
[Arena]
LogLevel=1
FilePrinting=True
ConsolePrinting=False
ScreenPrinting=False
Verbose=False
[Decks]
LogLevel=1
FilePrinting=True
ConsolePrinting=False
ScreenPrinting=False
Verbose=False
[Power]
LogLevel=1
FilePrinting=True
ConsolePrinting=False
ScreenPrinting=False
Verbose=True
```

### 参考
1. [lushi_script](https://github.com/zhoubin-me/lushi_script)
2. [炉石传说LOG日志文件解读及入门教程](https://nga.178.com/read.php?tid=11838545)

## 注
1. window系统使用缩放的，请自行修改zoom的值，如系统缩放`150%`，填`1.5`。
2. 自行修改delay投降延迟。
3. `pvpp.py`不使用pymouse的版本，如果你的Python>3.7，且运行报错缺少依赖，可以尝试使用。
4. 开宝箱延迟在`if flagTimesleep >= 100:`，根据需要调低数值。编写逻辑：长时间不匹配，即开宝箱。
5. 炉石安装非默认目录时，请修改`LOGFILE`值与实际`Power.log`一致。

