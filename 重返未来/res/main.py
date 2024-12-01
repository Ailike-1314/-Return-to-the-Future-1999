from .data import *
from .tools import *
from ascript.android.system import KeyValue

def UI(list):
    print('获取UI设置')
    global Zyhg
    global Rwjl
    global Mrdcj
    global Mrxx
    global Dqhd

    global Checkpoint
    global UI_xxgc_num
    global UI_again_num

    global HD_Checkpoint
    global UI_hd_mode
    global UI_hd_num
    global UI_hd_again_num
    ###########################
    ## 初始化
    ###########################
    Checkpoint = json.loads(KeyValue.get('ui', ''))['UI_Checkpoint']  # 选择关卡
    UI_xxgc_num = int(json.loads(KeyValue.get('ui', ''))['UI_UI_xxgc_num'])  # UI获取的心相观测
    UI_again_num = int(json.loads(KeyValue.get('ui', ''))['UI_UI_again_num'])  # 重复挑战关卡的次数

    # 活动关卡次数
    HD_Checkpoint = json.loads(KeyValue.get('ui', ''))['UI_HD_Checkpoint']  # 选择活动关卡
    UI_hd_num = int(json.loads(KeyValue.get('ui', ''))['UI_UI_hd_num'])
    UI_hd_again_num = int(json.loads(KeyValue.get('ui', ''))['UI_UI_hd_again_num'])
    UI_hd_mode = json.loads(KeyValue.get('ui', ''))['UI_UI_hd_mode']  # 故事、意外、艰难

    Zyhg = not json.loads(KeyValue.get('ui', ''))['UI_Zyhg']  # 每日资源好感领取
    Mrxx = not json.loads(KeyValue.get('ui', ''))['UI_Mrxx']  # 每日心相初始化
    Dqhd = not json.loads(KeyValue.get('ui', ''))['UI_Dqhd']  # 每日活动
    Rwjl = not json.loads(KeyValue.get('ui', ''))['UI_Rwjl']  # 每日奖励领取状态
    Mrdcj = not json.loads(KeyValue.get('ui', ''))['UI_Mrdcj']  # 每日点唱机
    return "Mrrw"

# 每日任务
def Mrrw(list):
    # 页面
    global Page
    # 状态
    global Mrxx
    global Zyhg
    global Rwjl
    global Dqhd
    global Mrdcj

    print(Page)


    #######################################
    ####### 第一次运行判断是否是主页面 #########
    #######################################

    if  list['is_main_page']== 0:
        if ld.element_exist('邮件') :
            Page='main'
            list['is_main_page'] = 1
        elif ld.element_exist('回主页') :
            ld.element('回主页').click_element(3).ramdom_sleep(5).execute()
            Page = 'main'
            list['is_main_page'] = 1
        else:
            # 弹出一个信息提示框,并更改确认按钮为知道了
            Dialog.alert('请返回主页面后再运行脚本哦~[不要遮挡邮箱]', '知道了')
            ld.ramdom_sleep(1)
            system.exit()


    #######################################
    #######        主程序          #########
    #######################################

    ### 判断是否是主界面 #####
    print('Mrxx:'+str(Mrxx))
    print('Zyhg:'+str(Zyhg))
    print('Rwjl:'+str(Rwjl))
    print('Dqhd:'+str(Dqhd))
    print('Mrdcj:' + str(Mrdcj))
    if Page == 'main':
        if Zyhg == False:
            ld.element('不朽荒原').click_element(3).ramdom_sleep(10).execute()
            Page = '不朽荒原页面'
            return "Mrzy"
        elif Mrxx == False:
            ld.element('入场').click_element(3).ramdom_sleep(3).execute()
            Page = '故事页面'
        elif Dqhd == False:
            ld.element('东区黎明').click_element(3).ramdom_sleep(5).execute()
            Page = '活动页面'
            return "Mrhd"
        elif Rwjl == False:
            ld.element('任务').click_element(3).ramdom_sleep(3).execute()
            Page = '任务页面'
            return "Mrjl"
        elif Mrdcj == False:
            ld.element('点唱机').click_element(3).ramdom_sleep(3).execute()
            Page = '点唱机页面'
            return "Dcj"
        else :
            ld.ramdom_sleep(2)
            Dialog.toast('今日任务结束啦~')
            #Dialog.alert('任务结束啦~', '知道了')
            system.exit()
            # 根据包名启动,推荐使用
            # system.close("com.shenlan.m.reverse1999")

    ################### 每日心相 ###################
    elif Page == '故事页面':
        if ld.element_exist('资源'):
            ld.element('资源').click_element(3).ramdom_sleep(3).execute()
            Page = '资源页面'
    elif Page == '资源页面':
        if ld.element_exist('意志解析'):
            ld.element('意志解析').click_element(3).ramdom_sleep(3).execute()
            Page = '心相观测页面'
        else:
            # 划动页面寻找关卡
            ld.swipe(['70%', '50%'], ['40%', '50%'])
    elif Page == '心相观测页面':
        #print(f'{Checkpoint}')
        #print(ld.element_exist(f'{Checkpoint}'))
        if ld.element_exist(f'{Checkpoint}'):
            ld.element(f'{Checkpoint}').click_element(3).ramdom_sleep(3).execute()
            Page = '开始行动页面'
            return 'Ksxd'
        else:
            # 划动页面寻找关卡
            ld.swipe(['40%', '80%'], ['70%', '80%'])
    ################### 每日心相 ###################

    else :
        list['is_main_page']=0
    return "Mrrw"

# 每日心相任务
def Ksxd(list):

    #######################################
    ####### 第一次运行判断是否是开始行动页面 ####
    #######################################
    global Page
    global UI_again_num
    global UI_xxgc_num
    global Mrxx
    global Dqhd
    print(Page)


    #######################################
    ######    判断是否正确页面      ##########
    #######################################
    if list['is_start_page'] == 0:
        if ld.element_exist('开始行动'):
            Page = '开始行动页面'
            list['is_start_page'] = 1
        else:
            return "Mrrw"


    #######################################
    ######           主逻辑       ##########
    #######################################
    if Page == '开始行动页面':
        if (not ld.element_exist('下一个') and not ld.element_exist('上一个')) or (ld.element_exist(f'{UI_hd_mode}')):
            ld.element('开始行动').click_element(3).ramdom_sleep(1).execute()
            Page = '行动子页面'
        elif not ld.element_exist(f'{UI_hd_mode}') and ld.element_exist('下一个'):
            ld.element('下一个').click_element(1).ramdom_sleep(1).execute()
        elif not ld.element_exist(f'{UI_hd_mode}') and ld.element_exist('上一个'):
            ld.element('上一个').click_element(1).ramdom_sleep(1).execute()


    elif Page == '行动子页面':
        if ld.element_exist('记忆回合'):
            ld.element('记忆回合').click_element(3).ramdom_sleep(1).execute()
            Page = '复现页面'
        else:
            Page = '复现页面'
    elif Page == '复现页面':
        print('UI_xxgc_num:'+str(UI_xxgc_num))
        # print(ld.find_element('复现').rect.__dict__)
        print('get_again_num:'+str(get_again_num(ld)))
        print(get_again_num(ld) == UI_xxgc_num)
        if get_again_num(ld) == UI_xxgc_num:
            print('点击复现')
            if UI_again_num>0:
                ld.element('复现').click_element(3).ramdom_sleep(5).execute()
                UI_again_num = UI_again_num-1
                Page = '战斗中'
            else :
                print('当前任务完成，返回Mrrw')
                if Mrxx==True and Dqhd == False:
                    Dqhd = True
                elif Dqhd == True and Mrxx == False:
                    Mrxx = True
                elif Mrxx==False and Dqhd == False:
                    Mrxx = True
                return 'Mrrw'
        else :
            # 选择重复次数
            if ld.element_exist(f'{UI_xxgc_num}') :
                print('选择复现次数')
                ld.element(f'{UI_xxgc_num}').click_element(1).execute()
            elif ld.element_exist('X1'):
                ld.element('X1').click_element(1).execute()
            elif ld.element_exist('X2'):
                ld.element('X2').click_element(1).execute()
            elif ld.element_exist('X3'):
                ld.element('X3').click_element(1).execute()
            elif ld.element_exist('X4'):
                ld.element('X4').click_element(1).execute()

    elif Page == "战斗中" :
        #print(ld.find_element('补充体力').rect.__dict__)
        if ld.element_exist('补充体力'):
            print('补充体力')
            ld.ramdom_sleep(3)
            UI_again_num = 0
            # 调整任务状态
            if Mrxx == True and Dqhd == False:
                Dqhd = True
            elif Dqhd == True and Mrxx == False:
                Mrxx = True
            elif Mrxx == False and Dqhd == False:
                Mrxx = True

            ld.click('90%', '90%', 5)
            ld.ramdom_sleep(5)
            return 'Mrrw'

        elif ld.element_exist('战斗胜利'):
            ld.ramdom_sleep(3)
            ld.click('85%', '10%', 3)
            Page ='复现页面'
            ld.ramdom_sleep(5)
        elif ld.element_exist('战斗失败'):
            print('战斗失败')
            UI_again_num = 0
            Mrxx = True
            ld.ramdom_sleep(3)
            ld.click('85%', '10%', 3)
            ld.ramdom_sleep(5)
            return 'Mrrw'
        else :
            ld.ramdom_sleep(5)
            #ld.click('85%', '10%', 3)

    return "Ksxd"

# 每日资源
def Mrzy(list):
    global Page
    global Zyhg
    print(Page)

    print(list['cw_is_click'])
    print(list['lc_is_click'])
    print(list['hg_is_click'])

    # print(list['cw_is_click'] == 1)
    # print(list['lc_is_click'] == 1)
    # print(list['hg_is_click'] == 1)
    if Page == '不朽荒原页面':
        if ld.element_exist('荒原资源'):
            ld.element('荒原资源').click_element(1).ramdom_sleep(2).execute()
            Page = '微尘利齿页面'
        elif ld.element_exist('好感'):
            ld.element('好感').click_element(1).ramdom_sleep(2).execute()
            # Page = '好感页面'
        else :
            Zyhg = True
            return "Mrrw"

    elif Page == '微尘利齿页面':
        if ld.element_exist('微尘') and list['cw_is_click']==0:
            ld.element('微尘').click_element(1).ramdom_sleep(2).execute()
            list['cw_is_click'] = 1
        elif ld.element_exist('利齿') and list['lc_is_click']==0:
            ld.element('利齿').click_element(1).ramdom_sleep(2).execute()
            list['lc_is_click'] = 1
        elif list['cw_is_click'] == 1 and list['lc_is_click'] == 1 :
            Page = '不朽荒原页面'

    # elif list['cw_is_click'] == 1 and list['lc_is_click'] == 1 and list['hg_is_click'] == 1:

    return "Mrzy"


# 每日奖励
def Mrjl(list):
    global Page
    global Rwjl
    print(Page)

    ##############################################
    ########## 检查是否跳转任务页面         ##########
    ##############################################
    if list['is_rw_page'] == 0:
        if ld.element_exist('每日活跃'):
            list['is_rw_page'] = 1
        else:
            return "Mrrw"


    ##############################################
    ##########            主逻辑         ##########
    ##############################################
    if Page == '任务页面':
        if ld.element_exist('每日活跃') and list['mrhy_click']==0:
            # 每日活跃奖励 -- 全部领取
            ld.element('每日活跃').click_element(1).ramdom_sleep(1).execute()
            Page = '每日活跃页面'
            if ld.element_exist('领取'):
                pass
            else:
                list['mrhy_click'] = 1
        elif ld.element_exist('每周活跃') and list['mzhy_click']==0:
            # 每周活跃奖励 -- 全部领取
            ld.element('每周活跃').click_element(1).ramdom_sleep(1).execute()
            Page = '每周活跃页面'
            if ld.element_exist('领取'):
                pass
            else:
                list['mzhy_click'] = 1

        elif list['mzhy_click']==1 and list['mrhy_click']==1:
            Rwjl = True
            return "Mrrw"

    elif Page == '每日活跃页面':
        print(not ld.element_exist('每日活跃'))
        if ld.element_exist('全部领取'):
            ld.element('全部领取').click_element(1).ramdom_sleep(1).execute()
        elif ld.element_exist('领取'):
            ld.element('领取').click_element(1).ramdom_sleep(1).execute()
        elif ld.element_exist('获得物品'):
            ld.element('获得物品').click_element(1).ramdom_sleep(1).execute()
            list['mrhy_click'] = 1
            Page = '任务页面'
        # elif not ld.element_exist('每日活跃') :
        #     ld.click('90%', '10%', 5)
        #     list['mrhy_click'] = 1
        #     Page = '任务页面'
        elif not ld.element_exist('领取') :
            ld.click('90%', '10%', 5)
            list['mrhy_click'] = 1
            Page = '任务页面'


    elif Page == '每周活跃页面':
        if ld.element_exist('全部领取'):
            ld.element('全部领取').click_element(1).ramdom_sleep(1).execute()
        elif ld.element_exist('领取'):
            ld.element('领取').click_element(1).ramdom_sleep(1).execute()
        elif ld.element_exist('获得物品'):
            ld.element('获得物品').click_element(1).ramdom_sleep(1).execute()
            list['mzhy_click'] = 1
            Page = '任务页面'
        # elif not ld.element_exist('每周活跃') :
        #     ld.click('90%', '10%', 5)
        #     list['mzhy_click'] = 1
        #     Page = '任务页面'
        elif not ld.element_exist('领取') :
            ld.click('90%', '10%', 5)
            list['mzhy_click'] = 1
            Page = '任务页面'

    return "Mrjl"


# 每日活动
def Mrhd(list):
    print('每日当期活动')

    global Page
    global Dqhd

    global UI_again_num
    global UI_xxgc_num

    global UI_hd_num
    global UI_hd_again_num

    print(Page)

    ##############################################
    ##########    检查是否跳转页面         ##########
    ##############################################
    if list['is_hd_page'] == 0:
        if ld.element_exist('圣火纪行'):
            list['is_hd_page'] = 1
        else:
            return "Mrrw"

    ##############################################
    ##########           主逻辑          ##########
    ##############################################
    if Page== '活动页面':
        if ld.element_exist('圣火纪行'):
            ld.element('圣火纪行').click_element(1).ramdom_sleep(1).execute()
            Page = '圣火纪行页面'
    elif Page == '圣火纪行页面':
        if ld.element_exist('步入剧情'):
            ld.element('步入剧情').click_element(1).ramdom_sleep(1).execute()
            Page = '步入剧情页面'
    elif Page == '步入剧情页面':
        if ld.element_exist('故事模式'):
            ld.element('故事模式').click_element(1).ramdom_sleep(1).execute()
            Page = '故事模式页面'
    elif Page == '故事模式页面':
        if ld.element_exist(f'{HD_Checkpoint}'):
            ld.element(f'{HD_Checkpoint}').click_element(3).ramdom_sleep(3).execute()
            Page = '开始行动页面'

            UI_again_num = UI_hd_again_num
            UI_xxgc_num = UI_hd_num
            return 'Ksxd'
        else:
            # 划动页面寻找关卡
            ld.swipe(['40%', '80%'], ['70%', '80%'])



    return "Mrhd"


# 每日点唱机
def Dcj(list):
    global Page
    global Mrdcj
    print(Page)

    ##############################################
    ########## 检查是否跳转任务页面         ##########
    ##############################################
    if list['is_dcj_page'] == 0:
        if ld.element_exist('读碟时间'):
            list['is_dcj_page'] = 1
        else:
            return "Mrrw"

    ##############################################
    ##########            主逻辑         ##########
    ##############################################
    if Page == "点唱机页面":
        if ld.element_exist('读碟时间'):
            ld.element('读碟时间').click_element(1).ramdom_sleep(1).execute()
            Page = "读碟页面"
    elif Page == "读碟页面" :
        if ld.element_exist('一键领取'):
            ld.element('一键领取').click_element(1).ramdom_sleep(1).execute()
            Page = '专注嘉奖页面'
        else:
            Page = '专注嘉奖页面'
    elif Page == "专注嘉奖页面":
        ld.element('专注嘉奖').click_element(1).ramdom_sleep(2).execute()
        if ld.element_exist('一键领取'):
            ld.element('一键领取').click_element(1).ramdom_sleep(3).execute()
            ld.click('90%', '80%', 5)
        Mrdcj = True
        return "Mrrw"

    return "Dcj"


fsm_state_dict["Mrrw"]=Mrrw   # 每日任务核心代码
fsm_state_dict["Ksxd"]=Ksxd   # 刷关卡核心代码
fsm_state_dict["Mrzy"]=Mrzy   # 每日资源
fsm_state_dict["Mrjl"]=Mrjl   # 每日奖励
fsm_state_dict["Mrhd"]=Mrhd   # 每日活动
fsm_state_dict["Dcj"]=Dcj   # 每日点唱机
fsm_state_dict["UI"]=UI

