with open('input.txt', 'r', encoding='utf-8') as input_file, open('output.txt', 'w', encoding='utf-8') as output_file:
    for i, line in enumerate(input_file, 1):
        output_file.write(f'{i};{line}')
