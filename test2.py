import os


def get_file_info(target_dir):
    """
    获取目标路径的所有文件信息
    Args:
        target_dir: <str> 目标路径
    Returns:

    """
    result = {}
    for _root, _dir, _files in os.walk(target_dir):
        for each_file in _files:
            root = _root.replace("\\", "/")
            file_info = os.path.splitext(each_file)
            value = result.get(root)
            if not value:
                result.update({root: [file_info]})
            else:
                value.append(file_info)
    print(result)
    return result

_target_dir = input("please input the path:")
get_file_info(_target_dir)
