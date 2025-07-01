# Bug Fixes Report

This document outlines 3 critical bugs found and fixed in the SnakeCult.net codebase.

## Bug #1: Configuration Conflict (Critical)

### Problem
The codebase contained two conflicting Hugo configuration files with different `baseURL` settings:
- `config/_default/config.toml`: `baseURL = "https://snakecult.net/"`
- `hugo.toml`: `baseURL = 'https://snakecult.netlify.app/'`

### Impact
- **Security Risk**: Inconsistent URL generation could lead to mixed content warnings
- **SEO Issues**: Search engines might index the wrong canonical URLs  
- **Deployment Failures**: Unclear which configuration Hugo would prioritize
- **Broken Links**: Site navigation could break depending on which config was used

### Root Cause
Duplicate configuration files created during development without proper cleanup.

### Fix Applied
1. Consolidated all configuration into `config/_default/config.toml`
2. Removed the duplicate `hugo.toml` file
3. Used the production domain (`https://snakecult.net/`) as the authoritative baseURL
4. Merged all necessary build and markup settings into the single config file

## Bug #2: Debug Output in Production Code (Performance/Maintenance)

### Problem
The `scripts/snakecult_clean.py` script contained debug print statements that would execute in production:
```python
print("DEBUG - First 100 chars code points:", [ord(c) for c in text[:100]])
print("DEBUG - First 100 bytes:", raw_bytes[:100])
print("DEBUG - Hex representation:", raw_bytes[:100].hex())
```

### Impact
- **Performance Degradation**: Unnecessary character processing and console output
- **Verbose Logs**: Cluttered output making it harder to identify real issues
- **Information Leakage**: Debug output could potentially expose sensitive content
- **Maintenance Overhead**: Confusing output for users running the script

### Root Cause
Debug statements left behind after development/testing phase.

### Fix Applied
Removed all debug print statements from the production code while preserving the functional logic.

## Bug #3: Broken Regex Patterns (Logic Error)

### Problem
Multiple regex patterns in `scripts/snakecult_clean.py` had incorrectly escaped backslashes:
```python
# Broken patterns:
r'\\b([a-z]+)-([a-z]+)\\b'  # Should be r'\b([a-z]+)-([a-z]+)\b'
r'(\\.)( )'                 # Should be r'(\.)( )'
```

### Impact
- **Non-functional Features**: The `dehyphenate()` function would never match hyphenated words
- **Spacing Issues**: The `randomize_spacing()` function would never match periods
- **Data Processing Failures**: Text cleaning operations would silently fail
- **Subtle Bugs**: Functions appeared to work but produced no output changes

### Root Cause
Incorrect understanding of Python raw string regex escaping rules.

### Fix Applied
Corrected the regex patterns by removing unnecessary backslash escaping:
- `r'\b([a-z]+)-([a-z]+)\b'` for word boundary matching
- `r'(\.)( )'` for period and space matching

## Summary

All three bugs have been successfully resolved:

1. ✅ **Configuration conflict eliminated** - Single authoritative config file
2. ✅ **Debug output removed** - Clean production-ready script 
3. ✅ **Regex patterns fixed** - Text processing functions now work correctly

These fixes improve site reliability, performance, and maintainability while eliminating potential security risks.