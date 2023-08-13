import game_of_life_interface
import numpy as np
import matplotlib.pyplot as plt


class GameOfLife(game_of_life_interface.GameOfLife):  # This is the way you construct a class that inherits properties
    def __init__(self, size_of_board, board_start_mode, rules, rle, pattern_position):
        self.size_of_board = size_of_board
        self.board_start_mode = board_start_mode
        self.rules = rules
        self.rle = rle
        self.pattern_position = pattern_position
        self.board = 0
        if self.rle != '':
            self.board = self.transform_rle_to_matrix(self)
        else:
            if board_start_mode == 2:
                self.board = np.random.choice([0, 255], self.size_of_board * self.size_of_board, p=[0.2, 0.8]).reshape(
                    self.size_of_board, self.size_of_board)
            elif board_start_mode == 3:
                self.board = np.random.choice([0, 255], self.size_of_board * self.size_of_board, p=[0.8, 0.2]).reshape(
                    self.size_of_board, self.size_of_board)
            elif board_start_mode == 4:
                self.board = np.zeros((self.size_of_board, self.size_of_board))
                self.board[14, 11] = 255
                self.board[15, 11] = 255
                self.board[14, 10] = 255
                self.board[15, 10] = 255
                self.board[14, 20] = 255
                self.board[15, 20] = 255
                self.board[16, 20] = 255
                self.board[13, 21] = 255
                self.board[17, 21] = 255
                self.board[12, 22] = 255
                self.board[18, 22] = 255
                self.board[12, 23] = 255
                self.board[18, 23] = 255
                self.board[15, 24] = 255
                self.board[13, 25] = 255
                self.board[17, 25] = 255
                self.board[14:17, 26] = 255
                self.board[15, 27] = 255
                self.board[12:15, 30] = 255
                self.board[12:15, 31] = 255
                self.board[11, 32] = 255
                self.board[15, 32] = 255
                self.board[10:12, 34] = 255
                self.board[15:17, 34] = 255
                self.board[12:14, 44] = 255
                self.board[12:14, 45] = 255
            else:
                self.board_start_mode = 1
                self.board = np.random.choice([0, 255], self.size_of_board * self.size_of_board, p=[0.5, 0.5]).reshape(
                    self.size_of_board, self.size_of_board)
        self.list2 = []
        self.list3 = []
        self.list1 = list(self.rules)
        n = 0
        for i in self.list1:
            if i == 's' or i == 'S':
                break
            else:
                n += 1
                if i.isdigit():
                    self.list2.append(int(i))
        n += 1
        while n <= (len(self.rules) - 1):
            self.list3.append(int(self.rules[n]))
            n += 1

    def update(self):
        # self.copy_board = self.board.copy()
        copy_board = np.zeros((self.size_of_board, self.size_of_board))
        for row in range(self.size_of_board):
            for col in range(self.size_of_board):
                number = int((self.board[row, (col - 1) % self.size_of_board] + self.board[
                    row, (col + 1) % self.size_of_board] + self.board[(row - 1) % self.size_of_board, col] + self.board[
                                  (row + 1) % self.size_of_board, col] + self.board[
                                  (row - 1) % self.size_of_board, (col - 1) % self.size_of_board] + self.board[
                                  (row - 1) % self.size_of_board, (col + 1) % self.size_of_board] + self.board[
                                  (row + 1) % self.size_of_board, (col - 1) % self.size_of_board] + self.board[
                                  (row + 1) % self.size_of_board, (col + 1) % self.size_of_board]) / 255)
                if self.board[row, col] == 0:
                    if number in self.list2:
                        copy_board[row, col] = int(255)
                else:
                    if number in self.list3:
                        copy_board[row, col] = int(255)
        self.board = copy_board.astype(int)

    def save_board_to_file(self, file_name):
        plt.imsave(file_name, self.board)

    def display_board(self):
        plt.matshow(self.board)
        plt.show()

    def return_board(self):
        # list10 = []
        # list20 = []
        # r = self.size_of_board
        # c = self.size_of_board
        # for row in range(r-1):
        #     for col in range(c-1):
        #         list20.append(self[row , col])
        #     list10.append(list20)
        #     list20 = []
        # return (list10)
        return self.board.tolist()

    def transform_rle_to_matrix(self, rle):
        self.board = np.zeros((self.size_of_board, self.size_of_board))
        x = self.pattern_position[0]
        y = self.pattern_position[1]
        num = ''
        list_2 = []
        for i in range(len(self.rle)):
            if self.rle[i].isdigit():
                num = num + self.rle[i]
                continue
            elif num != '':
                for n in range(0, int(num)):
                    if self.rle[i] == 'o':
                        list_2.append(255)
                    elif self.rle[i] == 'b':
                        list_2.append(0)
                    elif self.rle[i] == '$':
                        list_2.append('$')
                    elif self.rle[i] == '!':
                        pass
            elif num == '':
                if self.rle[i] == 'o':
                    list_2.append(255)
                elif self.rle[i] == 'b':
                    list_2.append(0)
                elif self.rle[i] == '$':
                    list_2.append('$')
                elif self.rle[i] == '!':
                    pass
            num = ''
        d = 0

        for d in range(len(list_2)):
            if list_2[d] == '$':
                x += 1
                y = self.pattern_position[1]
            else:
                self.board[x][y] = list_2[d]
                y += 1

        return self.board


if __name__ == '__main__':  # You should keep this line for our auto-grading code.
    print('write your tests here')  # don't forget to indent your code here!
    aaa = GameOfLife(20, 1, 'b23/s3', 'b3o$3ob$bo!', (5,10))
    print(aaa.size_of_board)
    aaa.return_board()
    aaa.display_board()
    aaa.update()
    aaa.return_board()
    aaa.display_board()
    aaa.update()
    aaa.return_board()
    aaa.display_board()
    aaa.update()
    aaa.return_board()
    aaa.update()
    aaa.return_board()
    aaa.update()
    aaa.return_board()
    aaa.display_board()
