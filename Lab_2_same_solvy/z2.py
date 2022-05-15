import csv


def main():
    file = open('zadanie2.csv')
    csvreader = csv.reader(file)
    headers = csvreader.__next__()
    items = []
    for row in csvreader:
        val = ''
        val += row[1]
        for i in range(2, len(row)):
            val += ','
            val += row[i]
        items.append({'id': row[0], 'val': val})

    items = [item for item in items if not item['val'] == '']
    last_id = 1
    for item in items:
        item['id'] = last_id
        last_id += 1
        item['val'] = item['val'].lower()
    for item in items:
        words = item['val'].split(' ')
        words_to_delete = []
        for word in words:
            word = ''.join(char for char in word if char.isalnum())
            if len(word) > 1 and ord(word[0]) == ord(word[1]) - 1:
                words_to_delete.append(word)
        for word in words_to_delete:
            item['val'].replace(word, '')
            print('id: ', item['id'], ', word: "', word, ',')


if __name__ == '__main__':
    main()
