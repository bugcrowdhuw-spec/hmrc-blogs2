#!/bin/bash
# TaxPrep Agent Deployment Script
# Version: 1.0.0

set -e

echo "=========================================="
echo "TaxPrep OpenCLAW Agent Deployment"
echo "=========================================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Check for OpenCLAW framework
check_openclaw() {
    if command -v openclaw &> /dev/null; then
        echo -e "${GREEN}✓${NC} OpenCLAW framework detected"
        openclaw --version
    else
        echo -e "${RED}✗${NC} OpenCLAW framework not found"
        echo "Please install from: https://docs.openclaw.ai"
        exit 1
    fi
}

# Check for required environment variables
check_env_vars() {
    echo -e "\n${YELLOW}Checking environment variables...${NC}"
    
    missing_vars=()
    
    if [ -z "$CLAUDE_API_KEY" ]; then
        missing_vars+=("CLAUDE_API_KEY")
    fi
    
    if [ -z "$OPENCLAW_API_KEY" ]; then
        missing_vars+=("OPENCLAW_API_KEY")
    fi
    
    if [ ${#missing_vars[@]} -gt 0 ]; then
        echo -e "${RED}✗${NC} Missing required variables:"
        for var in "${missing_vars[@]}"; do
            echo "  - $var"
        done
        echo ""
        echo "Set these in your environment before running:"
        echo "  export CLAUDE_API_KEY=your_key_here"
        echo "  export OPENCLAW_API_KEY=your_key_here"
        exit 1
    fi
    
    echo -e "${GREEN}✓${NC} All required environment variables set"
}

# Validate agent configuration
validate_config() {
    echo -e "\n${YELLOW}Validating agent configuration...${NC}"
    
    if [ ! -f "config/agent.yaml" ]; then
        echo -e "${RED}✗${NC} config/agent.yaml not found"
        exit 1
    fi
    
    if [ ! -f "SOUL.md" ]; then
        echo -e "${RED}✗${NC} SOUL.md not found"
        exit 1
    fi
    
    if [ ! -f "IDENTITY.md" ]; then
        echo -e "${RED}✗${NC} IDENTITY.md not found"
        exit 1
    fi
    
    if [ ! -d "skills" ]; then
        echo -e "${RED}✗${NC} skills directory not found"
        exit 1
    fi
    
    echo -e "${GREEN}✓${NC} Configuration files validated"
}

# Create memory directory structure
setup_memory() {
    echo -e "\n${YELLOW}Setting up memory directory...${NC}"
    
    mkdir -p memory
    mkdir -p data/users
    
    echo -e "${GREEN}✓${NC} Memory directories created"
}

# Run the agent
run_agent() {
    echo -e "\n${YELLOW}Starting TaxPrep agent...${NC}"
    openclaw run taxprep-assistant
}

# Main execution
main() {
    echo "Starting deployment process..."
    
    check_openclaw
    check_env_vars
    validate_config
    setup_memory
    
    echo -e "\n${GREEN}Deployment complete!${NC}"
    echo "Starting agent..."
    
    run_agent
}

main "$@"