import yara
import sys
import os

def main():
    # Verify arguments
    if len(sys.argv) < 2:
        print("Usage: python yara_keyloggerdetec.py <target_file> [rule_file]")
        print("Default rule file: yara_rules.yar")
        sys.exit(1)

    
    target_file = sys.argv[1]
    rule_file = sys.argv[2] if len(sys.argv) > 2 else "yara_rules.yar"

    
    if not os.path.exists(target_file):
        print(f"Error: Target file not found - {target_file}")
        sys.exit(1)

    if not os.path.exists(rule_file):
        print(f"Error: Rule file not found - {rule_file}")
        sys.exit(1)

   
    try:
        rules = yara.compile(filepath=rule_file)
        matches = rules.match(target_file)
        
        if matches:
            print("\n🚨 DETECTED THREATS:")
            for match in matches:
                print(f"• Rule: {match.rule}")
                if 'description' in match.meta:
                    print(f"  Description: {match.meta['description']}")
                print(f"  Tags: {', '.join(match.tags) if match.tags else 'None'}")
        else:
            print("\n✅ No threats detected in", target_file)
            
    except Exception as e:
        print(f"\n❌ Error scanning {target_file}: {str(e)}")

if __name__ == "__main__":
    main()
