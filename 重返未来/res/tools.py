import re
from .data import *

# 根据元素获取文字
def element_to_text(ele):
    return ld.ocr_mlkit_v2([ld.find_element(ele).rect.left,
                            ld.find_element(ele).rect.top,
                            ld.find_element(ele).rect.width,
                            ld.find_element(ele).rect.height])




# 获取复现次数
def get_again_num(ld):
    print('提取次数')
    # 方案1 ：识别不准确，弃用
    # if ld.element_exist('复现'):
    #     # 提取数字字符串
    #     result = re.findall(r'\d+', ld.ocr_mlkit_v2(
    #         # rect=[
    #         [
    #             ld.find_element('复现').rect.left - 450,
    #             ld.find_element('复现').rect.top,
    #             ld.find_element('复现').rect.width - 508,
    #             ld.find_element('复现').rect.height
    #         ]
    #     ))
    #
    #     # 确保 result 不为空
    #     if result:
    #         return int(result[0])  # 返回第一个匹配的数字
    #     else:
    #         return 0  # 或者返回一个默认值，比如 0

    # 方案二：通过图片识别
    if ld.element_exist('X1'):
        return 1
    elif ld.element_exist('X2'):
        return 2
    elif ld.element_exist('X3'):
        return 3
    elif ld.element_exist('X4'):
        return 4
    return 0  # 或者返回一个默认值，比如 0



# 处理传参
def num_to_object(num):
    if num =='1':
        return "Xl▲"
    elif num == '2':
        return "X2▲"
    elif num =='3':
        return "X3▲"
    elif num =='4':
        return "X4▲"
    else:
        return "参数异常"

