import pygame
from rotation import rotate_matrix
from configuration_matrices import cf_m1, cf_m2, cf_m3, cf_m4, cf_m5, cf_m6, cf_m7

pygame.init()

clock = pygame.time.Clock()

W = 600
H = 800
screen = pygame.display.set_mode((W, H))

# list of figure's configuration matrices
cf_m_list = [cf_m1, cf_m2, cf_m3, cf_m4, cf_m5, cf_m6, cf_m7]

# defining a font
my_font = pygame.font.SysFont('Arial', 22)


# displaying text or values of the variables on a screen
def draw_text(text, font, t_color, x_text, y_text):
    font_img = font.render(text, True, t_color)
    screen.blit(font_img, (x_text, y_text))


# put certain numbers in the figure shape (2 for showing the figure, 0 for erasing it, 1 when it stops)
def placing_numbers_in_block_coordinates(some_list, num):
    for indexes in some_list:
        tet_table[indexes[0]][indexes[1]] = num


# checking if there is a collision the figure with an obstacle on the next step
def figures_overlap(f_list1, f_list2):
    overlap_is_present = False
    # f_list1 is the figure, f_list2 is the next step figure
    for k in range (4):
        if (tet_table[f_list1[k][0]][f_list1[k][1]] == 2 and tet_table[f_list2[k][0]][f_list2[k][1]] == 1) or \
                (tet_table[f_list1[k][0]][f_list1[k][1]] == 1 and tet_table[f_list2[k][0]][f_list2[k][1]] == 2):
            overlap_is_present = True
            break
    return overlap_is_present


# returns the real time indexes list of a figure
def real_time_matrix(initial_matrix, some_i, some_j):
    real_time_m = [[x[0] + some_i, x[1] + some_j] for x in initial_matrix]
    return real_time_m


def horizontal_movement(m, stop, sign, some_list, some_config_mat, rotate, some_i, some_j):
    if m and not stop:
        # checking if there is no collision on the next step
        next_step_indexes_list = [[x[0], x[1] + sign * (-1)] for x in some_list]
        if not figures_overlap(some_list, next_step_indexes_list):
            # erasing previous figure
            placing_numbers_in_block_coordinates(real_time_matrix(
                rotate_matrix(some_config_mat, rotate), some_i, some_j), 0)
            some_j += sign * (-1)

    return some_j


# the number of blocks horizontally
nx_blocks = 10
# the number of blocks vertically
ny_blocks = 20
# filling the tetris table with zeros
tet_table = [[0 for col in range(nx_blocks + 2)] for row in range(ny_blocks + 1)]
# putting 1 at the edges of table, they will represent the walls
for i in range(ny_blocks + 1):
    tet_table[i][0] = 1
    tet_table[i][-1] = 1
for j in range(nx_blocks + 1):
    tet_table[ny_blocks][j] = 1

# variables that represent moving of the block
m_left = False
m_right = False
m_down = False
rotation = False


class Block():
    def __init__(self, matrix):
        self.config_matrix = matrix
        self.i = 0  # starting i position (row number)
        self.j = 5  # starting j position (column number)
        self.indexes_list = real_time_matrix(self.config_matrix, self.i, self.j)
        self.rot = 0
        self.stop = False
        self.current_ticks = 0

    def update(self):
        global tet_table, m_down, m_left, m_right, rotation

        m_down = True

        if rotation:
            # checking if there is no collision on the next step
            next_position = self.rot + 1
            if next_position == 4:
                next_position = 0
            next_step_indexes_list = real_time_matrix(rotate_matrix(self.config_matrix, next_position), self.i, self.j)

            if not figures_overlap(self.indexes_list, next_step_indexes_list):
                # erasing previous figure
                placing_numbers_in_block_coordinates(
                    real_time_matrix(rotate_matrix(self.config_matrix, self.rot), self.i, self.j), 0)
                self.rot += 1
                if self.rot == 4:
                    self.rot = 0

        self.j = horizontal_movement(m_left, self.stop, 1, self.indexes_list, self.config_matrix, self.rot, self.i,
                                     self.j)
        self.j = horizontal_movement(m_right, self.stop, -1, self.indexes_list, self.config_matrix, self.rot, self.i,
                                     self.j)

        if m_down and not self.stop:
            milliseconds = (pygame.time.get_ticks() - self.current_ticks)
            # number of seconds regulates the velocity of the figure
            if milliseconds > 1000:
                self.current_ticks = pygame.time.get_ticks()
                # checking if there is no collision on the next step
                next_step_indexes_list = [[x[0] + 1, x[1]] for x in self.indexes_list]
                if not figures_overlap(self.indexes_list, next_step_indexes_list):
                    # erasing previous figure
                    placing_numbers_in_block_coordinates(
                        real_time_matrix(rotate_matrix(self.config_matrix, self.rot), self.i, self.j), 0)
                    self.i += 1
                else:
                    self.stop = True

        self.indexes_list = real_time_matrix(rotate_matrix(self.config_matrix, self.rot), self.i, self.j)

        if not self.stop:
            placing_numbers_in_block_coordinates(self.indexes_list, 2)
        else:
            placing_numbers_in_block_coordinates(self.indexes_list, 1)


figure = Block(cf_m_list[1])
updating_figure_position = pygame.USEREVENT + 0
pygame.time.set_timer(updating_figure_position, 600)
start_ticks = pygame.time.get_ticks()  # starter tick

run = True

while run:

    clock.tick(10)

    screen.fill((0, 0, 40))

    # displaying a game field and a figure on a screen, elements of a matrix one by one
    for k in range(ny_blocks + 1):
        for m in range(nx_blocks + 2):
            draw_text(f"{tet_table[k][m]}", my_font, (0, 0, 110), 160 + m * 23, 100 + k * 25)
            if tet_table[k][m] == 2:
                draw_text(f"{tet_table[k][m]}", my_font, (128, 255, 0), 160 + m * 23, 100 + k * 25)
            elif tet_table[k][m] == 1:
                draw_text(f"{tet_table[k][m]}", my_font, (0, 120, 230), 160 + m * 23, 100 + k * 25)

    figure.update()

    # keys determination
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                m_down = True
            if event.key == pygame.K_LEFT:
                m_left = True
            if event.key == pygame.K_RIGHT:
                m_right = True
            if event.key == pygame.K_q:
                rotation = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                m_down = False
            if event.key == pygame.K_LEFT:
                m_left = False
            if event.key == pygame.K_RIGHT:
                m_right = False
            if event.key == pygame.K_q:
                rotation = False

    pygame.display.flip()
