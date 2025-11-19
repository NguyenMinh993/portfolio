#!/usr/bin/env python3
"""
Script để cập nhật portfolio:
1. Bỏ con vịt và hồ bơi
2. Thêm animated code window
3. Thêm highlights section
"""

import re

# Đọc file hiện tại
with open('portfolio/templates/portfolio/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Thêm CSS cho highlights section (sau phần .orb)
highlights_css = """
        /* Highlights Section */
        .highlights {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 25px;
            margin: 60px 0;
        }
        .highlight-card {
            background: linear-gradient(135deg, rgba(212, 175, 55, 0.1), rgba(244, 208, 63, 0.05));
            border: 2px solid rgba(212, 175, 55, 0.3);
            border-radius: 12px;
            padding: 30px;
            text-align: center;
            transition: all 0.3s ease;
            animation: fadeInUp 1s ease both;
        }
        .highlight-card:hover {
            transform: translateY(-10px);
            border-color: rgba(212, 175, 55, 0.6);
            box-shadow: 0 15px 40px rgba(212, 175, 55, 0.2);
        }
        .highlight-icon {
            font-size: 48px;
            margin-bottom: 15px;
            filter: drop-shadow(0 0 10px rgba(212, 175, 55, 0.5));
        }
        .highlight-card h3 {
            font-size: 20px;
            color: #d4af37;
            margin-bottom: 10px;
        }
        .highlight-card p {
            color: rgba(255, 255, 255, 0.7);
            font-size: 14px;
            line-height: 1.6;
        }
"""

# Tìm vị trí để chèn CSS (sau .orb)
orb_pattern = r'(\.orb \{[^}]+\})'
if re.search(orb_pattern, content):
    content = re.sub(orb_pattern, r'\1\n' + highlights_css, content)
    print("✅ Đã thêm Highlights CSS")
else:
    print("❌ Không tìm thấy .orb CSS")

# 2. Thêm HTML cho highlights section (sau hero section, trước profile)
highlights_html = """
    <!-- Highlights Section - Key Points for HR -->
    <section class="section" style="padding-top: 60px; padding-bottom: 40px;">
        <h2 class="section-title">Why Hire Me?</h2>
        <div class="highlights">
            <div class="highlight-card" style="animation-delay: 0.1s;">
                <div class="highlight-icon">🚀</div>
                <h3>Full Stack Ready</h3>
                <p>Proficient in both Frontend (Next.js, React) and Backend (NestJS, Node.js) with production experience</p>
            </div>
            <div class="highlight-card" style="animation-delay: 0.2s;">
                <div class="highlight-icon">⚡</div>
                <h3>Fast Learner</h3>
                <p>Quickly adapt to new technologies and frameworks. Self-taught multiple tech stacks through real projects</p>
            </div>
            <div class="highlight-card" style="animation-delay: 0.3s;">
                <div class="highlight-icon">💼</div>
                <h3>Real Experience</h3>
                <p>Built complete e-learning platform, e-commerce site, and worked as intern at UTA Solution</p>
            </div>
            <div class="highlight-card" style="animation-delay: 0.4s;">
                <div class="highlight-icon">🎯</div>
                <h3>Problem Solver</h3>
                <p>Strong analytical skills with experience in system design, API development, and database optimization</p>
            </div>
        </div>
    </section>

"""

# Tìm vị trí profile section và chèn highlights trước đó
profile_pattern = r'(\s*<!-- Profile Section -->)'
if re.search(profile_pattern, content):
    content = re.sub(profile_pattern, highlights_html + r'\1', content)
    print("✅ Đã thêm Highlights Section")
else:
    print("❌ Không tìm thấy Profile Section")

# 3. Xóa phần Cyber Duck HTML
duck_pattern = r'<!-- Cyber Duck -->.*?</div>\s*</div>\s*</div>'
content = re.sub(duck_pattern, '', content, flags=re.DOTALL)
print("✅ Đã xóa Cyber Duck")

# 4. Xóa JavaScript liên quan đến duck
duck_js_pattern = r'// Cyber Duck and Pool Interaction.*?(?=// Contact Form Submission|</script>)'
content = re.sub(duck_js_pattern, '', content, flags=re.DOTALL)
print("✅ Đã xóa Cyber Duck JavaScript")

# Lưu file
with open('portfolio/templates/portfolio/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("\n🎉 Hoàn tất! Portfolio đã được cập nhật.")
print("📝 Kiểm tra file và test trên local trước khi deploy.")
