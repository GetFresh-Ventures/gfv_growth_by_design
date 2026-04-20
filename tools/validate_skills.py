#!/usr/bin/env python3
import os
import sys

def validate_skills():
    skills_dir = 'skills'
    if not os.path.isdir(skills_dir):
        print(f"Directory '{skills_dir}' not found.")
        return False

    errors = 0
    checked = 0

    for skill_name in os.listdir(skills_dir):
        skill_path = os.path.join(skills_dir, skill_name, 'SKILL.md')
        if not os.path.isfile(skill_path):
            continue
        
        checked += 1
        with open(skill_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check frontmatter
        if not content.startswith("---"):
            print(f"❌ {skill_name}: Missing YAML frontmatter block.")
            errors += 1
            continue

        end_idx = content.find("---", 3)
        if end_idx == -1:
            print(f"❌ {skill_name}: Unclosed YAML frontmatter block.")
            errors += 1
            continue

        frontmatter = content[3:end_idx]

        # Mandate standard tags
        if "name:" not in frontmatter:
            print(f"❌ {skill_name}: Missing 'name' in frontmatter.")
            errors += 1
        
        if "description:" not in frontmatter:
            print(f"❌ {skill_name}: Missing 'description' in frontmatter.")
            errors += 1

        # NOTE: High risk tools could have specific heuristics to check whether they need human approval.
        # But we will leave it to the user to place the requires_human_approval flag for now.

        if "<verification_gate>" not in content:
            print(f"❌ {skill_name}: Missing <verification_gate> block.")
            errors += 1
    
    print(f"\n✅ Checked {checked} skills.")
    if errors > 0:
        print(f"💥 Failed with {errors} errors.")
        return False
    else:
        print("🎉 All skills validated.")
        return True

if __name__ == "__main__":
    if not validate_skills():
        sys.exit(1)
