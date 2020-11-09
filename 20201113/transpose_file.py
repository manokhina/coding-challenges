import numpy as np


class Solution:
    def transpose_file(self, file_path):
        matrix = np.loadtxt(file_path, dtype='str')
        matrix_t = np.array(np.transpose(matrix))
        np.savetxt('result.txt', matrix_t, delimiter=' ', newline='\n', fmt="%s")


class DumbSolution:
    def transpose_file(self, file_path):
        with open(file_path, 'r') as f:
            content = [s.strip().split(" ") for s in f.readlines()]
        with open('result2.txt', 'a') as fl:
            for col in range(len(content[0])):
                for row in range(len(content)):
                    fl.write(content[row][col] + ' ')
                fl.write("\n")


if __name__ == '__main__':
    solution = Solution()
    print(solution.transpose_file("filename.txt"))

    solution2 = DumbSolution()
    print(solution2.transpose_file("filename.txt"))
