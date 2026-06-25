import os
import json

# 配置
PHOTO_DIR = 'photos'
DATA_FILE = 'data.js' # 生成这个文件
VALID_EXTS = {'.jpg', '.jpeg', '.png', '.webp', '.mp4', '.mov', '.JPG', '.PNG', '.MP4'}

def get_files(sub_path):
    full_path = os.path.join(PHOTO_DIR, sub_path)
    if not os.path.exists(full_path):
        print(f"⚠️  警告：找不到文件夹 {full_path}")
        return []
    
    file_list = []
    try:
        # 按文件名排序，保证顺序一致
        files = sorted(os.listdir(full_path))
    except Exception as e:
        print(f"❌ 读取错误: {e}")
        return []
    
    for f in files:
        ext = os.path.splitext(f)[1]
        if ext in VALID_EXTS or ext.lower() in VALID_EXTS:
            # 路径：photos/life/xxx.jpg
            src_path = f"{PHOTO_DIR}/{sub_path}/{f}".replace("\\", "/")
            item = {
                "type": "video" if ext.lower() in ['.mp4', '.mov'] else "img",
                "src": src_path,
                "text": os.path.splitext(f)[0]
            }
            file_list.append(item)
    
    print(f"📂 {sub_path}: 找到 {len(file_list)} 个文件")
    return file_list

def main():
    print("🚀 正在生成数据文件...")
    
    app_data = {
        "life": get_files('life'),
        "school": get_files('school'),
        "future": {
            "real": get_files('future/real'),
            "ai": get_files('future/ai')
        }
    }

    # 写入 data.js
    # 格式：const appData = { ... };
    js_content = f"const appData = {json.dumps(app_data, ensure_ascii=False, indent=4)};"
    
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        f.write(js_content)
        
    print("-" * 30)
    print(f"✅ 成功生成 {DATA_FILE}！")
    print("现在网页会自动读取这个文件里的照片数据。")
    print("-" * 30)

if __name__ == '__main__':
    main()