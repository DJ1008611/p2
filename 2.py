import turtle

# 设置画布和画笔
canvas = turtle.Screen()
pen = turtle.Turtle()

# 绘制花瓣
def draw_petal():
    pen.circle(50, 70)
    pen.left(110)
    pen.circle(50, 70)

# 绘制花蕊
def draw_core():
    pen.color("red")
    pen.begin_fill()
    pen.circle(30)
    pen.end_fill()

# 绘制花朵
def draw_flower():
    pen.color("pink")
    pen.begin_fill()
    for i in range(8):
        draw_petal()
    pen.end_fill()
    draw_core()

# 移动画笔到画布中央
pen.penup()
pen.goto(0, -150)
pen.pendown()

# 绘制花朵
draw_flower()

# 隐藏画笔
pen.hideturtle()

# 关闭画布
canvas.exitonclick()