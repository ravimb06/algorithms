def main():
    amount_rows = int(input())
    amount_columns = int(input())
    matrix = []
    for i in range(amount_rows):
        matrix.append(list(map(int, input().split())))
    coord_rows = int(input())
    coord_columns = int(input())
    def find_coordinates(amount_rows, amount_columns, coord_rows, coord_columns):
        result = []
        if coord_rows > 0:
            result.append(matrix[coord_rows-1][coord_columns])
        if coord_columns > 0:
            result.append(matrix[coord_rows][coord_columns-1])
        if coord_columns+1 < amount_columns:
            result.append(matrix[coord_rows][coord_columns+1])
        if coord_rows+1 < amount_rows:
            result.append(matrix[coord_rows+1][coord_columns])
        for i in sorted(result):
            print(i, end=' ')
    
    find_coordinates(amount_rows, amount_columns, coord_rows, coord_columns)

if __name__ == '__main__':
    main()