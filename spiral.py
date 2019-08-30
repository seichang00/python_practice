https://leetcode.com/problems/spiral-matrix/
SPRIRAL MATRIX
m rows x n columns matrix

[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12],
  [9,10,11,12]
]

Output: [1,2,3,4,8,12,11,10,9,5,6,7]

1. store all the visited locations into list (unordered set)
2. spiral run, until reaches an item that has already been visited (0)
3. iterate over the rows and columns, etc.

	#var switch b/t 1/-1

  
  while
    #iterate through first row last item (rowIndex)

    #iterate through column (columnIndex)

    #iterate to left through row (1)
    
    #reduce # of columns

    #iterate upward through column (j = 2)

		NORTH [0, 1], SOUTH [0, -1], EAST [1, 0], WEST [-1, 0]

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]: