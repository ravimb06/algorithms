def main():
    amount_rows = int(input())
    amount_columns = int(input())
    matrix = []
    for i in range(amount_rows):
        matrix.append(list(map(int, input().split())))

    def flip_matrix(amount_rows, amount_columns, matrix):
        modified_matrix = []
        for i in range(amount_columns):
            new_row = []
            for j in range(amount_rows):
                new_row.append(matrix[j][i])
            modified_matrix.append(new_row)
        for i in modified_matrix:
            print(*i)
    
    flip_matrix(amount_rows, amount_columns, matrix)


if __name__ == '__main__':
    main()
