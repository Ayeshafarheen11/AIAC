def csv_file_stats(filename):
    total_rows = 0
    empty_rows = 0
    total_words = 0
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            total_rows += 1
            cells = [cell.strip() for cell in line.strip().split(',')]
            if all(cell == '' for cell in cells):
                empty_rows += 1
            # Count words in all cells
            for cell in cells:
                total_words += len(cell.split())
    return total_rows, empty_rows, total_words
print(csv_file_stats('Sample.csv'))