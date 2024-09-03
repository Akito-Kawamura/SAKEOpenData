import os
import json

import re

def remove_full_width_space_and_backslash(data):
    """
    リストや辞書内の全ての文字列に対して、全角スペースとバックスラッシュを削除する

    Args:
        data: 処理対象のデータ (リストまたは辞書)

    Returns:
        処理後のデータ
    """

    if isinstance(data, str):
        # 文字列の場合は置換処理
        return re.sub(r' |\\', '', data)
    elif isinstance(data, list):
        return [remove_full_width_space_and_backslash(item) for item in data]
    elif isinstance(data, dict):
        return {key: remove_full_width_space_and_backslash(value) for key, value in data.items()}
    else:
        return data

def json_to_jsonl(input_file, output_file):
  """
  JSONファイルをJSONL形式に変換する関数

  Args:
    input_file: 入力JSONファイルのパス
    output_file: 出力JSONLファイルのパス
  """

  with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    try:
      data = json.load(infile)
	#     remove_full_width_space_and_backslash(data)
      if isinstance(data, list):
        for item in data:
          json.dump(item, outfile)
          outfile.write('\n')
      else:
        json.dump(data, outfile)
        outfile.write('\n')
    except Exception as e:
      print(f"{input_file} is invalid")

# 変換対象ディレクトリ
directory = '../json/bottles'


for filename in os.listdir(directory):
    if filename.endswith('.json'):
        input_file = os.path.join(directory, filename)
        output_file = "../jsonl/bottles/" + filename.replace('.json', '.jsonl')
        json_to_jsonl(input_file, output_file)