import os
import shutil


def move_files_to_top_level(input_folder_path):
    # "input" フォルダ内のすべてのファイルをリストアップ
    all_files = []
    for root, _, files in os.walk(input_folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            all_files.append(file_path)

    # ファイルを最上位層に移動
    for file_path in all_files:
        file_name = os.path.basename(file_path)
        target_path = os.path.join(input_folder_path, file_name)

        # 同名のファイルが既に存在する場合、ファイル名を変更してコピー
        i = 1
        while os.path.exists(target_path):
            base_name, extension = os.path.splitext(file_name)
            new_name = f"{base_name}_{i}{extension}"
            target_path = os.path.join(input_folder_path, new_name)
            i += 1

        # ファイルを移動
        shutil.move(file_path, target_path)


if __name__ == "__main__":
    current_directory = os.getcwd()  # カレントディレクトリのパスを取得
    input_folder_path = os.path.join(current_directory, "input")  # "input" フォルダのパスを自動取得
    move_files_to_top_level(input_folder_path)
