import copy

from tkinter import *
import tkinter.colorchooser
import tkinter.filedialog
import tkinter.simpledialog

from tree import *
import json_data_file_manager

# the default tree parameters to be copied in tree_params.json at init or if there's an error
default_tree_params = {
    "regenerate_tree": True,
    "branches_nb": 2,
    "trunk_length": 200,
    "additional_trunk_length": 0,
    "length_dividor": 1.4,
    "branch_min_size": 5,
    "semi_angle": 25,
    "trunk_thickness": 20,
    "thickness_dividor": 1.28,
    "tree_color": ((255, 255, 255), "#ffffff"),
    "background_color": ((0, 0, 0), "#000000"),
    "animate_generation": False
}
tree_json_manager = json_data_file_manager.manager("tree_params.json", default_tree_params)

# the default windows parameters to be copied in win_params.json at init or if there's an error
default_win_params = {
    "width": 800,
    "height": 1000
}
win_json_manager = json_data_file_manager.manager("win_params.json", default_win_params)

# *** init pygame window and surface ***
pygame.init()
pygame.display.set_caption("Fractal tree render")
# create window with the resolution from win_params.json
win_size = win_width, win_height = win_json_manager.datas["height"], win_json_manager.datas["width"]
win_surface = pygame.display.set_mode(win_size, pygame.RESIZABLE)

# **** define window ****
root = Tk()
root.title("Fractal tree control panel")
root.geometry("290x700+100+100")
root.resizable(False, False)

main_frame = Frame(root)
main_frame.pack()

# create a tree with the params from tree_params.json
fractal_tree1 = tree(tree_json_manager.datas, root)

def draw_tree():
    """
    draw the tree on the screen
    and continue to update windows while generating
    :return:
    """
    print("generating tree...")
    fractal_tree1.draw((win_size[0] / 2, win_size[1]), win_surface)
    print("tree generated")

    pygame.display.flip()

tree_options_changed = True

def generate_tree():
    global tree_options_changed

    if not tree_options_changed:
        return

    # update all tree options
    tree_json_manager.datas["regenerate_tree"] = regenerate_tree_button_value.get()
    tree_json_manager.datas["branches_nb"] = branches_nb_scale.get()
    tree_json_manager.datas["trunk_length"] = trunk_length_scale.get()
    tree_json_manager.datas["additional_trunk_length"] = additional_trunk_length_scale.get()
    tree_json_manager.datas["length_dividor"] = length_dividor_scale.get()
    tree_json_manager.datas["branch_min_size"] = branch_min_size_scale.get()
    tree_json_manager.datas["semi_angle"] = semi_angle_scale.get()
    tree_json_manager.datas["trunk_thickness"] = trunk_thickness_scale.get()
    tree_json_manager.datas["thickness_dividor"] = thickness_dividor_scale.get()
    tree_json_manager.datas["animate_generation"] = animate_generation_button_value.get()

    fractal_tree1.params = tree_json_manager.datas

    win_surface.fill(tree_json_manager.datas["background_color"][0])
    draw_tree()

    tree_options_changed = False

# we don't regenerate the tree each time we move a slider to avoid lag
def tree_options_change(event_=None):
    global tree_options_changed
    tree_options_changed = True


regenerate_tree_button_value = IntVar(value=tree_json_manager.datas["regenerate_tree"])
regenerate_tree_button = Checkbutton(main_frame, text='Regenerate tree when a parameter is changed', variable=regenerate_tree_button_value, command=generate_tree)
regenerate_tree_button.pack(pady=2)

branches_nb_scale = Scale(main_frame, orient='horizontal', command=tree_options_change, from_=1, to=10, resolution=1, length=260, label='Branches Number')
branches_nb_scale.set(tree_json_manager.datas["branches_nb"])
branches_nb_scale.pack(pady=2)

trunk_length_scale = Scale(main_frame, orient='horizontal', command=tree_options_change, from_=1, to=500, resolution=1, length=260, label='Trunk Length')
trunk_length_scale.set(tree_json_manager.datas["trunk_length"])
trunk_length_scale.pack(pady=2)

additional_trunk_length_scale = Scale(main_frame, orient='horizontal', command=tree_options_change, from_=0, to=500, resolution=1, length=260, label='Additional trunk length')
additional_trunk_length_scale.set(tree_json_manager.datas["additional_trunk_length"])
additional_trunk_length_scale.pack(pady=2)

length_dividor_scale = Scale(main_frame, orient='horizontal', command=tree_options_change, from_=1.2, to=2.5, resolution=0.01, length=260, label='Length dividor')
length_dividor_scale.set(tree_json_manager.datas["length_dividor"])
length_dividor_scale.pack(pady=2)

branch_min_size_scale = Scale(main_frame, orient='horizontal', command=tree_options_change, from_=2, to=100, resolution=1, length=260, label='Branches min size')
branch_min_size_scale.set(tree_json_manager.datas["branch_min_size"])
branch_min_size_scale.pack(pady=2)

semi_angle_scale = Scale(main_frame, orient='horizontal', command=tree_options_change, from_=1, to=360, resolution=1, length=260, label='Semi angle scale')
semi_angle_scale.set(tree_json_manager.datas["semi_angle"])
semi_angle_scale.pack(pady=2)

trunk_thickness_scale = Scale(main_frame, orient='horizontal', command=tree_options_change, from_=1, to=40, resolution=1, length=260, label='Trunck thickness scale')
trunk_thickness_scale.set(tree_json_manager.datas["trunk_thickness"])
trunk_thickness_scale.pack(pady=2)

thickness_dividor_scale = Scale(main_frame, orient='horizontal', command=tree_options_change, from_=1.2, to=2.5, resolution=0.01, length=260, label='Thickness Dividor')
thickness_dividor_scale.set(tree_json_manager.datas["thickness_dividor"])
thickness_dividor_scale.pack(pady=2)

animate_generation_button_value = IntVar(value=tree_json_manager.datas["animate_generation"])
animate_generation_button = Checkbutton(main_frame, text='Animated generation', variable=animate_generation_button_value)
animate_generation_button.pack(pady=2)

def change_tree_color():
    tree_color = tkinter.colorchooser.askcolor(fractal_tree1.params["tree_color"][1])

    # if we clicked on "annuler"
    if tree_color==(None, None):
        return

    tree_json_manager.datas["tree_color"] = tree_color
    fractal_tree1.params["tree_color"] = tree_color
    generate_tree()
tree_color_button = Button(main_frame, text="Change tree color", command=change_tree_color)
tree_color_button.pack()

def change_background_color():
    background_color = tkinter.colorchooser.askcolor(tree_json_manager.datas["background_color"][1])

    # if we clicked on "annuler"
    if background_color==(None, None):
        return

    tree_json_manager.datas["background_color"] = background_color
    generate_tree()
background_color_button = Button(main_frame, text="Change background color", command=change_background_color)
background_color_button.pack()

generate_button = Button(main_frame, text="Generate tree", font=('Times', -20, 'bold'), command=generate_tree)
generate_button.pack()

def save_image():
    file_path = tkinter.filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("png image", '.png')])
    if not file_path[-4:] == ".png":
        file_path = file_path + ".png"
    pygame.image.save(win_surface, file_path)
save_button = Button(main_frame, text="Save tree as png", command=save_image)
save_button.pack()

def reset_params():
    # deep copy to really copy default_tree_params dict and not overright it
    tree_json_manager.datas = copy.deepcopy(default_tree_params)
    fractal_tree1.params = tree_json_manager.datas

    regenerate_tree_button_value.set(default_tree_params["regenerate_tree"])
    branches_nb_scale.set(default_tree_params["branches_nb"])
    trunk_length_scale.set(default_tree_params["trunk_length"])
    additional_trunk_length_scale.set(default_tree_params["additional_trunk_length"])
    length_dividor_scale.set(default_tree_params["length_dividor"])
    branch_min_size_scale.set(default_tree_params["branch_min_size"])
    semi_angle_scale.set(default_tree_params["semi_angle"])
    trunk_thickness_scale.set(default_tree_params["trunk_thickness"])
    thickness_dividor_scale.set(default_tree_params["thickness_dividor"])
    animate_generation_button_value.set(default_tree_params["animate_generation"])
    root.update()

    win_surface.fill(tree_json_manager.datas["background_color"][0])
    draw_tree()
reset_params_button = Button(main_frame, text="Reset parameters", fg="red", command=reset_params)
reset_params_button.pack()


root.update()

# handle tk window distroyed
tk_win_destroyed = False
def destroy():
    global run
    global tk_win_destroyed
    # save datas before closing
    tree_json_manager.write_datas()

    tk_win_destroyed = True
    root.destroy()
    run = False  # to close pygame win when tk win is closed
root.protocol("WM_DELETE_WINDOW", destroy)

run = True
while run:
    # *** EVENTS ***
    for event in pygame.event.get():
        event_type = event.type

        # end the loop if the game is closed
        if event_type == pygame.QUIT:
            # save datas before closing
            tree_json_manager.write_datas()
            run = False

        # this envent is trigered when lauching code and so draw the tree when code is lauched
        elif event_type == pygame.VIDEORESIZE:
            win_size = win_width, win_height = event.w, event.h
            win_surface = pygame.display.set_mode(win_size, pygame.RESIZABLE)
            win_surface.fill(fractal_tree1.params["background_color"][0])
            draw_tree()

            # we put back the tkinter param window
            root.lift()

    generate_tree()

    # if tk window not destroyed, keep updating it
    if not tk_win_destroyed:
        try:
            root.update()
        except:
            pass

    # wait a little to do not update to clickly
    time.sleep(1/100)