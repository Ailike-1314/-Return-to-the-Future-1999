from ascript.android import plug
plug.load("ld:1.1.8") # 这里是版本号
plug.load("FSM:5")
from FSM import *
from ld.android import *
# 导入系统资源模块
from ascript.android.system import R
# 导入动作模块
from ascript.android import action
# 导入节点检索模块
from ascript.android import node
# 导入图色检索模块
from ascript.android import screen
from ascript.android.screen import *
# 导包
from ascript.android.ui import Dialog
from ascript.android import system
# 设置音乐媒体音量 为0%
# 导包
from ascript.android import media
from ascript.android import system
from ascript.android.system import R, KeyValue

# 初始化状态机
unit_state["LOG"]=True #是否打印当前状态(默认为True)
unit_state["SLEEP"]=1 #检测状态间隔时间(不设置默认为1秒)
unit_state["Name"]="UI" #当前状态名(初始状态)
unit_param["Mrrw"]={
    "is_main_page": 0 #判断页面
    }

unit_param["Ksxd"]={
    "is_start_page": 0 #判断页面
    }

unit_param["Mrzy"]={
    "cw_is_click": 0,
    "lc_is_click": 0,
    "hg_is_click": 0
    }

unit_param["Mrjl"]={
    "mrhy_click": 0,
    "mzhy_click": 0,
    "is_rw_page": 0 #判断页面
    }

unit_param["Mrhd"]={
    "is_hd_page": 0 #判断页面
    }

unit_param["Dcj"]={
    "is_dcj_page": 0 #判断页面
    }


###########################
## 定义-默认值
###########################
Page = 'main' # 初始页面
# Checkpoint = None# 选择关卡
# UI_xxgc_num = None# UI获取的心相观测
# UI_again_num = None # 重复挑战关卡的次数
#
#
# #活动关卡次数
# HD_Checkpoint = None # 选择活动关卡
# UI_hd_num = None
# UI_hd_again_num = None
# UI_hd_mode = None# 故事、意外、艰难



Checkpoint = json.loads(KeyValue.get('ui', ''))['UI_Checkpoint'] # 选择关卡
UI_xxgc_num = int(json.loads(KeyValue.get('ui', ''))['UI_UI_xxgc_num'])  # UI获取的心相观测
UI_again_num = int(json.loads(KeyValue.get('ui', ''))['UI_UI_again_num'])  # 重复挑战关卡的次数

# 活动关卡次数
HD_Checkpoint = json.loads(KeyValue.get('ui', ''))['UI_HD_Checkpoint']  # 选择活动关卡
UI_hd_num = int(json.loads(KeyValue.get('ui', ''))['UI_UI_hd_num'])
UI_hd_again_num = int(json.loads(KeyValue.get('ui', ''))['UI_UI_hd_again_num'])
UI_hd_mode = json.loads(KeyValue.get('ui', ''))['UI_UI_hd_mode']  # 故事、意外、艰难

Zyhg = None # 每日资源好感领取
Mrxx = None # 每日心相初始化
Dqhd = None # 每日活动
Rwjl = None # 每日奖励领取状态
Mrdcj = None # 每日点唱机



# 特征库
elements = {
    '邮件': ImageQuery().find().img('邮件.png').rect_half_left().confidence(0.85),
    '点唱机': ImageQuery().find().img('点唱机.png').rect_left_top().confidence(0.85),
        '读碟时间': OcrQuery().mlkitocr_v2().rect_right_top().pattern('读碟时间'),
        '专注嘉奖': OcrQuery().mlkitocr_v2().rect_right_top().pattern('专注嘉奖'),
        '一键领取': ImageQuery().find().img('一键领取.png').rect_right_bottom().confidence(0.85),
    '任务': ImageQuery().find().img('任务.png').rect_half_left().confidence(0.85),
        '每日活跃': OcrQuery().mlkitocr_v2().rect_right_top().pattern('每日活跃'),
        '全部领取': OcrQuery().mlkitocr_v2().rect_right_top().pattern('全部领取'),
        '领取': OcrQuery().mlkitocr_v2().rect_half_right().pattern('领取'),
        '每周活跃': OcrQuery().mlkitocr_v2().rect_right_top().pattern('每周活跃'),
        '获得物品': OcrQuery().mlkitocr_v2().rect_right_top().pattern('获得物品'),

    '入场': ImageQuery().find().img('入场.png').rect_half_right().confidence(0.85),
    '东区黎明': ImageQuery().find().img('东区黎明.png').rect_half_right().confidence(0.85),
        '圣火纪行': OcrQuery().mlkitocr_v2().rect_left_top().pattern('东区黎明'),
        '步入剧情': OcrQuery().mlkitocr_v2().rect_right_bottom().pattern('步入剧情'),
            '故事模式': OcrQuery().mlkitocr_v2().rect_left_top().pattern('故事模式'),
            '下一个': ImageQuery().find().img('下一个.png').rect_right_top().confidence(0.85),
            '上一个': ImageQuery().find().img('上一个.png').rect_right_top().confidence(0.85),
            f'{HD_Checkpoint}': OcrQuery().mlkitocr_v2().rect_left_bottom().pattern(f'{HD_Checkpoint}'),
            f'{UI_hd_mode}': OcrQuery().mlkitocr_v2().rect_right_top().pattern(f'{UI_hd_mode}'),
    '不朽荒原': ImageQuery().find().img('不朽荒原.png').rect_half_right().confidence(0.85),
        '好感': ImageQuery().find().img('好感.png').rect_half_left().confidence(0.75),
        '荒原资源': ImageQuery().find().img('资源.png').rect_half_left().confidence(0.75),
            '微尘': ImageQuery().find().img('微尘.png').confidence(0.75),
            '利齿': ImageQuery().find().img('利齿.png').confidence(0.75),
    '回主页': ImageQuery().find().img('回主页.png').rect_left_top().confidence(0.95),

    '资源': OcrQuery().mlkitocr_v2().rect_left_bottom().pattern('资源'),
        '意志解析': ImageQuery().find().img('意志解析.png').rect_half_bottom().confidence(0.9),
        '尘埃运动': ImageQuery().find().img('尘埃运动.png').rect_half_bottom().confidence(0.9),
        '铸币美学': ImageQuery().find().img('铸币美学.png').rect_half_bottom().confidence(0.9),
        '丰收时令': ImageQuery().find().img('丰收时令.png').rect_half_bottom().confidence(0.9),

    '心相观测': OcrQuery().mlkitocr_v2().pattern('心相观测'),
        f'{Checkpoint}': OcrQuery().mlkitocr_v2().rect_left_bottom().pattern(f'{Checkpoint}'),
       # '07': OcrQuery().mlkitocr_v2().rect_left_bottom().pattern('07'),
    '开始行动': ImageQuery().find().img('开始行动.png').rect_right_bottom().confidence(0.85),
        '记忆回合': ImageQuery().find().img('记忆回合.png').rect_right_bottom().confidence(0.85),
        '复现': OcrQuery().mlkitocr_v2().rect_right_bottom().pattern('复现'),
         # 传参方式不可行，不会变动
        '1': OcrQuery().mlkitocr_v2().rect_right_bottom().pattern('X1'),
        '2': OcrQuery().mlkitocr_v2().rect_right_bottom().pattern('X2'),
        '3': OcrQuery().mlkitocr_v2().rect_right_bottom().pattern('X3'),
        '4': OcrQuery().mlkitocr_v2().rect_right_bottom().pattern('X4'),
        # 此处对识别图片，需要通过颜色精准识别，所以不能直接使用find
        'X1': ImageQuery().find_template().img('X1.png').rect_right_bottom().confidence(0.95),
        'X2': ImageQuery().find_template().img('X2.png').rect_right_bottom().confidence(0.95),
        'X3': ImageQuery().find_template().img('X3.png').rect_right_bottom().confidence(0.95),
        'X4': ImageQuery().find_template().img('X4.png').rect_right_bottom().confidence(0.95),

    '战斗胜利': OcrQuery().mlkitocr_v2().rect_half_top().pattern('战斗胜利'),
    '战斗失败': OcrQuery().mlkitocr_v2().rect_half_top().pattern('战斗失败'),
    '补充体力': OcrQuery().mlkitocr_v2().rect_half_bottom().pattern('下次活性恢复'),


}
ld = LDFramework(elements)
ld.set_log_level(20)
# print(FindImages.find_template([R.img("test.png"),],confidence= 0.95))
# print(ld.find_element('test'))


