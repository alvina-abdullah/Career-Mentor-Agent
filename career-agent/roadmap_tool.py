from agents import function_tool
@function_tool
def get_career_roadmap(field: str) -> str:
    maps = {
        "software_engineering": "Learn Python , DSA , Web Development, Github.",
        "data_science": "Learn Python, Statistics, Data Analysis, Machine Learning.",
        "product_management": "Learn Product Design, User Research, Agile Methodologies.",
        "cyber_security": "Learn Networking, Security Fundamentals, Ethical Hacking, Certifications.",
        "digital_marketing": "Learn SEO, Content Marketing, Social Media.",
        "graphic_design": "Learn Design Principles, Adobe Suite, Typography, Portfolio Development.",
        "cloud_computing": "Learn Cloud Platforms, DevOps, Networking, Security, Certifications.",
        "artificial_intelligence": "Learn Machine Learning, Deep Learning, NLP.",
        "blockchain": "Learn Blockchain Fundamentals, Smart Contracts, Cryptography.",
        "game_development": "Learn Game Design, Unity/Unreal Engine.",
        "mobile_app_development": "Learn Android/iOS Development, Flutter/React Native, UI/UX Design, Projects.",
    }

    return maps.get(field.lower(), "Career roadmap not found for the specified field.")