# gets co-ords of where mouse clicks on screen:
import turtle

def get_mouse_click_coord(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coord)
turtle.mainloop()
