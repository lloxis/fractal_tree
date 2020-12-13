import pygame
import time

class tree:
    def __init__(self, options, root):
        self.options = options
        self.last_win_update_time = 0
        self.root = root  # the tkinter window to keep updating while generating tree

    def draw(self, start_pos, win_surface):

        vec = pygame.math.Vector2((0, -self.options["trunk_length"]))
        self.last_win_update_time = time.time()

        # draw the additionnal tronk length
        pygame.draw.line(win_surface, self.options["tree_color"][0], start_pos, (start_pos[0], start_pos[1]-self.options["additional_trunk_length"]), self.options["trunk_thickness"])

        self.draw_branch(win_surface, (start_pos[0], start_pos[1] - self.options["additional_trunk_length"]), vec, self.options["trunk_thickness"])

    # this function will loop it self to generate all tree
    def draw_branch(self, win_surface, start_pos, vec, thickness):
        end_pos = start_pos+vec
        if int(thickness) < 1:
            thickness = 1
        pygame.draw.line(win_surface, self.options["tree_color"][0], start_pos, end_pos, int(thickness))
        if vec.length() / self.options["length_dividor"] < self.options["branch_min_size"]:
            return
        vec.scale_to_length(vec.length() / self.options["length_dividor"])
        for i in range(self.options["branches_nb"]):
            self.draw_branch(win_surface, end_pos, vec.rotate(self.options["semi_angle"]*(i//2+1)*(-1)**i), thickness/self.options["thickness_dividor"])

        # we update window every seconds while generating to avoid window not responding errors
        current_time = time.time()
        if (self.options["animate_generation"] and current_time - self.last_win_update_time > 1/50) or current_time - self.last_win_update_time > 0.5:
            pygame.display.flip()
            self.root.update()
            self.last_win_update_time = current_time
