BOARD_COLUMNS = 5
BOARD_ROWS = 5

class Board():

    def __init__(self, numbers):
        self.numbers = [[[numbers[i][j], False] for j in range(BOARD_ROWS)] for i in range(BOARD_COLUMNS)]
    
    def tick(self, num):
        for l in range(BOARD_COLUMNS):
            for r in range(BOARD_ROWS):
                if self.numbers[l][r][0] == num:
                    self.numbers[l][r][1] = True
                    return
        return 
    
    def hasWin(self):
        # check each row
        for r in range(BOARD_ROWS):
            # count the number of ticked numbers on the line
            count = 0
            for c in range(BOARD_COLUMNS):
                if self.numbers[r][c][1]:
                    count += 1
            if count == BOARD_COLUMNS:
                return True
        # check each column
        for c in range(BOARD_COLUMNS):
            # count the number of ticked numbers on the column
            count = 0
            for r in range(BOARD_ROWS):
                if self.numbers[r][c][1]:
                    count += 1
            if count == BOARD_ROWS:
                return True
        return False

    def getSumOfUnticked(self):
        count = 0
        for r in range(BOARD_ROWS):
            for c in range(BOARD_COLUMNS):
                if self.numbers[r][c][1] == False:
                    count += self.numbers[r][c][0]
        return count


if __name__ == '__main__':
    nums = [[r*BOARD_COLUMNS + c for c in range(BOARD_COLUMNS)] for r in range(BOARD_ROWS)]
    print(*nums, sep='\n')
    b = Board(nums)
    for i in range(10, 15):
        b.tick(i)
        print(b.hasWin())
        print(b.getSumOfUnticked())