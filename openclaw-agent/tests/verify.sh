#!/bin/bash
# TaxPrep Agent Verification Tests
# Version: 1.0.0

set -e

echo "=========================================="
echo "TaxPrep Agent Verification Tests"
echo "=========================================="

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

TESTS_PASSED=0
TESTS_FAILED=0

# Test helper functions
pass() {
    echo -e "${GREEN}✓ PASS${NC}: $1"
    TESTS_PASSED=$((TESTS_PASSED + 1))
}

fail() {
    echo -e "${RED}✗ FAIL${NC}: $1"
    TESTS_FAILED=$((TESTS_FAILED + 1))
}

# Test 1: Required files exist
test_required_files() {
    echo -e "\n${YELLOW}Test: Required files exist${NC}"
    
    required_files=(
        "SOUL.md"
        "IDENTITY.md"
        "USER.md"
        "AGENTS.md"
        "README.md"
        "LICENSE"
        "config/agent.yaml"
    )
    
    all_exist=true
    for file in "${required_files[@]}"; do
        if [ ! -f "$file" ]; then
            echo "  Missing: $file"
            all_exist=false
        fi
    done
    
    if $all_exist; then
        pass "All required files present"
    else
        fail "Some required files missing"
    fi
}

# Test 2: Skills directory structure
test_skills_directory() {
    echo -e "\n${YELLOW}Test: Skills directory${NC}"
    
    if [ ! -d "skills" ]; then
        fail "skills directory missing"
        return
    fi
    
    required_skills=(
        "tax-reporting.md"
        "mtd-compliance.md"
        "expense-categorization.md"
    )
    
    all_exist=true
    for skill in "${required_skills[@]}"; do
        if [ ! -f "skills/$skill" ]; then
            echo "  Missing: skills/$skill"
            all_exist=false
        fi
    done
    
    if $all_exist; then
        pass "All skills present"
    else
        fail "Some skills missing"
    fi
}

# Test 3: SOUL.md has required sections
test_soul_md() {
    echo -e "\n${YELLOW}Test: SOUL.md structure${NC}"
    
    required_sections=("Core Truths" "Boundaries" "Expertise" "Communication Style")
    
    if [ ! -f "SOUL.md" ]; then
        fail "SOUL.md not found"
        return
    fi
    
    content=$(cat SOUL.md)
    all_found=true
    
    for section in "${required_sections[@]}"; do
        if ! echo "$content" | grep -q "$section"; then
            echo "  Missing section: $section"
            all_found=false
        fi
    done
    
    if $all_found; then
        pass "SOUL.md has all required sections"
    else
        fail "SOUL.md missing some sections"
    fi
}

# Test 4: agent.yaml is valid YAML
test_agent_yaml() {
    echo -e "\n${YELLOW}Test: agent.yaml validity${NC}"
    
    if [ ! -f "config/agent.yaml" ]; then
        fail "config/agent.yaml not found"
        return
    fi
    
    # Check for required keys
    required_keys=("agent:" "runtime:" "memory:" "skills:")
    
    content=$(cat config/agent.yaml)
    all_found=true
    
    for key in "${required_keys[@]}"; do
        if ! echo "$content" | grep -q "$key"; then
            echo "  Missing key: $key"
            all_found=false
        fi
    done
    
    if $all_found; then
        pass "agent.yaml has required keys"
    else
        fail "agent.yaml missing required keys"
    fi
}

# Test 5: IDENTITY.md has required fields
test_identity_md() {
    echo -e "\n${YELLOW}Test: IDENTITY.md structure${NC}"
    
    if [ ! -f "IDENTITY.md" ]; then
        fail "IDENTITY.md not found"
        return
    fi
    
    required_fields=("Name:" "Role:" "Emoji:")
    
    content=$(cat IDENTITY.md)
    all_found=true
    
    for field in "${required_fields[@]}"; do
        if ! echo "$content" | grep -q "$field"; then
            echo "  Missing field: $field"
            all_found=false
        fi
    done
    
    if $all_found; then
        pass "IDENTITY.md has required fields"
    else
        fail "IDENTITY.md missing required fields"
    fi
}

# Test 6: License is present and valid
test_license() {
    echo -e "\n${YELLOW}Test: LICENSE file${NC}"
    
    if [ ! -f "LICENSE" ]; then
        fail "LICENSE file not found"
        return
    fi
    
    required_sections=("License Grant" "Restrictions" "Warranty Disclaimer")
    
    content=$(cat LICENSE)
    all_found=true
    
    for section in "${required_sections[@]}"; do
        if ! echo "$content" | grep -q "$section"; then
            echo "  Missing section: $section"
            all_found=false
        fi
    done
    
    if $all_found; then
        pass "LICENSE has all required sections"
    else
        fail "LICENSE missing required sections"
    fi
}

# Test 7: Deploy script exists and is executable
test_deploy_script() {
    echo -e "\n${YELLOW}Test: Deploy script${NC}"
    
    if [ ! -f "deploy.sh" ]; then
        fail "deploy.sh not found"
        return
    fi
    
    pass "Deploy script exists"
}

# Main execution
main() {
    test_required_files
    test_skills_directory
    test_soul_md
    test_agent_yaml
    test_identity_md
    test_license
    test_deploy_script
    
    echo -e "\n=========================================="
    echo "Test Results"
    echo "=========================================="
    echo -e "Passed: ${GREEN}$TESTS_PASSED${NC}"
    echo -e "Failed: ${RED}$TESTS_FAILED${NC}"
    
    if [ $TESTS_FAILED -eq 0 ]; then
        echo -e "\n${GREEN}All tests passed!${NC}"
        exit 0
    else
        echo -e "\n${RED}Some tests failed.${NC}"
        exit 1
    fi
}

main "$@"