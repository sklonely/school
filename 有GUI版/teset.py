import sys
import googlesheet
sys.path.append(sys.path[0] + '/mods/')  # 將自己mods的路徑加入倒python lib裡面


a = googlesheet.GoogleSheet()
a.init('test')
print(a.row_values(3))
