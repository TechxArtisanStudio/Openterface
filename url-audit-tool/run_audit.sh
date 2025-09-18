#!/bin/bash

# URL Audit Tool Runner Script
# Provides convenient shortcuts for running the URL audit tool

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Function to check if Python is available
check_python() {
    if ! command -v python3 &> /dev/null; then
        print_error "Python 3 is not installed or not in PATH"
        exit 1
    fi
    
    # Check Python version
    python_version=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
    major_version=$(echo $python_version | cut -d. -f1)
    minor_version=$(echo $python_version | cut -d. -f2)
    
    # Check if version is 3.7 or higher
    if [ "$major_version" -lt 3 ] || ([ "$major_version" -eq 3 ] && [ "$minor_version" -lt 7 ]); then
        print_error "Python 3.7 or higher is required. Found: $python_version"
        exit 1
    fi
    
    print_success "Python $python_version detected"
}

# Function to install dependencies
install_dependencies() {
    print_status "Checking dependencies..."
    
    if [ ! -f "requirements.txt" ]; then
        print_error "requirements.txt not found"
        exit 1
    fi
    
    # Check if pip is available
    if ! command -v pip3 &> /dev/null; then
        print_error "pip3 is not installed or not in PATH"
        exit 1
    fi
    
    print_status "Installing dependencies..."
    pip3 install -r requirements.txt
    
    print_success "Dependencies installed"
}

# Function to run complete audit
run_full_audit() {
    print_status "Starting complete URL audit..."
    python3 url_audit.py
    print_success "Complete audit finished"
}

# Function to run quick audit (extract and resolve only)
run_quick_audit() {
    print_status "Starting quick audit (extract and resolve only)..."
    python3 url_audit.py --extract-only
    python3 url_audit.py --resolve-only
    print_success "Quick audit finished"
}

# Function to validate only
run_validation() {
    print_status "Starting link validation..."
    python3 url_audit.py --validate-only
    print_success "Link validation finished"
}

# Function to generate reports only
run_reports() {
    print_status "Generating reports..."
    python3 url_audit.py --report-only
    print_success "Report generation finished"
}

# Function to show help
show_help() {
    echo "URL Audit Tool Runner"
    echo ""
    echo "Usage: $0 [COMMAND]"
    echo ""
    echo "Commands:"
    echo "  full        Run complete audit (default)"
    echo "  quick       Run quick audit (extract and resolve only)"
    echo "  validate    Run link validation only"
    echo "  reports     Generate reports only"
    echo "  install     Install dependencies"
    echo "  check       Check Python installation"
    echo "  help        Show this help message"
    echo ""
    echo "Examples:"
    echo "  $0 full              # Run complete audit"
    echo "  $0 quick             # Run quick audit"
    echo "  $0 validate          # Validate links only"
    echo ""
    echo "For more options, run: python3 url_audit.py --help"
}

# Main script logic
main() {
    case "${1:-full}" in
        "full")
            check_python
            install_dependencies
            run_full_audit
            ;;
        "quick")
            check_python
            install_dependencies
            run_quick_audit
            ;;
        "validate")
            check_python
            run_validation
            ;;
        "reports")
            check_python
            run_reports
            ;;
        "install")
            check_python
            install_dependencies
            ;;
        "check")
            check_python
            ;;
        "help"|"-h"|"--help")
            show_help
            ;;
        *)
            print_error "Unknown command: $1"
            show_help
            exit 1
            ;;
    esac
}

# Run main function with all arguments
main "$@"
