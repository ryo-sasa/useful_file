import csv
import os


def create_folders_from_csv(csv_file, base_folder):
    with open(csv_file, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            # フォルダ名を取得
            folder_name = row[0]

            # フォルダを作成
            create_folder(os.path.join(base_folder, folder_name))

            # 下の階層のフォルダがあれば作成
            if len(row) > 1:
                subfolders = row[1:]
                create_subfolders(os.path.join(base_folder, folder_name), subfolders)


def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def create_subfolders(parent_folder, subfolders):
    for subfolder in subfolders:
        folder_path = os.path.join(parent_folder, subfolder)
        create_folder(folder_path)


if __name__ == "__main__":
    # 同じフォルダにあるCSVファイルの名前を指定
    csv_file_name = "book1.csv"

    # プログラムが存在するフォルダのパスを取得
    current_folder = os.path.dirname(os.path.abspath(__file__))

    # create_folderという名前のフォルダを作成
    create_folder(os.path.join(current_folder, "create_folder"))

    # CSVファイルを読み取り、create_folder内に生成されたフォルダを格納
    create_folders_from_csv(
        os.path.join(current_folder, csv_file_name),
        os.path.join(current_folder, "create_folder"),
    )
