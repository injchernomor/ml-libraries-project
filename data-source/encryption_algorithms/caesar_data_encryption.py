import csv
from pathlib import Path
from encryption_algorithms.caesar_cipher import cesar


def create_a_сaesar_encrypted_scv_file(
    path_to_original_dict, path_to_save_the_created_file
):
    def add_сaesar_encrypted_words_to_the_list_of_encrypted_words_by_сaesar(path_to_original_dict):
        list_of_encrypted_words_by_сaesar = []
        with path_to_original_dict.open() as original_dict_csv:
            reader = csv.reader(original_dict_csv)
            for row in reader:
                english_word = row[0]
                list_of_encrypted_words_by_сaesar.append(
                    cesar(english_word, 3))

        return list_of_encrypted_words_by_сaesar

    def save_encrypted_data_to_a_data_file(path_to_save_the_created_file, list_of_encrypted_words_by_сaesar):
        path_to_save = path_to_save_the_created_file / 'сaesar_encrypted_data.csv'
        with open(path_to_save, 'w', newline='') as f:
            csv_writer = csv.writer(f)
            for item in list_of_encrypted_words_by_сaesar:
                csv_writer.writerow([item])

    list_of_encrypted_words_by_сaesar = add_сaesar_encrypted_words_to_the_list_of_encrypted_words_by_сaesar(
        path_to_original_dict)
    save_encrypted_data_to_a_data_file(
        path_to_save_the_created_file, list_of_encrypted_words_by_сaesar)


if __name__ == "__main__":
    path_to_original_dict = Path("../data/original_dict.csv")
    path_to_save_the_created_file = Path("../data/")

    create_a_сaesar_encrypted_scv_file(
        path_to_original_dict, path_to_save_the_created_file
    )
