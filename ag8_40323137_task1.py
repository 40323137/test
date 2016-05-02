# 各組分別在各自的 .py 程式中建立應用程式 (第1步/總共3步)
from flask import Blueprint, render_template

# 利用 Blueprint建立 ag1, 並且 url 前綴為 /ag1, 並設定 template 存放目錄
ag8_40323137a = Blueprint('ag8_40323137a', __name__, url_prefix='/ag8_40323137a', template_folder='templates')

# scrum1_task1 為完整可以單獨執行的繪圖程式
@ag8_40323137a.route('/task1')
def task1():
    outstring = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>網際 2D 繪圖</title>
    <!-- IE 9: display inline SVG -->
    <meta http-equiv="X-UA-Compatible" content="IE=9">
<script type="text/javascript" src="http://brython.info/src/brython_dist.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/Cango-8v03.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/Cango2D-6v13.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/CangoAxes-1v33.js"></script>

</head>
<body>

<script>
window.onload=function(){
brython(1);
}
</script>

<canvas id="plotarea" width="800" height="800"></canvas>

<script type="text/python">
from javascript import JSConstructor
from browser import window
import math

cango = JSConstructor(window.Cango)
cobj = JSConstructor(window.Cobj)
shapedefs = window.shapeDefs
obj2d = JSConstructor(window.Obj2D)
cgo = cango("plotarea")

cgo.setWorldCoords(-250, -250, 500, 500) 

# 決定要不要畫座標軸線
cgo.drawAxes(0, 240, 0, 240, {
    "strokeColor":"#aaaaaa",
    "fillColor": "#aaaaaa",
    "xTickInterval": 20,
    "xLabelInterval": 20,
    "yTickInterval": 20,
    "yLabelInterval": 20})
        
#cgo.drawText("使用 Cango 繪圖程式庫!", 0, 0, {"fontSize":60, "fontWeight": 1200, "lorg":5 })

deg = math.pi/180  
def O(x, y, rx, ry, rot, color, border, linewidth):
    # 旋轉必須要針對相對中心 rot not working yet
    chamber = "M -6.8397, -1.4894 \
                     A 7, 7, 0, 1, 0, 6.8397, -1.4894 \
                     A 40, 40, 0, 0, 1, 6.8397, -18.511 \
                     A 7, 7, 0, 1, 0, -6.8397, -18.511 \
                     A 40, 40, 0, 0, 1, -6.8397, -1.4894 z"
    cgoChamber = window.svgToCgoSVG(chamber)
    cmbr = cobj(cgoChamber, "SHAPE", {
            "fillColor": color,
            "border": border,
            "strokeColor": "tan",
            "lineWidth": linewidth })

    # 複製 cmbr, 然後命名為 basic1
    basic1 = cmbr.dup()
    # basic1 轉 120 度
    basic1.rotate(180)
    
    
    basic2 = cmbr.dup()
    basic2.rotate(-5)
    basic2.translate(2, 40)
    
    basic3 = basic2.dup()
    basic3.rotate(-15)
    basic3.translate(-3,21)
    
    basic4 = basic1.dup()
    basic4.rotate(-90)
    basic4.translate(0,0)
    
    basic5 = basic4.dup()
    basic5.translate(20,0)
    
    basic6 = basic4.dup()
    basic6.rotate(0)
    basic6.translate(10,59)
    
    basic7 = basic5.dup()
    basic7.rotate(90)
    basic7.translate(40, -40)
    
    basic8 = basic7.dup()
    basic8.rotate(0)
    basic8.translate(0,20)
    
    basic9 = cmbr.dup()
    basic9.rotate(5)
    basic9.translate(38, 40)
    
    basic10 = basic9.dup()
    basic10.rotate(15)
    basic10.translate(5, 10)
    
    basic11 = cmbr.dup()
    basic11.rotate(180)
    basic11.translate(0+60, 0)
    
    basic12 = cmbr.dup()
    basic12.rotate(-5)
    basic12.translate(2+60, 40)
    
    basic13 = basic2.dup()
    basic13.rotate(-15)
    basic13.translate(-3+60,21)
    
    basic14 = basic1.dup()
    basic14.rotate(-90)
    basic14.translate(0+60,0)
    
    basic15 = basic4.dup()
    basic15.translate(20+60,0)
    
    basic16 = basic4.dup()
    basic16.rotate(0)
    basic16.translate(10+60,59)
    
    basic17 = basic5.dup()
    basic17.rotate(90)
    basic17.translate(40+60, -40)
    
    basic18 = basic7.dup()
    basic18.rotate(0)
    basic18.translate(0+60,20)
    
    basic19 = cmbr.dup()
    basic19.rotate(5)
    basic19.translate(38+60, 40)
    
    basic20 = basic9.dup()
    basic20.rotate(15)
    basic20.translate(5+60, 10)
    
    basic21 = basic1.dup()
    basic21.rotate(180)
    basic21.translate(60, 0)
    
    basic22 = cmbr.dup()
    basic22.rotate(180)
    basic22.translate(0+60+60, 0)
    
    basic23 = cmbr.dup()
    basic23.rotate(-5)
    basic23.translate(2+60+60, 40)
    
    basic24 = basic2.dup()
    basic24.rotate(-15)
    basic24.translate(-3+60+60,21)
    
    basic25 = basic1.dup()
    basic25.rotate(-90)
    basic25.translate(0+60+60,0)
    
    basic26 = basic4.dup()
    basic26.translate(20+60+60,0)
    
    basic27 = basic4.dup()
    basic27.rotate(0)
    basic27.translate(10+60+60,59)
    
    basic28 = basic5.dup()
    basic28.rotate(90)
    basic28.translate(40+60+60, -40)
    
    basic29 = basic7.dup()
    basic29.rotate(0)
    basic29.translate(0+60+60,20)
    
    basic30 = cmbr.dup()
    basic30.rotate(5)
    basic30.translate(38+60+60, 40)
    
    basic31 = basic9.dup()
    basic31.rotate(15)
    basic31.translate(5+60+60, 10)
    
    basic32 = basic1.dup()
    basic32.rotate(180)
    basic32.translate(60+60, 0)
    
    basic33 = cmbr.dup()
    basic33.rotate(180)
    basic33.translate(0+60+60+60, 0)
    
    basic34 = cmbr.dup()
    basic34.rotate(-5)
    basic34.translate(2+60+60+60, 40)
    
    basic35 = basic2.dup()
    basic35.rotate(-15)
    basic35.translate(-3+60+60+60,21)
    
    basic36 = basic1.dup()
    basic36.rotate(-90)
    basic36.translate(0+60+60+60,0)
    
    basic37 = basic4.dup()
    basic37.translate(20+60+60+60,0)
    
    basic38 = basic4.dup()
    basic38.rotate(0)
    basic38.translate(10+60+60+60,59)
    
    basic39 = basic5.dup()
    basic39.rotate(90)
    basic39.translate(40+60+60+60, -40)
    
    basic40 = basic7.dup()
    basic40.rotate(0)
    basic40.translate(0+60+60+60,20)
    
    basic41 = cmbr.dup()
    basic41.rotate(5)
    basic41.translate(38+60+60+60, 40)
    
    basic42 = basic9.dup()
    basic42.rotate(15)
    basic42.translate(5+60+60+60, 10)
    
    basic43 = basic1.dup()
    basic43.rotate(180)
    basic43.translate(60+60+60, 0)
    
    cmbr.appendPath(basic1)
    cmbr.appendPath(basic2)
    cmbr.appendPath(basic3)
    cmbr.appendPath(basic4)
    cmbr.appendPath(basic5)
    cmbr.appendPath(basic6)
    cmbr.appendPath(basic7)
    cmbr.appendPath(basic8)
    cmbr.appendPath(basic9)
    cmbr.appendPath(basic10)
    cmbr.appendPath(basic11)
    cmbr.appendPath(basic12)
    cmbr.appendPath(basic13)
    cmbr.appendPath(basic14)
    cmbr.appendPath(basic15)
    cmbr.appendPath(basic16)
    cmbr.appendPath(basic17)
    cmbr.appendPath(basic18)
    cmbr.appendPath(basic19)
    cmbr.appendPath(basic20)    
    cmbr.appendPath(basic21)         
    cmbr.appendPath(basic22)
    cmbr.appendPath(basic23)
    cmbr.appendPath(basic24)
    cmbr.appendPath(basic25)
    cmbr.appendPath(basic26)
    cmbr.appendPath(basic27)
    cmbr.appendPath(basic28)
    cmbr.appendPath(basic29)
    cmbr.appendPath(basic30)
    cmbr.appendPath(basic31)
    cmbr.appendPath(basic32)
    cmbr.appendPath(basic33)    
    cmbr.appendPath(basic34)         
    cmbr.appendPath(basic35)
    cmbr.appendPath(basic36)
    cmbr.appendPath(basic37)
    cmbr.appendPath(basic38)
    cmbr.appendPath(basic39)
    cmbr.appendPath(basic40)
    cmbr.appendPath(basic41)
    cmbr.appendPath(basic42)
    cmbr.appendPath(basic43)     
    
    # hole 為原點位置
    hole = cobj(shapedefs.circle(4), "PATH")
    cmbr.appendPath(hole)

    # 表示放大 3 倍
    #cgo.render(cmbr, x, y, 3, rot)
    # 放大 5 倍
    cgo.render(cmbr, x, y, 1, rot)

O(0, 20, 0, 0, 0, "green", True, 4)
</script>

</body>
</html>
'''
    return outstring
    

    
    
