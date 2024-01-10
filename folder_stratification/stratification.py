### これは1つのフォルダにまとまって入っているファイルを階層化するプログラムです

import os
import shutil


def organize_files(input_dir, output_base_dir):
    # 指定されたディレクトリ内のファイルを取得
    files = os.listdir(input_dir)

    for filename in files:
        # ファイル名から年度、第、問を削除
        modified_filename = filename.replace("年度", "").replace("第", "").replace("問", "")

        # ファイル名を_で分割
        name_parts = modified_filename.split("_")

        # ファイル名が指定された形式である場合
        if len(name_parts) == 3:
            school_name, year, subject = name_parts

            # 移動先のフォルダを作成
            dest_folder = os.path.join(output_base_dir, school_name, subject)
            os.makedirs(dest_folder, exist_ok=True)

            # 移動先のファイルパスを組み立て
            dest_path = os.path.join(dest_folder, filename)

            # ファイルを移動
            shutil.move(os.path.join(input_dir, filename), dest_path)
            print(f"Moved {filename} to {dest_path}")


if __name__ == "__main__":
    # プログラムがある階層にあるoutputフォルダを移動先のベースディレクトリとして使用
    current_directory = os.path.dirname(os.path.abspath(__file__))
    output_base_directory = os.path.join(current_directory, "output")

    # プログラムがある階層にあるinputフォルダを元のファイルがあるディレクトリとして使用
    input_directory = os.path.join(current_directory, "input")

    # ファイルの整理
    organize_files(input_directory, output_base_directory)
