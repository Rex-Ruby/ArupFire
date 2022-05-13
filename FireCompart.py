import xlrd
import StackedWidget

def get_fire_rank():
    path = r'/DCM/防火分区+疏散距离.xlsx'
    data = xlrd.open_workbook(path)
    sheet_fire_rank = data.sheets()[0]             ### 耐火等级的表单
    sheet_fire_compart = data.sheets()[1]          ### 防火分区的表单
    sheet_evac_dist = data.sheets()[2]             ### 疏散距离的表单

