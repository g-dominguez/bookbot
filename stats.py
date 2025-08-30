def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        num_words = len(file_contents.split())
    return num_words

def get_char_count(file_path):
    with open(file_path) as f:
        file_contents = f.read().lower()
        char_dict = {}
        for char in file_contents:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict

def sort_characters(input_dict):
    new_list = []

    for i in input_dict:
        temp_dict = {}
        temp_dict['char'] = i
        temp_dict['count'] = input_dict[i]
        new_list.append(temp_dict)

    def sort_on(items):
        return items['count']
    
    new_list.sort(reverse=True, key=sort_on)

    for item in new_list:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['count']}")    