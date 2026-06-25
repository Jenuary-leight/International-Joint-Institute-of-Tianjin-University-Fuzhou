import os
import json

# 定义根目录
base_dir = 'photos'

# 初始化符合新网页结构的数据对象
result = {
    'life': [],
    'school': [],
    'future': {
        'real': [], # 对应 photos/future/real
        'ai': []    # 对应 photos/future/ai
    }
}

# --- 第一步：扫描普通文件夹 (life, school) ---
for cat in ['life', 'school']:
    folder_path = os.path.join(base_dir, cat)
    if os.path.exists(folder_path):
        for file in os.listdir(folder_path):
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.mp4', '.mov', '.webp')):
                is_video = file.lower().endswith(('.mp4', '.mov'))
                item = {
                    'type': 'video' if is_video else 'img',
                    'src': f'photos/{cat}/{file}',
                    'text': file.split('.')[0]
                }
                result[cat].append(item)

# --- 第二步：扫描 future 的子文件夹 (real, ai) ---
for sub_cat in ['real', 'ai']:
    # 路径拼接为: photos/future/real 或 photos/future/ai
    folder_path = os.path.join(base_dir, 'future', sub_cat)
    
    if os.path.exists(folder_path):
        for file in os.listdir(folder_path):
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.mp4', '.mov', '.webp')):
                is_video = file.lower().endswith(('.mp4', '.mov'))
                item = {
                    'type': 'video' if is_video else 'img',
                    # 注意这里的 src 路径多了子文件夹
                    'src': f'photos/future/{sub_cat}/{file}',
                    'text': file.split('.')[0]
                }
                # 将数据添加到 result['future']['real'] 或 result['future']['ai']
                result['future'][sub_cat].append(item)
    else:
        print(f"⚠️ 警告: 没找到文件夹 {folder_path}，请确认你是否创建了该文件夹。")

# --- 输出结果 ---
print("-" * 30)
print("✅ 生成成功！请全选复制下方内容替换 index.html 里的 const appData 部分：")
print("-" * 30)
print(f"const appData = {json.dumps(result, ensure_ascii=False, indent=4)};")
print("-" * 30)
input("\n按回车键退出...")