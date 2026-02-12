#!/usr/bin/env python3
"""
为每个 skill 生成 README.md 文件
"""

import os
from pathlib import Path

# 定义每个 skill 的 README 内容
SKILLS_README = {
    "bananapro-image-gen": {
        "title": "BananaPro Image Generator",
        "description": "Professional image generator using BananaPro API with support for batch generation and multiple styles.",
        "features": [
            "🎨 Multiple image styles support",
            "📦 Batch generation capability",
            "📖 Chapter illustration automation",
            "🎯 High-quality output",
            "⚡ Fast generation speed"
        ],
        "usage": """```bash
# Generate single image
python scripts/generate_image.py --prompt "A beautiful sunset"

# Batch generate for chapters
./test_chapters.sh
```""",
        "requirements": [
            "Python 3.x",
            "BananaPro API Key",
            "Required packages in requirements.txt"
        ]
    },
    
    "baoyu-comic": {
        "title": "Knowledge Comic Creator",
        "description": "Create educational comics with multiple visual styles including Logicomix/Ligne Claire and Ohmsha manga guide styles.",
        "features": [
            "📚 Logicomix/Ligne Claire style support",
            "🎌 Ohmsha manga guide style",
            "🎬 Multiple layout options (standard/cinematic/dense/splash/mixed/webtoon)",
            "🎨 7 preset styles (classic/dramatic/warm/tech/sepia/vibrant/ohmsha)",
            "📖 Sequential panel generation"
        ],
        "usage": """```bash
# Basic usage
/baoyu-comic posts/article.md

# With specific style and layout
/baoyu-comic posts/article.md --style dramatic --layout cinematic
```""",
        "requirements": [
            "Image generation API access",
            "Markdown source files"
        ]
    },
    
    "baoyu-cover-image": {
        "title": "Cover Image Generator",
        "description": "Generate professional cover images for articles and books with 8 preset styles.",
        "features": [
            "🎨 8 preset styles (minimal/elegant/tech/retro/nature/warm/bold/playful)",
            "🤖 Auto style selection based on content",
            "📐 Custom size and ratio support",
            "🎯 Optimized for various platforms"
        ],
        "usage": """```bash
# Auto-select style
/baoyu-cover-image article.md

# Specify style
/baoyu-cover-image article.md --style tech
```""",
        "requirements": [
            "Image generation API access"
        ]
    },
    
    "baoyu-article-illustrator": {
        "title": "Smart Article Illustrator",
        "description": "Analyze article structure and automatically generate illustrations at optimal positions.",
        "features": [
            "🔍 Smart position detection",
            "🎨 Multiple style options",
            "🎯 Content-aware illustration",
            "📊 Automatic image placement"
        ],
        "usage": """```bash
# Auto-select style
/baoyu-article-illustrator article.md

# Specify style
/baoyu-article-illustrator article.md --style tech
```""",
        "requirements": [
            "Image generation API access",
            "Markdown articles"
        ]
    },
    
    "baoyu-xhs-images": {
        "title": "Xiaohongshu Image Generator",
        "description": "Generate images optimized for Xiaohongshu (Little Red Book) platform.",
        "features": [
            "📱 Xiaohongshu platform optimization",
            "🎨 Platform-specific styles",
            "📐 Optimal dimensions",
            "🎯 High engagement design"
        ],
        "usage": """```bash
/baoyu-xhs-images content.md
```""",
        "requirements": [
            "Image generation API access"
        ]
    },
    
    "ai-ui-design-improver": {
        "title": "AI UI Design Improver",
        "description": "AI-powered tool to analyze and improve UI designs.",
        "features": [
            "🔍 Design analysis",
            "💡 Improvement suggestions",
            "🎨 Best practices recommendations",
            "📊 Accessibility checks"
        ],
        "usage": """```bash
# Analyze design
/ai-ui-design-improver design-file.fig
```""",
        "requirements": [
            "Design files (Figma, Sketch, etc.)"
        ]
    },
    
    "deploying-to-production": {
        "title": "Production Deployment Assistant",
        "description": "Complete guide and automation for deploying applications to production.",
        "features": [
            "📋 Deployment checklists",
            "🔒 Security best practices",
            "⚡ Performance optimization",
            "📊 Monitoring setup",
            "🔄 CI/CD integration"
        ],
        "usage": """```bash
# Get deployment guide
/deploying-to-production --platform aws

# Run deployment checks
/deploying-to-production --check
```""",
        "requirements": [
            "Cloud platform access",
            "Application ready for deployment"
        ]
    },
    
    "doc-sync-tool": {
        "title": "Documentation Sync Tool",
        "description": "Synchronize documentation across multiple platforms automatically.",
        "features": [
            "🔄 Multi-platform sync",
            "📝 Format conversion",
            "🔗 Link management",
            "📊 Version control"
        ],
        "usage": """```bash
# Sync to all platforms
/doc-sync-tool sync --all

# Sync to specific platform
/doc-sync-tool sync --platform github
```""",
        "requirements": [
            "Platform API keys",
            "Documentation source"
        ]
    },
    
    "shipany": {
        "title": "ShipAny - Fast Deployment Tool",
        "description": "Quickly publish and deploy applications with minimal configuration.",
        "features": [
            "⚡ Fast deployment",
            "🎯 Minimal configuration",
            "🔄 Auto-scaling support",
            "📊 Deployment monitoring"
        ],
        "usage": """```bash
# Deploy application
shipany deploy

# Deploy with custom config
shipany deploy --config custom.yml
```""",
        "requirements": [
            "Application source code",
            "Cloud platform credentials"
        ]
    },
    
    "google-official-seo-guide": {
        "title": "Google Official SEO Guide",
        "description": "SEO optimization guide based on official Google documentation.",
        "features": [
            "📚 Official Google guidelines",
            "🔍 SEO best practices",
            "📊 Performance metrics",
            "🎯 Actionable recommendations"
        ],
        "usage": """```bash
# Analyze website SEO
/google-seo-guide analyze https://example.com

# Get recommendations
/google-seo-guide recommend
```""",
        "requirements": [
            "Website URL",
            "Google Search Console access (optional)"
        ]
    },
    
    "internationalizing-websites": {
        "title": "Website Internationalization Guide",
        "description": "Complete guide for implementing multi-language support and internationalization.",
        "features": [
            "🌍 Multi-language support",
            "🔤 Translation management",
            "📍 Locale handling",
            "🎯 Best practices"
        ],
        "usage": """```bash
# Setup i18n
/i18n-websites setup --languages en,zh,ja

# Extract translatable strings
/i18n-websites extract
```""",
        "requirements": [
            "Website source code",
            "Translation files"
        ]
    },
    
    "web-performance-seo": {
        "title": "Web Performance & SEO Optimizer",
        "description": "Comprehensive web performance optimization and SEO improvement solutions.",
        "features": [
            "⚡ Performance analysis",
            "🔍 SEO optimization",
            "📊 Core Web Vitals",
            "🎯 Actionable insights"
        ],
        "usage": """```bash
# Analyze performance
/web-perf-seo analyze https://example.com

# Get optimization suggestions
/web-perf-seo optimize
```""",
        "requirements": [
            "Website URL"
        ]
    },
    
    "skill-generator": {
        "title": "Claude Skill Generator",
        "description": "Scaffolding tool to quickly create new Claude skill templates.",
        "features": [
            "🚀 Quick skill creation",
            "📋 Standard templates",
            "✅ Best practices included",
            "📝 Auto-generated documentation"
        ],
        "usage": """```bash
# Create new skill
/skill-generator create my-awesome-skill

# Create with template
/skill-generator create my-skill --template advanced
```""",
        "requirements": [
            "None"
        ]
    },
    
    "baoyu-gemini-web": {
        "title": "Gemini Web Integration",
        "description": "Web integration tool for Google Gemini API.",
        "features": [
            "🔌 Gemini API integration",
            "🌐 Web interface",
            "🔐 Authentication handling",
            "📊 Usage tracking"
        ],
        "usage": """```bash
# Start web interface
npm start

# Configure API
npm run config
```""",
        "requirements": [
            "Node.js",
            "Google Gemini API key"
        ]
    },
    
    "baoyu-post-to-wechat": {
        "title": "WeChat Auto Publisher",
        "description": "Automatically publish content to WeChat public accounts.",
        "features": [
            "📱 Auto publishing",
            "📝 Format conversion",
            "🖼️ Image handling",
            "⏰ Scheduled posting"
        ],
        "usage": """```bash
# Publish article
/post-to-wechat article.md

# Schedule post
/post-to-wechat article.md --schedule "2024-01-01 10:00"
```""",
        "requirements": [
            "WeChat public account",
            "API credentials"
        ]
    },
    
    "baoyu-post-to-x": {
        "title": "X (Twitter) Auto Publisher",
        "description": "Automatically publish content to X (formerly Twitter).",
        "features": [
            "🐦 Auto posting",
            "🧵 Thread support",
            "🖼️ Media upload",
            "⏰ Scheduled tweets"
        ],
        "usage": """```bash
# Post tweet
/post-to-x "Your tweet content"

# Post thread
/post-to-x thread.md
```""",
        "requirements": [
            "X (Twitter) account",
            "API credentials"
        ]
    },
    
    "baoyu-slide-deck": {
        "title": "Slide Deck Generator",
        "description": "Generate professional presentations from Markdown.",
        "features": [
            "📊 Markdown to slides",
            "🎨 Multiple themes",
            "🖼️ Image support",
            "📤 Export formats (PDF, PPTX)"
        ],
        "usage": """```bash
# Generate slides
/slide-deck presentation.md

# With custom theme
/slide-deck presentation.md --theme dark
```""",
        "requirements": [
            "Markdown source"
        ]
    },
    
    "ziliu-content-distribution": {
        "title": "Multi-Platform Content Distribution",
        "description": "Automate content distribution across multiple platforms.",
        "features": [
            "🌐 Multi-platform support",
            "🔄 Auto synchronization",
            "📝 Format adaptation",
            "📊 Analytics tracking"
        ],
        "usage": """```bash
# Distribute to all platforms
/ziliu-distribute article.md --all

# Distribute to specific platforms
/ziliu-distribute article.md --platforms wechat,twitter
```""",
        "requirements": [
            "Platform API credentials",
            "Content source"
        ]
    },
    
    "wechat-publisher-0.1.0": {
        "title": "WeChat Publisher v0.1.0",
        "description": "WeChat content publisher (legacy version).",
        "features": [
            "📱 Basic publishing",
            "📝 Content formatting",
            "🖼️ Image upload"
        ],
        "usage": """```bash
# Publish content
/wechat-publisher publish article.md
```""",
        "requirements": [
            "WeChat credentials"
        ]
    },
    
    "markdown-to-video-script": {
        "title": "Markdown to Video Script Converter",
        "description": "Convert Markdown documents to video script format.",
        "features": [
            "🎬 Script formatting",
            "⏱️ Timing suggestions",
            "🎭 Scene breakdown",
            "📝 Narration text"
        ],
        "usage": """```bash
# Convert to script
/md-to-script article.md

# With timing
/md-to-script article.md --add-timing
```""",
        "requirements": [
            "Markdown source"
        ]
    },
    
    "wechat-zimage-generator": {
        "title": "WeChat Article Image Generator",
        "description": "Generate images specifically for WeChat articles.",
        "features": [
            "📱 WeChat optimization",
            "🎨 Article-specific styles",
            "📐 Optimal dimensions",
            "🖼️ Batch generation"
        ],
        "usage": """```bash
# Generate images for article
/wechat-zimage article.md

# Batch generate
/wechat-zimage batch articles/
```""",
        "requirements": [
            "Image generation API",
            "Article content"
        ]
    },
    
    "wechat-auto-writer": {
        "title": "WeChat Auto Writer",
        "description": "Automatically generate articles optimized for WeChat public accounts.",
        "features": [
            "✍️ Auto content generation",
            "📱 WeChat style optimization",
            "🎯 Engagement optimization",
            "📊 SEO for WeChat"
        ],
        "usage": """```bash
# Generate article
/wechat-auto-writer --topic "Your topic"

# With specific style
/wechat-auto-writer --topic "Topic" --style professional
```""",
        "requirements": [
            "AI API access"
        ]
    },
    
    "小红书AI教程短视频脚本生成器": {
        "title": "Xiaohongshu Video Script Generator",
        "description": "Generate short video scripts optimized for Xiaohongshu (Little Red Book) platform, specialized in AI tutorials.",
        "features": [
            "📱 Xiaohongshu optimization",
            "🎬 Short video format",
            "🤖 AI tutorial focus",
            "🎯 High engagement"
        ],
        "usage": """```bash
# Generate script
/xhs-video-script --topic "AI Tutorial Topic"
```""",
        "requirements": [
            "Tutorial content"
        ]
    }
}


def create_readme(skill_name, info):
    """生成 README.md 内容"""
    features_list = '\n'.join(info['features'])
    requirements_list = '\n'.join(f"- {req}" for req in info['requirements'])
    
    return f"""# {info['title']}

{info['description']}

## Features

{features_list}

## Usage

{info['usage']}

## Requirements

{requirements_list}

## Installation

```bash
npx skills add xianyu110/claudeskills@{skill_name}
```

Or manually copy this skill to your `~/.claude/skills/` directory.

## Configuration

See `SKILL.md` for detailed configuration and usage instructions.

## License

See the main repository LICENSE file.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

- GitHub Issues: [https://github.com/xianyu110/claudeskills/issues](https://github.com/xianyu110/claudeskills/issues)
- Repository: [https://github.com/xianyu110/claudeskills](https://github.com/xianyu110/claudeskills)
"""


def main():
    print("📝 开始生成 README.md 文件...\n")
    
    created = 0
    skipped = 0
    
    for skill_name, info in SKILLS_README.items():
        skill_dir = Path(skill_name)
        
        if not skill_dir.exists():
            print(f"⚠️  跳过 {skill_name} (目录不存在)")
            skipped += 1
            continue
        
        readme_file = skill_dir / 'README.md'
        
        if readme_file.exists():
            print(f"✅ {skill_name} (README.md 已存在)")
            skipped += 1
            continue
        
        # 创建 README.md
        content = create_readme(skill_name, info)
        with open(readme_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ {skill_name} (已创建 README.md)")
        created += 1
    
    print(f"\n✅ 完成！")
    print(f"   - 已创建: {created}")
    print(f"   - 已跳过: {skipped}")
    print(f"\n📋 下一步：")
    print("git add . && git commit -m 'docs: 为所有 skills 添加 README.md'")
    print("git push origin main")


if __name__ == '__main__':
    main()
