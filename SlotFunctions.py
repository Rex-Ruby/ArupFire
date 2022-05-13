from xlwt import Workbook
from os import remove, listdir
######################################################以下均为写入excel信息的槽函数########################################
def type_building_choice(index: 1):
    if index == 0:
        return ('建筑类型未选择，默认民用建筑')  # 默认为民用建筑
    elif index == 1:
        return ('民用建筑')
    elif index == 2:
        return ('工业建筑')


def write_into_excel(*s):
    # path = 'C:/Users/jing.ma/Desktop/DCM/dataForoutput'
    path = r'./'
    files_list = listdir(path)
    wb = Workbook(path)
    sht = wb.add_sheet('基本信息', cell_overwrite_ok=True)
    sht.write(0, 0, '建筑/项目名')
    sht.write(0, 1, '建筑类型')
    sht.write(0, 2, '建筑高度')
    str1 = []

    for i in s:
        str1.append(i)
    for j in range(len(str1)):
        sht.write(1, j, str1[j])

    # print(type(wb, str1[0]))
    print(str1)
    print(len(str1))
    # print(files_list)
    # search_key = re.compile(r".xls$", re.S)
    for file_name in files_list:
        print(file_name)
        if ".xls" in file_name:
            if not '.xlsx' in file_name:
                remove(file_name)                 ### 删除输入改变后生成的多余的excel文件，好像不支持自定义路径
    wb.save(str1[0] + '.xls')
######################################################以上均为写入excel信息的槽函数########################################

def transfer_tab(mTabWidget, mstackedWidget):     ###### 切换不同的项
    tabIndex = mTabWidget.currentIndex()
    if tabIndex == 3:
        mstackedWidget.show()
    elif tabIndex !=3:
        mstackedWidget.hide()
    pass

def judgeResult():
    pass





