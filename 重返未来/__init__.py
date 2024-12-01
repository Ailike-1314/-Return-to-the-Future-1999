# __init__.py 为初始化加载文件
from .res.main import *
# 游戏包名 com.shenlan.m.reverse1999

import json
from ascript.android import system
from ascript.android.ui import WebWindow
from ascript.android.system import R, KeyValue


def tunnel(k, v):
    if k == 'default':  # 点击默认返回 default，在拖拽ui界面中的默认按钮事件中查看
        print(f"恢复默认ui")
        system.reboot()
    if k == 'save':  # 点击默认返回 save，在拖拽ui界面中的默认保存事件中查看
        print(f"保存了ui")
    if k == 'close':  # 点击默认返回 close，在拖拽ui界面中的关闭按钮事件中查看
        print(f"关闭了ui")
        system.exit()
    if k == 'start':  # 点击默认返回 start，在拖拽ui界面中的运行按钮事件中查看
        print(f"ui选择状态: {v}")  # 这里的v是字符串类型，所以后续提取要json.loads一下
        KeyValue.save('ui', v)  # as的数据缓存方法: 将数据存储在本地

        # global Zyhg
        # global Rwjl
        # global Mrdcj
        # global Mrxx
        # global Dqhd
        #
        # global Checkpoint
        # global UI_xxgc_num
        # global UI_again_num
        #
        # global HD_Checkpoint
        # global UI_hd_mode
        # global UI_hd_num
        # global UI_hd_again_num

        # 使用KeyValue.get方法可以在任何一个xx.py的文件中,随时读取ui设置的值
        # 想在哪个文件读取就要在哪个文件导包: from ascript.android.system import KeyValue
        # 不管ui中有几个标签页，读取方式都一样，示例如下：
        # 任务 = json.loads(KeyValue.get('ui',''))['ui任务']
        # 评分 = json.loads(KeyValue.get('ui',''))['ui评分']
        # ['ui任务']：这个ui任务是在拖拽ui中设置的字段名称，要以字母开头

        # Checkpoint = json.loads(KeyValue.get('ui', ''))['UI_Checkpoint']  # 选择关卡
        # UI_xxgc_num = int(json.loads(KeyValue.get('ui', ''))['UI_UI_xxgc_num'])  # UI获取的心相观测
        # UI_again_num = int(json.loads(KeyValue.get('ui', ''))['UI_UI_again_num'])  # 重复挑战关卡的次数
        #
        # # 活动关卡次数
        # HD_Checkpoint = json.loads(KeyValue.get('ui', ''))['UI_HD_Checkpoint']  # 选择活动关卡
        # UI_hd_num = int(json.loads(KeyValue.get('ui', ''))['UI_UI_hd_num'])
        # UI_hd_again_num = int(json.loads(KeyValue.get('ui', ''))['UI_UI_hd_again_num'])
        # UI_hd_mode = json.loads(KeyValue.get('ui', ''))['UI_UI_hd_mode']  # 故事、意外、艰难
        #
        # Zyhg = not json.loads(KeyValue.get('ui', ''))['UI_Zyhg']  # 每日资源好感领取
        # Mrxx = not json.loads(KeyValue.get('ui', ''))['UI_Mrxx']  # 每日心相初始化
        # Dqhd = not json.loads(KeyValue.get('ui', ''))['UI_Dqhd']  # 每日活动
        # Rwjl = not json.loads(KeyValue.get('ui', ''))['UI_Rwjl']  # 每日奖励领取状态
        # Mrdcj = not json.loads(KeyValue.get('ui', ''))['UI_Mrdcj']  # 每日点唱机
        # print(Mrxx)
        #启动
        run()


# 版本说明：
# 1.mobile：这个版本特别特别小，加载起来会快一些，但是ui的样式和功能相对少一些
# 2.pc：这个版本会大一点，加载没有那么快，但是优化以后也已经很小了，样式多功能多
# 3.这两个版本都是可以用于as的ui的，并不是pc要用as的电脑版，都是可以用于手机脚本的ui
# 4.使用的时候用哪个版本保存哪个文件夹就可以了，另一个可以删除


w = WebWindow(R.ui('/formCreateMobile/mobile.html'), tunnel)  # 移动版：小，但是样式功能少不好看
# w = WebWindow(R.ui('/formCreatepc/pc.html'), tunnel) # pc版：大，但是样式多功能多好看
# w.size(-1, -1)  # 全屏
# w.background('#00000000')  # 透明背景
w.show()



