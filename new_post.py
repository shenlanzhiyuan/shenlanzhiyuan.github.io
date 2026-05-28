# -*- coding: utf-8 -*-
"""
博客管理工具
用法: py new_post.py "文章标题" "文章slug"
"""
import sys
import os
from datetime import date

BLOG_DIR = os.path.dirname(os.path.abspath(__file__))
POSTS_DIR = os.path.join(BLOG_DIR, 'posts')
INDEX_FILE = os.path.join(BLOG_DIR, 'index.html')

TEMPLATE = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} · 深蓝之源</title>
<link rel="stylesheet" href="../static/style.css">
</head>
<body>

<header class="site-header">
  <div class="container">
    <h1 class="site-title">深蓝之源</h1>
    <p class="site-desc">火力发电厂安全生产管理实战笔记</p>
    <nav>
      <a href="../index.html">文章</a>
      <a href="../about.html">关于</a>
    </nav>
  </div>
</header>

<main class="container">
  <article class="article">

    <h2>{title}</h2>
    <div class="meta">{date_str}</div>

    <!-- 文章正文在这里写 HTML -->

  </article>
</main>

<footer class="site-footer">
  <div class="container">
    <p>© 2026 深蓝之源 · 用心守护每一度电的安全</p>
  </div>
</footer>

</body>
</html>
"""

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('用法: py new_post.py "文章标题" "文章slug"')
        print('示例: py new_post.py "有限空间安全管理实战" "confined-space-safety"')
        sys.exit(1)

    title = sys.argv[1]
    slug = sys.argv[2]
    today = date.today().strftime('%Y-%m-%d')
    
    # 创建文章文件
    post_file = os.path.join(POSTS_DIR, f'{slug}.html')
    if os.path.exists(post_file):
        print(f'错误: {post_file} 已存在')
        sys.exit(1)
    
    content = TEMPLATE.format(title=title, date_str=today)
    with open(post_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    # 更新 index.html 的文章列表
    new_entry = f"""  {{
    title: "{title}",
    slug: "{slug}",
    date: "{today}",
    summary: "（待补充摘要）"
  }}"""
    
    with open(INDEX_FILE, 'r', encoding='utf-8') as f:
        index_content = f.read()
    
    # 在 posts 数组第一个位置插入
    index_content = index_content.replace(
        'const posts = [',
        f'const posts = [\n{new_entry},'
    )
    
    with open(INDEX_FILE, 'w', encoding='utf-8') as f:
        f.write(index_content)
    
    print(f'✅ 文章已创建: posts/{slug}.html')
    print(f'   index.html 已更新')
    print(f'   接下来: 打开 {post_file}，在 <!-- 文章正文在这里写 HTML --> 处写内容')
