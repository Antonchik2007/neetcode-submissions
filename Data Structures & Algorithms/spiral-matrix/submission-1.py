class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        result = []
        rows = len(matrix)-1
        columns = len(matrix[0])-1
        visited = set()
        def collect(maxTop, maxLeft):
            if (maxTop, maxLeft) in visited or maxTop > rows or maxLeft > columns:
                return result
            row = maxTop
            column = maxLeft


            while column <= columns - maxLeft:
                if (row, column) in visited:
                    column += 1 
                    continue
                res = matrix[row][column]
                visited.add((row, column))
                result.append(res)
                column += 1
            column -= 1
            while row <= rows-maxTop:
                if (row, column) in visited:
                    row += 1
                    continue
                res = matrix[row][column]
                visited.add((row, column))
                result.append(res)
                row += 1
            row -= 1
            while column >= maxLeft:
                if (row, column) in visited:
                    column -= 1
                    continue
                res = matrix[row][column]
                visited.add((row, column))
                result.append(res)
                column -= 1
            column +=1
            while row >= maxTop:
                if (row, column) in visited:
                    row -= 1
                    continue
                res = matrix[row][column]
                visited.add((row, column))
                result.append(res)
                row -= 1
            row +=1


            collect(maxTop+1, maxLeft+1)
            
        collect(0, 0)
        return result

